from flask import Flask, render_template, jsonify
import random
import os

# Initialize Flask application
app = Flask(__name__)

# Configure security settings
# In production, SECRET_KEY will be set by environment variable
# In development, we use a default key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')

# Define South African themed symbols with their corresponding payout values
# Symbols are arranged in descending order of value
# Each symbol represents an aspect of South African culture or wildlife
SYMBOLS = [
    {"name": "lion", "value": 500},      # Highest value - King of the savanna
    {"name": "elephant", "value": 400},   # Symbol of wisdom and strength
    {"name": "rhino", "value": 300},      # Symbol of power and protection
    {"name": "protea", "value": 250},     # South Africa's national flower
    {"name": "springbok", "value": 200},  # National animal
    {"name": "diamond", "value": 150},    # Representing mineral wealth
    {"name": "drum", "value": 100},       # African musical heritage
    {"name": "mask", "value": 50}         # Traditional African art - Lowest value
]

@app.route('/')
def index():
    """
    Render the main game interface.
    Returns the index.html template with the slot machine UI.
    """
    return render_template('index.html')

@app.route('/spin')
def spin():
    """
    Handle the slot machine spin action.
    
    Game Logic:
    1. Generates a random 3x3 grid of symbols
    2. Checks for winning combinations:
       - Horizontal lines (3 rows)
       - Vertical lines (3 columns)
    3. Calculates total winnings based on matching symbols
    
    Returns:
        JSON response containing:
        - The grid of symbols generated
        - Total winnings from this spin
    """
    # Generate random spin results for 3x3 grid
    result = []
    for _ in range(9):  # 9 positions in 3x3 grid
        result.append(random.choice(SYMBOLS))
    
    # Calculate winnings
    winnings = 0
    
    # Check horizontal lines (rows)
    # Iterate through each row (0-2, 3-5, 6-8)
    for i in range(0, 9, 3):
        # Check if all three symbols in the row match
        if result[i]['name'] == result[i+1]['name'] == result[i+2]['name']:
            winnings += result[i]['value']  # Add the symbol's value to winnings
    
    # Check vertical lines (columns)
    # Iterate through each column (0,3,6 | 1,4,7 | 2,5,8)
    for i in range(3):
        # Check if all three symbols in the column match
        if result[i]['name'] == result[i+3]['name'] == result[i+6]['name']:
            winnings += result[i]['value']  # Add the symbol's value to winnings
    
    # Return the results as JSON
    return jsonify({
        'symbols': result,    # The complete grid of symbols
        'winnings': winnings  # Total winnings from this spin
    })

# Run the application
if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Run the app on 0.0.0.0 to make it externally visible
    app.run(host='0.0.0.0', port=port) 
