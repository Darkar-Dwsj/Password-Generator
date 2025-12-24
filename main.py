import random
import tkinter as tk
from tkinter import ttk
import cadenas as strings

def generar_password(n):
    caracteres = ""
    if var_minus.get():
        caracteres += strings.letras_minusculas
    if var_mayus.get():
        caracteres += strings.letras_mayusculas
    if var_num.get():
        caracteres += strings.numeros
    if var_esp.get():
        caracteres += strings.especiales

    if not caracteres:
        return "Selecciona al menos un tipo"

    return "".join(random.choice(caracteres) for _ in range(n))

def mostrar_password():
    longitud = int(barra.get())
    password = generar_password(longitud)
    ver_texto.delete(0, tk.END)
    ver_texto.insert(0, password)
    evaluar_password(None)

def evaluar_password(event):
    pwd = ver_texto.get()
    score = 0

    if len(pwd) >= 8:
        score += 1
    if any(c in strings.letras_minusculas for c in pwd):
        score += 1
    if any(c in strings.letras_mayusculas for c in pwd):
        score += 1
    if any(c in strings.numeros for c in pwd):
        score += 1
    if any(c in strings.especiales for c in pwd):
        score += 1

    if score <= 2:
        resultado_pwd.config(text="🔴 Seguridad: Baja", foreground="red")
    elif score == 3 or score == 4:
        resultado_pwd.config(text="🟠 Seguridad: Media", foreground="orange")
    else:
        resultado_pwd.config(text="🟢 Seguridad: Alta", foreground="green")

def actualizar_longitud(val):
    etiqueta_longitud.config(text=f"Longitud: {int(float(val))}")

app = tk.Tk()
app.title("Generador de Contraseñas Seguras")
app.geometry("560x600")
app.resizable(False, False)
app.configure(bg="gray24")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 11), background="gray24", foreground="white")
style.configure("TCheckbutton", background="gray24", foreground="white", font=("Segoe UI", 10))
style.configure("TScale", background="gray24", troughcolor="gray30", sliderthickness=15)

ttk.Label(app, text="Generador de Contraseñas Seguras", font=("Segoe UI", 16, "bold")).pack(pady=15)

ver_texto = tk.Entry(app, width=40, font=("Consolas", 14), justify="center", bg="gray15", fg="white", insertbackground="white")
ver_texto.pack(pady=10)
ver_texto.bind("<KeyRelease>", evaluar_password)

resultado_pwd = ttk.Label(app, text="Seguridad: ", font=("Segoe UI", 12, "bold"))
resultado_pwd.pack(pady=10)

frame_longitud = ttk.Frame(app)
frame_longitud.pack(pady=10)
etiqueta_longitud = ttk.Label(frame_longitud, text="Longitud: 16")
etiqueta_longitud.pack(side="left", padx=5)
barra = ttk.Scale(frame_longitud, from_=8, to=32, orient="horizontal", length=200, command=actualizar_longitud)
barra.set(16)
barra.pack(side="left")

frame_opciones = ttk.LabelFrame(app, text="Incluir:")
frame_opciones.pack(pady=15, padx=20, fill="x")

var_minus = tk.BooleanVar(value=True)
var_mayus = tk.BooleanVar(value=True)
var_num = tk.BooleanVar(value=True)
var_esp = tk.BooleanVar(value=True)

ttk.Checkbutton(frame_opciones, text="Minúsculas (a-z)", variable=var_minus).pack(anchor="w", padx=10, pady=2)
ttk.Checkbutton(frame_opciones, text="Mayúsculas (A-Z)", variable=var_mayus).pack(anchor="w", padx=10, pady=2)
ttk.Checkbutton(frame_opciones, text="Números (0-9)", variable=var_num).pack(anchor="w", padx=10, pady=2)
ttk.Checkbutton(frame_opciones, text="Símbolos (!@#$...)", variable=var_esp).pack(anchor="w", padx=10, pady=2)

ttk.Button(app, text="Generar Contraseña", command=mostrar_password).pack(pady=20)

app.mainloop()
