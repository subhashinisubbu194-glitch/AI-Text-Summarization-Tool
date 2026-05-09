import tkinter as tk
from tkinter import scrolledtext, messagebox

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')


# =========================
# SUMMARIZATION FUNCTION
# =========================
def summarize_text():

    # Get input text
    text = input_text.get("1.0", tk.END).strip()

    # Validate input
    if len(text) < 100:
        messagebox.showwarning(
            "Warning",
            "Please enter a longer article (minimum 100 characters)."
        )
        return

    try:

        # Parse text
        parser = PlaintextParser.from_string(
            text,
            Tokenizer("english")
        )

        # Create summarizer
        summarizer = LsaSummarizer()

        # Dynamic summary length
        total_sentences = len(text.split("."))

        sentence_count = max(2, total_sentences // 4)

        # Generate summary
        summary = summarizer(
            parser.document,
            sentence_count
        )

        # Format summary
        final_summary = ""

        for sentence in summary:

            cleaned = str(sentence).strip()

            # Shorten lengthy sentences
            if len(cleaned) > 150:
                cleaned = cleaned[:150] + "..."

            final_summary += "• " + cleaned + "\n\n"

        # Clear previous output
        output_text.delete("1.0", tk.END)

        # Display summary
        output_text.insert(tk.END, final_summary)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()

root.title("AI Text Summarization Tool")

root.geometry("1000x700")

root.config(bg="#f2f2f2")


# =========================
# TITLE
# =========================
title = tk.Label(
    root,
    text="AI Text Summarization Tool",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)

title.pack(pady=15)


# =========================
# INPUT LABEL
# =========================
input_label = tk.Label(
    root,
    text="Enter Long Article / Paragraph:",
    font=("Arial", 14),
    bg="#f2f2f2"
)

input_label.pack()


# =========================
# INPUT TEXT AREA
# =========================
input_text = scrolledtext.ScrolledText(
    root,
    width=110,
    height=15,
    font=("Arial", 11),
    wrap=tk.WORD
)

input_text.pack(pady=10)


# =========================
# SUMMARIZE BUTTON
# =========================
summarize_btn = tk.Button(
    root,
    text="Generate Summary",
    font=("Arial", 14, "bold"),
    bg="#0078D7",
    fg="white",
    padx=15,
    pady=8,
    cursor="hand2",
    command=summarize_text
)

summarize_btn.pack(pady=10)


# =========================
# OUTPUT LABEL
# =========================
output_label = tk.Label(
    root,
    text="Summary Output:",
    font=("Arial", 14),
    bg="#f2f2f2"
)

output_label.pack()


# =========================
# OUTPUT TEXT AREA
# =========================
output_text = scrolledtext.ScrolledText(
    root,
    width=110,
    height=12,
    font=("Arial", 11),
    wrap=tk.WORD
)

output_text.pack(pady=10)


# =========================
# FOOTER
# =========================
footer = tk.Label(
    root,
    text="Developed using Python, NLP, Sumy, and NLTK",
    font=("Arial", 10),
    bg="#f2f2f2",
    fg="gray"
)

footer.pack(pady=5)


# =========================
# RUN APPLICATION
# =========================
root.mainloop()
