import time
import socket

from windows_accessor import get_active_window_info
from data_processor import create_log_entry
from db_connector import save_to_db

def run_collector():
    client_id = socket.gethostname()
    print(f"Log collection started on {client_id}... (Ctrl+C to stop)")
    try:
        while True:
            exe_name, title = get_active_window_info()
            new_log_df = create_log_entry(client_id, exe_name, title)
            save_to_db(new_log_df)
            print(f"Logged: {exe_name}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    run_collector()

