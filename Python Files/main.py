from tkinter import Tk, Label, Canvas
from settings import GAME_WIDTH, GAME_HEIGHT, BACKGROUND_COLOR, SPEED, SPACE_SIZE, SNAKE_COLOR
from snake import Snake
from food import Food

# Create the game window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Score label
score = 0
label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

# Game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()


# Draw Grid for Retro Pixel Look
def draw_grid():
    """Draw a retro pixel grid on the background"""
    for x in range(0, GAME_WIDTH, SPACE_SIZE):
        canvas.create_line(x, 0, x, GAME_HEIGHT, fill="#333333")  # Vertical lines
    for y in range(0, GAME_HEIGHT, SPACE_SIZE):
        canvas.create_line(0, y, GAME_WIDTH, y, fill="#333333")  # Horizontal lines


draw_grid()  # Call before the game starts

# Create game objects
snake = Snake(canvas)
food = Food(canvas)

# Default movement direction
direction = "right"
game_running = True  # Track if the game is running


def change_direction(new_direction: str):
    """Change the direction of the snake, preventing 180° turns."""
    global direction
    if new_direction == "up" and direction != "down":
        direction = "up"
    elif new_direction == "down" and direction != "up":
        direction = "down"
    elif new_direction == "left" and direction != "right":
        direction = "left"
    elif new_direction == "right" and direction != "left":
        direction = "right"


def next_turn():
    """Move the snake and check for collisions."""
    global direction, score, game_running

    if not game_running:
        return  # Stop updating if the game is over

    x, y = snake.coordinates[0]  # Get current head position

    # Move the snake in the correct direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Prevent game over from triggering before the snake moves
    if len(snake.coordinates) > 3:  # Only check collisions after a few moves
        # Properly detect collision with all walls
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            game_over()
            return

        # Check if the snake bites itself (Game Over)
        if [x, y] in snake.coordinates[1:]:  # Ignore the first position
            game_over()
            return

    # Check if the snake eats food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")  # Update score label
        canvas.delete("food")  # Remove old food
        food.spawn_food()  # Spawn new food
    else:
        # Remove last segment to simulate movement
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Update snake's position
    snake.coordinates.insert(0, [x, y])
    segment = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR,
                                 outline="gray", width=2, tag="snake")
    snake.squares.insert(0, segment)

    window.after(SPEED, next_turn)


def game_over():
    """Display 'GAME OVER' with a smooth fade-in effect."""
    global game_running
    game_running = False  # Stop the game loop

    for i in range(10):  # Create a fading effect with 10 flashes
        color = "red" if i % 2 == 0 else "black"  # Alternate between red and black
        canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2,
                           text="GAME OVER", font=('consolas', 50), fill=color, tag="gameover")
        window.update()
        window.after(100)

    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2,
                       text="GAME OVER", font=('consolas', 50, 'bold'), fill="red", tag="gameover")


# Start the game after 1 second to prevent instant game over
window.after(1000, next_turn)

# Bind arrow keys for controls
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

# Start the game loop
window.mainloop()
