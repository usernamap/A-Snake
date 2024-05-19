# game.py
import random
import logging
from game_config import *
from ai import astar
import numpy as np

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    filename="snake_game_ai.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    import pygame
except ImportError:
    pygame = None


class SnakeGame:
    def __init__(self, visualize=True, real_time_visualize=True, display_mode="full"):
        self.visualize = visualize
        self.real_time_visualize = real_time_visualize
        self.display_mode = display_mode
        if display_mode == "full":
            if pygame:
                pygame.init()
                self.width = self.height = TAILLE_CASE * NB_CASES
                self.screen = pygame.display.set_mode((self.width, self.height + 40))
                self.clock = pygame.time.Clock()
                self.font = pygame.font.Font(None, POLICE_TAILLE)
            else:
                raise ImportError(
                    "Pygame is not available but DISPLAY_MODE is set to full."
                )
        self.total_steps = 0
        self.best_score = self.load_best_score()
        self.reset_game()

    def load_best_score(self):
        try:
            with open("best_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_best_score(self):
        with open("best_score.txt", "w") as file:
            file.write(str(self.best_score))

    def reset_game(self):
        self.snake = [self.get_center()]
        self.direction = pygame.math.Vector2(0, -1)  # Start moving up
        self.food = self.place_food()
        self.score = 0
        self.done = False
        logging.info("Game reset.")
        print("Game reset.")

    def get_center(self):
        return NB_CASES // 2, NB_CASES // 2

    def place_food(self):
        while True:
            pos = (random.randint(0, NB_CASES - 1), random.randint(0, NB_CASES - 1))
            if pos not in self.snake:
                logging.info(f"Food placed at {pos}.")
                print(f"Food placed at {pos}.")
                return pos

    def run_step(self, direction):
        self.total_steps += 1
        new_head = tuple(self.snake[0] + direction)
        collision = self.check_collision(new_head)
        if collision:
            self.done = True
            logging.warning(f"Collision detected at {new_head}. Game over.")
            print(f"Collision detected at {new_head}. Game over.")
            return PENALTY_COLLISION, self.done
        self.move_snake(new_head)
        reward = REWARD_MOVE

        # Reward for getting closer to the food
        if np.linalg.norm(np.array(new_head) - np.array(self.food)) < np.linalg.norm(
            np.array(self.snake[0]) - np.array(self.food)
        ):
            reward += REWARD_CLOSE_FOOD

        logging.debug(
            f"Step: {self.total_steps}, Move: {direction}, Reward: {reward}, New Head: {new_head}"
        )
        print(
            f"Step: {self.total_steps}, Move: {direction}, Reward: {reward}, New Head: {new_head}"
        )

        if self.visualize and self.display_mode == "full":
            self.update_screen()
        return reward, self.done

    def move_snake(self, new_head):
        if new_head == self.food:
            self.score += REWARD_APPLE
            self.food = self.place_food()
            logging.info(f"Food eaten at {new_head}. New score: {self.score}.")
            print(f"Food eaten at {new_head}. New score: {self.score}.")
        else:
            self.snake.pop()
        self.snake.insert(0, new_head)

    def check_collision(self, new_head):
        collision = (
            new_head[0] < 0
            or new_head[0] >= NB_CASES
            or new_head[1] < 0
            or new_head[1] >= NB_CASES
            or new_head in self.snake[1:]
        )
        if collision:
            logging.warning(f"Collision detected at {new_head}.")
            print(f"Collision detected at {new_head}.")
        return collision

    def update_screen(self):
        if self.display_mode == "full":
            self.screen.fill((0, 0, 0))
            self.draw_elements()
            self.draw_info()
            pygame.display.flip()
            self.clock.tick(FPS)

    def draw_elements(self):
        for segment in self.snake:
            rect = pygame.Rect(
                segment[0] * TAILLE_CASE,
                segment[1] * TAILLE_CASE,
                TAILLE_CASE,
                TAILLE_CASE,
            )
            pygame.draw.rect(self.screen, COULEUR_SERPENT, rect)
        apple_rect = pygame.Rect(
            self.food[0] * TAILLE_CASE,
            self.food[1] * TAILLE_CASE,
            TAILLE_CASE,
            TAILLE_CASE,
        )
        pygame.draw.ellipse(self.screen, COULEUR_NOURRITURE, apple_rect)

    def draw_info(self):
        if self.display_mode == "full":
            info_text = f"Score: {self.score} Best: {self.best_score}"
            rendered_text = self.font.render(info_text, True, (255, 255, 255))
            self.screen.blit(rendered_text, (10, self.height + 10))

    def draw_winner(self):
        if self.display_mode == "full":
            self.screen.fill((0, 0, 0))
            winner_text = "You Win!"
            rendered_text = self.font.render(winner_text, True, (255, 255, 255))
            self.screen.blit(
                rendered_text, (self.width // 2 - 50, self.height // 2 - 10)
            )
            pygame.display.flip()

    def draw_loser(self):
        if self.display_mode == "full":
            self.screen.fill((0, 0, 0))
            loser_text = "Game Over!"
            rendered_text = self.font.render(loser_text, True, (255, 255, 255))
            self.screen.blit(
                rendered_text, (self.width // 2 - 50, self.height // 2 - 10)
            )
            pygame.display.flip()

    def run_with_ai(self):
        self.reset_game()
        while not self.done:
            path = astar(self.snake[0], self.food, self.snake, NB_CASES)
            if path and len(path) > 1:
                next_move = pygame.math.Vector2(
                    path[1][0], path[1][1]
                ) - pygame.math.Vector2(path[0][0], path[0][1])
                reward, done = self.run_step(next_move)
                logging.info(f"Path found. Next move: {next_move}. Reward: {reward}.")
                print(f"Path found. Next move: {next_move}. Reward: {reward}.")
            else:
                self.done = True
                logging.warning("No path found. Ending game.")
                print("No path found. Ending game.")

            if self.done:
                self.best_score = max(self.best_score, self.score)
                self.save_best_score()
                logging.info(
                    f"Game Over. Score: {self.score}, Best score: {self.best_score}"
                )
                print(f"Game Over. Score: {self.score}, Best score: {self.best_score}")
                break

            if self.visualize and self.display_mode == "full":
                self.update_screen()
