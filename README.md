# ♟️ Chessboard-Simulation

Simulates the movement of King, Queen, and Pawn on an empty 8x8 chessboard.

---

## ✅ Features
- Object-oriented & modular design
- Clean and readable Python code
- Unit test coverage for all pieces
- Handles edge and boundary cases

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/aafankadri/Chessboard-Simulation.git
cd Chessboard-Simulation
```

### 2. Run the program

```bash
python main.py
```

Then enter input like:

```bash
Queen, E4
```

---

## 🧪 Run Unit Tests

```bash
python test_chess.py
```

---

## 🛠️ Structure

```bash
.
├── main.py              # Entry point
├── utils.py             # Helpers to convert positions
├── test_chess.py        # Unit tests
├── README.md
└── pieces/
    ├── base.py          # Base class
    ├── king.py
    ├── queen.py
    └── pawn.py
```

---

## 📌 Example Inputs

| Input        | Output                                         |
|--------------|------------------------------------------------|
| King, D5     | C4, C5, C6, D4, D6, E4, E5, E6                 |
| Pawn, G1     | G2                                             |
| Queen, E4    | All valid horizontal, vertical, diagonal moves |

---
