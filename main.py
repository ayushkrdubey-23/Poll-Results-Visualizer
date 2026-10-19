"""
main.py
Entry point for the Poll Results Visualizer project.
Orchestrates the full pipeline: load -> clean -> analyze -> visualize -> insights.
"""

import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader import generate_synthetic_poll_data, load_poll_data
from cleaning import clean_poll_data, save_cleaned_data
from analysis import run_full_analysis
from visualization import generate_all_charts
from insights import generate_insights


def run_pipeline(use_synthetic=True, data_path="data/polls.csv"):
    """
    Run the complete Poll Results Visualizer pipeline.

    Parameters
    ----------
    use_synthetic : bool
        If True, generate synthetic poll data. If False, load from data_path.
    data_path : str
        Path to the poll data CSV file.
    """
    print("=" * 60)
    print("POLL RESULTS VISUALIZER - FULL PIPELINE")
    print("=" * 60)

    # Step 1: Load or generate data
    print("\n[STEP 1] Loading/Generating Poll Data")
    print("-" * 40)
    if use_synthetic:
        df = generate_synthetic_poll_data(n_rows=1000, output_path=data_path)
    else:
        df = load_poll_data(file_path=data_path)

    print(f"\n[INFO] Raw data shape: {df.shape}")

    # Step 2: Clean data
    print("\n[STEP 2] Data Cleaning")
    print("-" * 40)
    df_cleaned = clean_poll_data(df)
    save_cleaned_data(df_cleaned, output_path="data/polls_cleaned.csv")

    print(f"\n[INFO] Cleaned data shape: {df_cleaned.shape}")

    # Step 3: Analysis
    print("\n[STEP 3] Analysis")
    print("-" * 40)
    analysis_results = run_full_analysis(df_cleaned)

    # Step 4: Visualization
    print("\n[STEP 4] Visualization")
    print("-" * 40)
    generate_all_charts(df_cleaned, analysis_results)

    # Step 5: Insights
    print("\n[STEP 5] Summary Insights")
    print("-" * 40)
    generate_insights(analysis_results, output_path="outputs/summary_insights.txt")

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE!")
    print("=" * 60)
    print("\nOutputs generated:")
    print("  - data/polls.csv (raw dataset)")
    print("  - data/polls_cleaned.csv (cleaned dataset)")
    print("  - outputs/bar_chart.png")
    print("  - outputs/pie_chart.png")
    print("  - outputs/stacked_chart.png")
    print("  - outputs/trend_chart.png")
    print("  - outputs/demographic_chart.png")
    print("  - outputs/summary_insights.txt")
    print("\nTo run the Streamlit dashboard:")
    print("  streamlit run src/dashboard.py")


if __name__ == "__main__":
    run_pipeline(use_synthetic=True)
