"""
analysis.py
Analysis functions for poll data: aggregation, percentage calculation,
and comparative analysis by region/demographic.
"""

import pandas as pd
import numpy as np


def calculate_vote_share(df, group_col="option_selected"):
    """
    Calculate vote counts and percentage share for each option.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.
    group_col : str
        Column to group by (default: option_selected).

    Returns
    -------
    pd.DataFrame
        DataFrame with vote counts and percentages.
    """
    vote_counts = df[group_col].value_counts().reset_index()
    vote_counts.columns = [group_col, "vote_count"]
    total_votes = vote_counts["vote_count"].sum()
    vote_counts["percentage"] = (vote_counts["vote_count"] / total_votes * 100).round(2)
    vote_counts = vote_counts.sort_values("vote_count", ascending=False).reset_index(drop=True)

    print(f"[INFO] Vote share by {group_col}:")
    print(vote_counts.to_string(index=False))
    print(f"[INFO] Total votes: {total_votes}")

    return vote_counts


def analyze_by_region(df):
    """
    Analyze poll results by region.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.

    Returns
    -------
    pd.DataFrame
        Region-wise vote distribution.
    """
    if "region" not in df.columns:
        print("[WARNING] 'region' column not found. Skipping region analysis.")
        return None

    region_analysis = (
        df.groupby(["region", "option_selected"])
        .size()
        .reset_index(name="vote_count")
    )

    region_totals = (
        df.groupby("region").size().reset_index(name="total_votes")
    )

    region_analysis = region_analysis.merge(region_totals, on="region")
    region_analysis["percentage"] = (
        region_analysis["vote_count"] / region_analysis["total_votes"] * 100
    ).round(2)

    print("[INFO] Region-wise analysis:")
    print(region_analysis.to_string(index=False))

    return region_analysis


def analyze_by_age_group(df):
    """
    Analyze poll results by age group.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.

    Returns
    -------
    pd.DataFrame
        Age group-wise vote distribution.
    """
    if "age_group" not in df.columns:
        print("[WARNING] 'age_group' column not found. Skipping age group analysis.")
        return None

    age_analysis = (
        df.groupby(["age_group", "option_selected"])
        .size()
        .reset_index(name="vote_count")
    )

    age_totals = (
        df.groupby("age_group").size().reset_index(name="total_votes")
    )

    age_analysis = age_analysis.merge(age_totals, on="age_group")
    age_analysis["percentage"] = (
        age_analysis["vote_count"] / age_analysis["total_votes"] * 100
    ).round(2)

    print("[INFO] Age group-wise analysis:")
    print(age_analysis.to_string(index=False))

    return age_analysis


def analyze_by_gender(df):
    """
    Analyze poll results by gender.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.

    Returns
    -------
    pd.DataFrame
        Gender-wise vote distribution.
    """
    if "gender" not in df.columns:
        print("[WARNING] 'gender' column not found. Skipping gender analysis.")
        return None

    gender_analysis = (
        df.groupby(["gender", "option_selected"])
        .size()
        .reset_index(name="vote_count")
    )

    gender_totals = (
        df.groupby("gender").size().reset_index(name="total_votes")
    )

    gender_analysis = gender_analysis.merge(gender_totals, on="gender")
    gender_analysis["percentage"] = (
        gender_analysis["vote_count"] / gender_analysis["total_votes"] * 100
    ).round(2)

    print("[INFO] Gender-wise analysis:")
    print(gender_analysis.to_string(index=False))

    return gender_analysis


def identify_leading_option(df, group_col="option_selected"):
    """
    Identify the leading option with the highest vote count.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.
    group_col : str
        Column to identify leading option from.

    Returns
    -------
    dict
        Dictionary with leading option, vote count, and percentage.
    """
    vote_share = calculate_vote_share(df, group_col)
    leading = vote_share.iloc[0]

    result = {
        "leading_option": leading[group_col],
        "vote_count": int(leading["vote_count"]),
        "percentage": float(leading["percentage"]),
    }

    print(f"[INFO] Leading option: {result['leading_option']} ({result['vote_count']} votes, {result['percentage']}%)")

    return result


def analyze_trend_over_time(df):
    """
    Analyze poll response trends over time if date column exists.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.

    Returns
    -------
    pd.DataFrame
        Daily vote counts over time.
    """
    if "date" not in df.columns:
        print("[WARNING] 'date' column not found. Skipping trend analysis.")
        return None

    df_copy = df.copy()
    df_copy["date_only"] = df_copy["date"].dt.date

    trend = (
        df_copy.groupby("date_only")
        .size()
        .reset_index(name="vote_count")
    )
    trend.columns = ["date", "vote_count"]

    print("[INFO] Trend over time (first 10 days):")
    print(trend.head(10).to_string(index=False))

    return trend


def run_full_analysis(df):
    """
    Run the complete analysis pipeline on the poll dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.

    Returns
    -------
    dict
        Dictionary containing all analysis results.
    """
    print("\n" + "=" * 60)
    print("RUNNING FULL POLL ANALYSIS")
    print("=" * 60 + "\n")

    results = {}

    # Vote share by option
    results["vote_share"] = calculate_vote_share(df)

    # Leading option
    results["leading_option"] = identify_leading_option(df)

    # Region-wise analysis
    results["region_analysis"] = analyze_by_region(df)

    # Age group analysis
    results["age_analysis"] = analyze_by_age_group(df)

    # Gender analysis
    results["gender_analysis"] = analyze_by_gender(df)

    # Trend over time
    results["trend"] = analyze_trend_over_time(df)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60 + "\n")

    return results
