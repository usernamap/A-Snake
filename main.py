# main.py
from game import SnakeGame
import sys
from game_config import DISPLAY_MODE


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "console":
        display_mode = "console"
    else:
        display_mode = DISPLAY_MODE

    game = SnakeGame(
        visualize=True, real_time_visualize=False, display_mode=display_mode
    )
    game.run_with_ai()


if __name__ == "__main__":
    main()
