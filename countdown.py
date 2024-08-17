import tkinter as tk
import time

def start_countdown():
    try:
        countdown_time = int(entry.get())
    except ValueError:
        label.config(text="Por favor, ingresa un número válido")
        return
    
    while countdown_time > 0:
        mins, secs = divmod(countdown_time, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        label.config(text=timeformat)
        root.update()
        time.sleep(1)
        countdown_time -= 1

    label.config(text="Tiempo finalizado")

root = tk.Tk()
root.title("Cuenta regreseiva")

label = tk.Label(root, font=('Helvetica', 48), text="")
label.pack()

entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack()

button = tk.Button(root, text="Iniciar", command=start_countdown, font=('Helvetica', 24))
button.pack()

root.mainloop()