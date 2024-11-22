from typing import TypedDict
from typing import List


class SupportCard(TypedDict):
    name: str
    cost: int
    attribute: List[str]
    is_flash: bool

class PlayerSupport(TypedDict):
    ally: List[SupportCard]
    hands: List[SupportCard]
    spells: List[SupportCard]
    artifact: List[SupportCard]
    tarot: List[SupportCard]
    other_supports: List[SupportCard]


class Player(TypedDict):
    supports: PlayerSupport
