import tkinter as tk
from tkinter import filedialog
import os


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text.delete("1.0", tk.END)
                text.insert(tk.END, file.read())
                update_word_char_count()
                update_file_size(file_path)
        except Exception as e:
            # Handle the exception and show a custom error message
            tk.messagebox.showerror(
                "Error", "Failed to open : Invalid file type")


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                             ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
        update_word_char_count()
        update_file_size(file_path)


def clear_text():
    text.delete("1.0", tk.END)
    update_word_char_count()
    update_file_size(None)  # Reset file size when clearing text


def update_word_char_count(event=None):
    content = text.get("1.0", tk.END)
    word_count = len(content.split())
    char_count = len(content) - content.count('\n') - content.count(' ')
    count_label.config(
        text=f"Words: {word_count}, Characters (no spaces): {char_count}")


def update_file_size(file_path):
    if file_path and os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        size_label.config(text=f"File Size: {file_size} bytes")
    else:
        size_label.config(text="File Size: N/A")


def search_text():
    search_term = search_entry.get().lower()  # Convert search term to lowercase
    if search_term:
        # Remove previous highlights
        text.tag_remove("highlight", "1.0", tk.END)
        start = "1.0"
        found = False
        while True:
            # Use nocase=True for case-insensitive search
            start = text.search(search_term, start,
                                stopindex=tk.END, nocase=True)
            if not start:
                break
            found = True
            end = f"{start}+{len(search_term)}c"
            text.tag_add("highlight", start, end)
            start = end
        if not found:
            # Display a message when the search term is not found
            tk.messagebox.showinfo("Search", "Search term not found.")
        # Focus on the first highlighted word if found
        elif found:
            text.see(text.index("highlight.first"))


root = tk.Tk()
root.title("Text Editor")

# Set background and foreground colors for the root window
root.configure(bg="light gray")

# Create a frame for the left column with background color
left_frame = tk.Frame(root, bg="light gray")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Create and place buttons with background and foreground colors
open_button = tk.Button(left_frame, text="Open",
                        command=open_file, bg="dark blue", fg="black")
open_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

save_button = tk.Button(left_frame, text="Save",
                        command=save_file, bg="dark green", fg="black")
save_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

clear_button = tk.Button(left_frame, text="Clear",
                         command=clear_text, bg="dark red", fg="black")
clear_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

search_entry = tk.Entry(left_frame)
search_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

search_button = tk.Button(left_frame, text="Search",
                          command=search_text, bg="orange", fg="black")
search_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# Create a Text widget with a black background, white text, and white cursor
text = tk.Text(root, bg="black", fg="white", insertbackground="white")
text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create a label to display word and character count
count_label = tk.Label(root, text="", bg="light gray", fg="black")
count_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Create a label to display file size
size_label = tk.Label(root, text="", bg="light gray", fg="black")
size_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Configure row and column weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Bind the Text widget's KeyRelease event to update the count_label
text.bind("<KeyRelease>", update_word_char_count)

# Create a tag for highlighting search results
text.tag_configure("highlight", background="yellow")

root.geometry("800x600")
root.mainloop()
