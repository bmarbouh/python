#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        data_list = list(data)
        count = len(data_list)
        total = sum(data_list)
        avg = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"
    
    def validate(self, data: Any) -> bool:
        data_list = list(data)
        try:
            for i in data_list:
                int(i)
            return True
        except:
            return False
    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(self, data):
        str_data = str(data)
        size = len(str_data)
        count_word = len(str_data.split(" "))
        return f"Processed text: {size} characters, {count_word} words"

    def validate(self, data):
        if isinstance(data,str):
            return True
        else:
            return False
    def format_output(self, result):
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def process(self, data):
        log_type = str(data).split(":")
        return f"Output: [ALERT] {log_type[0]} level detected: {log_type[1]}"


    def validate(self, data):
        if not isinstance(data,str):
            return False
        avilable_log = ["INFO", "ERROR", "DEBUG", "WARNING", "ALERT"]
        for log in avilable_log:
            if data.startswith(log):
                return True
        return False

    def format_output(self, result):
        return f"Output: {result}" 




def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")
    #Numeric Handle
    data_num = [1,2,3,4,5]
    num = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data_num}")
    if num.validate(data_num):
        print("Validation: Numeric data verified")
        print(num.format_output(num.process(data_num)))
    else:
        print("Validition: Insucssusfull Validte")
        print(num.format_output("Not availible"))
    #Text Handle
    print("")
    print("Initializing Text Processor...")
    data_text = "Hello Nexus World"
    text = TextProcessor()
    print(f"Processing data: {data_text}")
    if text.validate(data_text):
        print("Validation: Text data verified")
        print(text.format_output(text.process(data_text)))
    else:
        print("Validition: Insucssusfull Validte")
        print(num.format_output("Not availible"))
    # log handle
    print("")
    print("Initializing Log Processor...")
    data_log = "ERROR: Connection timeout"
    log = LogProcessor()
    print(f"Processing data: {data_log}")
    if log.validate(data_log):
        print("Validation: Log entry verified")
        print(log.format_output(log.process(data_log)))
    else:
        print("Validation: Log entry Not verified")
        print(log.format_output("Not availible"))
    print("")
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    all_data = [[1, 2, 3], "Hello Nexuss", "INFO: System ready"]
    classes = [NumericProcessor(), TextProcessor(), LogProcessor()]
    i = 0
    while i < len(all_data):
        proc = classes[i]
        data = all_data[i]
        if proc.validate(data):
            print(f"Result {i + 1}: {proc.process(data)}")
        i += 1
    print("")
    print("Foundation systems online. Nexus ready for advanced streams.")




if __name__ == "__main__":
    main()

