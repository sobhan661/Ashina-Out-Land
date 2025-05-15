## Ashina-Out-Land

A lightweight 2D space-themed game built with Python and Pygame. Pilot your ship through the outer lands, customize settings, and enjoy smooth, frame-rate–capped gameplay.

---

### 🚀 Features

* **Ship Control**
  A simple, responsive spaceship you can move around the screen.
* **Configurable Settings**
  All key parameters (window size, background color, FPS cap, etc.) live in `Setting.py`.
* **Smooth Rendering**
  Game loop is frame-rate capped to 60 FPS for consistent performance.
* **Asset Management**
  Ship and background images stored in `images/` for easy swapping.

---

### 🛠️ Getting Started

#### Prerequisites

* **Python 3.8+**
* **Pygame**
  Install via pip:

  ```bash
  pip install pygame
  ```

#### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/sobhan661/Ashina-Out-Land.git
   cd Ashina-Out-Land/src
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

---

### ▶️ Running the Game

From within the `src/` directory, simply run:

```bash
python Game.py
```

The game window will open with your ship ready to pilot. Use the arrow keys (or WASD) to move.

---

### ⚙️ Configuration (`Setting.py`)

All editable parameters are centralized here:

```python
# Example entries in Setting.py

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
BG_COLOR      = (255, 255, 255)   # Default: white
FPS_LIMIT     = 60
SHIP_SPEED    = 5
```

Feel free to tweak values to change resolution, color scheme, or ship velocity.

---

### 📂 Project Structure

```
Ashina-Out-Land/
└── src/
    ├── Game.py       # Main game loop and initialization
    ├── Ship.py       # Ship class: drawing & movement logic
    ├── Setting.py    # All changeable game settings
    └── images/       # Sprites and background artwork
```

---

### 🤝 Contributing

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add YourFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please make sure your code follows the existing style and includes comments where needed.

---

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

### ✉️ Contact

For questions or feedback, please open an issue or reach out to the author at **[sobhan661@example.com](mailto:sobhan661@example.com)**.
