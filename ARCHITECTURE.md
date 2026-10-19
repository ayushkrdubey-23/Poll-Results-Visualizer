# Project Architecture - Poll Results Visualizer

## Input

Poll data containing the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| respondent_id | Unique identifier for each respondent | R001, R002 |
| date | Date the response was submitted | 2026-01-15 |
| question | The poll question asked | "Which product do you prefer?" |
| option_selected | The option chosen by the respondent | "Product A" |
| region | Geographic region of the respondent | North, South, East, West |
| age_group | Age bracket of the respondent | 18-25, 26-35, 36-45 |
| gender | Gender of the respondent | Male, Female, Other |
| rating | Optional numerical rating (1-5) | 4 |

## Processing

1. **Data Cleaning** - Handle missing values, remove duplicates, standardize column names, fix data types
2. **Grouping** - Group responses by question, option, region, age group, gender
3. **Aggregation** - Count votes per option, compute totals per group
4. **Percentage Calculation** - Calculate vote share percentage for each option
5. **Comparative Analysis** - Compare options across regions, demographics, and time

## Output

- **Charts** - Bar charts, pie charts, stacked charts, trend charts (PNG/HTML)
- **Dashboards** - Optional interactive Streamlit dashboard
- **Summary Insights** - Text-based insights: leading option, regional patterns, demographic trends

## Text-Based Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  CSV File   │  │  Excel File │  │ Google Forms Export │ │
│  │  (polls.csv)│  │  (.xlsx)    │  │    (.csv)           │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                     │            │
│         └────────────────┴─────────────────────┘            │
│                         │                                   │
└─────────────────────────┼───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  PROCESSING LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Data Cleaning│ │ Grouping &  │ │ Percentage Calc.    │ │
│  │ - Missing   │ │ Aggregation │ │ - Vote share %      │ │
│  │   values    │ │ - By option │ │ - Comparative       │ │
│  │ - Duplicates│ │   by region │ │   analysis          │ │
│  │ - Types     │ │   by age    │ │                     │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                     │            │
│         └────────────────┴─────────────────────┘            │
│                         │                                   │
└─────────────────────────┼───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   OUTPUT LAYER                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Charts     │  │ Dashboard   │ │ Summary Insights    │ │
│  │ - Bar       │  │ (Streamlit) │ │ - Leading option    │ │
│  │ - Pie       │  │             │ │ - Regional patterns │ │
│  │ - Stacked   │  │             │ │ - Demographic trends│ │
│  │ - Trend     │  │             │ └─────────────────────┘ │
│  └─────────────┘  └─────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Explanation

1. **Data Ingestion**: Raw poll data is loaded from CSV/Excel/Google Forms export into a Pandas DataFrame
2. **Data Cleaning**: Missing values are filled or dropped, duplicates removed, column names standardized, data types corrected (dates to datetime, strings stripped)
3. **Grouping & Aggregation**: Responses are grouped by question, option_selected, region, age_group, and gender; vote counts are computed for each group
4. **Percentage Calculation**: Each option's vote count is divided by total responses to compute percentage share
5. **Comparative Analysis**: Options are compared across regions, age groups, and over time (if dates exist) to identify patterns
6. **Visualization**: Cleaned and aggregated data is plotted as bar charts, pie charts, stacked charts, and trend charts using Matplotlib/Seaborn/Plotly
7. **Insights Generation**: The system identifies the leading option, strongest region, demographic preferences, and generates text-based recommendations
8. **Output Delivery**: Charts are saved as PNG/HTML files, summary insights are written to a text file, and optionally an interactive Streamlit dashboard is launched

## Folder Structure Mapping

```
data/           → Input layer (raw poll CSVs)
src/            → Processing layer (cleaning.py, analysis.py, visualization.py)
outputs/        → Output layer (charts, insights, dashboard)
notebooks/      → EDA and exploration
images/         → Generated chart images
main.py         → Entry point that orchestrates the pipeline
```
