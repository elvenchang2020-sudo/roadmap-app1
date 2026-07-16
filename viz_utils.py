import matplotlib.pyplot as plt
import seaborn as sns

def create_plot(df):
    """Generates a stacked bar chart from the dataframe."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Simple check to ensure we have data
    if df.empty:
        ax.text(0.5, 0.5, 'No data available', ha='center', va='center')
        return fig

    # Plotting the stacked bar chart
    sns.histplot(
        data=df, 
        x="Timestamp", 
        # Note: If you don't have 'Duration_hours' in your DB log, 
        # you might need to aggregate the data here.
        hue="Executable_name", 
        multiple="stack",
        shrink=0.8,
        ax=ax
    )
    
    plt.xticks(rotation=45)
    plt.title("Daily App Usage")
    plt.tight_layout()
    
    return fig