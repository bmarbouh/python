#!/usr/bin/env python3
from enum import Enum
from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from typing import List


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=300)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode="after")
    def validition(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("ID must start with 'M'")
        require = [Rank.commander, Rank.captain]
        if not any(m.rank in require for m in self.crew):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew" " (5+ years)"
                )
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(f"All crew members must be active. Inactive: {inactive}")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    crew_list = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.officer,
            age=40,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.commander,
            age=32,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.captain,
            age=27,
            specialization="Engineering",
            years_experience=5,
        ),
    ]

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-09-01T06:00:00",
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for p in mission.crew:
            print(f"- {p.name} ({p.rank}) - {p.specialization}")
    except ValidationError as v:
        print("Expected validation error:")
        for error in v.errors():
            print(error["msg"])
    print("")
    print("=" * 40)
    invalid_crew_list = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.officer,
            age=40,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.cadet,
            age=32,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.lieutenant,
            age=27,
            specialization="Engineering",
            years_experience=5,
        ),
    ]
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-09-01T06:00:00",
            duration_days=900,
            crew=invalid_crew_list,
            budget_millions=2500.0,
        )
    except ValidationError as v:
        print("Expected validation error:")
        for error in v.errors():
            print(error['msg'].split(", ")[1])


if __name__ == "__main__":
    main()
