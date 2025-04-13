# South African Treasures Slots Game 🎰

[![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://casino-slots-game.onrender.com)
[![Made with Flask](https://img.shields.io/badge/made%20with-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A themed slot machine game featuring South African wildlife and cultural symbols. Built with Python (Flask), HTML, CSS, and JavaScript.

## 🎮 Play Now!

**[Click here to play South African Treasures Slots](https://casino-slots-game.onrender.com)**

![Game Preview](screenshots/game-preview.png)

## ✨ Features

- 🦁 South African themed symbols (Lion, Elephant, Rhino, Protea, etc.)
- 📱 Responsive design that works on both desktop and mobile
- 🎰 Realistic slot machine animations
- 💰 Betting system with adjustable bet amounts
- 🎉 Win celebrations and effects
- 🎨 South African color scheme and styling

## 🎯 Game Logic

The game implements a classic 3x3 slot machine with South African themed symbols. Here's how it works:

1. **Symbols & Values**:
   ```python
   SYMBOLS = [
       {"name": "lion", "value": 500},     # Highest value
       {"name": "elephant", "value": 400},
       {"name": "rhino", "value": 300},
       {"name": "protea", "value": 250},
       {"name": "springbok", "value": 200},
       {"name": "diamond", "value": 150},
       {"name": "drum", "value": 100},
       {"name": "mask", "value": 50}       # Lowest value
   ]
   ```

2. **Winning Combinations**:
   - Three matching symbols in any horizontal row
   - Three matching symbols in any vertical column
   - Winnings are calculated based on the symbol's value

3. **Betting System**:
   - Minimum bet: R10
   - Maximum bet: R100
   - Starting balance: R1000

## 🛠️ Technical Implementation

### Backend (Python/Flask)
- RESTful API endpoint for spin mechanics
- Random symbol generation
- Win calculation logic
- Secure configuration with environment variables

### Frontend (HTML/CSS/JavaScript)
- Responsive grid layout
- CSS animations for spinning effect
- Real-time balance updates
- Interactive betting controls
- Win celebrations

## 📸 Screenshots

### Desktop View
![Desktop View](screenshots/desktop.png)

### Mobile View
![Mobile View](screenshots/mobile.png)

### Winning Celebration
![Winning](screenshots/winning.png)

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd casino-slots-game
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎲 Running the Game

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎯 How to Play

1. Set your bet amount using the + and - buttons
2. Click the SPIN button to play
3. Match 3 symbols in a row (horizontally or vertically) to win
4. Each symbol has different payout values
5. Your current balance and winnings are displayed on screen

## 💎 Symbol Values

- 🦁 Lion: R500 - King of the African savanna
- 🐘 Elephant: R400 - Symbol of wisdom and strength
- 🦏 Rhino: R300 - Representing power and protection
- 🌺 Protea: R250 - South Africa's national flower
- 🦌 Springbok: R200 - National animal of South Africa
- 💎 Diamond: R150 - Representing South Africa's mineral wealth
- 🥁 Drum: R100 - African musical heritage
- 🎭 Mask: R50 - Traditional African art

## 📄 License

MIT License
