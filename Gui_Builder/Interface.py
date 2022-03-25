import tkinter
import os
import PyPDF2


class interface:
    def __init__(self):
        def add_PDFs(pdfs):
            pdf_writer = PyPDF2.PdfFileWriter()
            for file in pdfs:
                f = open(file, "rb")
                pdf_reader = PyPDF2.PdfFileReader(f)
                for i in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(i)
                    pdf_writer.addPage(page)
            pdf_output = open("New Appended File.pdf", "wb")
            pdf_writer.write(pdf_output)
            f.close()
            pdf_output.close()

        def listdirectory(e):
            try:
                lstbx.delete(0, tkinter.END)
                for i, v in enumerate(os.listdir(e1.get())):
                    lstbx.insert(i, v)
            except:
                lstbx.insert(0, "Invalid Directory. Try Again!")

        def joinpdfs(e):
            all_pdfs = []
            for file in os.listdir(e1.get()):
                if file[len(file) - 3 :] == "pdf":
                    all_pdfs.append(e1.get() + "/" + file)
            if all_pdfs == []:
                lbl2.config(text="No, PDFs found directly under this directory.")
            else:
                add_PDFs(all_pdfs)
                lbl2.config(text="PDFs are successfully consolidated!")

        root = tkinter.Tk()
        root.geometry("370x600")
        root.resizable(False, False)
        logo_img = tkinter.PhotoImage(
            file=r".\Gui_Builder\Logo.png"
        )
        logo_img = logo_img.subsample(3, 3)
        logo = tkinter.Label(root, image=logo_img)
        lbl1 = tkinter.Label(root, text="Enter Directory Name.")
        lstbx = tkinter.Listbox(root)
        btn = tkinter.Button(root, text="Condolidate PDFs")
        btn.bind("<Button>", joinpdfs)
        e1 = tkinter.Entry(root)
        e1.bind("<Return>", listdirectory)
        lbl2 = tkinter.Label(root, font="Arial 10 bold")
        logo.grid(row=0, column=0, pady=10, columnspan=2, padx=50)
        lbl1.grid(row=1, column=0, padx=(50, 0))
        e1.grid(row=1, column=1, padx=(0, 50))
        lstbx.grid(row=2, column=0, columnspan=2, pady=10)
        btn.grid(row=3, column=0)
        lbl2.grid(row=4, column=0, pady=10, columnspan=3)
        root.mainloop()
