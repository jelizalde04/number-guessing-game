# Number Guessing Game

This is a simple Python-based number guessing game where the computer selects a random number between 1 and 100, and the player has 3 attempts to guess it.

## Features

- The computer generates a random number between 1 and 100.
- The player has 3 attempts to guess the number.
- After each guess, the game will tell the player if the guess was too high, too low, or correct.
- The game ends when the player guesses the correct number or exhausts all attempts.

## How to Run the Game Locally

Follow the steps below to run the game on your local machine:

1. **Clone this repository:**

    ```bash
    git clone https://github.com/jelizalde04/number-guessing-game.git
    cd number-guessing-game
    ```

2. **Install Python (if you don't have it installed):**

    - Download and install Python 

3. **Run the Python script:**

    ```bash
    python app.py
    ```

4. The game will start, and you can begin guessing the number.

## How to Run with Docker

If you prefer to run the game using Docker, follow these steps:

1. **Build the Docker image:**

    ```bash
    docker build -t number-guessing-game .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 number-guessing-game
    ```

    This will start the game within a Docker container, accessible on port 5000.

