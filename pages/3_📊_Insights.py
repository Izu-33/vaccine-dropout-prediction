import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


st.set_page_config(page_title='Insight', layout='wide')
st.logo("images/ovl-logo.png", size="large")
with st.sidebar:
    st.image("images/ovl-logo.png", width=150)

df = pd.read_csv("data/dropout_data.csv")

df["Year"] = df["Year"].astype(int)

latest_year = df["Year"].max()
prev_year = latest_year - 1

dropout_latest = df[df["Year"] == latest_year]["DropoutRate"].mean()
dropout_prev = df[df["Year"] == prev_year]["DropoutRate"].mean()
dropout_diff = dropout_latest - dropout_prev

coverage_cols = ["DTP3", "DTP1", "MCV1"]  # or just one antigen
coverage_latest = df[df["Year"] == latest_year][coverage_cols].mean().mean()
coverage_prev = df[df["Year"] == prev_year][coverage_cols].mean().mean()
coverage_diff = coverage_latest - coverage_prev

latest_dtp3 = df[df["Year"] == latest_year]["DTP3"].mean()
prev_dtp3 = df[df["Year"] == prev_year]["DTP3"].mean()
delta_dtp3 = latest_dtp3 - prev_dtp3

st.title("📈 Dropout and Coverage Report")
st.markdown("---")

st.subheader("📏 Dropout KPIs")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.metric(
        label="Dropout Rate (Latest)",
        value=f"{dropout_latest:.2%}",
        delta=f"{dropout_diff:+.2%}",
        delta_color="inverse",
        border=True
    )

with col2:
    st.metric(
        label=f"Avg Coverage ({latest_year})",
        value=f"{coverage_latest:.2f}%",
        delta=f"{coverage_diff:+.2f}%",
        delta_color="normal",
        border=True
    )

with col3:
    st.metric(
        label=f"DTP3 Coverage ({latest_year})",
        value=f"{latest_dtp3:.1f}%",
        delta=f"{delta_dtp3:+.1f}%",
        delta_color="normal",
        border=True
    )

region_summary = df.groupby("Region").agg({
    "CoverageAvg": "mean",
    "DropoutRate": "mean",
    "DTP3": "mean"
})

region_summary = region_summary.reset_index()
st.table(region_summary)

st.markdown("---")

# Display dropout rate plot
st.subheader("📶 Distribution of Dropout Rates")
fig = px.histogram(df, x="DropoutRate", nbins=20,
                   labels={"DropoutRate": "Dropout Rate (%)"},
                   opacity=0.75,
                   color_discrete_sequence=["#036442"])

fig.update_layout(
    bargap=0.1,
    xaxis_title="Dropout Rate (%)",
    yaxis_title="Frequency",
    template="plotly_white",
    font=dict(
        family="Arial",      
        size=14,             
        color="#036442"
    )
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("🌍 Dropout Rate by Region")

fig = px.box(
    df,
    x="Region",
    y="DropoutRate",
    color="Region",
    color_discrete_sequence=["#036442"]
)

fig.update_layout(
    xaxis_title="Region",
    yaxis_title="Dropout Rate (%)",
    template="plotly_white",
    font=dict(
        family="Arial",
        size=14,
        color="#036442"
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("📈 Dropout vs No Dropout Distribution")

dropout_counts = df['dropout_flag'].value_counts().rename(index={0: 'No Dropout (0)', 1: 'Dropout (1)'})
pie_df = dropout_counts.reset_index()
pie_df.columns = ['Dropout Status', 'Count']

fig = px.pie(pie_df, values='Count', names='Dropout Status',
             color_discrete_sequence=['#4CAF50', '#F44336'])

st.plotly_chart(fig, use_container_width=True)

