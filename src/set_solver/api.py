from __future__ import annotations

from pathlib import Path

from set_solver import SetGame


def solve_image(image_path: str | Path) -> SetGame:
    game = SetGame(str(image_path))
    game.solve()
    return game
