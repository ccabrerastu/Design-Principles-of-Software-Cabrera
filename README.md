# 🐾 Animal Shelter Project

This project demonstrates design principles like **SOLID, DRY, and KISS** in Python.

It simulates a small animal shelter where animals can introduce themselves and make sounds.

It also includes a **CI workflow with GitHub Actions** to automatically run tests.

---

## 🚀 Structure
- `src/animals` → Base and derived animal classes.
- `src/services` → Services used by animals.
- `src/main.py` → Program entry point.
- `tests` → Testing with `pytest`.
- `.github/workflows` → CI with GitHub Actions.

---

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/youruser/animal-shelter.git
cd animal-shelter
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Execution
Run the main program:

```bash
python -m src.main
```

Example output:
```
Buddy, 3 years old, says Woof!
Luna, 2 years old, says Meow!
```

Run tests with `pytest`:

```bash
pytest
```

---

## 🔄 Continuous Integration (CI)
This project includes a workflow in **GitHub Actions** that:
- Installs dependencies.
- Runs tests automatically on each push or pull request to the `main` branch.

Configuration file:
`.github/workflows/python-app.yml`

---

## 📚 Applied principles
- **SRP (Single Responsibility Principle)**: Each class has a single responsibility (`Dog`, `Cat`).
- **OCP (Open/Closed Principle)**: New animals can be added without modifying existing code.
- **LSP (Liskov Substitution Principle)**: Subclasses (`Dog`, `Cat`) seamlessly replace the superclass `Animal`.
- **ISP (Interface Segregation Principle)**: Classes implement only the methods they need.
- **DIP (Dependency Inversion Principle)**: `AnimalService` depends on the `Animal` abstraction, not on concrete implementations.

Other principles:
- **DRY (Don't Repeat Yourself)**: Duplicate logic is avoided (e.g., `get_info()` in `Animal`).
- **KISS (Keep It Simple, Stupid)**: Simple, readable, and maintainable code.