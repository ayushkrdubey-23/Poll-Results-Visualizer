# Poll Results Visualizer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-yellow.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.15+-red.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-pink.svg)

## 📌 Project Title
**Poll Results Visualizer**

## Overview
A beginner-friendly, industry-oriented Python project that collects, cleans, analyzes, and visualizes poll/survey results. It generates bar charts, pie charts, stacked charts, trend charts, and summary insights — with an optional interactive Streamlit dashboard. Built entirely with public/synthetic data, making it ideal for student portfolios, placements, and internships.

## Problem
Organizations collect vast amounts of poll and survey data but often lack a simple, accessible tool to:
- Clean and preprocess raw survey responses
- Calculate vote shares and percentages by option
- Analyze results by region, age group, gender, and other demographics
- Visualize findings with clear, professional charts
- Generate actionable insights for decision-making

Existing enterprise tools (Qualtrics, SurveyMonkey, Google Forms) are powerful but expensive and not easily customizable for learning or small-scale use.

## Solution
**Poll Results Visualizer** is a complete Python data pipeline that:

1. **Ingests** poll data from CSV files, Excel, or Google Forms exports (or generates synthetic data)
2. **Cleans** the data — handles missing values, removes duplicates, standardizes formats
3. **Analyzes** vote counts, percentages, and comparative patterns by region, age group, and gender
4. **Visualizes** results with bar, pie, stacked, trend, and demographic charts
5. **Generates** summary insights and recommendations
6. **Optionally deploys** an interactive Streamlit dashboard

## Features

| Feature | Description |
|---------|-------------|
| Synthetic Data Generation | Creates realistic poll datasets (1,000+ responses) with weighted distributions |
| Data Cleaning | Handles missing values, removes duplicates, standardizes column names and values |
| Vote Share Analysis | Calculates vote counts and percentages per option |
| Regional Analysis | Breaks down results by geographic region |
| Demographic Analysis | Analyzes by age group and gender |
| Trend Analysis | Tracks responses over time (if dates exist) |
| Bar Chart | Option-wise vote share visualization |
| Pie Chart | Overall option distribution |
| Stacked Chart | Region-wise option distribution |
| Trend Chart | Responses over time |
| Demographic Chart | Age group vs option comparison |
| Summary Insights | Text-based findings and recommendations |
| Streamlit Dashboard | Optional interactive web dashboard |
| Modular Code | Clean separation: data_loader, cleaning, analysis, visualization, insights, dashboard |

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit (optional) |
| Data Input | CSV, Excel, Google Forms export |
| Output | PNG charts, TXT insights, HTML charts |

**Selected Option:** Option B (Intermediate) — professional but beginner-friendly, with optional Streamlit dashboard.

## Folder Structure

```
Poll-Results-Visualizer/
├── data/                    # Raw and cleaned poll datasets
├── notebooks/               # Jupyter notebooks for EDA
├── src/                     # Source code modules
│   ├── data_loader.py       # Data loading and synthetic generation
│   ├── cleaning.py          # Data cleaning functions
│   ├── analysis.py          # Vote share, %, demographic analysis
│   ├── visualization.py     # Chart generation (bar, pie, stacked, trend)
│   ├── insights.py          # Summary insights generation
│   └── dashboard.py         # Streamlit dashboard
├── outputs/                 # Generated charts and insights
├── images/                  # Screenshots for README
├── docs/                    # Documentation (steps 1-10)
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point - runs full pipeline
└── README.md                # Project documentation
```

## How to Run

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

```powershell
# 1. Clone the repository
git clone https://github.com/ayushkrdubey-23/Poll-Results-Visualizer.git
cd Poll-Results-Visualizer

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the full pipeline
python main.py

# 5. (Optional) Run the Streamlit dashboard
streamlit run src/dashboard.py
```

### Requirements (`requirements.txt`)
```
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0
streamlit>=1.25.0
jupyter>=1.0.0
```

## Results

Running `python main.py` generates:

### Data Files
| File | Description |
|------|-------------|
| `data/polls.csv` | Raw synthetic poll dataset |
| `data/polls_cleaned.csv` | Cleaned dataset |

### Chart Files
| File | Description |
|------|-------------|
| `outputs/bar_chart.png` | Option-wise vote share |
| `outputs/pie_chart.png` | Option distribution |
| `outputs/stacked_chart.png` | Region-wise option distribution |
| `outputs/trend_chart.png` | Responses over time |
| `outputs/demographic_chart.png` | Age group vs option |

### Report Files
| File | Description |
|------|-------------|
| `outputs/summary_insights.txt` | Text-based insights and recommendations |

## Screenshots

Add the following screenshots to the `images/` folder:

- Dataset preview (`data/polls.csv`)
- Cleaned dataset preview (`data/polls_cleaned.csv`)
- Vote/share summary table
- Bar chart (`outputs/bar_chart.png`)
- Pie chart (`outputs/pie_chart.png`)
- Region-wise chart (`outputs/stacked_chart.png`)
- Demographic comparison chart (`outputs/demographic_chart.png`)
- Final dashboard (Streamlit)
- GitHub repo preview

## Industry Relevance

Companies like **Google** (Forms/Surveys), **Qualtrics**, **SurveyMonkey**, **YouGov**, and **Nielsen** rely on similar data pipelines to convert feedback into decisions. This project demonstrates practical skills relevant to:

- Data Analyst
- Business Analyst
- Research Analyst
- Insights Analyst

## Documentation

Complete step-by-step documentation is available in the `docs/` folder:

| Document | Description |
|----------|-------------|
| `docs/PROJECT_EXPLANATION.md` | What/why/use cases/workflow |
| `docs/TECH_STACK.md` | Tech stack options and selection |
| `docs/ARCHITECTURE.md` | Input/processing/output layers, data flow |
| `docs/IMPLEMENTATION_PLAN.md` | 8-phase implementation plan |
| `docs/FOLDER_STRUCTURE.md` | Folder structure explanation |
| `docs/INSTALLATION_GUIDE.md` | Installation guide |
| `docs/VIRTUAL_SIMULATION.md` | Virtual simulation guide |
| `docs/HOW_TO_RUN.md` | How to run the project |
| `docs/GITHUB_UPLOAD.md` | GitHub upload steps |

## GitHub Upload

See `docs/GITHUB_UPLOAD.md` for complete instructions on creating the repository, connecting the local project, and pushing code.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built as a placement/internship portfolio project. Ideal for Data Analyst, Business Analyst, Research Analyst, and Insights Analyst roles.
