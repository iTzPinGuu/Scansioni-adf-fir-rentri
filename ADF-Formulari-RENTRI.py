from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os
import random
import string
import json
from pathlib import Path

# Costanti per la configurazione
CONFIG_DIR = Path.home() / ".pdfmerger"
CONFIG_FILE = CONFIG_DIR / "preferenze.json"

def salva_config(output_folder):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"output_folder": output_folder}, f)

def carica_config():
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                return config.get("output_folder", "")
        return ""
    except Exception:
        return ""

def nome_casuale(lunghezza=15):
    caratteri = string.ascii_lowercase + string.digits
    return ''.join(random.choices(caratteri, k=lunghezza))

def crea_pdf_fronte_retro(front_path, back_path, output_folder):
    try:
        front_reader = PdfReader(front_path)
        back_reader = PdfReader(back_path)
        
        if len(front_reader.pages) != len(back_reader.pages):
            messagebox.showerror("Errore", "I file PDF devono avere lo stesso numero di pagine")
            return False
            
        retro_pages = list(back_reader.pages)[::-1]
        
        for i in range(len(front_reader.pages)):
            writer = PdfWriter()
            writer.add_page(front_reader.pages[i])
            writer.add_page(retro_pages[i])
            
            output_path = os.path.join(output_folder, f"{nome_casuale()}.pdf")
            with open(output_path, "wb") as f:
                writer.write(f)
                
        return True
        
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore:\n{str(e)}")
        return False

class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unione PDF Fronti/Retro")
        self.root.geometry("500x300")
        
        self.front_path = ""
        self.back_path = ""
        self.output_folder = carica_config()
        
        self.create_widgets()
        self.update_status()
    
    def create_widgets(self):
        main_frame = Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=BOTH)
        
        Button(main_frame, text="Seleziona PDF Fronti", command=self.select_front).pack(pady=10, fill=X)
        Button(main_frame, text="Seleziona PDF Retro", command=self.select_back).pack(pady=10, fill=X)
        Button(main_frame, text="Seleziona Cartella Output", command=self.select_output).pack(pady=10, fill=X)
        Button(main_frame, text="Elabora PDF", command=self.process_files).pack(pady=20, fill=X)
        
        self.status_label = Label(main_frame, text="", fg="gray")
        self.status_label.pack()
    
    def select_front(self):
        self.front_path = filedialog.askopenfilename(
            title="Seleziona file FRONTI",
            filetypes=[("PDF files", "*.pdf")]
        )
        self.update_status()
    
    def select_back(self):
        self.back_path = filedialog.askopenfilename(
            title="Seleziona file RETRO",
            filetypes=[("PDF files", "*.pdf")]
        )
        self.update_status()
    
    def select_output(self):
        new_folder = filedialog.askdirectory(title="Seleziona cartella di output")
        if new_folder:
            self.output_folder = new_folder
            salva_config(self.output_folder)
            self.update_status()
    
    def update_status(self):
        status = []
        if self.front_path:
            status.append(f"Fronti: {os.path.basename(self.front_path)}")
        if self.back_path:
            status.append(f"Retro: {os.path.basename(self.back_path)}")
        if self.output_folder:
            status.append(f"Output: {os.path.basename(self.output_folder)}")
        
        self.status_label.config(text=" | ".join(status))
    
    def process_files(self):
        if not all([self.front_path, self.back_path, self.output_folder]):
            messagebox.showwarning("Attenzione", "Seleziona tutti i file e la cartella di output")
            return
            
        if crea_pdf_fronte_retro(self.front_path, self.back_path, self.output_folder):
            messagebox.showinfo("Successo", "PDF creati correttamente!")
            self.front_path = ""
            self.back_path = ""
            self.update_status()

if __name__ == "__main__":
    root = Tk()
    app = PdfMergerApp(root)
    root.mainloop()
