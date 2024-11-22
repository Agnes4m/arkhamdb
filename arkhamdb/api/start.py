
from typing import Literal


class Start:
    async def __init__(self):
        pass
    
    
    @classmethod
    async def start(
        cls,
        player_number: Literal[1, 2, 3, 4],
        initial_cards: list[int],
        initial_cost: list[int],
    ):
        """游戏初始化操作"""