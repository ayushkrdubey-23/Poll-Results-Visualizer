# Installation Guide - Poll Results Visualizer

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git (for version control)

---

## Step 1: Install Python

### Windows
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click "Install Now"

Verify installation:
```powershell
python --version
pip --version
```

### Mac
1. Install Homebrew (if not installed): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Python: `brew install python@3.11`
3. Verify: `python3 --version` and `pip3 --version`

---

## Step 2: Clone or Download the Project

### Option A: Clone from GitHub
```powershell
git clone https://github.com/your-username/Poll-Results-Visualizer.git
cd Poll-Results-Visualizer
```

### Option B: Download ZIP
1. Download the ZIP from GitHub
2. Extract to a folder
3. Open terminal in that folder

---

## Step 3: Create Virtual Environment

### Windows
```powershell
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal, indicating the virtual environment is active.

---

## Step 4: Install Required Libraries

```powershell
pip install -r requirements.txt
```

### If requirements.txt doesn't exist yet, install manually:
```powershell
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
```

### Verify installation:
```powershell
pip list
```

You should see: pandas, numpy, matplotlib, seaborn, plotly, streamlit, jupyter

---

## Step 5: Project Folder Structure

After installation, your folder should look like:

```
Poll-Results-Visualizer/
├── data/
├── notebooks/
├── src/
├── outputs/
├── images/
├── docs/
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

---

## Step 6: Create requirements.txt

Create a `requirements.txt` file with the following content:

```
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0
streamlit>=1.25.0
jupyter>=1.0.0
```

Then install:
```powershell
pip install -r requirements.txt
```

---

## Commands Summary

| Action | Windows Command | Mac/Linux Command |
|--------|-----------------|-------------------|
| Check Python version | `python --version` | `python3 --version` |
| Create venv | `python -m venv venv` | `python3 -m venv venv` |
| Activate venv | `venv\Scripts\activate` | `source venv/bin/activate` |
| Install deps | `pip install -r requirements.txt` | `pip3 install -r requirements.txt` |
| Run project | `python main.py` | `python3 main.py` |
| Run Streamlit | `streamlit run src/dashboard.py` | `streamlit run src/dashboard.py` |
| Deactivate venv | `deactivate` | `deactivate` |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` not recognized | Reinstall Python and check "Add Python to PATH" |
| `pip` not recognized | Run `python -m ensurepip` or reinstall Python |
| Permission denied on install | Use `--user` flag or run terminal as Administrator |
| Virtual environment not activating | Check execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Module not found errors | Make sure venv is activated and run `pip install -r requirements.txt` |

---

## Verification

After installation, verify everything works:

```powershell
python -c "import pandas; import numpy; import matplotlib; import seaborn; import plotly; import streamlit; print('All libraries installed successfully!')"
```

Expected output:
```
All libraries installed successfully!
```
