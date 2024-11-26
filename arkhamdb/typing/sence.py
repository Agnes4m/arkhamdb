from typing import TypedDict
from .assist import Ally

# from .card import SupportCard, PlayerSupport


class PLOT(TypedDict):
    """密谋"""

    order: str
    """密谋序号"""
    name: str
    """密谋昵称"""
    description: str
    """密谋介绍"""
    max_plot_points: int
    """推进密谋最大点数"""
    plot_points: int
    """当前密谋点数"""
    extra_points: int
    """额外密谋点数"""


class SCENE(TypedDict):
    """场景"""

    order: str
    """场景序号"""
    name: str
    """场景昵称"""
    description: str
    """场景介绍"""


class Blood(TypedDict):
    """血量"""

    max_blood_points: int
    """最大血量"""
    wound_blood_points: int
    """肉体创伤"""
    blood_points: int
    """当前血量"""


class San(TypedDict):
    """理智"""

    max_san_points: int
    """最大理智"""
    wound_san_points: int
    """精神创伤"""
    san_points: int
    """当前理智"""


class Player(TypedDict):
    """玩家"""

    order: str
    name: str
    description: str
    blood: Blood
    san: San
    ally: Ally
    ally_list: list

class AllSence(TypedDict):
    polt: PLOT
    scene: SCENE
    players: list[Player]