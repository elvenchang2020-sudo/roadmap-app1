import win32api
import win32process
import win32gui
import socket
import time
import pandas as pd
from datetime import datetime, timedelta
import os

# create a dataframe table to hold records of log data
# timestamp - the time point when log is recorded
# client_id - the current windows user
# excutable_name - the core app the user is using
# win_title - the title of windows the user is using, detailed information of what the user is doing
# status - the current state, active or idel
log_record = pd.DataFrame(columns=['Timestamp', 'Client_ID', 'Executable_name', 'Win_title', 'Status'])

# get data for the 2nd column - Client_ID
client_id = socket.gethostname()

# show notice of starting
print("Collecting PC logs... (Please press ctrl + C to stop)")

# collect log every 2 seconds, with a non-stopping while loop
while True:
    # get data for the first column - Timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # get the id of current windows opened from Windows system
    win_id = win32gui.GetForegroundWindow()
    # get data for the 4th column - Win_title
    win_title = win32gui.GetWindowText(win_id)

    try:    
        # get the id of the process id of current app
        _, process_id = win32process.GetWindowThreadProcessId(win_id)
        # get temporary access to current process, ox0400 | ox0010 means Query & Read
        process_handle = win32api.OpenProcess(0x0400 | 0x0010, False, process_id)
        # find the install path of current process
        executable_path =  win32process.GetModuleFileNameEx(process_handle, 0)
        # close the process reading, or it will cause error
        win32api.CloseHandle(process_handle)
        # get data for the 3rd column - Excutable_name, which means the actual app is being used
        executable_name = os.path.basename(executable_path)
    except Exception:
        # build error handling method, in case this program failed to get the process name
        executable_name = 'unkown'

    # get data for the 5th column - Status, now by default 'active'
    status = 'active'

    # write all data into the dataframe table
    log_captured = [timestamp, client_id, executable_name, win_title, status]
    log_record.loc[len(log_record)] = log_captured 

    # show the acquired log data
    print(log_captured)
    # set the pace as every 2 seconds
    time.sleep(2)


