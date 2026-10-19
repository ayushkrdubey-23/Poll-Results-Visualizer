"""
dashboard.py
Optional Streamlit dashboard for interactive poll results exploration.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def load_data(file_path="data/polls_cleaned.csv"):
    """Load cleaned poll data."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"File not found: {file_path}. Please run main.py first to generate data.")
        return None


def main():
    st.set_page_config(page_title="Poll Results Visualizer", layout="wide")

    st.title("Poll Results Visualizer")
    st.markdown("Interactive dashboard for exploring poll and survey results.")

    df = load_data()
    if df is None:
        return

    # Sidebar filters
    st.sidebar.header("Filters")
    questions = df["question"].unique() if "question" in df.columns else []
    selected_question = st.sidebar.selectbox("Select Question", ["All"] + list(questions))

    regions = df["region"].unique() if "region" in df.columns else []
    selected_region = st.sidebar.selectbox("Select Region", ["All"] + list(regions))

    age_groups = df["age_group"].unique() if "age_group" in df.columns else []
    selected_age = st.sidebar.selectbox("Select Age Group", ["All"] + list(age_groups))

    # Apply filters
    filtered_df = df.copy()
    if selected_question != "All" and "question" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["question"] == selected_question]
    if selected_region != "All" and "region" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["region"] == selected_region]
    if selected_age != "All" and "age_group" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["age_group"] == selected_age]

    # Key metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Responses", len(filtered_df))
    with col2:
        if "option_selected" in filtered_df.columns:
            top_option = filtered_df["option_selected"].value_counts().index[0]
            st.metric("Top Option", top_option)
    with col3:
        if "option_selected" in filtered_df.columns:
            top_pct = filtered_df["option_selected"].value_counts(normalize=True).iloc[0] * 100
            st.metric("Top Option Share", f"{top_pct:.1f}%")

    # Option-wise bar chart
    st.subheader("Option-wise Vote Share")
    if "option_selected" in filtered_df.columns:
        vote_counts = filtered_df["option_selected"].value_counts().reset_index()
        vote_counts.columns = ["Option", "Votes"]
        fig = px.bar(vote_counts, x="Option", y="Votes", color="Option",
                     title="Vote Count by Option")
        st.plotly_chart(fig, use_container_width=True)

    # Pie chart
    st.subheader("Option Distribution (Pie Chart)")
    if "option_selected" in filtered_df.columns:
        fig = px.pie(vote_counts, names="Option", values="Votes", title="Option Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # Region-wise stacked bar
    st.subheader("Region-wise Option Distribution")
    if "region" in filtered_df.columns and "option_selected" in filtered_df.columns:
        region_df = (
            filtered_df.groupby(["region", "option_selected"])
            .size()
            .reset_index(name="count")
        )
        fig = px.bar(region_df, x="region", y="count", color="option_selected",
                     title="Region-wise Option Distribution",
                     barmode="stack")
        st.plotly_chart(fig, use_container_width=True)

    # Age group analysis
    st.subheader("Age Group vs Option")
    if "age_group" in filtered_df.columns and "option_selected" in filtered_df.columns:
        age_df = (
            filtered_df.groupby(["age_group", "option_selected"])
            .size()
            .reset_index(name="count")
        )
        fig = px.bar(age_df, x="age_group", y="count", color="option_selected",
                     title="Age Group vs Option Distribution",
                     barmode="group")
        st.plotly_chart(fig, use_container_width=True)

    # Trend over time
    st.subheader("Responses Over Time")
    if "date" in filtered_df.columns:
        filtered_df["date"] = pd.to_datetime(filtered_df["date"])
        trend_df = (
            filtered_df.groupby(filtered_df["date"].dt.date)
            .size()
            .reset_index(name="count")
        )
        trend_df.columns = ["Date", "Count"]
        fig = px.line(trend_df, x="Date", y="Count", markers=True,
                      title="Poll Responses Over Time")
        st.plotly_chart(fig, use_container_width=True)

    # Data preview
    st.subheader("Data Preview")
    st.dataframe(filtered_df.head(20), use_container_width=True)

    st.markdown("---")
    st.markdown("**Poll Results Visualizer** | Built with Streamlit, Pandas, and Plotly")


if __name__ == "__main__":
    main()
