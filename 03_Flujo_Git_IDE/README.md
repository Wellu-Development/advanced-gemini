# Lección 3: El Flujo de Trabajo Real (Git, IDE y Gemini)

## Objetivo
Aprender a integrar `gemini-cli` en un flujo de trabajo de desarrollo profesional que incluye Git para control de versiones y un IDE (como VS Code, Rider o IntelliJ) para la edición de código.

## ¿Cómo integro Gemini con Git y mi IDE?

La clave es entender que `gemini-cli` no reemplaza a estas herramientas, sino que **las complementa**. Actúa como un asistente al que consultas en momentos específicos del ciclo de desarrollo.

El flujo de trabajo más efectivo es el siguiente:

1.  **IDE (Preparación):** Creas una nueva rama en Git (`git checkout -b mi-feature`). Escribes el grueso de tu código en tu IDE, aprovechando su autocompletado, depuración y refactorización.
2.  **GEMINI (Revisión y Aumento):** **Antes de hacer commit**, vas a la terminal. Aquí es donde invocas a Gemini para:
    *   **Revisar tu código:** "Revisa los cambios que he hecho en esta rama comparados con 'main'வுகளை."
    *   **Generar documentación:** "Genera docstrings para las funciones que añadí en mi último cambio".
    *   **Crear pruebas unitarias:** "Escribe una prueba unitaria para la función 'X' que acabo de crear".
3.  **IDE (Aplicación):** Vuelves a tu IDE para aplicar las sugerencias de Gemini o para pegar el código que generó (como una prueba unitaria).
4.  **TERMINAL (Finalización):** Una vez satisfecho, usas la terminal para hacer `git add .` y `git commit`.

Gemini actúa como un *codesniffer* y un generador de boilerplate inteligente que usas entre la fase de escritura y la de commit.

## Ejercicio Práctico: Revisando un "Pull Request" antes de crearlo

1.  **Prepara el Repositorio:**
    ```bash
    git init
    # Crea el GEMINI.md del 'Crítico Desalmado' para esta lección
    echo "# CONTEXTO: Eres un revisor de código severo." > GEMINI.md
    
    # Crea el estado inicial en la rama main
    echo "def mi_funcion_original():\n    return True" > codigo.py
    git add .
    git commit -m "Versión inicial"
    ```

2.  **Trabaja en una Nueva Feature (simulado):**
    Crea una nueva rama y modifica el código con una calidad cuestionable.
    ```bash
    git checkout -b feature/nueva-logica
    echo "def mi_funcion_original():\n    return True\n\ndef funcionNueva(data):\n    # TODO: validar data\n    print('procesando...')\n    return len(data)" > codigo.py
    ```
    Has añadido la `funcionNueva` con un nombre inconsistente, un TODO y sin validación.

3.  **Pide a Gemini que Revise tus Cambios:**
    Ahora, el paso clave. Pídele a Gemini que actúe como un revisor que solo ve lo que ha cambiado.
    ```bash
    gemini
    ```
    **Tu petición:**
    ```
    quiero que revises los cambios de código que he hecho en mi rama actual. Para darte el contexto, primero ejecuta el comando 'git diff main' y luego, basándote en ese diff y en tu personalidad de revisor severo, dame tu feedback.
    ```

4.  **Analiza el Resultado:**
    Gemini primero ejecutará `git diff main`, lo que le mostrará únicamente las líneas que has añadido o modificado. Luego, aplicará su personalidad de "revisor severo" **solo a ese fragmento de código**.

    Te dirá cosas como:
    *   "El nombre `funcionNueva` es inconsistente con `mi_funcion_original`. Usa snake_case."
    *   "¿Un `TODO` en el código? Inaceptable. Implementa la validación ahora o elimínalo."
    *   "La función no tiene docstring ni type hints. Esto es de aficionados."

5.  **Ciclo de Mejora:**
    Con este feedback, volverías a tu IDE, corregirías el código, y solo entonces harías `git add .` y `git commit`.

## Puntos Clave
- **Gemini en la terminal, código en el IDE:** Usa cada herramienta para lo que es mejor.
- El mejor momento para usar Gemini es **después de escribir tu borrador y antes de hacer commit**.
- El flujo `git diff` + `gemini` es extremadamente potente para obtener revisiones de código rápidas y enfocadas solo en tus cambios.
- Gemini no necesita "integración" directa con el IDE; se integra en tu **flujo de trabajo**.
