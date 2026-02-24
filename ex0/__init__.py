__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .Card import play, is_playable
from .CreatureCard import get_card_info

__all__ = ["play", "is_playable", "get_card_info"]
