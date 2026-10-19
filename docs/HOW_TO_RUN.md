# How to Run Project - Poll Results Visualizer

## Prerequisites

Before running the project, complete the installation steps from `INSTALLATION_GUIDE.md`:

1. Python 3.10+ installed
2. Virtual environment created and activated
3. Required libraries installed (`pip install -r requirements.txt`)

---

## Step 1: Activate Virtual Environment

### Windows
```powershell
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

## Step 2: Run the Full Pipeline

From the project root directory (`Poll-Results-Visualizer/`), run:

```powershell
python main.py
```

### What This Does

The `main.py` script executes the complete pipeline:

| Step | Action | Output |
|------|--------|--------|
| 1 | Generate synthetic poll data (1,000 responses) | `data/polls.csv` |
| 2 | Clean the data (handle missing, duplicates, standardize) | `data/polls_cleaned.csv` |
| 3 | Analyze vote shares, regions, demographics, trends | Console output |
| 4 | Generate 5 visualization charts | `outputs/*.png` |
| 5 | Generate summary insights | `outputs/summary_insights.txt` |

### Expected Console Output

```
============================================================
POLL RESULTS VISUALIZER - FULL PIPELINE
============================================================

[STEP 1] Loading/Generating Poll Data
----------------------------------------
[INFO] Synthetic poll dataset generated: data/polls.csv
[INFO] Total rows: 1010
[INFO] Columns: ['respondent_id', 'date', 'question', 'option_selected', 'region', 'age_group', 'gender']

[INFO] Raw data shape: (1010, 7)

[STEP 2] Data Cleaning
----------------------------------------
[INFO] Initial rows: 1010
[INFO] Missing values before cleaning: 20
[INFO] Missing values after cleaning: 0
[INFO] Duplicate rows before: 10
[INFO] Duplicate rows after: 0
[INFO] Final rows after cleaning: 1000

[INFO] Cleaned data shape: (1000, 7)

[STEP 3] Analysis
...
[INFO] Leading option: Yes (117 votes, 11.7%)
...

[STEP 4] Visualization
...
[INFO] Bar chart saved: outputs/bar_chart.png
[INFO] Pie chart saved: outputs/pie_chart.png
[INFO] Stacked chart saved: outputs/stacked_chart.png
[INFO] Trend chart saved: outputs/trend_chart.png
[INFO] Demographic chart saved: outputs/demographic_chart.png

[STEP 5] Summary Insights
...
[INFO] Summary insights saved to: outputs/summary_insights.txt

============================================================
PIPELINE COMPLETE!
============================================================
```

---

## Step 3: Run the Streamlit Dashboard (Optional)

For an interactive dashboard, run:

```powershell
streamlit run src/dashboard.py
```

This opens a web browser at `http://localhost:8501` with:
- Key metrics (total responses, top option, top option share)
- Option-wise bar chart
- Option distribution pie chart
- Region-wise stacked bar chart
- Age group vs option grouped bar chart
- Responses over time line chart
- Data preview table

To stop the dashboard, press `Ctrl+C` in the terminal.

---

## Step 4: Run Individual Modules (Optional)

You can also run individual modules directly:

### Generate data only
```powershell
python -c "from src.data_loader import generate_synthetic_poll_data; generate_synthetic_poll_data()"
```

### Clean data only
```powershell
python -c "from src.data_loader import load_poll_data; from src.cleaning import clean_poll_data, save_cleaned_data; df = load_poll_data(); df_cleaned = clean_poll_data(df); save_cleaned_data(df_cleaned)"
```

### Run analysis only
```powershell
python -c "from src.data_loader import load_poll_data; from src.cleaning import clean_poll_data; from src.analysis import run_full_analysis; df = load_poll_data('data/polls_cleaned.csv'); run_full_analysis(df)"
```

---

## Expected Outputs

After running `python main.py`, the following files are generated:

### Data Files
| File | Description |
|------|-------------|
| `data/polls.csv` | Raw synthetic poll dataset (1,000+ rows) |
| `data/polls_cleaned.csv` | Cleaned dataset (missing values handled, duplicates removed) |

### Chart Files
| File | Description |
|------|-------------|
| `outputs/bar_chart.png` | Option-wise vote share bar chart |
| `outputs/pie_chart.png` | Option distribution pie chart |
| `outputs/stacked_chart.png` | Region-wise option stacked chart |
| `outputs/trend_chart.png` | Responses over time trend chart |
| `outputs/demographic_chart.png` | Age group vs option comparison chart |

### Report Files
| File | Description |
|------|-------------|
| `outputs/summary_insights.txt` | Text-based insights and recommendations |

---

## Verification Checklist

After running, verify:

- [ ] `data/polls.csv` exists and has data
- [ ] `data/polls_cleaned.csv` exists and has cleaned data
- [ ] All 5 PNG charts exist in `outputs/`
- [ ] `outputs/summary_insights.txt` exists with insights
- [ ] Console shows "PIPELINE COMPLETE!" message
- [ ] No error messages in console output

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'pandas'` | Run `pip install -r requirements.txt` |
| `FileNotFoundError: data/polls.csv` | Run `python main.py` first to generate data |
| Streamlit not opening | Run `streamlit run src/dashboard.py` and check `http://localhost:8501` |
| Charts not saving | Check `outputs/` directory exists; script creates it automatically |
| Virtual environment not activating | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (Windows PowerShell) |

---

## Complete Command Summary

```powershell
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Run the full pipeline
python main.py

# 4. (Optional) Run interactive dashboard
streamlit run src/dashboard.py

# 5. Deactivate when done
deactivate
```
