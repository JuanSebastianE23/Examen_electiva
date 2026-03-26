# Portafolio Profesional - Django

Proyecto Django con portafolios de 3 desarrolladores.
# Proyecto Django - Portafolio Profesional

## 📋 Descripción
Aplicación web en Django que presenta un portafolio profesional con las hojas de vida de 3 desarrolladores. Cada desarrollador tiene su propia app independiente con diseño único en HTML y CSS.

## 🌳 Estructura de Ramas

- `main`: Rama principal de producción
- `dev`: Rama de desarrollo (base)
- `feature/dev1-hoja-vida`: Funcionalidad de hoja de vida del desarrollador 1
- `feature/dev2-hoja-vida`: Funcionalidad de hoja de vida del desarrollador 2
- `feature/dev3-hoja-vida`: Funcionalidad de hoja de vida del desarrollador 3

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/JuanSebastianE23/Examen_electiva.git
cd Examen_electiva
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate

# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
python manage.py runserver
```

## URLs

- `/` - Página principal
- `/dev1/` - Desarrollador 1
- `/dev2/` - Desarrollador 2
- `/dev3/` - Desarrollador 3
### 4. Ejecutar migraciones
```bash
python manage.py migrate
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

Visita: http://127.0.0.1:8000/

## 📁 Estructura del Proyecto

```
Examen_electiva/
├── config/              # Configuración principal de Django
├── core/                # App principal (página de inicio)
├── dev1/                # App del Desarrollador 1
├── dev2/                # App del Desarrollador 2
├── dev3/                # App del Desarrollador 3
├── templates/           # Templates HTML organizados por desarrollador
│   ├── dev1/
│   ├── dev2/
│   └── dev3/
├── static/              # Archivos estáticos (CSS)
│   └── css/
│       ├── dev1/
│       ├── dev2/
│       └── dev3/
└── manage.py
```

## 🎨 Características

- ✅ 3 apps independientes (una por desarrollador)
- ✅ Diseño único para cada desarrollador
- ✅ Solo HTML y CSS (sin base de datos)
- ✅ Diseño responsive
- ✅ Tarjetas con sombras y efectos
- ✅ Gradientes personalizados
- ✅ Navegación entre portafolios

## 👥 Desarrolladores

### Desarrollador 1 - Full Stack
- Especialidad: Desarrollo Full Stack
- Colores: Púrpura y Azul (#667eea, #764ba2)

### Desarrollador 2 - Backend
- Especialidad: Desarrollo Backend
- Colores: Rosa y Rojo (#f093fb, #f5576c)

### Desarrollador 3 - Frontend
- Especialidad: Desarrollo Frontend
- Colores: Azul Cielo (#4facfe, #00f2fe)

## 🔄 Flujo de Trabajo GitFlow

1. Crear rama desde `dev`:
```bash
git checkout dev
git pull origin dev
git checkout -b feature/nombre-funcionalidad
```

2. Hacer commits descriptivos:
```bash
git add .
git commit -m "Feature: Descripción del cambio"
```

3. Subir rama al remoto:
```bash
git push origin feature/nombre-funcionalidad
```

4. Crear Pull Request hacia `dev` en GitHub

5. Después de revisión, hacer merge a `dev`

6. Para producción, merge de `dev` a `main`

## 📌 Versión Actual

**v1.0.0** - Release inicial con portafolios de 3 desarrolladores

## 🛠️ Tecnologías

- Python 3.14.3
- Django 6.0.3
- HTML5
- CSS3
- Git & GitHub

## 📝 Notas

- No se utilizan modelos ni base de datos
- Solo vistas basadas en funciones
- Diseño completamente estático
- Cada desarrollador mantiene su código independiente
