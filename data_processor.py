from datetime import datetime
import pandas as pd

def create_log_entry(client_id, executable_name, win_title):
    data = {
        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        'Client_ID': [client_id],
        'Executable_name': [executable_name],
        'Win_title': [win_title],
        'Status': ['active']
    }
    return pd.DataFrame(data)