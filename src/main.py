import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from python_gedcom_2.parser import Parser
from python_gedcom_2.element.individual import IndividualElement


class MainWindow(tk.Tk):
    def __init__(self, parser: Parser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = parser
        self.config(bg="#36312D")
        self.container = tk.Frame(self, bg="#36312D")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.show_frame(SelectorFrame)

    def show_frame(self, frame_class) -> None:
        for widget in self.container.winfo_children():
            widget.destroy()

        frame = frame_class(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class SelectorFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: MainWindow):
        super().__init__(parent, bg="#36312D")
        self.controller = controller

        self.logo_image_original = Image.open("./images/logo.png")

        self.logo_label = tk.Label(self, bg="#36312D")
        self.logo_label.place(relx=0.5, rely=0.3, anchor="center")

        self.drop_area = tk.Frame(self, bg="#36312D")
        self.drop_area.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.6, relheight=0.2)

        self.button_canvas = tk.Canvas(self.drop_area, highlightthickness=0, bg="#36312D")
        self.button_canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3, relheight=0.5)

        self.button_canvas.bind("<Configure>", self.resize_elements)

        self.button_canvas.bind("<Button-1>", self.on_button_click)

        self.after_idle(self.initial_draw)

    def initial_draw(self):
        self.update_idletasks()
        event = type('event', (object,), {'width': self.button_canvas.winfo_width(), 'height': self.button_canvas.winfo_height()})
        self.resize_elements(event)


    def choose_file(self):
        file_path = filedialog.askopenfilename(
            title="Wähle eine GEDCOM-Datei aus",
            filetypes=[("GEDCOM-Dateien", "*.ged"), ("Alle Dateien", "*.*")]
        )
        if file_path:
            self.controller.parser.parse_file(file_path)
            self.controller.show_frame(DisplayFrame)

    def on_button_click(self, event):
        self.choose_file()

    def drop_file(self):
        messagebox.showinfo("Drag-and-Drop", "Datei abgelegt!")

    def draw_rounded_rect_button(self, canvas_width, canvas_height):
        self.button_canvas.delete("all")

        border_color = "#A48164"
        bg_color = "#BF9874"
        text_color = "#ffffff"
        border_thickness = 4

        corner_radius = min(canvas_width, canvas_height) * 0.2

        x1, y1 = 0, 0
        x2, y2 = canvas_width, canvas_height
        ix1, iy1 = border_thickness, border_thickness
        ix2, iy2 = canvas_width - border_thickness, canvas_height - border_thickness

        self._draw_rounded_rect(self.button_canvas, x1, y1, x2, y2, corner_radius, border_color)
        self._draw_rounded_rect(self.button_canvas, ix1, iy1, ix2, iy2, corner_radius - border_thickness, bg_color)

        font_size = max(8, int(canvas_height * 0.3))
        self.button_canvas.create_text(
            canvas_width / 2,
            canvas_height / 2,
            text="Datei auswählen",
            fill=text_color,
            font=("Arial", font_size, "bold")
        )

    def _draw_rounded_rect(self, canvas, x1, y1, x2, y2, r, color):
        canvas.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(x2-2*r, y1, x2, y1+2*r, start=0, extent=90, fill=color, outline=color)
        canvas.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90, fill=color, outline=color)
        canvas.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90, fill=color, outline=color)

        canvas.create_rectangle(x1+r, y1, x2-r, y1+r, fill=color, outline=color)
        canvas.create_rectangle(x1+r, y2-r, x2-r, y2, fill=color, outline=color)
        canvas.create_rectangle(x1, y1+r, x1+r, y2-r, fill=color, outline=color)
        canvas.create_rectangle(x2-r, y1+r, x2, y2-r, fill=color, outline=color)
        canvas.create_rectangle(x1+r, y1+r, x2-r, y2-r, fill=color, outline=color)

    def resize_elements(self, event):
        width = self.winfo_width()
        if width > 0:
            logo_size = int(width * 0.2)
            if logo_size > 0:
                resized_logo = self.logo_image_original.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(resized_logo)
                self.logo_label.config(image=self.logo_photo)

        canvas_w = self.button_canvas.winfo_width()
        canvas_h = self.button_canvas.winfo_height()
        if canvas_w > 0 and canvas_h > 0:
            self.draw_rounded_rect_button(canvas_w, canvas_h)


class DisplayFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: MainWindow):
        super().__init__(parent, bg="#36312D")
        self.controller = controller

        root_elements = controller.parser.get_root_child_elements()

        display_label = tk.Label(self, text="Parsed GEDCOM Data:", font=("Arial", 16), bg="#36312D", fg="#FFFFFF")
        display_label.pack(pady=20)

        data_text = tk.Text(self, wrap="word", width=80, height=20, bg="#36312D", fg="#FFFFFF", insertbackground="#FFFFFF")
        data_text.pack(pady=10)

        children: list[tuple[IndividualElement, int]] = []

        for element in root_elements:
            if isinstance(element, IndividualElement):
                if not element.is_child_in_a_family():
                    children.append((element, 0))

        while len(children) > 0:
            indiv, level = children.pop(0)
            data_text.insert(tk.END, f"{'   ' * level}{indiv.get_name()}\n")
            c: list[IndividualElement] = self.controller.parser.get_natural_children(indiv)
            for child in c:
                children.insert(0, (child, level + 1))


if __name__ == "__main__":
    parser: Parser = Parser()
    main = MainWindow(parser)
    main.title("Roots Revealed - Ancestry Research")
    main.state("zoomed")
    main.mainloop()
