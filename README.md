# Numerical Computing Project

Este repositorio contiene el código desarrollado para el proyecto de la materia **Cálculo Numérico** de la carrera de Ingeniería en Computación. Este proyecto tiene como objetivo integrar herramientas matemáticas y computacionales aplicadas a problemas complejos, con un enfoque particular en operaciones numéricas, álgebra lineal, métodos iterativos y optimización, utilizando Python y sus bibliotecas.

## Características del Proyecto

### Funcionalidades Actuales

1. **Determinación de Cifras Significativas:**

   * Cálculo del número de cifras significativas de un valor.
2. **Sistemas Numéricos y Operaciones Elementales:**

   * Representación y operaciones en sistemas decimal, hexadecimal y binario.
3. **Cálculo de Errores:**

   * **Errores Absolutos y Relativos.**
   * **Errores por Truncamiento y Propagación.**

### Tecnologías Utilizadas

* **Lenguaje de Programación:** Python.
* **Gestor de Dependencias:** Virtualenv y archivo `requirements.txt`.

### Arquitectura del Proyecto

El punto de entrada principal del programa es el archivo `src/main.py`. Todos los módulos y componentes adicionales se encuentran organizados dentro de la carpeta `src`.

## Instalación y Uso

### Requisitos Previos

1. Tener instalado [Python 3.8+](https://www.python.org/).
2. Tener instalado Virtualenv:

   ```bash
   pip install virtualenv
   ```

### Instrucciones de Instalación

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/Abisaac1809/Numerical-Computing-Project.git
   ```
2. Navegar al directorio del proyecto:

   ```bash
   cd Numerical-Computing-Project
   ```
3. Crear y activar un entorno virtual:

   ```bash
   virtualenv -p python env
   env/Scripts/activate
   ```
4. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Ejecución del Programa

Ejecutar el archivo principal:

```bash
python src/main.py
```