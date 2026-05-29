# 📚 Sistema de Notas

Sistema básico desarrollado en Python para gestionar notas de estudiantes, calcular promedios, clasificar rendimiento académico y verificar aprobación.

---

# 🚀 Características

* Calcular promedio de notas
* Clasificar rendimiento académico
* Verificar aprobación
* Uso de variables de entorno con `.env`
* Código modular y organizado
* Funciones documentadas con docstrings

---

# 🛠️ Tecnologías utilizadas

* Python 3
* python-dotenv

---

# 📂 Estructura del proyecto

```plaintext
sistema-notas/
├── .env
├── notas.py
├── main.py
├── requirements.txt
├── README.md
└── .venv/
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sistema-notas.git
```

---

## 2. Entrar al proyecto

```bash
cd sistema-notas
```

---

## 3. Crear entorno virtual

```bash
python -m venv .venv
```

---

## 4. Activar entorno virtual

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### CMD

```cmd
.venv\Scripts\activate.bat
```

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🔐 Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
APP_NAME=Sistema de Notas
VERSION=1.0.0
MAX_NOTA=5.0
MIN_APROBACION=3.0
```

---

# 📖 Descripción de variables

| Variable       | Descripción                |
| -------------- | -------------------------- |
| APP_NAME       | Nombre de la aplicación    |
| VERSION        | Versión actual del sistema |
| MAX_NOTA       | Nota máxima permitida      |
| MIN_APROBACION | Nota mínima para aprobar   |

---

# ▶️ Ejemplo de uso

```python
from notas import (
    calcular_promedio,
    clasificar_nota,
    esta_aprobado
)

notas = [4.5, 3.8, 5.0]

promedio = calcular_promedio(notas)

print("Promedio:", promedio)
print("Clasificación:", clasificar_nota(promedio))
print("¿Aprobó?:", esta_aprobado(promedio))
```

---

# ✅ Resultado esperado

```plaintext
Promedio: 4.43
Clasificación: Sobresaliente
¿Aprobó?: True
```

---

# 📌 Autor

Proyecto desarrollado por Dilan.
