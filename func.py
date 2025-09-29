import psutil
import uuid
import datetime
import random
import string


def get_disk_info(path='/'):
    """Retrieve disk usage statistics for the given path."""
    try:
        disk_usage = psutil.disk_usage(path)
        total_gb = round(disk_usage.total / (1024 ** 3), 2)
        used_gb = round(disk_usage.used / (1024 ** 3), 2)
        free_gb = round(disk_usage.free / (1024 ** 3), 2)
        return total_gb, used_gb, free_gb
    except FileNotFoundError:
        return None, None, None


def update_disk_display(total_label, used_label, free_label, progress_bar, 
                        path):
    """Update disk usage statistics for the given path."""
    total, used, free = get_disk_info(path)
    if total is not None:
        total_label.config(text=f"Total: {total} GB")
        used_label.config(text=f"Used: {used} GB")
        free_label.config(text=f"Free: {free} GB")
        percentage_used = (used / total) * 100 if total > 0 else 0
        progress_bar['value'] = percentage_used
    else:
        total_label.config(text="Path not found")
        used_label.config(text="")
        free_label.config(text="")
        progress_bar['value'] = 0
    
        
def create_disk_space_gui():
    """Create the main GUI window for disk space monitoring."""
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("Disk Space Monitor")

    path = '/'

    total_label = tk.Label(root, text="Total: ")
    total_label.pack()

    used_label = tk.Label(root, text="Used: ")
    used_label.pack()

    free_label = tk.Label(root, text="Free: ")
    free_label.pack()

    progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, 
                                   mode='determinate')
    progress_bar.pack(pady=10)

    def refresh():
        update_disk_display(total_label, used_label, free_label, progress_bar,
                            path)
        root.after(5000, refresh)  # Refresh every 5 seconds

    refresh()  # Initial call to populate data
    root.mainloop()


def generate_uuid_primary_key():
    id_control = str(uuid.uuid4())[0:7]
    return id_control


# new_id = generate_uuid_primary_key()
# print(f'Generated UUID: {new_id}')


def generate_timestamp_key():
    timestamp_now = datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S')
    random_suffix = ''.join(random.choices(string.ascii_uppercase + 
                                           string.digits, k=5))
    print(f'{timestamp_now}-{random_suffix}')
   
    
class CustomIntructionGenerator:
    def __init__(self, initial_value=19800):
        self._current_id = initial_value
        self.date_now = datetime.datetime.now().strftime('%d-%m-%y')
        
    def generate_next_key(self):
        self._current_id += 1 
        return str(f'PN-PNH/CSP/USGPN-Instruction-{
          self._current_id}-{self.date_now}')    


key_gen = CustomIntructionGenerator()
new_id_1 = key_gen.generate_next_key()
new_id_2 = key_gen.generate_next_key()
print(f'Custem Sequential Keys: {new_id_1}, {new_id_2}')


    
