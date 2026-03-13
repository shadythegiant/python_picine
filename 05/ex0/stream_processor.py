from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            print("Validation: Numeric data verified")
            return True
        return False

    def process(self, data: List[Union[int, float]]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data provided")

        count = len(data)
        total = sum(data)
        avg = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg:.1f}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data provided")

        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and (":" in data):
            print("Validation: Log entry verified")
            return True
        return False

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data provided")

        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()
        prefix = "[ALERT]" if level in ["ERROR", "CRITICAL"] else "[INFO]"
        return f"{prefix} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("\nInitializing Numeric Processor...")
    num_proc = NumericProcessor()
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    print(num_proc.format_output(num_proc.process(data_num)))

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    data_text = "Hello Nexus World"
    print(f"Processing data: \"{data_text}\"")
    print(text_proc.format_output(text_proc.process(data_text)))

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_log}\"")
    print(log_proc.format_output(log_proc.process(data_log)))
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors: List[DataProcessor] = [
        NumericProcessor(), TextProcessor(), LogProcessor()]
    mixed_data = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]

    for i, (proc, data) in enumerate(zip(processors, mixed_data), 1):
        try:
            result = proc.process(data)
            print(f"Result {i}: {result}")
        except Exception as e:
            print(f"Error in Result {i}: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
