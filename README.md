# Tutorial Avanzado de Gemini CLI: Ejercicios Prácticos

¡Bienvenido! Este proyecto es una colección de ejercicios prácticos diseñados para explorar y demostrar las capacidades avanzadas del Asistente Gemini a través de su interfaz de línea de comandos (CLI).

## 🎯 Objetivo del Proyecto

El objetivo principal es mostrar cómo Gemini puede ser utilizado como una herramienta de ingeniería de software para realizar tareas complejas que van más allá de la simple generación de código. A través de estos ejercicios, aprenderás a guiar al agente para:

-   Analizar y refactorizar código existente.
-   Transformar datos y manipular archivos.
-   Interactuar con herramientas de desarrollo como `git`.
-   Generar documentación técnica y diagramas.
-   Operar bajo diferentes "personas" para adaptar su comportamiento a tareas específicas.

---

## 🎭 Personas de Agente y Configuración

Una característica clave de este tutorial es el uso de diferentes **personas** para instruir a Gemini. Cada persona define un rol, una experiencia y un enfoque específico, lo que permite obtener respuestas más precisas y contextualizadas.

El directorio `agents/` contiene las definiciones de estas personas:

-   `architect`: Para decisiones de diseño y arquitectura de software.
-   `critic`: Para revisiones de código y detección de posibles fallos.
-   `documenter`: Para generar documentación clara y concisa.
-   `tester`: Para crear casos de prueba y asegurar la calidad.
-   `gemini`: La persona por defecto, un asistente AI generalista.

El script `load_persona.sh` es una utilidad para cargar estas definiciones de persona en el contexto del agente Gemini.

---

## 📂 Estructura del Proyecto y Ejercicios

El proyecto está organizado en directorios numerados, cada uno representando un ejercicio o concepto específico.

### [01_Configuracion_y_Modelos](./01_Configuracion_y_Modelos/)
-   **Objetivo:** Familiarizarse con la configuración inicial de Gemini, la selección de modelos y la ejecución de prompts básicos.

### [02_Multiples_Agentes](./02_Multiples_Agentes/)
-   **Objetivo:** Explorar cómo interactuar con Gemini cuando se le asignan diferentes personas (`architect`, `critic`, `tester`), observando cómo su enfoque y respuestas cambian según el rol asignado.

### [03_Flujo_Git_IDE](./03_Flujo_Git_IDE/)
-   **Objetivo:** Demostrar cómo Gemini puede integrarse en un flujo de trabajo de desarrollo típico, realizando operaciones de `git` como `status`, `diff`, `add` y `commit` directamente desde la CLI.

### [04_Ventajas_vs_IDE](./04_Ventajas_vs_IDE/)
-   **Objetivo:** Comparar la eficiencia de Gemini CLI con un IDE tradicional para ciertas tareas, destacando escenarios donde el agente puede acelerar el desarrollo.

### [05-Transformando_Archivos](./05-Transformando_Archivos/)
-   **Objetivo:** Realizar una tarea de ETL (Extracción, Transformación y Carga) de datos.
-   **Contenido:**
    -   `create_data.py`: Script que lee un archivo CSV (`estados-municipios-ciudades-SOINDI.csv`), lo procesa y lo convierte en un `vzla_data.json` jerárquico.
    -   `finder.py`: Script que utiliza el JSON generado para buscar ubicaciones.
    -   **Conceptos demostrados:** Manipulación de archivos, normalización de datos, y revisión de código para identificar posibles problemas de correspondencia o datos faltantes.

### [06-Diagramas_Mermaid](./06-Diagramas_Mermaid/)
-   **Objetivo:** Utilizar Gemini para documentar procesos de software complejos mediante la generación de diagramas de Mermaid.
-   **Contenido:**
    -   `generar_diagramas.py`: Script que genera archivos `.mmd` con el código de diagramas para procesos complejos como el flujo OAuth 2.0, el patrón Saga y `git rebase`.
    -   `README.md`: Incluye instrucciones detalladas sobre cómo compilar estos diagramas a formato SVG utilizando la herramienta `mmdc`.
    -   **Conceptos demostrados:** Generación de documentación técnica, uso de herramientas externas (`mmdc`) y visualización de arquitecturas complejas.

---

## 🚀 Cómo Empezar

1.  Navega a través de los directorios de los ejercicios en orden numérico.
2.  Lee el archivo `README.md` de cada ejercicio para entender el contexto y los objetivos.
3.  Utiliza los prompts y las instrucciones para guiar a Gemini a completar las tareas de cada ejercicio.
4.  Experimenta con tus propias ideas y modificaciones para profundizar tu aprendizaje.

Este es un entorno de aprendizaje interactivo. ¡No dudes en desafiar al agente con tareas creativas y complejas!
