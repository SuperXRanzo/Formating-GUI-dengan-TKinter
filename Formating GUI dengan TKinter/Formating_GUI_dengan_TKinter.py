import tkinter as tk

def hasil_prediksi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

