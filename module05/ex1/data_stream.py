#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        count_reading = 0
        avg = 0
        sum_count = 0
        for item in data_batch:
            if isinstance(item, str):
                part = item.split(":")
                if part[0] == "temp":
                    try:
                        sum_count += float(part[1])
                        avg += 1
                    except:
                        print("sensor Error: Erro while processing")
            count_reading += 1
        if avg > 0:
            return f"{count_reading} readings processed, avg temp: {sum_count / avg}°C"
        else:
            return f"{count_reading} readings processed, avg temp: 0.0°C"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        filter_list = []
        if not criteria:
            return filter_list
        for item in data_batch:
            if isinstance(item, str):
                part = item.split(":")
                cr = criteria.split(":")
                try:
                    if part[0] == cr[0] and float(part[1]) > float(cr[1]):
                        filter_list.append(item)
                except:
                    print("error while filtring sensor data")
        return filter_list


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        count_reading = 0
        buy_count = 0
        sell_count = 0
        for item in data_batch:
            if isinstance(item, str):
                part = item.split(":")
                if part[0] == "sell":
                    try:
                        sell_count += int(part[1])
                    except:
                        print("Transiction Error: data incorrect")
                elif part[0] == "buy":
                    try:
                        buy_count += int(part[1])
                    except:
                        print("Transiction Error: data incorrect")
            count_reading += 1
        return f"{count_reading} operations, net flow: +{buy_count - sell_count} units"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        filter_list = []
        if not criteria:
            return filter_list
        for item in data_batch:
            if isinstance(item, str):
                part = item.split(":")
                cr = criteria.split(":")
                if part[0] == cr[0]:
                    try:
                        if float(part[1]) > float(cr[1]):
                            filter_list.append(item)
                    except:
                        print("error while filtring transiction data")
        return filter_list


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        count_error = 0
        count_reading = 0
        for item in data_batch:
            count_reading += 1
            if isinstance(item, str) and item == "error":
                count_error += 1
        return f"{count_reading} events, {count_error} error detected"


class StreamProcessor:
    def __init__(self):
        self.streams = []

    def add_streams(self, stream):
        self.streams.append(stream)

    def process_streams(self, data_batch: List[Any]):
        i = 0
        while i < len(self.streams):
            st = self.streams[i]
            data = data_batch[i]
            if isinstance(st, SensorStream):
                print("Initializing Sensor Stream...")
                print(f"Stream ID: {st.stream_id}, Type: Environmental Data")
                print(f"Processing sensor batch: {data}")
                print(f"Sensor analysis: {st.process_batch(data)}")
                print("")
            elif isinstance(st, TransactionStream):
                print("Initializing Transaction Stream...")
                print(f"Stream ID: {st.stream_id}, Type: Financial Data")
                print(f"Processing event batch: {data}")
                print(f"Event analysis: {st.process_batch(data)}")
                print("")
            elif isinstance(st, EventStream):
                print("Initializing Event Stream...")
                print(f"Stream ID: {st.stream_id}, Type: System Events")
                print(f"Processing event batch: {data}")
                print(f"Event analysis: {st.process_batch(data)}")
                print("")
            i += 1


def main():
    data = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"],
    ]
    sensor = SensorStream("SENSOR_001")
    transiction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    st_precessor = StreamProcessor()
    st_precessor.add_streams(sensor)
    st_precessor.add_streams(transiction)
    st_precessor.add_streams(event)
    st_precessor.process_streams(data)
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("")
    print("Batch 1 Results:")
    data_batch = [
        ["temp:39.5", "humidity:6"],
        ["buy:100", "sell:150", "buy:75", "sell:10"],
        ["login", "error", "logout"],
    ]
    print(f"- Sensor data: {sensor.process_batch(data_batch[0]).split(",")[0]}")
    print(
        f"- Transaction data: {transiction.process_batch(data_batch[1]).split(",")[0]} processed"
    )
    print(
        f"- Event data: {transiction.process_batch(data_batch).split(",")[0]} processed"
    )
    print("")
    print("Stream filtering active: High-priority data only")
    critical = sensor.filter_data(["temp:32.5", "temp: 30.5", "temp: 20"], "temp:30")
    large_transiction = transiction.filter_data(
        ["buy:120", "sell:150", "buy:175", "sell:105"], "buy:150"
    )
    print(
        f"Filtered results: {len(critical)} critical sensor alerts, {len(large_transiction)} large transaction"
    )
    print("")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    main()
