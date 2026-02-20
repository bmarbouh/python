#!/usr/bin/env python3
from abc import ABC,abstractmethod
from typing import Any,List,Optional,Union,Dict


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_item = 0
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id" : self.stream_id,
            "processed_item" : self.processed_item
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        s_tmp = 0
        avg_tmp = 0
        count = 0
        while count < len(data_batch):
            if isinstance(data_batch[count],str):
                item = data_batch[count].split(":")
                if item[0] == "temp":
                    try:
                        s_tmp += float(item[1])
                        avg_tmp += 1
                    except ValueError:
                        print("temp: is not a valid number")
            count += 1
        if avg_tmp > 0:
            avg_tmp = s_tmp / avg_tmp
        else:
            avg_tmp = 0.0
        return f"{count} readings processed, avg temp: {avg_tmp}°C"
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        buy_count = 0
        sell_count = 0
        while count < len(data_batch):
            if isinstance(data_batch[count],str):
                item = data_batch[count].split(":")
                if item[0] == "buy":
                    try:
                        buy_count += int(item[1])
                    except :
                        print("buy item have value not a number")
                if item[0] == "sell":
                    try:
                        sell_count += int(item[1])
                    except:
                        print("sell item have a value not a number")
            count += 1
        flow  = buy_count - sell_count
        return f"Transaction analysis: {count} operations, net flow: +{flow} units"
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class StreamProcessor():
    pass


def main():
    # sensor stream test
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_data}")
    print(f"Sensor analysis: {sensor.process_batch(sensor_data)}")
    print("")
    # transiction stream test
    print("Initializing Transaction Stream...")
    transiction = TransactionStream("TRANS_001")
    transiction_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transiction_data}")
    print(f"Transaction analysis: {transiction.process_batch(transiction_data)}")
    print("")
    # event stream test
    print(f"Initializing Event Stream...")
    event = EventStream("EVENT_001")
    event_data =  ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    main()