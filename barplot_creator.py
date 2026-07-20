import matplotlib.pyplot as plt
import seaborn as sns

# define a accumulative bar plot function to show app using times within a day
def create_plot(df):
    # fix the barplot size to suit web display
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # handle no data error
    if df.empty:
        ax.text(0.5, 0.5, 'No data available', ha='center', va='center')
        return fig

    # use histplot method because sns.barplot() cannot support accumulative bar plot
    sns.histplot(
        data=df, 
        x="Timestamp", 
        hue="Executable_name", 
        multiple="stack",
        shrink=0.8,
        ax=ax
    )
    
    plt.title("Daily Work Time")
    
    return fig