import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from document_translator import translate_document
from text_translator import translate_text
from voice_translator import translate_voice

# ====== File Browse for Document ======
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[
        ("Supported files", "*.txt *.docx"),
        ("Text files", "*.txt"),
        ("Word documents", "*.docx")
    ])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# ====== Document Translation ======
def handle_document_translation():
    file_path = file_entry.get().strip()
    lang = doc_lang_entry.get().strip()
    if not file_path or not lang:
        messagebox.showerror("Error", "Please select a file and enter target language code.")
        return
    try:
        _, file_out = translate_document(file_path, lang)
        messagebox.showinfo("Success", f"✅ Document translated successfully!\nSaved to:\n{file_out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ====== Text Translation ======
def handle_text_translation():
    input_text = text_input.get("1.0", tk.END).strip()
    lang = text_lang_entry.get().strip()
    output_type = text_output_choice.get()
    if not input_text or not lang:
        messagebox.showerror("Error", "Please enter text and target language code.")
        return
    try:
        result = translate_text(input_text, lang, output_type)
        if output_type == "text" and result:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, result)
        elif output_type == "voice":
            messagebox.showinfo("Playing Audio", "🔊 Translation is being played as voice.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ====== Voice Translation ======
def handle_voice_translation():
    lang = voice_lang_entry.get().strip()
    output_type = voice_output_choice.get()
    if not lang:
        messagebox.showerror("Error", "Please enter target language code.")
        return
    try:
        result = translate_voice(lang, output_type)
        if output_type == "text" and result:
            voice_output.delete("1.0", tk.END)
            voice_output.insert(tk.END, result)
        elif output_type == "voice":
            messagebox.showinfo("Playing Audio", "🎧 Translation is being played as voice.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ====== Main Window ======
root = tk.Tk()
root.title("🌍 Multimodal Translator")
root.geometry("680x520")
root.configure(bg="#eceff1")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ====== Document Tab ======
doc_tab = tk.Frame(notebook, bg="#eef2f3")
notebook.add(doc_tab, text="📄 Document Translator")

tk.Label(doc_tab, text="Select File:", bg="#eef2f3").pack(pady=5)
file_entry = tk.Entry(doc_tab, width=50)
file_entry.pack(pady=5)
tk.Button(doc_tab, text="Browse", command=browse_file, bg="#4CAF50", fg="white").pack(pady=5)

tk.Label(doc_tab, text="Target Language Code:", bg="#eef2f3").pack(pady=5)
doc_lang_entry = tk.Entry(doc_tab)
doc_lang_entry.pack(pady=5)

tk.Button(doc_tab, text="Translate Document", command=handle_document_translation,
          bg="#2196F3", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

# ====== Text Tab ======
text_tab = tk.Frame(notebook, bg="#f9f9f9")
notebook.add(text_tab, text="📝 Text Translator")

tk.Label(text_tab, text="Enter Text:", bg="#f9f9f9").pack(pady=5)
text_input = tk.Text(text_tab, height=5, width=60)
text_input.pack(pady=5)

tk.Label(text_tab, text="Target Language Code:", bg="#f9f9f9").pack(pady=5)
text_lang_entry = tk.Entry(text_tab)
text_lang_entry.pack(pady=5)

text_output_choice = tk.StringVar(value="text")
tk.Radiobutton(text_tab, text="Text Output", variable=text_output_choice, value="text", bg="#f9f9f9").pack()
tk.Radiobutton(text_tab, text="Voice Output", variable=text_output_choice, value="voice", bg="#f9f9f9").pack()

tk.Button(text_tab, text="Translate", command=handle_text_translation,
          bg="#FF9800", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

text_output = tk.Text(text_tab, height=5, width=60)
text_output.pack(pady=5)

# ====== Voice Tab ======
voice_tab = tk.Frame(notebook, bg="#fffaf0")
notebook.add(voice_tab, text="🎤 Voice Translator")

tk.Label(voice_tab, text="Target Language Code:", bg="#fffaf0").pack(pady=5)
voice_lang_entry = tk.Entry(voice_tab)
voice_lang_entry.pack(pady=5)

voice_output_choice = tk.StringVar(value="text")
tk.Radiobutton(voice_tab, text="Text Output", variable=voice_output_choice, value="text", bg="#fffaf0").pack()
tk.Radiobutton(voice_tab, text="Voice Output", variable=voice_output_choice, value="voice", bg="#fffaf0").pack()

tk.Button(voice_tab, text="Start Voice Translation", command=handle_voice_translation,
          bg="#9C27B0", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

voice_output = tk.Text(voice_tab, height=5, width=60)
voice_output.pack(pady=5)

root.mainloop()
