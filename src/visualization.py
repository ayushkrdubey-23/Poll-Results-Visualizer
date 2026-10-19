"""
visualization.py
Chart generation for poll results: bar, pie, stacked, trend, and demographic charts.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


def set_plot_style():
    """Set consistent styling for matplotlib/seaborn charts."""
    plt.style.use("seaborn-v0_8")
    sns.set_palette("Set2")


def plot_bar_chart(vote_share_df, output_path="outputs/bar_chart.png"):
    """
    Create a bar chart of option-wise vote share.

    Parameters
    ----------
    vote_share_df : pd.DataFrame
        Output from calculate_vote_share with columns [option_selected, vote_count, percentage].
    output_path : str
        Path to save the chart image.
    """
    set_plot_style()
    fig, ax = plt.subplots(figsize=(10, 6))

    options = vote_share_df["option_selected"]
    counts = vote_share_df["vote_count"]
    percentages = vote_share_df["percentage"]

    bars = ax.bar(options, counts, color=sns.color_palette("Set2", len(options)))
    ax.set_xlabel("Option", fontsize=12)
    ax.set_ylabel("Vote Count", fontsize=12)
    ax.set_title("Option-wise Vote Share", fontsize=16, fontweight="bold")
    ax.tick_params(axis="x", rotation=45)

    # Add value labels on bars
    for bar, count, pct in zip(bars, counts, percentages):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(counts) * 0.01,
            f"{count}\n({pct}%)",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Bar chart saved: {output_path}")


def plot_pie_chart(vote_share_df, output_path="outputs/pie_chart.png"):
    """
    Create a pie chart of option distribution.

    Parameters
    ----------
    vote_share_df : pd.DataFrame
        Output from calculate_vote_share.
    output_path : str
        Path to save the chart image.
    """
    set_plot_style()
    fig, ax = plt.subplots(figsize=(8, 8))

    options = vote_share_df["option_selected"]
    counts = vote_share_df["vote_count"]
    percentages = vote_share_df["percentage"]

    wedges, texts, autotexts = ax.pie(
        counts,
        labels=options,
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2", len(options)),
        startangle=90,
        textprops={"fontsize": 10},
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.set_title("Option Distribution", fontsize=16, fontweight="bold")
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Pie chart saved: {output_path}")


def plot_stacked_chart(region_analysis_df, output_path="outputs/stacked_chart.png"):
    """
    Create a stacked bar chart of region-wise option distribution.

    Parameters
    ----------
    region_analysis_df : pd.DataFrame
        Output from analyze_by_region.
    output_path : str
        Path to save the chart image.
    """
    if region_analysis_df is None:
        print("[WARNING] No region analysis data. Skipping stacked chart.")
        return

    set_plot_style()

    # Pivot data for stacked bar chart
    pivot = region_analysis_df.pivot(index="region", columns="option_selected", values="vote_count").fillna(0)

    fig, ax = plt.subplots(figsize=(10, 6))

    bottom = np.zeros(len(pivot))
    colors = sns.color_palette("Set2", len(pivot.columns))

    for i, option in enumerate(pivot.columns):
        ax.bar(
            pivot.index,
            pivot[option],
            bottom=bottom,
            label=option,
            color=colors[i],
        )
        bottom += pivot[option].values

    ax.set_xlabel("Region", fontsize=12)
    ax.set_ylabel("Vote Count", fontsize=12)
    ax.set_title("Region-wise Option Distribution (Stacked)", fontsize=16, fontweight="bold")
    ax.legend(title="Option", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Stacked chart saved: {output_path}")


def plot_trend_chart(trend_df, output_path="outputs/trend_chart.png"):
    """
    Create a line chart of votes over time.

    Parameters
    ----------
    trend_df : pd.DataFrame
        Output from analyze_trend_over_time with columns [date, vote_count].
    output_path : str
        Path to save the chart image.
    """
    if trend_df is None or trend_df.empty:
        print("[WARNING] No trend data. Skipping trend chart.")
        return

    set_plot_style()
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(trend_df["date"], trend_df["vote_count"], marker="o", linewidth=2, markersize=6)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Vote Count", fontsize=12)
    ax.set_title("Poll Responses Over Time", fontsize=16, fontweight="bold")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Trend chart saved: {output_path}")


def plot_demographic_chart(age_analysis_df, output_path="outputs/demographic_chart.png"):
    """
    Create a grouped bar chart of age group vs option distribution.

    Parameters
    ----------
    age_analysis_df : pd.DataFrame
        Output from analyze_by_age_group.
    output_path : str
        Path to save the chart image.
    """
    if age_analysis_df is None:
        print("[WARNING] No age group analysis data. Skipping demographic chart.")
        return

    set_plot_style()

    pivot = age_analysis_df.pivot(index="age_group", columns="option_selected", values="percentage").fillna(0)

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(pivot))
    width = 0.8 / len(pivot.columns)
    colors = sns.color_palette("Set2", len(pivot.columns))

    for i, option in enumerate(pivot.columns):
        ax.bar(
            x + i * width,
            pivot[option],
            width,
            label=option,
            color=colors[i],
        )

    ax.set_xlabel("Age Group", fontsize=12)
    ax.set_ylabel("Percentage (%)", fontsize=12)
    ax.set_title("Demographic Comparison: Age Group vs Option", fontsize=16, fontweight="bold")
    ax.set_xticks(x + width * (len(pivot.columns) - 1) / 2)
    ax.set_xticklabels(pivot.index)
    ax.legend(title="Option", bbox_to_anchor=(1.05, 1), loc="upper left")
    ax.set_ylim(0, 100)
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] Demographic chart saved: {output_path}")


def generate_all_charts(df, analysis_results):
    """
    Generate all visualization charts from the analysis results.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned poll dataset.
    analysis_results : dict
        Output from run_full_analysis.
    """
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60 + "\n")

    plot_bar_chart(analysis_results["vote_share"])
    plot_pie_chart(analysis_results["vote_share"])
    plot_stacked_chart(analysis_results.get("region_analysis"))
    plot_trend_chart(analysis_results.get("trend"))
    plot_demographic_chart(analysis_results.get("age_analysis"))

    print("\n[INFO] All charts generated successfully!")
