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

# Funktion für Drag-and-Drop-Feld (nur als Platzhalter)
def drop_file():
    messagebox.showinfo("Drag-and-Drop", "Datei abgelegt!")

# Funktion zum Anpassen der Größe und Position von Canvas, Drag-and-Drop-Feld und Buttons
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

    # Position und Größe des Drag-and-Drop-Feldes
    drop_zone_width = int(width * 0.6)  # 60% der Fensterbreite
    drop_zone_height = int(height * 0.2)  # 20% der Fensterhöhe
    drop_zone_x = int(width * 0.2)  # Horizontal zentriert
    drop_zone_y = int(height * 0.6)  # Im unteren Drittel

    # Anpassen des Drag-and-Drop-Rechtecks
    canvas.coords(drop_zone_rect, drop_zone_x, drop_zone_y,
                  drop_zone_x + drop_zone_width, drop_zone_y + drop_zone_height)
    
    # Position und Größe des "Datei auswählen"-Buttons
    btn_width = int(drop_zone_width * 0.3)  # 30% der Breite der Drag-and-Drop-Zone
    btn_height = int(drop_zone_height * 0.5)  # 50% der Höhe der Drag-and-Drop-Zone
    btn_x = drop_zone_x + (drop_zone_width - btn_width) // 2
    btn_y = drop_zone_y + (drop_zone_height - btn_height) // 2

    resized_choose_file = choose_file_image.resize((btn_width, btn_height), Image.Resampling.LANCZOS)
    choose_file_photo_resized = ImageTk.PhotoImage(resized_choose_file)
    choose_file_btn.config(image=choose_file_photo_resized)
    choose_file_btn.image = choose_file_photo_resized
    choose_file_btn.place(x=btn_x, y=btn_y)

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

# Drag-and-Drop-Feld als Rechteck hinzufügen
drop_zone_rect = canvas.create_rectangle(0, 0, 0, 0, fill="#d9d9d9", outline="#aaa", width=2)

# Button-Bild für "Datei auswählen"
choose_file_image = Image.open("h:\\Downloads\\datei auswhlen.png")

# Klickbarer "Datei auswählen"-Button innerhalb des Drag-and-Drop-Feldes
choose_file_btn = tk.Button(
    root, command=choose_file, borderwidth=0, bg="#d9d9d9", activebackground="#c9c9c9"
)

# Eventlistener für Fenstergröße
root.bind("<Configure>", resize_elements)

# Hauptfenster starten
root.mainloop()
