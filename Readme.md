# 🔐 Generador de Contraseñas Seguras

Aplicación sencilla y moderna en **Python** para generar contraseñas seguras de forma aleatoria y evaluar su nivel de seguridad en tiempo real.

Permite personalizar la longitud y los tipos de caracteres que se incluirán en la contraseña.

  <img width="693" height="779" alt="Screenshot 2025-12-23 204218" src="https://github.com/user-attachments/assets/e3644142-bd7e-4897-85e6-2c7fff6d3fb1" />

## ✨ Características

- Generación de contraseñas aleatorias de **8 a 32 caracteres**
- Interfaz gráfica intuitiva con **Tkinter**
- Selección personalizada de tipos de caracteres mediante checkboxes:
  - Minúsculas (a-z)
  - Mayúsculas (A-Z)
  - Números (0-9)
  - Símbolos especiales (!@#$%^&* etc.)
- Evaluación automática del nivel de seguridad:
  - 🔴 Baja
  - 🟡 Media
  - 🟢 Alta
- Copiar contraseña al portapapeles con un solo clic

## 🛠️ Tecnologías utilizadas

- Python 3.8+
- tkinter (interfaz gráfica)
- random (generación aleatoria)

## 🚀 Instalación y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/generador-contrasenas.git

# 2. Entrar al directorio del proyecto
cd generador-contrasenas

# 3. Ejecutar la aplicación
python main.py
# o si usas python3 específicamente:
python3 main.py

