import win32gui
import win32process
import win32api
import os

def get_active_window_info():
    try:
        win_id = win32gui.GetForegroundWindow()
        win_title = win32gui.GetWindowText(win_id)
        _, pid = win32process.GetWindowThreadProcessId(win_id)
        process_handle = win32api.OpenProcess(0x0400 | 0x0010, False, pid)
        executable_path = win32process.GetModuleFileNameEx(process_handle, 0)
        win32api.CloseHandle(process_handle)
        executable_name = os.path.basename(executable_path)
        return executable_name, win_title
    except Exception:
        return 'unknown', 'unknown'