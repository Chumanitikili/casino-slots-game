from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Define South African themed symbols
SYMBOLS = [
    {"name": "lion", "value": 500},
    {"name": "elephant", "value": 400},
    {"name": "rhino", "value": 300},
    {"name": "protea", "value": 250},
    {"name": "springbok", "value": 200},
    {"name": "diamond", "value": 150},
    {"name": "drum", "value": 100},
    {"name": "mask", "value": 50}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    # Generate random spin results
    result = []
    for _ in range(9):  # 3x3 grid
        result.append(random.choice(SYMBOLS))
    
    # Check for wins (simplified version)
    winnings = 0
    # Check horizontal lines
    for i in range(0, 9, 3):
        if result[i]['name'] == result[i+1]['name'] == result[i+2]['name']:
            winnings += result[i]['value']
    
    # Check vertical lines
    for i in range(3):
        if result[i]['name'] == result[i+3]['name'] == result[i+6]['name']:
            winnings += result[i]['value']
    
    return jsonify({
        'symbols': result,
        'winnings': winnings
    })

if __name__ == '__main__':
    app.run(debug=True) 