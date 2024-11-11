import tkinter as tk

def hasil_prediksi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

entry_list = []
for i in range(10):
    tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:").grid(row=i+1, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entry_list.append(entry)
