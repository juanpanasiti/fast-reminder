# 🚀 Proyecto Base - Curso Python + FastAPI 2025

Este repositorio contiene la estructura inicial para trabajar con **FastAPI**, diseñado especialmente para el curso **Python + FastAPI 2025**.

El proyecto implementa una API REST organizada, con rutas versionadas dentro de la carpeta `src/routes/v1`.

---

## 🐍 Requisitos

- Python **3.10 o superior**
- Git (opcional para clonar el repo)
- pip (gestor de paquetes de Python)

---

## ⚙️ Instalación

1. **Clonar el repositorio** (opcional)

   ```bash
   git clone https://github.com/juanpanasiti/fast-reminder.git
   cd fast-reminder
   ```

2. **Crear entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate       # En Linux/Mac
   .\venv\Scripts\activate        # En Windows
   ```

3. **Instalar dependencias**

   - Solo para producción:

     ```bash
     pip install -r requirements.txt
     ```

   - Para desarrollo (incluye fastapi CLI, httpx, etc.):

     ```bash
     pip install -r requirements-dev.txt
     ```

---

## ▶️ Cómo levantar el servidor

Podés ejecutar el servidor de 3 formas distintas:

---

### 1. 💻 Usando el CLI de FastAPI (modo desarrollo)

```bash
fastapi dev src/app.py
```

> ✅ Requiere tener instalado `fastapi[standard]` (ya incluido en `requirements-dev.txt`).

---

### 2. 🔥 Usando Uvicorn desde la terminal

```bash
uvicorn src.app:api_server --reload
```

> Recomendado para entornos de desarrollo avanzados o producción controlada.

---

### 3. 🐍 Ejecutando directamente `main.py`

```bash
python main.py
```

> Útil para entornos simples o educativos. Ideal para ver cómo importar y ejecutar manualmente la app.

---

## 📁 Estructura del proyecto

```
.
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── src
│   ├── app.py
│   └── routes
│       └── v1
│           ├── expense_routes.py
│           └── payment_routes.py
```

---

## 📚 Autor

Proyecto para el curso **Python + FastAPI 2025**  
Desarrollado por: *Juan Marcelo Panasiti*
