import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Masterlist V5")
        self.geometry("500x500")
        self.option_add("*tearOff", False)
        self.after(0, lambda: self.state("zoomed"))

        style = ttk.Style(self)

        self.tk.call('source', 'forest-light.tcl')
        style.theme_use('forest-light')

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=5, pady=5, fill='both', expand=True)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=10)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # SIDE PANEL WIDGETS
        self.side_panel = tk.Frame(self.main_frame)
        self.side_panel.grid(column=0, row=0, padx=5, pady=5, sticky='news')
        self.side_panel.grid_columnconfigure(0, weight=1)

        self.area_cbox = ttk.Combobox(self.side_panel, state='readonly', values=["Area 1", "Area 2", "Area 3", "Area 4"])
        self.area_cbox.set(value="Select Area")
        self.area_cbox.grid(column=0, row=0, padx=5, pady=5, sticky='news')

        self.ar_category = ttk.Entry(self.side_panel)
        self.ar_category.grid(column=0, row=1, padx=5, pady=5, sticky='ew')
        self.placeholder(self.ar_category, "AR Category")

        abnormality_ph = "Nature of abnormality"
        self.abnormality = ttk.Entry(self.side_panel)
        self.abnormality.grid(column=0, row=2, padx=5, pady=5, sticky='ew')
        self.placeholder(self.abnormality, abnormality_ph)

        self.affected_item = ttk.Entry(self.side_panel)
        self.affected_item.grid(column=0, row=3, padx=5, pady=5, sticky='ew')
        self.placeholder(self.affected_item, "Affected Items")

        self.level_frame = tk.Frame(self.side_panel)
        self.level_frame.grid(column=0, row=4, padx=5, pady=5, sticky='ew')

        self.level_label = ttk.Label(self.level_frame, text="Level: ")
        self.level_label.grid(column=0, row=0, padx=5, pady=5, sticky='we')

        self.level_spin = ttk.Spinbox(self.level_frame, values=[1, 2])
        self.level_spin.set(value=1)
        self.level_spin.grid(column=1, row=0, padx=5, pady=5, sticky='we')

        # MAIN PANEL WIDGETS
        self.main_panel = tk.Frame(self.main_frame)
        self.main_panel.grid(column=1, row=0, padx=5, pady=5, sticky='news')

    def placeholder(self, entry, placeholder):
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry.insert(0, placeholder)

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def run_app(self):    
        self.mainloop()

if __name__ == "__main__":
    app = GUI().run_app()