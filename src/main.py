from python_gedcom_2.parser import Parser
from python_gedcom_2.element.element import Element
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk


class SelectorWindow:

    def __init__(self, root: TkinterDnD.Tk):
        self.root = root

        # Hintergrundbild
        background_image_path = "./images/startbildschirm.1.png"
        self.bg_image = Image.open(background_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Canvas erstellen und Hintergrundbild setzen
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Drag-and-Drop-Feld als Rechteck hinzufügen
        self.drop_zone_rect = self.canvas.create_rectangle(0, 0, 0, 0, fill="#d9d9d9", outline="#aaa", width=2)

        # Button-Bild für "Datei auswählen"
        self.choose_file_image_button = Image.open("./images/Datei auswählen.png")
        

        # Klickbarer "Datei auswählen"-Button innerhalb des Drag-and-Drop-Feldes
        self.choose_file_btn = tk.Button(
            self.root, command=self.choose_file, borderwidth=0, bg="#d9d9d9", activebackground="#c9c9c9"
        )

        # Drag-and-Drop aktivieren
        self.canvas.drop_target_register(DND_FILES)
        self.canvas.dnd_bind('<<Drop>>', self.drop_file)

        # Fenstergröße überwachen und Elemente anpassen
        self.root.bind("<Configure>", self.resize_elements)

    def choose_file(self):
        file_path = filedialog.askopenfilename(
            title="Wähle eine GEDCOM-Datei aus",
            filetypes=[("GEDCOM-Dateien", "*.ged"), ("Alle Dateien", "*.*")]
        )
        if file_path:
            self.process_file(file_path)

    def drop_file(self, event):
        file_path = event.data
        if file_path:
            self.process_file(file_path.strip())

    def process_file(self, file_path):
        # Beispielverarbeitung der Datei
        messagebox.showinfo("Dateiverarbeitung", f"Datei erfolgreich geladen: {file_path}")

    def resize_elements(self, event):
        # Neue Fenstergröße
        width, height = self.root.winfo_width(), self.root.winfo_height()

        # Canvas auf Fullscreen einstellen
        self.canvas.config(width=width, height=height)

        # Hintergrundbild dynamisch skalieren
        resized_bg = self.bg_image.resize((width, height), Image.Resampling.LANCZOS)
        bg_photo_resized = ImageTk.PhotoImage(resized_bg)
        self.canvas.itemconfig(self.bg_image_id, image=bg_photo_resized)
        self.canvas.image = bg_photo_resized  # Verhindert das Entfernen des Bildes durch Garbage Collection

        # Position und Größe des Drag-and-Drop-Feldes
        drop_zone_width = int(width * 0.6)  # 60% der Fensterbreite
        drop_zone_height = int(height * 0.2)  # 20% der Fensterhöhe
        drop_zone_x = int(width * 0.2)  # Horizontal zentriert
        drop_zone_y = int(height * 0.6)  # Im unteren Drittel

        # Anpassen des Drag-and-Drop-Rechtecks
        self.canvas.coords(
            self.drop_zone_rect,
            drop_zone_x,
            drop_zone_y,
            drop_zone_x + drop_zone_width,
            drop_zone_y + drop_zone_height
        )

        # Position und Größe des "Datei auswählen"-Buttons
        btn_width = int(drop_zone_width * 0.3)  # 30% der Breite der Drag-and-Drop-Zone
        btn_height = int(drop_zone_height * 0.5)  # 50% der Höhe der Drag-and-Drop-Zone
        btn_x = drop_zone_x + (drop_zone_width - btn_width) // 2
        btn_y = drop_zone_y + (drop_zone_height - btn_height) // 2
        resized_choose_file = self.choose_file_image_button.resize((btn_width, btn_height), Image.Resampling.LANCZOS)
        choose_file_photo_resized = ImageTk.PhotoImage(resized_choose_file)
        self.choose_file_btn.config(image=choose_file_photo_resized)
        self.choose_file_btn.image = choose_file_photo_resized
        self.choose_file_btn.place(x=btn_x, y=btn_y)


if __name__ == "__main__":
    root = TkinterDnD.Tk()  # TkinterDnD verwenden
    root.title("Roots Revealed - Ancestry Research")
    root.state("zoomed")  # Startet im Fullscreen-Modus
    selector = SelectorWindow(root)
    root.mainloop()

