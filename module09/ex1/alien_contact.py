#!/usr/bin/env python3
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional

class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"
    

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15),
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100),
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10),
    duration_minutes: int = Field(ge=1, le=1440),
    witness_count: int = Field(ge=1, le=100),
    message_received: Optional[str] = Field(le=500),
    is_verified: bool = Field(default=False),
    
    @model_validator(mode="after")
    def validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID must start with 'AC'")
        if self.contact_type ==  ContactType.physical and not self.is_verified:
            raise ValueError("Physical Contact must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self
    
def main():
    print("Alien Contact Log Validation")
    print("="*40)
    try:
        print("Valid contact report:")
        valide = AlienContact(
            contact_id = "AC_2024_001",
            timestamp = "2024-06-15T22:30:00",
            location = "Area 51, Nevada",
            contact_type = ContactType.radio,
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 5,
            message_received = "'Greetings from Zeta Reticuli'",
            is_verified = True
        )
        print(f"ID: {valide.contact_id}")
        print(f"Type: {valide.contact_type}")
        print(f"Location: {valide.location}")
        print(f"Signal: {valide.signal_strength}/10")
        print(f"Duration: {valide.duration_minutes} minutes")
        print(f"Witnesses: {valide.witness_count}")
        print(f"Message: {valide.message_received}")
    except ValidationError as v:
        print("Expected validation error:")
        for error in v.errors:
            print(error['msj'])
    print("=" * 40)
    
    try:
        pass
    except ValidationError as v:
        pass

main()