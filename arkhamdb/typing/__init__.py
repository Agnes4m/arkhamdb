from arkhamdb.typing import AllSence
from arkhamdb.typing.assist import *  # noqa: F403
from arkhamdb.typing.card import *  # noqa: F403
from arkhamdb.typing.sence import *  # noqa: F403

from typing import TypedDict


class Game(TypedDict):
    """游戏"""

    group_id: str
    """群号"""
    player_id: list[str]
    game_name: str
    """关卡名称"""
    sence: AllSence
