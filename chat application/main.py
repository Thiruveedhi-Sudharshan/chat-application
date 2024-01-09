import tkinter as tk
from tkinter import Scrollbar

def send_message():
    message = entry.get()
    if message:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You: {message}\n")
        chat_display.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

def receive_message():
    message = "Hello! How can I help you?"
    message="good morning?"
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Bot: {message}\n")
    chat_display.config(state=tk.DISABLED)

# GUI setup
app = tk.Tk()
app.title("Chat Application")

chat_display = tk.Text(app, height=15, width=50,bg='orange', state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

scrollbar = Scrollbar(app, command=chat_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_display.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(app, width=40,bg='pink')
entry.pack(pady=10)

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(pady=5)

receive_message()  # Display an initial message from the bot


app.mainloop()
