# Navegación Dinámica ITM Minatitlán

[![Flask≥2.0](https://img.shields.io/badge/Flask-2.0%2B-blue)](https://flask.palletsprojects.com/)
[![Python≥3.7](https://img.shields.io/badge/Python-3.7%2B-yellow)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

---

## 📑 Contenido

1. [Qué es este proyecto](#qué-es-este-proyecto)
2. [Principales funciones](#principales-funciones)
3. [Dependencias necesarias](#dependencias-necesarias)
4. [Instalación paso a paso](#instalación-paso-a-paso)
5. [Cómo ejecutar](#cómo-ejecutar)
6. [Estructura de carpetas](#estructuras-de-carpetas)
7. [Personalización](#personalización)
8. [Aporte de la comunidad](#aporte-de-la-comunidad)
9. [Licencia](#licencia)

---

## Qué es este proyecto

Esta aplicación, construida con **Flask** y **Bootstrap 5**, crea un menú de navegación recursivo para el Instituto Tecnológico Nacional de Minatitlán. Se basa en un diccionario de Python que la macro de **Jinja2** transforma en una estructura desplegable con múltiples niveles.

![alt text](<Captura de pantalla 2025-07-14 003729.png>)

## Principales funciones

- **Menú anidado**: cualquier cantidad de subniveles.
- **Responsive**: ajusta el menú para móviles y escritorio.
- **Código limpio**: organizado y comentado.
- **Extensible**: agregar nuevas secciones con un diccionario.

![alt text](<Captura de pantalla 2025-07-14 003736.png>)

## Dependencias necesarias

- **Python** v3.7 o superior
- **pip** para instalar paquetes
- **Flask** ≥ 2.0

## Instalación paso a paso

```bash
# 1. Clonar el repositorio
git clone https://tu-repo.git
cd proyecto-itm-nav

# 2. Entorno virtual (opcional pero recomendado)
python -m venv venv
# Linux/macOS
env/bin/activate
# Windows
venv\Scripts\activate

# 3. Instalar librerías
pip install -r requirements.txt
```

## Cómo ejecutar

### Con Flask CLI

```bash
# Configura las variables de entorno
env FLASK_APP=main.py
env FLASK_ENV=development
flask run
```

### Directamente con Python

```bash
python main.py
```

Abrir en el navegador: `http://127.0.0.1:5000/`

## Estructuras de carpetas

```bash
proyecto-itm-nav/
├─ main.py            # Servidor Flask
├─ requirements.txt   # Dependencias
├─ README.md          # Guía de uso
└─ templates/         # Vistas y plantillas
   └─ menu.html       # Plantilla Jinja2
```

## Personalización

- **Título**: cambia `page_title` en `main.py`.
- **Menú**: modifica el diccionario de navegación en `main.py`.
- **Estilos**: ajusta el `<style>` de `menu.html` o añade un CSS propio.

## Aporte de la comunidad

1. Forkea este proyecto
2. Crea una rama de función (`git checkout -b feature/nombre`)
3. Haz tus cambios y un commit descriptivo
4. Envía tu Pull Request

## Licencia

Proyecto licenciado bajo **MIT License**. Consulte `LICENSE` para más información.
