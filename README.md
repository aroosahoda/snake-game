# 🐍 Python Turtle Snake Game

A classic Snake game built with Python's turtle graphics library. Navigate the snake to collect food, grow longer, and avoid collisions. The game uses clean, modular design with separate classes for Snake, Food, and Scoreboard.

## 🚀 Features

- Arrow-key navigation
- Score tracking and reset logic
- Object-oriented structure using custom classes
- Wall and self-collision detection
- Refreshing food after each collision

## 🧰 Built With

- Python 3.x
- turtle (standard Python graphics module)

## 📁 Project Structure
├── main.py          # Game setup and main loop 
├── snake.py         # Snake class: movement, reset, extend 
├── food.py          # Food class: positioning, refresh 
└── scoreboard.py    # Score class: UI and scoring logic


## ▶️ How to Run

1. Clone this repository
2. Run the game:
   python main.py
   
> ⚠️ No extra libraries needed! Python's `turtle` module is built-in.

## 🎮 Controls

| Action      | Key     |
|-------------|---------|
| Move Up     | ↑ Arrow |
| Move Down   | ↓ Arrow |
| Move Left   | ← Arrow |
| Move Right  | → Arrow |
| Exit        | Click anywhere on the screen |

## 📚 Learning Highlights

- Class-based design for better modularity
- Collision detection using coordinates
- Keyboard event binding with `onkey`
- Dynamic screen updates with `screen.tracer` and `time.sleep`

## 🙌 Contributions

Pull requests welcome! Feel free to open issues or suggest new features.
