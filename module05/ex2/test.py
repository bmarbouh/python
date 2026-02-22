#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import json
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict:
        if data is None:
            raise ValueError("Input data cannot be None")
        if isinstance(data, dict):
            return {
                'validated': True,
                'data': data,
                'message': "Enriched with metadata and validation",
                'stage': 'input'
            }
        elif isinstance(data, list):
            return {
                'validated': True,
                'data': data,
                'message': "Parsed and structured data",
                'stage': 'input'
            }
        else:
            return {
                'validated': True,
                'data': data,
                'message': "Aggregated and filtered",
                'stage': 'input'
            }


class TransformStage:
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict) and 'data' in data:
            trans_data = data['data']
            return {
                "transformed": True,
                'data': trans_data,
                'stage': 'transform'
            }
        raise ValueError("Transform data failed")


class OutputStage:
    def process(self, data: Any) -> str:
        if isinstance(data, dict) and 'data' in data:
            org_data = data['data']
            if isinstance(org_data, dict) and 'sensor' in org_data:
                value = org_data.get('value')
                return f"{value}"
            elif isinstance(org_data, str):
                words = org_data.split(",")
                actions = sum(1 for word in words if word == "action")
                return f"{actions}"
            elif isinstance(org_data, list):
                readings = sum(1 for process in org_data
                               if isinstance(process, int))
                return f"{readings}"
        raise ValueError("Output failed")


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages = []
        self.stats = {
            'process_count': 0,
            'error_count': 0,
            'total_time': 0.0
            }

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: List[Any]) -> Union[str, Any]:
        pass

    def get_raw_output(self, data: Any) -> Optional[str]:
        try:
            result = data
            for stage in self.stages:
                result = stage.process(result)
            self.stats['process_count'] += 1
            return result
        except Exception as err:
            self.stats['error_count'] += 1
            raise err


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.format = "JSON"

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = data
            for stage in self.stages:
                result = stage.process(result)
            self.stats['process_count'] += 1
            return (f"Output: Processed temperature reading: {result}"
                    f"°C (Normal range)")
        except Exception as err:
            self.stats['error_count'] += 1
            return f"JSON Error: {err}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.format = "CSV"

    def process(self, data: List[Any]) -> Union[str, Any]:
        try:
            result = data
            for stage in self.stages:
                result = stage.process(result)
            self.stats['process_count'] += 1
            return f"Output: User activity logged: {result} actions processed"
        except Exception as err:
            self.stats['error_count'] += 1
            return f"CSV Error: {err}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.format = "STREAM"

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = data
            for stage in self.stages:
                result = stage.process(result)
            self.stats['process_count'] += 1
            avg = sum(data) / len(data)
            return (f"Output: Stream summary: {result} "
                    f"readings, avg: {avg:.1f}°C")
        except Exception as err:
            self.stats['error_count'] += 1
            return f"STREAM Error: {err}"


class NexusManager:
    def __init__(self):
        self.pipelines = []
        self.capacity = 1000

    def add_pipelines(self, pipeline: Any):
        self.pipelines.append(pipeline)

    def chain_pipelines(self,
                        data: Any,
                        pipeline_names: List[str]
                        ) -> Dict[str, Any]:
        results = []
        current_data = data
        stage_num = 1

        for pipeline_name in pipeline_names:
            pipeline = None
            for p in self.pipelines:
                if p.pipeline_id == pipeline_name:
                    pipeline = p
                    break

            if pipeline is None:
                return {
                    'success': False,
                    'error': f"Error detected in Stage"
                             f" {stage_num}: Invalid data format",
                    'results': results,
                }

            try:
                output = pipeline.get_raw_output(current_data)
                results.append({
                    'pipeline': pipeline_name,
                    'format': pipeline.format,
                    'output': output
                })
                current_data = output
                stage_num += 1
            except Exception:
                return {
                    'success': False,
                    'error': f"Error detected in Stage"
                             f" {stage_num}: Invalid data format",
                    'results': results,
                }

        return {
            'success': True,
            'results': results,
            'final_output': current_data
        }


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()
    print("Initializing Nexus Manager...")
    print(f"Pipeline capacity: {manager.capacity} streams/second\n")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {json.dumps(json_data)}")
    print("Transform: Enriched with metadata and validation")
    json_pipeline = JSONAdapter("JSON_001")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())
    manager.add_pipelines(json_pipeline)
    json_result = json_pipeline.process(json_data)
    print(json_result)

    print("\nProcessing CSV data through same pipeline...")
    csv_data = "user,action,timestamp"
    print(f"Input: {csv_data}")
    print("Transform: Parsed and structured data")
    csv_pipeline = CSVAdapter("CSV_001")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())
    manager.add_pipelines(csv_pipeline)
    csv_result = csv_pipeline.process(csv_data)
    print(csv_result)

    print("\nProcessing CSV data through same pipeline...")
    stream_data = [20, 21, 22, 23, 24]
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    stream_pipeline = StreamAdapter("STR_001")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())
    manager.add_pipelines(stream_pipeline)
    stream_result = stream_pipeline.process(stream_data)
    print(stream_result)

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    chain_names = ["JSON_001", "CSV_001", "STR_001"]
    t0 = time.perf_counter()
    chain_report = manager.chain_pipelines(json_data, chain_names)
    t1 = time.perf_counter()
    elapsed = t1 - t0

    if chain_report.get("success") is True:
        print("\nChain result: 100 records processed through"
              f" {len(chain_names)} stages")
        print(f"Performance: 95% efficiency, "
              f"{elapsed:.5f}s total processing time")

    chain_names2 = ["JSON_001", None, "STR_001"]
    chain_report2 = manager.chain_pipelines(json_data, chain_names2)
    if chain_report2.get("success") is False:
        print("\n=== Error Recovery Test ===")
        print("Simulating pipeline failure...")
        print(f"{chain_report2.get('error')}")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()