import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Funktion für "Datei auswählen"-Button
def choose_file():
    file_path = filedialog.askopenfilename(
        title="Wähle eine GEDCOM-Datei aus",
        filetypes=[("GEDCOM-Dateien", "*.ged"), ("Alle Dateien", "*.*")]
    )
    if file_path:
        messagebox.showinfo("Datei ausgewählt", f"Datei: {file_path}")

# Funktion für "Datei ablegen"-Button
def drop_file():
    messagebox.showinfo("Datei ablegen", "Funktion 'Datei ablegen' ist noch nicht implementiert.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Roots Revealed - Ancestry Research")
root.geometry("800x600")  # Fenstergröße festlegen
root.resizable(False, False)

# Hintergrundbild laden
background_image_path = "h:\Downloads\startbildschirm.1.png"  # Pfad zu Ihrem hochgeladenen Bild
bg_image = Image.open(background_image_path)
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Größe anpassen
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas erstellen und Hintergrundbild setzen
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Button-Bilder laden und skalieren
choose_file_image = Image.open("h:\Downloads\Müll.jpg")  # Pfad zum Bild "Datei auswählen"
choose_file_image = choose_file_image.resize((138, 41), Image.Resampling.LANCZOS)  # Zielgröße skalieren
choose_file_photo = ImageTk.PhotoImage(choose_file_image)

drop_file_image = Image.open("h:\Downloads\preview_datei ablegen.png")  # Pfad zum Bild "Datei ablegen"
drop_file_image = drop_file_image.resize((138, 41), Image.Resampling.LANCZOS)  # Zielgröße skalieren
drop_file_photo = ImageTk.PhotoImage(drop_file_image)

# Buttons anpassen
choose_file_btn = tk.Button(
    root, image=choose_file_photo, command=choose_file,
    borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)
choose_file_btn.place(x=330, y=370)

drop_file_btn = tk.Button(
    root, image=drop_file_photo, command=drop_file,
    borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)
drop_file_btn.place(x=330, y=435)


# Hauptfenster starten
root.mainloop()
