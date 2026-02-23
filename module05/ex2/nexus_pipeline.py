#!/usr/bin/env python3
from typing import Protocol, Any, Union, Optional, runtime_checkable
from abc import ABC, abstractmethod


@runtime_checkable
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def process(self, data: Any) -> Any:
        
        if isinstance(data, str):
            if data.startswith("{") and data.endswith("}"):
                data = data.split(',')
                dict_data = {}
                dict_data['type'] = 'JSON'
                for item in data:
                    parts = item.split(":")
                    dict_data[parts[0]] = parts[1]
                return dict_data
            elif "," in data:
                part = data.split(",")
                return {
                    "type": "CVS",
                    "usr": part[0],
                    "action":part[1],
                    "val":part[2]
                }
            else:
                data_list = []
                data = data.split(",")
                for num in data:
                    try:
                        data_list.append(float(num))
                    except:
                        return f"Error while Input Data"
                return {
                    "type": "stream",
                    "data": data_list
                }

class TransformStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            return f"Invalid Data to Transforme"
        if data['type'] == "JSON":
            print("Transform: Enriched with metadata and validation")
            return data
        elif data['type'] == "CSV":
            print("Transform: Parsed and structured data")
            return data
        elif data['type'] == "stream":
            print("Transform: Aggregated and filtered")
            return data
        else:
            print("Imsucssufull Transform Stage")


class OutputStage:
    def process(self, data: Any) -> Any:
        if data['type'] == "JSON":
            return f"Processed temperature reading: {data['value']}°{data['unit']} (Normal range)"
        elif data['type'] == "CSV":
            action = sum(1 for item in data if data == "actions")
            return f"{data['usr']} activity logged: {action} actions processed"
        elif data['type'] == 'stream':
            data_avg = sum([item for item in data['data']])
            return f"Stream summary: {len(data)} readings, avg: {data_avg / len(data)}°C"
        return f"Erorr deticted in stage 3"


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"JSON Error Deticted : {e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"CVS Error Deticted : {e}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"STREAM Error Deticted : {e}"


class NexusManager:
    def __init__(self):
        self.piplens = []

    def add_pipline(self, pipline: ProcessingPipeline):
        self.piplens.append(pipline)

    def process_data(self, Data: Any):
        for pipline in self.piplens:
            if isinstance(pipline,JSONAdapter):
                print("Processing JSON data through pipeline...")
                res = pipline.process(Data['json'])
                print(f"Output: {res}")
            elif isinstance(pipline, CSVAdapter):
                print("Processing CSV data through same pipeline...")
                res = pipline.process(Data['cvs'])
                print(f"Output: {res}")
            elif isinstance(pipline,StreamAdapter):
                print("Processing Stream data through same pipeline...")
                res = pipline.process(Data['stream'])
                print(f"Output: {res}")
            print()


def main() -> None:
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("")
    data = {
        'json' : '{"sensor": "temp", "value": 23.5, "unit": "C"}',
        'cvs': 'user,action,timestamp',
        'stream':'22.05,30.0,29.50,40.0,29'
    }
    manager = NexusManager()
    print("Creating Data Processing Pipeline...")
    json = JSONAdapter("json_01")
    csv = CSVAdapter("csv_01")
    stream = StreamAdapter("stream_01")
    
    print("Stage 1: Input validation and parsing")
    json.add_stage(InputStage())
    csv.add_stage(InputStage())
    stream.add_stage(InputStage())
    print("Stage 2: Data transformation and enrichment")
    json.add_stage(TransformStage())
    csv.add_stage(TransformStage())
    stream.add_stage(TransformStage())
    print("Stage 3: Output formatting and delivery")
    json.add_stage(OutputStage())
    csv.add_stage(OutputStage())
    stream.add_stage(OutputStage())
    print("\n=== Multi-Format Data Processing ===\n")
    manager.add_pipline(json)
    manager.add_pipline(csv)
    manager.add_pipline(stream)
    manager.process_data(data)
    print("")
    



if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("")
    main()
