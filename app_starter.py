import streamlit as st
import db_reader
import barplot_creator
import AI_summarizor

st.title("Daily Work Dashboard")

# load data from database into dataframe
df = db_reader.get_from_db()

# create barplot for the dataframe
st.header("Activity Log")
fig = barplot_creator.create_plot(df)
st.pyplot(fig)

# generate AI summary with gemini API
if st.button("Generate AI Summary"):
    summary = AI_summarizor.get_summary(df.to_markdown())
    st.write(summary)