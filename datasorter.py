import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import json

# Name of the settings file
SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}  # Start with an empty dictionary

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def handle_file(file_path, destinations):
    if not os.path.isfile(file_path):
        return f"❌ '{file_path}' is not a valid file."

    ext = os.path.splitext(file_path)[1].lower()
    dest = destinations.get(ext)

    if not dest:
        return f"⚠️ '{file_path}' has an unsupported extension or no target folder set."

    os.makedirs(dest, exist_ok=True)

    try:
        shutil.copy(file_path, dest)
        return f"✅ {os.path.basename(file_path)} → {dest}"
    except Exception as e:
        return f"❌ Error with {file_path}: {e}"

def upload_files():
    files = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("All Files", "*.*")]
    )
    if files:
        messages = []
        for file_path in files:
            result = handle_file(file_path, destinations)
            messages.append(result)
        messagebox.showinfo("Result", "\n".join(messages))

def open_settings():
    for ext in destinations:
        current = destinations[ext]
        new_path = filedialog.askdirectory(title=f"Select target folder for {ext} files", initialdir=current)
        if new_path:
            destinations[ext] = os.path.normpath(new_path) + os.sep
    save_settings(destinations)
    messagebox.showinfo("Saved", "Settings have been saved.")
    update_supported_filetypes_label()

def update_supported_filetypes_label():
    """Updates the label with the supported file types."""
    supported_types = ", ".join(destinations.keys()) if destinations else "None"
    supported_label.config(text=f"Supported: {supported_types}")

def add_file_type():
    # Ask the user for a new file extension
    new_ext = simpledialog.askstring("Add New File Type", "Enter the file extension (e.g., .txt):")
    
    if not new_ext or not new_ext.startswith("."):
        messagebox.showerror("Error", "Invalid file extension entered. It should start with a dot (e.g., .txt).")
        return

    # Strip spaces and validate the extension
    new_ext = new_ext.strip()

    if not new_ext[1:].isalnum():  # Check if the extension contains only alphanumeric characters after the dot
        messagebox.showerror("Error", "Invalid file extension entered. It should contain only alphanumeric characters (e.g., .txt, .jpg).")
        return

    # Select the target folder for the new file type
    new_path = filedialog.askdirectory(title=f"Select target folder for {new_ext} files")
    if not new_path:
        messagebox.showerror("Error", "No target folder selected.")
        return

    # Save the file type and target folder
    destinations[new_ext] = os.path.normpath(new_path) + os.sep
    save_settings(destinations)
    update_supported_filetypes_label()  # Update the label
    messagebox.showinfo("Success", f"File type {new_ext} has been added and saved.")

def delete_file_type():
    """Allows the user to delete a file type."""
    if not destinations:
        messagebox.showinfo("Info", "No file types to delete.")
        return

    # Ask the user to select a file type to delete
    file_type_to_delete = simpledialog.askstring(
        "Delete File Type", 
        f"Enter the file extension to delete (e.g., .txt):\nSupported: {', '.join(destinations.keys())}"
    )
    if not file_type_to_delete or file_type_to_delete not in destinations:
        messagebox.showerror("Error", "Invalid or non-existent file type entered.")
        return

    # Remove the file type and update settings
    del destinations[file_type_to_delete]
    save_settings(destinations)
    update_supported_filetypes_label()  # Update the label
    messagebox.showinfo("Success", f"File type {file_type_to_delete} has been deleted.")

def delete_file_types_with_checkboxes():
    """Allows the user to delete multiple file types using checkboxes."""
    if not destinations:
        messagebox.showinfo("Info", "No file types to delete.")
        return

    # Create a new window for selecting file types
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete File Types")
    delete_window.geometry("300x400")
    delete_window.resizable(False, False)

    # Dictionary to store the state of each checkbox
    checkbox_vars = {}

    # Function to select all checkboxes
    def select_all():
        for var in checkbox_vars.values():
            var.set(1)

    # Function to deselect all checkboxes
    def deselect_all():
        for var in checkbox_vars.values():
            var.set(0)

    # Function to delete selected file types
    def delete_selected():
        selected_types = [ext for ext, var in checkbox_vars.items() if var.get() == 1]
        if not selected_types:
            messagebox.showinfo("Info", "No file types selected.")
            return

        for ext in selected_types:
            del destinations[ext]

        save_settings(destinations)
        update_supported_filetypes_label()  # Update the label
        messagebox.showinfo("Success", f"Deleted file types: {', '.join(selected_types)}")
        delete_window.destroy()

    # Create checkboxes for each file type
    tk.Label(delete_window, text="Select file types to delete:", pady=10).pack()
    for ext in destinations.keys():
        var = tk.IntVar()
        checkbox_vars[ext] = var
        tk.Checkbutton(delete_window, text=ext, variable=var).pack(anchor="w")

    # Add buttons for "Select All", "Deselect All", and "Delete"
    tk.Button(delete_window, text="Select All", command=select_all).pack(pady=5)
    tk.Button(delete_window, text="Deselect All", command=deselect_all).pack(pady=5)
    tk.Button(delete_window, text="Delete Selected", command=delete_selected).pack(pady=10)

# Start the GUI
root = tk.Tk()
root.title("Portal File Manager")
root.geometry("400x300")  # Adjusted height for additional button
root.resizable(False, False)

destinations = load_settings()

tk.Label(root, text="Portal Data Tool", pady=20).pack()

tk.Button(root, text="Choose Data", command=upload_files, height=2, width=20).pack(pady=10)
tk.Button(root, text="Settings", command=open_settings).pack(pady=5)
tk.Button(root, text="Add File Type", command=add_file_type).pack(pady=5)  # Button to add file types
tk.Button(root, text="Delete File Type", command=delete_file_types_with_checkboxes).pack(pady=5)  # Updated button

# Label for supported file types
supported_label = tk.Label(root, text=f"Supported: {', '.join(destinations.keys()) if destinations else 'None'}")
supported_label.pack(pady=10)

root.mainloop()