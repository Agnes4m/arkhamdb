from pydantic import BaseModel, validator
from typing import List


class SupportCard(BaseModel):
    name: str
    cost: int
    attribute: List[str]
    is_flash: bool = False


class PlayerSupport(BaseModel):
    ally: List[SupportCard] = []
    hands: List[SupportCard] = []
    spells: List[SupportCard] = []
    artifact: List[SupportCard] = []
    tarot: List[SupportCard] = []
    other_supports: List[SupportCard]

    @validator("hands")
    def validate_hands(cls, hands, values, max_items=2, required_attributes=None):
        if required_attributes is None:
            required_attributes = []

        # 检查是否存在超过指定数量的支援卡
        if len(hands) > max_items:
            raise ValueError(f"手部位置只能有最多 {max_items} 张支援卡")

        # 检查是否存在指定属性的支援卡
        for attribute in required_attributes:
            if not any(attribute in card.attributes for card in hands):
                raise ValueError(f"手部位置至少需要一张具有属性 {attribute} 的支援卡")

        return hands


class Player(BaseModel):
    supports: PlayerSupport
