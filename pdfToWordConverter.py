import tkinter as tk
from tkinter import filedialog   
import pdf2docx  
import os 


def select_file():
   #opens up a window where you can select a PDF file which you want to convert it into the word file
    file_path = filedialog.askopenfilename(    
        filetypes=[("PDF Files", "*.pdf")])
    pdf_path_entry.delete(0, tk.END)
    pdf_path_entry.insert(0, file_path)

def convert_pdf_to_word():
#Here you are giving the path,to whre the docx flie is stored
    pdf_path = pdf_path_entry.get()

    downloads_dir = os.path.expanduser("~/Downloads")

    initial_dir = downloads_dir

    file_path = filedialog.asksaveasfilename(
        initialdir=initial_dir,
        title="Save Word File",
        defaultextension=".docx",
        filetypes=[("Word Files", "*.docx")],
    )

    pdf2docx.parse(pdf_path, file_path)

root = tk.Tk()
root.title("PDF_to_Word Converter")
root.geometry("400x400")
root.configure(padx=200, pady=200)
root.configure(padx=20, pady=20, bg="cyan")


font = ("TkDefaultFont", 20)

# Labels and buttons of user interface
pdf_path_label = tk.Label(root,text=" PDF to WORD file Converter ", font=("Arial",34),bg="cyan")
pdf_path_label.grid(row=0, column=2, padx=20, pady=20)

pdf_path_label = tk.Label(root, text="PDF File:", font=(font),bg="cyan")
pdf_path_label.grid(row=1, column=1, padx=120, pady=60)

pdf_path_entry = tk.Entry(root, font=font)
pdf_path_entry.grid(row=1, column=2, padx=120, pady=60)

pdf_path_button = tk.Button(root, text="Select File", command=select_file, font=('arial',20,'bold'),height=1,width=20,bg="silver",fg='black')
pdf_path_button.grid(row=1, column=3, padx=120, pady=60)

word_path_label = tk.Label(root, text=" Word File:", font=font,bg="cyan")
word_path_label.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to Word", command=convert_pdf_to_word, font=('arial',20,'bold'),height=1,width=20,bg="silver",fg='black')
convert_button.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()