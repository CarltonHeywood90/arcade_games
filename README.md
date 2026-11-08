# 🕹️ Python Retro Arcade Hub

A multi-game 2D arcade collection built from scratch using **Python** and **Pygame**. Featuring a unified master launcher and clean architectural separation of concerns (`logic`, `gui`, `scoreboard`), this project brings classic arcade action right to your desktop.

---

## 🎮 Included Games

1. **Pong** – The ultimate grandfather of arcade games with 2-player controls and vector physics.
2. **Snake** – Grid-based movement, growing body state management, and food-spawning mechanics.
3. **Space Invaders** – Wave-based alien descent, multi-directional bullet mechanics, and defense action.
4. **Breakout** – Bouncing ball physics, multi-tiered breakable brick grids, and paddle-deflection angles.
5. **Flappy Bird** – Constant gravitational acceleration, jump impulse velocity, and procedural pipe generation.

---

## 📂 Project Architecture

Each game is organized into its own modular package to keep the codebase clean, testable, and scalable:

```text
arcade_games/
├── pong/
│   ├── __init__.py
│   ├── main.py
│   ├── logic.py
│   ├── gui.py
│   └── scoreboard.py
├── snake/
│   ├── __init__.py
│   └── ...
├── space_invaders/
│   ├── __init__.py
│   └── ...
├── breakout/
│   ├── __init__.py
│   └── ...
├── flappy_bird/
│   ├── __init__.py
│   └── ...
└── arcade_launcher.py