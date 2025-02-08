from settings import SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT
import random

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.coordinates = [0, 0]  # Placeholder for food position
        self.food_object = None  # Store reference to the food object
        self.spawn_food()  # Spawn first food

    def spawn_food(self):
        """Spawn food at a new random position with a glowing effect"""
        # Remove previous food if it exists
        if self.food_object:
            self.canvas.delete(self.food_object)

        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]  # Update food position

        # Draw food with a glowing effect
        self.food_object = self.canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, outline="yellow", width=3, tag="food"
        )



