"""
insights.py
Summary insights generation from poll analysis results.
"""

import os


def generate_insights(analysis_results, output_path="outputs/summary_insights.txt"):
    """
    Generate text-based summary insights from the analysis results.

    Parameters
    ----------
    analysis_results : dict
        Output from run_full_analysis containing vote_share, leading_option,
        region_analysis, age_analysis, gender_analysis, and trend.
    output_path : str
        Path to save the insights text file.
    """
    lines = []
    lines.append("=" * 60)
    lines.append("POLL RESULTS - SUMMARY INSIGHTS")
    lines.append("=" * 60)
    lines.append("")

    # Leading option
    leading = analysis_results.get("leading_option", {})
    lines.append("1. LEADING OPTION")
    lines.append("-" * 40)
    if leading:
        lines.append(f"   Option: {leading.get('leading_option', 'N/A')}")
        lines.append(f"   Votes: {leading.get('vote_count', 'N/A')}")
        lines.append(f"   Percentage: {leading.get('percentage', 'N/A')}%")
    lines.append("")

    # Vote share summary
    vote_share = analysis_results.get("vote_share")
    lines.append("2. VOTE SHARE SUMMARY")
    lines.append("-" * 40)
    if vote_share is not None:
        for _, row in vote_share.iterrows():
            lines.append(f"   {row['option_selected']}: {row['vote_count']} votes ({row['percentage']}%)")
    lines.append("")

    # Region-wise insights
    region_analysis = analysis_results.get("region_analysis")
    lines.append("3. REGION-WISE INSIGHTS")
    lines.append("-" * 40)
    if region_analysis is not None:
        # Find top region per option
        for option in region_analysis["option_selected"].unique():
            subset = region_analysis[region_analysis["option_selected"] == option]
            top_region = subset.loc[subset["vote_count"].idxmax()]
            lines.append(f"   {option} leads in: {top_region['region']} ({top_region['vote_count']} votes, {top_region['percentage']}%)")
    lines.append("")

    # Age group insights
    age_analysis = analysis_results.get("age_analysis")
    lines.append("4. DEMOGRAPHIC INSIGHTS (AGE GROUP)")
    lines.append("-" * 40)
    if age_analysis is not None:
        for option in age_analysis["option_selected"].unique():
            subset = age_analysis[age_analysis["option_selected"] == option]
            top_age = subset.loc[subset["vote_count"].idxmax()]
            lines.append(f"   {option} most popular among: {top_age['age_group']} ({top_age['vote_count']} votes, {top_age['percentage']}%)")
    lines.append("")

    # Gender insights
    gender_analysis = analysis_results.get("gender_analysis")
    lines.append("5. GENDER-WISE INSIGHTS")
    lines.append("-" * 40)
    if gender_analysis is not None:
        for option in gender_analysis["option_selected"].unique():
            subset = gender_analysis[gender_analysis["option_selected"] == option]
            top_gender = subset.loc[subset["vote_count"].idxmax()]
            lines.append(f"   {option} preferred by: {top_gender['gender']} ({top_gender['vote_count']} votes, {top_gender['percentage']}%)")
    lines.append("")

    # Trend insights
    trend = analysis_results.get("trend")
    lines.append("6. TREND OVER TIME")
    lines.append("-" * 40)
    if trend is not None and not trend.empty:
        max_day = trend.loc[trend["vote_count"].idxmax()]
        min_day = trend.loc[trend["vote_count"].idxmin()]
        lines.append(f"   Peak day: {max_day['date']} ({max_day['vote_count']} votes)")
        lines.append(f"   Lowest day: {min_day['date']} ({min_day['vote_count']} votes)")
        lines.append(f"   Total responses over period: {trend['vote_count'].sum()}")
    lines.append("")

    # Recommendations
    lines.append("7. RECOMMENDATIONS")
    lines.append("-" * 40)
    if leading:
        lines.append(f"   - Focus on {leading['leading_option']} as it is the most preferred option ({leading['percentage']}% of votes).")
    if region_analysis is not None:
        top_region = region_analysis.loc[region_analysis["vote_count"].idxmax(), "region"]
        lines.append(f"   - Target marketing efforts in {top_region} region which shows highest engagement.")
    if age_analysis is not None:
        top_age = age_analysis.loc[age_analysis["vote_count"].idxmax(), "age_group"]
        lines.append(f"   - Tailor messaging for {top_age} age group which has the highest response rate.")
    lines.append("")
    lines.append("=" * 60)
    lines.append("END OF INSIGHTS REPORT")
    lines.append("=" * 60)

    insights_text = "\n".join(lines)

    # Save to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(insights_text)

    print(f"[INFO] Summary insights saved to: {output_path}")
    print("\n" + insights_text)

    return insights_text
