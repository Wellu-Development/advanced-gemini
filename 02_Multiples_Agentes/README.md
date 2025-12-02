# Lección 2: El Proyecto Multi-Agente

## Objetivo
Aprender un método práctico para tener y gestionar múltiples "agentes" o "personas" dentro de un mismo proyecto, permitiéndote cambiar rápidamente entre un revisor de código, un documentador, un experto en seguridad, etc.

## ¿Cómo puedo tener múltiples agentes?

`gemini-cli` solo busca un archivo de contexto llamado `GEMINI.md` en la raíz del proyecto. No puedes tener varios archivos `GEMINI.md` activos a la vez. Sin embargo, puedes usar una técnica simple y poderosa para gestionar una "biblioteca" de agentes y activarlos a voluntad.

La estrategia es:
1.  Crear una carpeta (ej. `.gemini/personas/`) para almacenar las definiciones de todos tus agentes.
2.  Cada agente se define en su propio archivo Markdown (ej. `critico.md`, `documentador.md`).
3.  Para "activar" un agente, simplemente copias el contenido del archivo de la persona deseada al archivo raíz `GEMINI.md`.

Esto te da un control total y explícito sobre qué agente está activo en cada momento.

## Ejercicio Práctico: Activando al "Crítico" y al "Documentador"

1.  **Crea la Biblioteca de Agentes:**
    Primero, vamos a crear la estructura y definir dos agentes muy diferentes.
    ```bash
    mkdir -p .gemini/personas
    ```

2.  **Define al "Crítico Desalmado":**
    (Este es el agente que solicitaste, ideal para revisiones de código)
    ```bash
    # Usamos write_file para crear la definición del primer agente
    write_file --file_path ".gemini/personas/critico.md" --content "
    # CONTEXTO: Eres el 'Crítico Desalmado'.
    Tu única misión es revisar el código que se te presenta y destruirlo con críticas brutalmente honestas y sin filtro. Enfócate en errores, malas prácticas, y estilo. Tu tono es sarcástico y severo. No te guardes nada.
    "
    ```

3.  **Define al "Documentador Amable":**
    Este agente es el opuesto polar, útil para generar documentación para usuarios finales.
    ```bash
    # Usamos write_file para crear la definición del segundo agente
    write_file --file_path ".gemini/personas/documentador.md" --content "
    # CONTEXTO: Eres el 'Documentador Amable'.
    Tu misión es leer el código que se te presenta y generar documentación clara, concisa y amigable para el usuario final. Explica el propósito del código en términos sencillos, cómo usarlo, y qué resultados esperar. Usa un tono didáctico y paciente.
    "
    ```

4.  **Crea un Código de Ejemplo:**
    ```bash
    write_file --file_path "mi_funcion.py" --content "
    def add(x,y): return x+y
    "
    ```

5.  **Activa y Usa al "Crítico Desalmado":**
    Copia la personalidad del crítico al archivo `GEMINI.md` raíz.
    ```bash
    cp .gemini/personas/critico.md ./GEMINI.md
    ```
    Ahora, inicia Gemini y pide la revisión:
    ```bash
    gemini
    # Dentro de Gemini:
    revisa el código en 'mi_funcion.py'
    ```
    La respuesta será dura, señalando el nombre de la función en minúsculas, la falta de espacios, la falta de type hints y la ausencia de docstrings.

6.  **Activa y Usa al "Documentador Amable":**
    Sal de Gemini. Ahora, activa al otro agente.
    ```bash
    cp .gemini/personas/documentador.md ./GEMINI.md
    ```
    Inicia Gemini de nuevo y haz la misma petición:
    ```bash
    gemini
    # Dentro de Gemini:
    revisa el código en 'mi_funcion.py'
    ```
    La respuesta será completamente diferente. Probablemente generará un `README.md` o una explicación de usuario sobre cómo la función `add` suma dos números.

## Puntos Clave
- `gemini-cli` solo lee `GEMINI.md`, pero tú puedes tener una librería de agentes en otros archivos.
- Cambiar de agente es tan simple como copiar un archivo. Puedes incluso crear un pequeño script de shell para hacerlo más rápido (ej. `activar_agente critico`).
- Esta técnica te permite aplicar la personalidad correcta a la tarea correcta, maximizando la calidad de los resultados de la IA.
