from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    # strings
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)

    # ints & floats
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygene_level: float = Field(ge=0.0, le=100.0)

    # complex types
    last_maintenance: datetime

    # boolean and Optional
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None)


def main() -> None:
    today = datetime.today()
    print("\nSpace Station Data Validation")
    print("==============================")
    try:
        valid_station = SpaceStation(
            station_id="ISS1337",
            name="UM6P international station",
            crew_size=20,
            power_level=20.5,
            oxygene_level=43.3,
            last_maintenance=today)
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygene_level}%")
        print(f"Last maintenance : {valid_station.last_maintenance}")
        status = "Operational" if valid_station.is_operational else "Offline"
        print(f"Status: {status}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")
    print("\n================================================")
    print("Testing invalid data  ☠️")
    try:
        non_valid_station = SpaceStation(
            station_id="ISS1337",
            name="UM6P international station",
            crew_size=25,
            power_level=20.5,
            oxygene_level=43.3,
            last_maintenance=today)
        print(f"invalid_station's name = {non_valid_station.name}")

    except ValidationError as e:
        for errors in e.errors():
            print(errors['loc'], errors['msg'])


if __name__ == "__main__":
    main()
