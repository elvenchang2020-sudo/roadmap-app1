import streamlit as st
import db_utils
import viz_utils
import ai_utils

st.title("📊 Productivity Dashboard")

# 1. Load Data
df = db_utils.get_from_db()

# 2. Visualization
st.header("Activity Log")
fig = viz_utils.create_plot(df)
st.pyplot(fig)

# 3. AI Insights
if st.button("Generate AI Summary"):
    summary = ai_utils.get_summary(df.to_markdown())
    st.write(summary)