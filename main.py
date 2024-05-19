import sys
import signal
from game import SnakeGame
from game_config import DISPLAY_MODE
import cProfile
import pstats


def signal_handler(sig, frame):
    print("\nProgram interrupted! Exiting ...")
    sys.exit(0)


def main():
    display_mode = sys.argv[1] if len(sys.argv) > 1 else DISPLAY_MODE

    game = SnakeGame(
        visualize=True, real_time_visualize=False, display_mode=display_mode
    )
    game.run_with_ai()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    cProfile.run("main()", "profile_stats")
    with open("profile_results.txt", "w") as f:
        p = pstats.Stats("profile_stats", stream=f)
        p.sort_stats("cumulative").print_stats(50)
