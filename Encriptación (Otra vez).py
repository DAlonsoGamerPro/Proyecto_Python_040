from tkinter import *
from tkinter import filedialog as fd
import hashlib
root = Tk()
root.geometry("250x190")
root.title("Encriptación")
root.config(bg="light coral")

def apply_md5():
    print("Función MD5")
    text_file = fd.askopenfilename(title = "Abrir Archivo de Texto", filetypes = (("Text Files", "*.txt"), ))
    print(text_file)
    read_file = open(text_file,'r')
    parrafo = read_file.read()
    file_result = hashlib.md5(parrafo.encode())
    file_hex = file_result.hexdigest()
    print(file_hex)
    md5_file = open("md5.txt", 'w')
    md5_file.write(file_hex)
    print(file_hex)
    md5_file.close()
    
btn = Button(root,text="Aplicar MD5", command=apply_md5)
btn.place(relx=0.3,rely=0.5,anchor=CENTER)

root.mainloop()