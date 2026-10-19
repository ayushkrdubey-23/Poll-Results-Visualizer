"""
cleaning.py
Data cleaning functions for poll datasets.
"""

import pandas as pd
import numpy as np


def clean_poll_data(df):
    """
    Clean the poll dataset by handling missing values, duplicates,
    and standardizing formats.

    Parameters
    ----------
    df : pd.DataFrame
        Raw poll dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned poll dataset.
    """
    df = df.copy()

    initial_rows = len(df)
    print(f"[INFO] Initial rows: {initial_rows}")

    # 1. Handle missing values
    missing_before = df.isnull().sum().sum()
    print(f"[INFO] Missing values before cleaning: {missing_before}")

    # Fill missing categorical values with mode
    for col in ["region", "age_group", "gender", "option_selected"]:
        if col in df.columns and df[col].isnull().any():
            mode_val = df[col].mode()
            if not mode_val.empty:
                df[col] = df[col].fillna(mode_val[0])

    # Drop rows where critical columns are still missing
    critical_cols = ["respondent_id", "question", "option_selected"]
    df = df.dropna(subset=[c for c in critical_cols if c in df.columns])

    missing_after = df.isnull().sum().sum()
    print(f"[INFO] Missing values after cleaning: {missing_after}")

    # 2. Remove duplicates
    duplicates_before = df.duplicated().sum()
    print(f"[INFO] Duplicate rows before: {duplicates_before}")
    df = df.drop_duplicates()
    duplicates_after = df.duplicated().sum()
    print(f"[INFO] Duplicate rows after: {duplicates_after}")

    # 3. Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 4. Standardize categorical values
    if "region" in df.columns:
        df["region"] = df["region"].str.strip().str.title()
    if "age_group" in df.columns:
        df["age_group"] = df["age_group"].str.strip()
    if "gender" in df.columns:
        df["gender"] = df["gender"].str.strip().str.title()
    if "option_selected" in df.columns:
        df["option_selected"] = df["option_selected"].str.strip()
    if "question" in df.columns:
        df["question"] = df["question"].str.strip()

    # 5. Convert date column to datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        # Drop rows with invalid dates
        invalid_dates = df["date"].isnull().sum()
        if invalid_dates > 0:
            print(f"[INFO] Rows with invalid dates dropped: {invalid_dates}")
            df = df.dropna(subset=["date"])

    # 6. Reset index
    df = df.reset_index(drop=True)

    final_rows = len(df)
    print(f"[INFO] Final rows after cleaning: {final_rows}")
    print(f"[INFO] Rows removed: {initial_rows - final_rows}")

    return df


def save_cleaned_data(df, output_path="data/polls_cleaned.csv"):
    """
    Save the cleaned dataset to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.
    output_path : str
        Path to save the cleaned CSV file.
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Cleaned data saved to: {output_path}")
