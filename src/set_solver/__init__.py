from __future__ import annotations

import sys
from pathlib import Path

_LEGACY_ROOT = Path(__file__).resolve().parents[2]
if str(_LEGACY_ROOT) not in sys.path:
    sys.path.insert(0, str(_LEGACY_ROOT))

from SetGame import SetGame  # noqa: E402
from classify_card import classify_card_from_file, classify_card_from_im  # noqa: E402
from common import game_img_filename  # noqa: E402

__all__ = [
    "SetGame",
    "classify_card_from_file",
    "classify_card_from_im",
    "game_img_filename",
]
