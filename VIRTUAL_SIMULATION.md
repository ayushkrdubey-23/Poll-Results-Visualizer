# Virtual Simulation - Poll Results Visualizer

## Overview

The virtual simulation demonstrates how poll data is generated, how questions and options are created, how responses are distributed, how regional/demographic patterns are created, how the leading option is identified, and how insights are generated — all without needing real survey data.

This simulation is embedded directly in `src/data_loader.py` (the `generate_synthetic_poll_data` function) and can be run via `main.py`.

---

## Simulation Design

### Step 1: Define the Poll Questions

We define 4 poll questions covering different use cases:

| Question | Use Case | Options |
|----------|----------|---------|
| "Which product do you prefer?" | Product preference | Product A, B, C, D |
| "How satisfied are you with our service?" | Customer feedback | Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied |
| "Which feature is most important to you?" | Feature prioritization | Performance, Price, Design, Support |
| "Would you recommend us to a friend?" | NPS / Recommendation | Yes, No, Maybe |

### Step 2: Create Questions and Options

Each question has a predefined set of options with different probability distributions to create realistic variation:

- **Product preference**: Product A most popular (40%), then B (30%), C (20%), D (10%)
- **Satisfaction**: Weighted toward positive responses
- **Feature importance**: Performance highest, then Price, Design, Support
- **Recommendation**: Yes most common, then No, Maybe

### Step 3: Distribute Responses

1,000 synthetic responses are generated. Each response includes:
- `respondent_id` (R0001 to R1000)
- `date` (random date over 90 days starting 2026-01-01)
- `question` (randomly selected from the 4 questions)
- `option_selected` (weighted random choice based on question-specific probabilities)
- `region` (North 30%, South 25%, East 25%, West 20%)
- `age_group` (18-25: 25%, 26-35: 30%, 36-45: 25%, 46-60: 15%, 60+: 5%)
- `gender` (Male: 45%, Female: 50%, Other: 5%)

### Step 4: Create Regional and Demographic Patterns

Regional and demographic patterns emerge naturally from the weighted distributions:
- North region has highest response volume (30%)
- 26-35 age group is most represented (30%)
- Female respondents are slightly more common (50%)

### Step 5: Identify the Leading Option

The leading option is identified by counting votes per option and selecting the one with the highest count. The result includes vote count and percentage share.

### Step 6: Generate Insights

Insights are generated from:
- Leading option (highest vote share)
- Top region per option
- Top age group per option
- Top gender per option
- Peak and lowest response days over time
- Recommendations based on findings

---

## Step-by-Step Simulation Flow

```
Step 1: Define poll questions and options
   ↓
Step 2: Generate 1,000 synthetic responses with weighted distributions
   ↓
Step 3: Introduce realistic data issues (2% missing values, 1% duplicates)
   ↓
Step 4: Clean the data (handle missing, remove duplicates, standardize)
   ↓
Step 5: Analyze - calculate vote counts, percentages, group by region/age/gender
   ↓
Step 6: Identify leading option and demographic patterns
   ↓
Step 7: Visualize - bar, pie, stacked, trend, demographic charts
   ↓
Step 8: Generate summary insights and recommendations
   ↓
Step 9: Save outputs to data/, outputs/ directories
```

---

## How to Run the Simulation

```powershell
# Activate virtual environment
venv\Scripts\activate

# Run the full simulation pipeline
python main.py
```

### Expected Output

```
[INFO] Synthetic poll dataset generated: data/polls.csv
[INFO] Total rows: 1010
[INFO] Columns: ['respondent_id', 'date', 'question', 'option_selected', 'region', 'age_group', 'gender']

[INFO] Raw data shape: (1010, 7)

[INFO] Initial rows: 1010
[INFO] Missing values before cleaning: 20
[INFO] Missing values after cleaning: 0
[INFO] Duplicate rows before: 10
[INFO] Duplicate rows after: 0
[INFO] Final rows after cleaning: 1000

[INFO] Leading option: Yes (117 votes, 11.7%)
...

[INFO] Bar chart saved: outputs/bar_chart.png
[INFO] Pie chart saved: outputs/pie_chart.png
[INFO] Stacked chart saved: outputs/stacked_chart.png
[INFO] Trend chart saved: outputs/trend_chart.png
[INFO] Demographic chart saved: outputs/demographic_chart.png

[INFO] Summary insights saved to: outputs/summary_insights.txt
```

---

## What Screenshots to Take (for Proof Building)

| Screenshot | File | Purpose |
|------------|------|---------|
| Dataset preview | `data/polls.csv` opened in Excel/editor | Shows raw poll data structure |
| Cleaned dataset | `data/polls_cleaned.csv` | Shows data after cleaning |
| Vote summary table | Console output from `calculate_vote_share` | Shows vote counts and percentages |
| Bar chart | `outputs/bar_chart.png` | Option-wise vote share visualization |
| Pie chart | `outputs/pie_chart.png` | Option distribution visualization |
| Region-wise chart | `outputs/stacked_chart.png` | Regional option distribution |
| Demographic chart | `outputs/demographic_chart.png` | Age group vs option comparison |
| Trend chart | `outputs/trend_chart.png` | Responses over time |
| Summary insights | `outputs/summary_insights.txt` | Text-based findings and recommendations |
| GitHub repo | Your GitHub repository page | Public proof of work |

---

## What Graphs to Generate

1. **Bar Chart** (`outputs/bar_chart.png`) - Option-wise vote share with counts and percentages
2. **Pie Chart** (`outputs/pie_chart.png`) - Overall option distribution
3. **Stacked Bar Chart** (`outputs/stacked_chart.png`) - Region-wise option distribution
4. **Trend Line Chart** (`outputs/trend_chart.png`) - Responses over time (dates)
5. **Demographic Grouped Bar Chart** (`outputs/demographic_chart.png`) - Age group vs option

---

## What Proof to Save

For placements and internships, save the following as proof:

1. **Code**: All `src/*.py` files and `main.py` on GitHub
2. **Data**: `data/polls.csv` and `data/polls_cleaned.csv` (or reference in .gitignore)
3. **Charts**: All 5 PNG files in `outputs/` (or images/ for README)
4. **Insights**: `outputs/summary_insights.txt`
5. **Documentation**: README.md with screenshots and instructions
6. **Git history**: Meaningful commit messages showing phase-by-phase progress
7. **README screenshots**: Screenshots of charts embedded in README.md

---

## Simulation Code Reference

The simulation logic lives in `src/data_loader.py:generate_synthetic_poll_data()`:

- **Questions & Options**: Lines 32-37 define 4 questions with their options
- **Regional Distribution**: Line 54 uses `p=[0.3, 0.25, 0.25, 0.2]` for North/South/East/West
- **Age Group Distribution**: Line 55 uses `p=[0.25, 0.3, 0.25, 0.15, 0.05]`
- **Gender Distribution**: Line 56 uses `p=[0.45, 0.5, 0.05]` for Male/Female/Other
- **Missing Values**: Lines 61-62 introduce 2% missing region values
- **Duplicates**: Lines 64-65 introduce 1% duplicate rows

Run `python main.py` to execute the complete simulation from data generation through insights.
