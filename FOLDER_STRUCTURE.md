# Folder Structure - Poll Results Visualizer

## GitHub-Ready Folder Structure

```
Poll-Results-Visualizer/
│
├── data/
│   ├── polls.csv                 # Raw synthetic poll dataset
│   └── polls_cleaned.csv         # Cleaned poll dataset
│
├── notebooks/
│   └── eda.ipynb                 # Exploratory data analysis notebook
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Load CSV/Excel/Google Forms export
│   ├── cleaning.py               # Data cleaning functions
│   ├── analysis.py               # Aggregation and percentage calculation
│   ├── visualization.py          # Chart generation (bar, pie, stacked, trend)
│   ├── insights.py               # Summary insights generation
│   └── dashboard.py              # Optional Streamlit dashboard
│
├── outputs/
│   ├── bar_chart.png             # Option-wise vote share bar chart
│   ├── pie_chart.png             # Option distribution pie chart
│   ├── stacked_chart.png         # Region-wise option stacked chart
│   ├── trend_chart.png           # Votes over time trend chart
│   ├── demographic_chart.png     # Age group vs option comparison
│   └── summary_insights.txt      # Text-based insights and recommendations
│
├── images/
│   └── (screenshots for README)
│
├── docs/
│   ├── PROJECT_EXPLANATION.md    # Step 1: Project explanation
│   ├── TECH_STACK.md             # Step 2: Tech stack options
│   ├── ARCHITECTURE.md           # Step 3: Project architecture
│   └── IMPLEMENTATION_PLAN.md    # Step 4: Phase-wise implementation plan
│
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── main.py                       # Entry point - orchestrates the pipeline
└── README.md                     # Project documentation
```

## Explanation of Each Folder/File

### `data/`
Stores the raw and cleaned poll datasets.
- `polls.csv` — Original synthetic poll data with respondent_id, date, question, option_selected, region, age_group, gender
- `polls_cleaned.csv` — Cleaned version after handling missing values, duplicates, and type conversions

### `notebooks/`
Jupyter notebooks for exploration and documentation.
- `eda.ipynb` — Exploratory data analysis with summary statistics and initial distributions

### `src/`
Source code containing the core logic, organized by responsibility.
- `data_loader.py` — Functions to load data from CSV, Excel, or Google Forms export
- `cleaning.py` — Data cleaning: missing values, duplicates, standardization, type conversion
- `analysis.py` — Grouping, aggregation, percentage calculation, comparative analysis
- `visualization.py` — Chart generation: bar, pie, stacked, trend, demographic charts
- `insights.py` — Summary insights and recommendations generation
- `dashboard.py` — Optional Streamlit dashboard for interactive exploration

### `outputs/`
Generated charts, reports, and insights.
- `bar_chart.png` — Option-wise vote share
- `pie_chart.png` — Option distribution
- `stacked_chart.png` — Region-wise option distribution
- `trend_chart.png` — Votes over time
- `demographic_chart.png` — Age group vs option comparison
- `summary_insights.txt` — Text-based findings and recommendations

### `images/`
Screenshots and visual assets for the README and proof building.

### `docs/`
Phase 1-4 documentation files:
- `PROJECT_EXPLANATION.md` — What/why/use cases/workflow
- `TECH_STACK.md` — Tech stack options and selection
- `ARCHITECTURE.md` — Input/processing/output layers, data flow
- `IMPLEMENTATION_PLAN.md` — 8-phase implementation plan

### `.gitignore`
Excludes Python cache, virtual environments, IDE files, OS files, and large data/output files from version control.

### `requirements.txt`
Lists all Python dependencies needed to run the project.

### `main.py`
Entry point script that orchestrates the full pipeline: load → clean → analyze → visualize → insights.

### `README.md`
Project documentation with overview, problem, solution, features, tech stack, how to run, results, and screenshots.
