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
        self.processed_item += len(data_batch)
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
        high_tmp = []
        i = 0
        while i < len(data_batch):
            if isinstance(data_batch[i],str):
                item = data_batch[i].split(":")
                try:
                    if int(item) > int(criteria):
                        high_tmp.append(data_batch[i])
                except:
                    print("filtring error")
            i += 1
        return high_tmp
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_item += len(data_batch)
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
        filter_criteria = []
        i = 0
        while i < len(data_batch):
            try:
                if isinstance(data_batch[i],str):
                    item = data_batch[i].split(":")
                    
                i += 1 
            except:
                print("has en error while filtring data")
            return filter_criteria
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_item += len(data_batch)
        count = 0
        errors = 0
        while count < len(data_batch):
            if isinstance(data_batch[count],str) and data_batch[count] == "error":
                errors += 1
            count += 1
        return f"Event analysis: {count} events, {errors} error detected"
    
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
    print(f"Event analysis: {event.process_batch(event_data)}")
    print("")
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("")
    print("Batch 1 Results:")
    


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    main()
    a = ["temp:50","temp:120","temp:800","temp:700"]
    b = TransactionStream("sx")
    print(b.filter_data(a,"temp:60"))





