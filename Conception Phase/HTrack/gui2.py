import tkinter as tk

def open_file():
   print("Opening file...")

def save_file():
   print("Saving file...")

def cut_text():
   print("Cutting text...")

def copy_text():
   print("Copying text...")

def paste_text():
   print("Pasting text...")

def create_menu(root):
   menu = tk.Menu(root)

   # Create the "File" menu
   file_menu = tk.Menu(menu, tearoff=False)
   file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
   file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
   file_menu.add_separator()
   file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q")
   menu.add_cascade(label="File", menu=file_menu)

   # Create the "Edit" menu
   edit_menu = tk.Menu(menu, tearoff=False)
   edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
   edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
   edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
   menu.add_cascade(label="Edit", menu=edit_menu)

   # Add the menu to the root window
   root.config(menu=menu)

def create_toolbar(root):
   toolbar = tk.Frame(root)

   # Create toolbar buttons
   open_button = tk.Button(toolbar, text="Open", command=open_file)
   open_button.pack(side=tk.LEFT, padx=2, pady=2)

   save_button = tk.Button(toolbar, text="Save", command=save_file)
   save_button.pack(side=tk.LEFT, padx=2, pady=2)

   cut_button = tk.Button(toolbar, text="Cut", command=cut_text)
   cut_button.pack(side=tk.LEFT, padx=2, pady=2)

   copy_button = tk.Button(toolbar, text="Copy", command=copy_text)
   copy_button.pack(side=tk.LEFT, padx=2, pady=2)

   paste_button = tk.Button(toolbar, text="Paste", command=paste_text)
   paste_button.pack(side=tk.LEFT, padx=2, pady=2)

   # Add the toolbar to the root window
   toolbar.pack(side=tk.TOP, fill=tk.X)

def main():
   root = tk.Tk()
   root.title("Menu and Toolbar Example")
   create_menu(root)
   create_toolbar(root)

   # Configure keyboard shortcuts or bindings
   root.bind("<Control-o>", lambda e: open_file())
   root.bind("<Control-s>", lambda e: save_file())
   root.bind("<Control-x>", lambda e: cut_text())
   root.bind("<Control-c>", lambda e: copy_text())
   root.bind("<Control-v>", lambda e: paste_text())
   root.bind("<Control-q>", lambda e: root.quit())

   root.mainloop()

if __name__ == "__main__":
   main()