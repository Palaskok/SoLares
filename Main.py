from tkinter import *
from tkinter import ttk

# Crie a janela principal
root = Tk()
root.title("Monitoramento Placa Solar")

# Defina a cor de fundo da janela principal
root.configure(bg="#ADD8E6")  # Azul claro

# Adicione o ícone da aplicação
# root.iconbitmap("seu_icone.ico")  # Substitua "seu_icone.ico" pelo caminho do seu ícone

# Crie a barra de menu
menubar = Menu(root)

# Crie o menu "Arquivo"
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Sair", command=root.quit)
menubar.add_cascade(label="Arquivo", menu=filemenu)

# Crie o menu "Ajuda"
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Sobre", command=lambda: print("Sobre a aplicação..."))
menubar.add_cascade(label="Ajuda", menu=helpmenu)

# Exiba a barra de menu
root.config(menu=menubar)

# Crie o frame para o cabeçalho
header_frame = Frame(root, bg="#ADD8E6")
header_frame.pack(side=TOP, fill=X)

# Adicione o logotipo
logo_label = Label(header_frame, text="SOLARES", font=("Arial", 14, "bold"), fg="white", bg="#007bff", padx=10, pady=5)
logo_label.pack(side=LEFT)

# Adicione o local
location_label = Label(header_frame, text="Feira de Santana - BA", font=("Arial", 12), fg="black", bg="#ADD8E6", padx=10, pady=5)
location_label.pack(side=LEFT)

# Adicione a temperatura
temp_label = Label(header_frame, text="27°C", font=("Arial", 12), fg="black", bg="#ADD8E6", padx=10, pady=5)
temp_label.pack(side=RIGHT)

# Crie o frame para o conteúdo
content_frame = Frame(root, bg="#ADD8E6")
content_frame.pack(expand=True, fill=BOTH)

# Crie o frame esquerdo
left_frame = Frame(content_frame, bg="#ADD8E6")
left_frame.pack(side=LEFT, fill=Y, expand=False)

# Adicione o ícone da bateria
battery_label = Label(left_frame, text="🔋", font=("Arial", 48), bg="#ADD8E6")
battery_label.pack(pady=20)

# Adicione o indicador de nível de bateria
battery_level = ttk.Progressbar(left_frame, orient="vertical", mode="determinate", length=100)
battery_level.pack(pady=20)

# Crie o frame direito
right_frame = Frame(content_frame, bg="#ADD8E6")
right_frame.pack(side=RIGHT, fill=Y, expand=False)

# Adicione o ícone do clima
weather_label = Label(right_frame, text="🌧️", font=("Arial", 48), bg="#ADD8E6")
weather_label.pack(pady=20)

# Adicione o indicador de chuva
rain_level = ttk.Progressbar(right_frame, orient="vertical", mode="determinate", length=100)
rain_level.pack(pady=20)

# Crie o frame para a seção de monitoramento
monitor_frame = Frame(content_frame, bg="#ADD8E6")
monitor_frame.pack(expand=True, fill=BOTH)

# Adicione o título do monitoramento
monitor_title = Label(monitor_frame, text="Monitoramento Placa Solar", font=("Arial", 16, "bold"), fg="black", bg="#ADD8E6", padx=10, pady=10)
monitor_title.pack()

# Crie os botões de monitoramento
monitor_buttons = [
    ("💧", "Water", "#ADD8E6"),
    ("🏠", "Solar Panel", "#ADD8E6"),
    ("⚪", "Light", "#ADD8E6"),
    ("💡", "Smart Bulb", "#ADD8E6")
]

for text, tooltip, bg_color in monitor_buttons:
    button = Button(monitor_frame, text=text, font=("Arial", 12), fg="black", bg=bg_color, width=3, height=2, relief="flat", borderwidth=0, command=lambda t=tooltip: print(f"Ação para {t}"))
    button.pack(side=LEFT, padx=10, pady=10)

# Crie o frame para os indicadores de energia
energy_frame = Frame(monitor_frame, bg="#ADD8E6")
energy_frame.pack(pady=10)

# Adicione os indicadores de energia
energy_values = [
    ("30%", "#ADD8E6"),
    ("40°", "#ADD8E6"),
    ("40°", "#ADD8E6"),
]

for value, bg_color in energy_values:
    energy_label = Label(energy_frame, text=value, font=("Arial", 14, "bold"), fg="black", bg=bg_color, padx=10, pady=5, borderwidth=1, relief="solid")
    energy_label.pack(side=LEFT, padx=5)

# Crie o frame para a energia produzida
energy_produced_frame = Frame(root, bg="#ADD8E6")
energy_produced_frame.pack(side=BOTTOM, fill=X)

# Adicione o título da energia produzida
energy_produced_title = Label(energy_produced_frame, text="Energia Produzida", font=("Arial", 12), fg="black", bg="#ADD8E6", padx=10, pady=5)
energy_produced_title.pack()

# Exiba a janela
root.mainloop()