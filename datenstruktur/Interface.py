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

# Funktion zum Anpassen der Größe und Position von Canvas und Buttons
def resize_elements(event):
    # Neue Fenstergröße
    width, height = root.winfo_width(), root.winfo_height()
    
    # Canvas auf Fullscreen einstellen
    canvas.config(width=width, height=height)
    
    # Hintergrundbild dynamisch skalieren
    resized_bg = bg_image.resize((width, height), Image.Resampling.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(resized_bg)
    canvas.itemconfig(bg_image_id, image=bg_photo_resized)
    canvas.image = bg_photo_resized  # Verhindert das Entfernen des Bildes durch Garbage Collection

    # Buttons dynamisch skalieren und positionieren
    btn_width = int(width * 0.15)  # Buttons sollen 15% der Fensterbreite haben
    btn_height = int(height * 0.07)  # Buttons sollen 7% der Fensterhöhe haben

    # Buttons neu skalieren
    resized_choose_file = choose_file_image.resize((btn_width, btn_height), Image.Resampling.LANCZOS)
    choose_file_photo_resized = ImageTk.PhotoImage(resized_choose_file)
    choose_file_btn.config(image=choose_file_photo_resized)
    choose_file_btn.image = choose_file_photo_resized

    resized_drop_file = drop_file_image.resize((btn_width, btn_height), Image.Resampling.LANCZOS)
    drop_file_photo_resized = ImageTk.PhotoImage(resized_drop_file)
    drop_file_btn.config(image=drop_file_photo_resized)
    drop_file_btn.image = drop_file_photo_resized

    # Buttons neu positionieren
    choose_file_btn.place(x=int(width * 0.42), y=int(height * 0.6))
    drop_file_btn.place(x=int(width * 0.42), y=int(height * 0.7))

# Hauptfenster erstellen
root = tk.Tk()
root.title("Roots Revealed - Ancestry Research")
root.state("zoomed")  # Startet im Fullscreen-Modus

# Hintergrundbild laden
background_image_path = "h:\\Downloads\\startbildschirm.1.png"
bg_image = Image.open(background_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas erstellen und Hintergrundbild setzen
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)
bg_image_id = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Button-Bilder laden
choose_file_image = Image.open("h:\\Downloads\\datei auswhlen.png")
drop_file_image = Image.open("h:\\Downloads\\preview_datei ablegen.png")

# Buttons erstellen
choose_file_btn = tk.Button(
    root, command=choose_file, borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)
drop_file_btn = tk.Button(
    root, command=drop_file, borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)

# Eventlistener für Fenstergröße
root.bind("<Configure>", resize_elements)

# Hauptfenster starten
root.mainloop()
