import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SolarApp:
    def __init__(self, master):
        self.master = master
        master.title("Solar App")

        # Load images
        self.solar_icon = Image.open("solar_icon.png")
        self.solar_icon = ImageTk.PhotoImage(self.solar_icon)
        self.rain_icon = Image.open("rain_icon.png")
        self.rain_icon = ImageTk.PhotoImage(self.rain_icon)

        # Create menu bar
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

        # Create location label
        self.location_label = tk.Label(master, text="Feira de Santana - BA", font=("Helvetica", 14))
        self.location_label.pack(pady=10)

        # Create weather label
        self.weather_label = tk.Label(master, text="27°C", font=("Helvetica", 14))
        self.weather_label.pack()

        # Create battery frame
        self.battery_frame = tk.Frame(master)
        self.battery_frame.pack(pady=20)

        # Create battery label
        self.battery_label = tk.Label(self.battery_frame, text="Battery", font=("Helvetica", 12))
        self.battery_label.grid(row=0, column=0)

        # Create battery icon
        self.battery_icon = tk.Canvas(self.battery_frame, width=50, height=50)
        self.battery_icon.grid(row=1, column=0, pady=10)
        self.battery_icon.create_rectangle(10, 10, 40, 40, fill="green", outline="black", width=2)

        # Create weather frame
        self.weather_frame = tk.Frame(master)
        self.weather_frame.pack()

        # Create weather label
        self.weather_label = tk.Label(self.weather_frame, text="Weather", font=("Helvetica", 12))
        self.weather_label.grid(row=0, column=0)

        # Create weather icon
        self.weather_icon = tk.Label(self.weather_frame, image=self.rain_icon)
        self.weather_icon.grid(row=1, column=0, pady=10)

        # Create solar panel frame
        self.solar_frame = tk.Frame(master)
        self.solar_frame.pack(pady=20)

        # Create solar panel label
        self.solar_label = tk.Label(self.solar_frame, text="Monitoramento Placa Solar", font=("Helvetica", 12))
        self.solar_label.pack()

        # Create solar panel options
        self.options_frame = tk.Frame(self.solar_frame)
        self.options_frame.pack()

        # Create water icon
        self.water_icon = tk.Button(self.options_frame, text="", image=self.rain_icon, command=self.show_water_status)
        self.water_icon.grid(row=0, column=0, padx=5)

        # Create solar panel icon
        self.solar_panel_icon = tk.Button(self.options_frame, text="", image=self.solar_icon, command=self.show_solar_panel_status)
        self.solar_panel_icon.grid(row=0, column=1, padx=5)

        # Create empty icon
        self.empty_icon = tk.Button(self.options_frame, text="", command=self.show_empty_status)
        self.empty_icon.grid(row=0, column=2, padx=5)

        # Create light bulb icon
        self.light_bulb_icon = tk.Button(self.options_frame, text="", image=self.rain_icon, command=self.show_light_bulb_status)
        self.light_bulb_icon.grid(row=0, column=3, padx=5)

        # Create progress bar frame
        self.progress_bar_frame = tk.Frame(self.solar_frame)
        self.progress_bar_frame.pack(pady=10)

        # Create progress bar labels
        self.progress_bar_labels = []
        self.progress_bar_labels.append(tk.Label(self.progress_bar_frame, text="30%", font=("Helvetica", 10), fg="white", bg="blue"))
        self.progress_bar_labels.append(tk.Label(self.progress_bar_frame, text="40%", font=("Helvetica", 10), fg="white", bg="blue"))
        self.progress_bar_labels.append(tk.Label(self.progress_bar_frame, text="40%", font=("Helvetica", 10), fg="white", bg="blue"))

        # Create progress bar labels
        for i, label in enumerate(self.progress_bar_labels):
            label.grid(row=0, column=i, padx=5)

        # Create progress bar
        self.progress_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=1, column=0, columnspan=3)

        # Create energy produced label
        self.energy_label = tk.Label(self.solar_frame, text="Energia Produzida", font=("Helvetica", 12))
        self.energy_label.pack(pady=10)

    def show_water_status(self):
        # Show water status
        pass

    def show_solar_panel_status(self):
        # Show solar panel status
        pass

    def show_empty_status(self):
        # Show empty status
        pass

    def show_light_bulb_status(self):
        # Show light bulb status
        pass

root = tk.Tk()
app = SolarApp(root)
root.mainloop()