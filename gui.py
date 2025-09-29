import tkinter as tk
import os
from tkinter import filedialog, messagebox


def open_file_explorer():
    root = tk.Tk()
    root.title('File Explorer')
    root.geometry('600x400')
    
    content_lbl = tk.Label(root, text='File content')
    content_lbl.pack(pady=40)
    
    open_btn = tk.Button(root, text='Open Local File',
                         command=browser_local_files(content_lbl=content_lbl))
    open_btn.pack(pady=20)
    
    root.mainloop()
   
    
def browser_local_files(content_lbl):
    file_path = filedialog.askopenfilename(title='Select a file',
                                           filetypes=(('Text files', '*.txt'), 
                                                      ('All files', '*.*')))
    if file_path:
        messagebox.showinfo('Selected File', file_path)
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(f'File content:\n {content}')
                content_lbl.config(text=content)
        except Exception as e:
            print(f'Error reading file: {e}')         
            
            
def pop_up_menu():
    root = tk.Tk()
    root.title('Pop-Up App')  
    root.geometry('600x400')
    
    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label='Option 1', 
                           command=lambda: print('option 1 selected'))          
    popup_menu.add_command(label='Option 2', 
                           command=lambda: print('option 2 selected'))
    popup_menu.add_separator()
    popup_menu.add_command(label='Exit', command=root.quit)
    
    def show_popup_menu(event):
        try:
            popup_menu.tk_popup(event.x_root, event.y_root)
        except Exception as e:
            print(e)
        finally:
            popup_menu.grab_release() 
            
    root.bind('<Button-3>', show_popup_menu)
    lbl = tk.Label(root, text='Right-click anywhere')
    lbl.pack(pady=10) 
    
    root.mainloop()  
  
  
global_folder_path = None


def folder_gui():
  
    def browser_folder():
        folder_path = filedialog.askdirectory()
        global global_folder_path
        global_folder_path = folder_path
        if folder_path:
            folder_contents.delete(0, tk.END)
            current_path_lbl.config(text=f'Current Path: {folder_path}')
            for item in os.listdir(folder_path):
                folder_contents.insert(tk.END, item)
                            
    def open_selected_file(event):
        selected_index = folder_contents.curselection()
        if selected_index:
            file_path = folder_contents.get(selected_index[0])
            folder_path = global_folder_path
            # print(folder_path)
            # print(absolute_path)
            file_path_real = os.path.join(folder_path, file_path)
            try:
                os.startfile(file_path_real)
                # print(file_path_real)
                
            except Exception as e:
                print(f'Error opening file {e}')               
                
    root = tk.Tk()
    root.title('Folder Explorer App')
    root.geometry('600x400')
    
    current_path_lbl = tk.Label(root, text='Current Path: ')
    current_path_lbl.pack(pady=10)
    browser_btn = tk.Button(root, text='Browser Folder',
                            command=browser_folder)
    browser_btn.pack(pady=5)
    
    folder_contents = tk.Listbox(root, selectmode=tk.SINGLE)
    folder_contents.pack(fill='both', expand=True)
    
    scroll_bar = tk.Scrollbar(root, orient='vertical',
                              command=folder_contents.yview)
    scroll_bar.pack(side='right', fill='y')
    folder_contents.config(yscrollcommand=scroll_bar.set)
    
    folder_contents.bind('<Double-Button-1>', open_selected_file)
    
    root.mainloop()
    
    
              
                                      