from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Store the number to guess and attempts globally
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 3

@app.route('/', methods=['GET', 'POST'])
def index():
    global attempts, number_to_guess, max_attempts
    message = ""
    
    if request.method == 'POST':
        try:
            # Check if maximum attempts reached
            if attempts >= max_attempts:
                message = f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}. Try again!"
                # Restart game after attempts exhausted
                number_to_guess = random.randint(1, 100)
                attempts = 0
            else:
                # Get user's guess
                guess = int(request.form['guess'])
                attempts += 1

                if guess < number_to_guess:
                    message = "Too low! Try again."
                elif guess > number_to_guess:
                    message = "Too high! Try again."
                else:
                    message = f"Correct! The number was {number_to_guess}. You guessed it in {attempts} attempts."
                    # Restart with new number after correct guess
                    number_to_guess = random.randint(1, 100)
                    attempts = 0
        
        except ValueError:
            message = "Please enter a valid number."
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

