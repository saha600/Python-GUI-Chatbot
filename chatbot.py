import tkinter as tk
from tkinter import scrolledtext
from responses import get_response

# -------------------------------
# Send Message Function
# -------------------------------
def send_message(event=None):
    user_message = entry.get().strip()

    if user_message == "":
        return

    chat_area.config(state="normal")

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    bot_response = get_response(user_message)

    chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")

    chat_area.config(state="disabled")

    chat_area.see(tk.END)

    entry.delete(0, tk.END)

# -------------------------------
# Clear Chat
# -------------------------------
def clear_chat():
    chat_area.config(state="normal")
    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Hello! 👋 I am your Python GUI Chatbot.\n"
        "Bot: Type a message to begin.\n\n"
    )

    chat_area.config(state="disabled")

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()

root.title("Python GUI Chatbot")
root.geometry("700x600")
root.configure(bg="#e8f4f8")

# -------------------------------
# Heading
# -------------------------------
heading = tk.Label(
    root,
    text="🤖 Python GUI Chatbot",
    font=("Arial", 20, "bold"),
    bg="#e8f4f8",
    fg="#0b5394"
)

heading.pack(pady=10)

# -------------------------------
# Chat Area
# -------------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=75,
    height=22,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    "Bot: Hello! 👋 I am your Python GUI Chatbot.\n"
    "Bot: Type a message to begin.\n\n"
)

chat_area.config(state="disabled")

# -------------------------------
# Entry Box
# -------------------------------
entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=50
)

entry.pack(pady=10)

entry.bind("<Return>", send_message)

# -------------------------------
# Buttons
# -------------------------------
button_frame = tk.Frame(root, bg="#e8f4f8")
button_frame.pack()

send_button = tk.Button(
    button_frame,
    text="Send",
    width=12,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    command=send_message
)

send_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    bg="orange",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear_chat
)

clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=12,
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    command=root.destroy
)

exit_button.grid(row=0, column=2, padx=10)

root.mainloop()