#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)
    
def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name=" International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T08:00:00",
            is_operational=True
            )
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        print(
            "Status: Operational\n"
            if valid.is_operational
            else "Status: Not Operational\n"
            )
        print("=" * 40)
        not_valid = SpaceStation(
            station_id="ISS001",
            name=" International Space Station",
            crew_size=26,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T08:00:00",
            is_operational=True
            )
    except ValidationError as v:
        print("Expected validation error:")
        for error in v.errors():
            print(error['msg'])

if __name__ == "__main__":
    main()