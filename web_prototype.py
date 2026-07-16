import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Productivity Dashboard")

data = {
    'Timestamp': [
        '07-12', '07-12', '07-12', '07-12', '07-12',
        '07-13', '07-13', '07-13', '07-13', '07-13',
        '07-14', '07-14', '07-14', '07-14', '07-14'
    ],
    'Executable_name': [
        'excel.exe', 'slack.exe', 'chrome.exe', 'vscode.exe', 'spotify.exe',
        'excel.exe', 'slack.exe', 'chrome.exe', 'vscode.exe', 'spotify.exe',
        'excel.exe', 'slack.exe', 'chrome.exe', 'vscode.exe', 'spotify.exe'
    ],
    'Duration_hours': [
        1.64, 1.63, 1.58, 1.58, 1.56,  # 07-12
        1.20, 2.10, 0.50, 3.00, 0.80,  # 07-13
        0.90, 1.50, 2.20, 1.10, 0.40   # 07-14
    ]
}
df = pd.DataFrame(data)

# Streamlit App Layout
st.set_page_config(page_title="Productivity Dashboard", layout="wide")
st.title("My Daily Productivity")

# 2. Top 3 Most Used Apps Section
st.header("Top 3 Apps")
col1, col2, col3 = st.columns(3)
col1.metric("1st Place", "excel.exe")
col2.metric("2nd Place", "slack.exe")
col3.metric("3rd Place", "chrome.exe")

st.divider()

# 3. Daily Usage Stacked Bar Section
st.header("📈 Daily Usage Stacked Bar")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(
    data=df, 
    x="Timestamp", 
    weights="Duration_hours", 
    hue="Executable_name", 
    multiple="stack",
    shrink=0.5,
    ax=ax
)
st.pyplot(fig)

# 4. AI Summary Section
st.header("📝 Daily AI Summary")
st.markdown("""
* **作業内容1**：Slackを用いたチームメンバーとのコミュニケーションおよびチャット対応
* **作業内容2**：Excelを使用した予算レポートの作成および売上データの集計
* **作業内容3**：VS Codeによるプログラムのコーディングおよび開発環境の設定変更
""")