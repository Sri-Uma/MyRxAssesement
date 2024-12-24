from datetime import datetime
from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zipcode: str

@dataclass(frozen=True)
class ImmutableClass:
    name: str
    id: str
    date_of_joining: datetime
    addresses: List[Address]

    def __post_init__(self):
        # Enforce immutability for the addresses list
        object.__setattr__(self, 'addresses', tuple(self.addresses))

# Example usage
if __name__ == "__main__":
    address1 = Address("Punjagutta", "Hyderabad", "TS", "500082")

    immutable_object = ImmutableClass(
        name="Sri Uma",
        id="001",
        date_of_joining=datetime(2022, 1, 15),
        addresses=[address1]
    )

    print(immutable_object)
    # Attempting to modify an attribute will raise a FrozenInstanceError
    # immutable_object.name = "Jane Doe"  # Uncommenting this line will raise an error
