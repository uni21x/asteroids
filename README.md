# 🪐 Asteroids

Asteroids is a small clone of the classic arcade game, built with **pygame**. Pilot your ship, dodge asteroids, and blast them into smaller chunks.  
This project was created as a practice exercise for the [Boot.dev](https://www.boot.dev) course.

---

## ✨ Features

- 🚀 Ship controls with rotation and thrust
- 🌌 Random asteroid spawns at screen edges
- 💥 Asteroids split into smaller pieces on hit
- 🔫 Fire cooldown to limit shooting

---

## 🧰 Prerequisites

- 🐍 Python **3.12+**
- 📦 Dependency: `pygame==2.6.1`

---

## ⚙️ Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install pygame==2.6.1
```

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install pygame==2.6.1
```
---

## ▶️ Run

```bash
python main.py
```

---

## 🎮 Controls

- **W**: Forward
- **S**: Backward
- **A / D**: Rotate left / right
- **Space**: Shoot

---

## 🗂️ Project Structure

- `main.py` – Game loop & setup
- `player.py` – Player logic & shots
- `asteroid.py` / `asteroidfield.py` – Asteroids & spawning
- `circleshape.py` – Base class for circular objects
- `constants.py` – Game constants
