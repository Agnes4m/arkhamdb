from typing import TypedDict


# class SpecialAlly(TypedDict):
#     """特殊盟友类型"""

#     ally_type: str
#     """盟友类型"""
#     max_ally_points: int
#     """最大盟友位"""
#     ally_points: int
#     """已占用盟友位"""
#     ally_spare: int
#     """空余盟友位"""


# class Ally(BaseModel):
#     """盟友"""

#     max_ally_points: int
#     """最大盟友位"""
#     ally_points: int
#     """已占用盟友位"""
#     ally_spare: int
#     """空余盟友位"""
#     other_ally: list[SpecialAlly] = []
#     """额外盟友"""


class SpecialBase(TypedDict):
    is_sure: bool
    """必要还是不能"""
    hand_attribute: list[str]
    """指定属性"""
    number: int
    """限制数量"""


class Base(TypedDict):
    max_hand_points: int
    """最大部位"""
    any_hand_points: int
    """任意属性部位"""
    hand_points: int
    """已占用部位"""
    hand_spare: int
    """空余部位"""
    hand_attribute: SpecialBase
    """特殊限制"""


class Limitpart(TypedDict):
    """基础限制数量"""

    ally: int
    hand: int
    spells: int
    artifact: int
    other: int
