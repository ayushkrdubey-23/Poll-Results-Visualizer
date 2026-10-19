"""
data_loader.py
Loads poll data from CSV, Excel, or generates a synthetic dataset.
"""

import os
import pandas as pd
import numpy as np


def generate_synthetic_poll_data(n_rows=1000, output_path="data/polls.csv"):
    """
    Generate a synthetic poll dataset with realistic response patterns.

    Parameters
    ----------
    n_rows : int
        Number of poll responses to generate.
    output_path : str
        Path to save the generated CSV file.

    Returns
    -------
    pd.DataFrame
        The generated poll dataset.
    """
    np.random.seed(42)

    questions = [
        "Which product do you prefer?",
        "How satisfied are you with our service?",
        "Which feature is most important to you?",
        "Would you recommend us to a friend?",
    ]

    options_by_question = {
        "Which product do you prefer?": ["Product A", "Product B", "Product C", "Product D"],
        "How satisfied are you with our service?": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"],
        "Which feature is most important to you?": ["Performance", "Price", "Design", "Support"],
        "Would you recommend us to a friend?": ["Yes", "No", "Maybe"],
    }

    regions = ["North", "South", "East", "West"]
    age_groups = ["18-25", "26-35", "36-45", "46-60", "60+"]
    genders = ["Male", "Female", "Other"]

    data = []
    for i in range(n_rows):
        respondent_id = f"R{i+1:04d}"
        date = pd.Timestamp("2026-01-01") + pd.Timedelta(days=np.random.randint(0, 90))
        question = np.random.choice(questions)
        options = options_by_question[question]
        option_selected = np.random.choice(options, p=[0.4, 0.3, 0.2, 0.1][: len(options)])
        region = np.random.choice(regions, p=[0.3, 0.25, 0.25, 0.2])
        age_group = np.random.choice(age_groups, p=[0.25, 0.3, 0.25, 0.15, 0.05])
        gender = np.random.choice(genders, p=[0.45, 0.5, 0.05])

        data.append({
            "respondent_id": respondent_id,
            "date": date.strftime("%Y-%m-%d"),
            "question": question,
            "option_selected": option_selected,
            "region": region,
            "age_group": age_group,
            "gender": gender,
        })

    df = pd.DataFrame(data)

    # Introduce some missing values and duplicates for realism
    missing_indices = np.random.choice(df.index, size=int(n_rows * 0.02), replace=False)
    df.loc[missing_indices, "region"] = np.nan

    duplicate_indices = np.random.choice(df.index, size=int(n_rows * 0.01), replace=False)
    df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"[INFO] Synthetic poll dataset generated: {output_path}")
    print(f"[INFO] Total rows: {len(df)}")
    print(f"[INFO] Columns: {list(df.columns)}")

    return df


def load_poll_data(file_path="data/polls.csv"):
    """
    Load poll data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded poll dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    print(f"[INFO] Loaded poll data from: {file_path}")
    print(f"[INFO] Shape: {df.shape}")
    print(f"[INFO] Columns: {list(df.columns)}")

    return df


def load_excel_data(file_path, sheet_name=0):
    """
    Load poll data from an Excel file.

    Parameters
    ----------
    file_path : str
        Path to the Excel file.
    sheet_name : str or int
        Sheet name or index to load.

    Returns
    -------
    pd.DataFrame
        The loaded poll dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(f"[INFO] Loaded poll data from Excel: {file_path}")
    print(f"[INFO] Shape: {df.shape}")
    print(f"[INFO] Columns: {list(df.columns)}")

    return df
