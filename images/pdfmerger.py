import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")

        self.pdf_files = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.file_listbox = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=5)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.frame, text="Add PDFs", command=self.add_pdf_files)
        self.add_button.pack(pady=5)

        self.merge_button = tk.Button(self.frame, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=10)

    def add_pdf_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file_path in file_paths:
            self.pdf_files.append(file_path)
            self.file_listbox.insert(tk.END, file_path)

    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            return

        pdf_merger = PdfMerger()
        for pdf_file in self.pdf_files:
            pdf_merger.append(pdf_file)

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_file:
            pdf_merger.write(output_file)
            pdf_merger.close()
            tk.messagebox.showinfo("Success", "PDFs merged successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
