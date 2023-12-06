from pydantic import BaseModel
from .assist import Ally

# from .card import SupportCard, PlayerSupport


class PLOT(BaseModel):
    """密谋"""

    order: str
    name: str
    description: str
    max_plot_points: int
    plot_points: int


class SCENE(BaseModel):
    """场景"""

    order: str
    name: str
    description: str
    max_scene_points: int
    scene_points: int


class Blood(BaseModel):
    """血量"""

    max_blood_points: int
    """最大血量"""
    wound_blood_points: int
    """肉体创伤"""
    blood_points: int
    """当前血量"""


class San(BaseModel):
    """血量"""

    max_san_points: int
    """最大理智"""
    wound_san_points: int
    """精神创伤"""
    san_points: int
    """当前理智"""


class Player(BaseModel):
    """玩家"""

    order: str
    name: str = ""
    description: str = ""
    blood: Blood
    san: San
    ally: Ally
    ally_list: list = []
