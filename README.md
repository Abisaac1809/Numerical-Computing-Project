# Numerical Computing Project

## Integración de herramientas matemáticas computacionales para resolver operaciones numéricas con Python y sus librerías




## 🚀 Acerca del Proyecto

Esta aplicación web de visualización de datos numéricos, desarrollada con **Django y Python**, tiene como objetivo principal generar y presentar gráficas de puntos aleatorios en un entorno interactivo. Más allá de la visualización, el sistema realiza complejas operaciones matemáticas computacionales, como la resolución de sistemas de ecuaciones lineales mediante el método de Gauss-Jordan, y proporciona un análisis detallado de los datos numéricos involucrados.

El programa está diseñado para ser accesible a través de una única URL principal, desde donde los usuarios pueden interactuar con la gráfica generada y obtener información sobre los puntos. La capacidad de generar nuevas gráficas dinámicamente mediante solicitudes a la API interna, junto con el registro exhaustivo de resultados y errores, lo convierte en una herramienta robusta para el estudio y análisis de problemas numéricos.

---

## ✨ Características Principales

* **Generación Dinámica de Gráficas:** Crea y visualiza gráficas 2D con puntos generados aleatoriamente.
* **Operaciones Numéricas Avanzadas:** Procesa matrices y resuelve sistemas de ecuaciones utilizando el método de Gauss-Jordan.
* **Análisis Numérico Detallado:** Genera un estudio de cada número, incluyendo cifras significativas, validez y posibles operaciones elementales.
* **Reporte de Resultados Formales:** Proporciona archivos con las matrices originales, resultados de fórmulas, resultados de Gauss-Jordan y distancias entre puntos, todo en notación formal.
* **Trazabilidad de Errores:** Registra errores en archivos de log dedicados, detallando tipo, ubicación y momento del fallo.
* **Monitoreo de Precisión:** Calcula y guarda el error relativo de las iteraciones para evaluar la validez y precisión de los cálculos numéricos.
* **Interfaz Web Intuitiva:** Acceso sencillo a través de una URL para interactuar con la visualización y funcionalidades.

---

## 🛠️ Tecnologías Utilizadas

La aplicación está construida sobre un stack tecnológico robusto, utilizando **Python** como lenguaje principal y **Django** como framework web.

* **Aplicación:** Aplicación de Visualización de Datos Numéricos `v2.0.0`
* **Lenguaje de Programación:** Python (se recomienda 3.9 o superior)
* **Framework Web:** Django `5.2.4`
* **Base de Datos:** SQLite `(integrado con Django ORM)`
* **Frontend:** HTML, CSS

**Librerías Python Principales:**

* `numpy==2.2.6`: Fundamental para todas las operaciones numéricas y matriciales.
* `matplotlib==3.10.3`: Utilizada para la generación y renderización de las gráficas.
* `asgiref==3.9.1`: Soporte ASGI para Django.
* `sqlparse==0.5.3`: Parseo de SQL, utilizado por Django ORM.
* Otras dependencias como `contourpy`, `cycler`, `fonttools`, `kiwisolver`, `packaging`, `pillow`, `pyparsing`, `python-dateutil`, `six`, y `tzdata` para funcionalidades de Matplotlib y Django.

Para la lista completa y exacta de dependencias, consulte el archivo `requirements.txt`.

---

## ⚙️ Configuración y Ejecución

Siga estos pasos para configurar y ejecutar la aplicación en su entorno local (entorno de desarrollo).

### Pre-requisitos

Asegúrese de tener **Python (3.9 o superior)** instalado en su sistema. Se recomienda el uso de `virtualenv` para gestionar las dependencias del proyecto de forma aislada.

### Clonar el Repositorio

Abra su terminal o línea de comandos y ejecute:

```bash
git clone [https://github.com/Abisaac1809/Numerical-Computing-Project.git](https://github.com/Abisaac1809/Numerical-Computing-Project.git)
cd Numerical-Computing-Project

### Configurar Entorno Virtual

1.  **Instale `virtualenv`** (si no lo tiene globalmente):
    ```bash
    pip install virtualenv
    ```
2.  **Cree el entorno virtual:**
    ```bash
    virtualenv env
    ```
3.  **Active el entorno virtual:**
    * **En Windows:**
        ```bash
        .\env\Scripts\activate
        ```
    * **En macOS/Linux:**
        ```bash
        source env/bin/activate
        ```

### Instalar Dependencias

Con el entorno virtual activado, instale todas las librerías necesarias:

```bash
pip install -r requirements.txt
