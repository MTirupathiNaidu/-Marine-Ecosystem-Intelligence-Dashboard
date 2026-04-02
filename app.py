import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_model, predict
from utils import generate_alert

st.set_page_config(page_title="Marine Ecosystem Intelligence", layout="wide")

st.title("🌊 Marine Ecosystem Intelligence Dashboard")

# Load data
df = pd.read_csv("data.csv")

# Train AI model
model = train_model(df)
df["Status"] = predict(model, df)
df["Alert"] = df.apply(generate_alert, axis=1)

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🤖 AI Analysis", "📄 Report"])

# ---------------- Dashboard ----------------
with tab1:
    st.subheader("Environmental Parameters")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(px.line(df, y="temperature", title="Temperature Trend"))

    with col2:
        st.plotly_chart(px.line(df, y="oxygen", title="Oxygen Levels"))

# ---------------- AI ----------------
with tab2:
    st.subheader("AI Ecosystem Analysis")

    st.dataframe(df)

    st.write("### Status Count")
    st.bar_chart(df["Status"].value_counts())

# ---------------- Report ----------------
with tab3:
    st.subheader("Ecosystem Report")

    anomalies = df[df["Status"] == "Anomaly"]

    if not anomalies.empty:
        st.error("⚠️ Ecosystem Risk Detected")
    else:
        st.success("✅ Ecosystem Stable")

    st.write("### Alerts")
    st.write(df[["temperature", "oxygen", "Alert"]])