from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=5, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=100)
    is_verified: bool = Field(default=False)
    # model_validator

    @model_validator(mode='after')
    def validate_data(self) -> 'AlienContact':
        # 1 - contact ID must start with AC:
        if not self.contact_id.startswith('AC'):
            raise ValueError('contact ID must start with AC')
        # 2 Physical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        # 3 - Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        # 4. Strong signals (>7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) must include a received message")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("============================")
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-11-01T22:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.physical,  # Automatically cast to Enum
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from MNT",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type : {valid.contact_type}")
        print(f"Location : {valid.location}")
        print(f"Signal : {valid.signal_strength}/ 10")
        print(f"Duration : {valid.duration_minutes} minuets")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message {valid.message_received}")

    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
