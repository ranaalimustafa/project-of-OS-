import tkinter as tk
from tkinter import scrolledtext, messagebox
from backend import get_bot_reply
from database import save_to_db, export_chat

def run_gui():
    def send_message():
        user_msg = user_input.get()
        if not user_msg.strip():
            return

        insert_chat("You", user_msg, "user")
        user_input.delete(0, tk.END)
        root.after(200, lambda: handle_bot(user_msg))

    def handle_bot(user_msg):
        bot_msg = get_bot_reply(user_msg)
        insert_chat("Bot", bot_msg, "bot")
        save_to_db(user_msg, bot_msg)

    def insert_chat(sender, msg, tag):
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"{sender}: ", tag)
        chat_area.insert(tk.END, msg + "\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)

    def export_history():
        result = export_chat()
        messagebox.showinfo("Export", result)

    global root, user_input, chat_area
    root = tk.Tk()
    root.title("🧠 DeepSeek Styled Chatbot")
    root.geometry("700x720")
    root.configure(bg="#0f172a")

    title = tk.Label(root, text="💬 Chatbot Project", font=("Helvetica", 18, "bold"),
                     bg="#0f172a", fg="#38bdf8")
    title.pack(pady=10)

    frame = tk.Frame(root, bg="#0f172a")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    chat_area = scrolledtext.ScrolledText(
        frame, wrap=tk.WORD, font=("Consolas", 13),
        bg="#1e293b", fg="#f1f5f9", insertbackground="white"
    )
    chat_area.pack(fill=tk.BOTH, expand=True)
    chat_area.config(state=tk.DISABLED)
    chat_area.tag_config("user", foreground="#60a5fa")
    chat_area.tag_config("bot", foreground="#34d399")

    bottom = tk.Frame(root, bg="#0f172a")
    bottom.pack(pady=5, fill=tk.X)

    user_input = tk.Entry(bottom, font=("Consolas", 13), bg="#1e293b", fg="white", insertbackground="white")
    user_input.pack(side=tk.LEFT, padx=10, ipady=8, fill=tk.X, expand=True)
    user_input.bind("<Return>", lambda e: send_message())

    send_btn = tk.Button(bottom, text="Send", command=send_message, bg="#38bdf8", fg="white",
                         font=("Helvetica", 11, "bold"))
    send_btn.pack(side=tk.LEFT, padx=10, ipadx=10)

    export_btn = tk.Button(root, text="📤 Export Chat", command=export_history,
                           bg="#4ade80", fg="black", font=("Helvetica", 10, "bold"))
    export_btn.pack(pady=(0, 10))


    root.mainloop()