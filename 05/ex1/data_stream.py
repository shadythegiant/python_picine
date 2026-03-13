from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = [x for x in data_batch if isinstance(x, (int, float))]
            if not readings:
                return "Sensor analysis: No valid readings in batch"

            avg = sum(readings) / len(readings)
            self.processed_count += len(readings)
            return (
                f"Sensor analysis: {len(readings)} readings processed, "
                f"avg: {avg:.1f}"
            )
        except Exception:
            self.error_count += 1
            return "Sensor analysis: Error processing batch"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_tx = [x for x in data_batch if isinstance(
                x, dict) and "amount" in x]
            net_flow = sum(x["amount"] if x.get("type") ==
                           "buy" else -x["amount"] for x in valid_tx)

            self.processed_count += len(valid_tx)
            return (
                f"Transaction analysis: {len(valid_tx)} operations, "
                f"net flow: {net_flow:+d} units"
            )
        except Exception:
            self.error_count += 1
            return "Transaction analysis: Error processing batch"


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [str(x) for x in data_batch]
            errors = len([x for x in events if "error" in x.lower()])

            self.processed_count += len(events)
            return (
                f"Event analysis: {len(events)} events, "
                f"{errors} error(s) detected"
            )
        except Exception:
            self.error_count += 1
            return "Event analysis: Error processing batch"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, multi_batch: List[List[Any]]) -> List[str]:
        results = []
        for stream, batch in zip(self.streams, multi_batch):
            results.append(stream.process_batch(batch))
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = [
        [22.5, 23.0, "invalid", 21.8],
        [{"type": "buy", "amount": 100}, {
            "type": "sell", "amount": 50}],
        ["login", "system_error", "logout"]
    ]

    results = processor.process_all(batches)
    for res in results:
        print(res)

    print("\nStream Statistics:")
    for s in [sensor, transaction, event]:
        print(s.get_stats())


if __name__ == "__main__":
    main()
