from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List


class CrewRanks(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    commander = "commander "
    captain = "captain"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=15)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        # 1- validating name
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission Id must start With 'M'☠️")
        # 2 validating req for leadership
        has_leadership = any(c.rank in (CrewRanks.commander, CrewRanks.captain)
                             for c in self.crew)
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain☠️")
        # 3 long mission and experience
        if self.duration_days > 365:
            experienced_count = sum(
                1 for c in self.crew if c.years_experience >= 5)
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError(
                    "Long missions require at least 50% of crew to have"
                    " 5+ years experience ☠️"
                )
        # 4 all crew members must be active :
        if not all(c.is_active for c in self.crew):
            raise ValueError("all crew members must be active ☠️")
        # ☠️ -> always return self
        return self


def main() -> None:
    abde_aljabr = CrewMember(
        member_id="C001",
        name="abodaljabr lmrakechi",
        rank=CrewRanks.commander,
        age=45,
        specialization="Command",
        years_experience=20
    )
    karima = CrewMember(
        member_id="C002",
        name="KArim saiida",
        rank=CrewRanks.lieutenant,
        age=30,
        specialization="Navigation",
        years_experience=6
    )
    adil = CrewMember(
        member_id="C003",
        name="adil the New Guy",
        rank=CrewRanks.cadet,
        age=19,
        specialization="Engineering",
        years_experience=0
    )
    print("Space Mission Crew Validation")
    print("=============================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-01-01T00:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[abde_aljabr, karima, adil]
        )
        print("Valid mission created:")
        print(f"Mission  :{mission.mission_name}")
        print(f"ID : {mission.mission_id}")
        print(f"destination : {mission.destination}")
        print(f"duration : {mission.duration_days} days")
        print(f"Budget : ${mission.budget_millions}M")
        print(f"crew size :{ len(mission.crew)}")
        print("Crew Members :")
        for c in mission.crew:
            print(f"- {c.name} ({c.rank}) - {c.specialization}")
    except ValidationError as e:
        print(e)
    print("\n ========================================")
    print("Expected invalid data")
    try:
        invalid = SpaceMission(
            mission_id="2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-01-01T00:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[abde_aljabr, karima, adil]
        )
        print(invalid.mission_name)

    except ValidationError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])


if __name__ == "__main__":
    main()
