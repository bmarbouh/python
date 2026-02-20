#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Optional, Any, List, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "processed": self.items_processed}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        reading_count = 0
        avg = 0
        sam = 0
        self.items_processed += len(data_batch)
        for item in data_batch:
            reading_count += 1
            if isinstance(item, str) and item.startswith("temp"):
                parts = item.split(":")
                if len(parts) == 2:
                    avg += float(parts[1])
                    sam += 1
        if sam > 0:
            avg = avg / sam
        else:
            avg = 0
        return f"{reading_count} readings processed, avg temp: {avg}°C"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List:
        filter_list = []
        for item in data_batch:
            if isinstance(item, str) and item.startswith("temp"):
                parts = item.split(":")
                if criteria is not None and float(parts[1]) > criteria:
                    filter_list.append(f"temp:{parts[1]}")
        return filter_list


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        count_op = 0
        count_sell = 0
        count_buy = 0
        self.items_processed += len(data_batch)
        for item in data_batch:
            count_op += 1
            if isinstance(item, str) and item.startswith("sell"):
                parts = item.split(":")
                if len(parts) == 2:
                    count_sell += float(parts[1])
            elif isinstance(item, str) and item.startswith("buy"):
                parts = item.split(":")
                if len(parts) == 2:
                    count_buy += float(parts[1])
        net_flow = count_buy - count_sell
        if net_flow > 0:
            return f"{count_op} operations, net flow: +{net_flow} units"
        else:
            return f"{count_op} operations, net flow: {net_flow} units"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List:
        filter_list = []
        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("sell") or item.startswith("buy"):
                    parts = item.split(":")
                    if (
                        len(parts) == 2
                        and criteria is not None
                        and float(parts[1]) > criteria
                    ):
                        filter_list.append(item)
        return filter_list


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.items_processed += len(data_batch)
        count_event = 0
        count_error = 0
        for item in data_batch:
            count_event += 1
            if isinstance(item, str) and item == "error":
                count_error += 1
        return f"{count_event} events, {count_error} error detected"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List:
        filter_list = []
        for item in data_batch:
            if criteria is not None and item == criteria:
                filter_list.append(item)
        return filter_list


def main():
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    data_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data_sensor}")
    print(f"Sensor analysis: {sensor.process_batch(data_sensor)}")
    print("")
    print("Initializing Transaction Stream...")
    transiction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transiction.stream_id}, Type: Financial Data")
    data_transiction = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {data_transiction}")
    print(f"Transaction analysis: {transiction.process_batch(data_transiction)}")
    print("")
    event = EventStream("EVENT_001")
    data_event = ["login", "error", "logout"]
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print(f"Processing event batch: {data_event}")
    print(f"Event analysis: {event.process_batch(data_event)}")
    print("")
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("")
    
    print("")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    main()
