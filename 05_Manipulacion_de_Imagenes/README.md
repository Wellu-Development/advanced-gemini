# Lección 5: Más Allá del Texto - Manipulación de Imágenes

## Objetivo
Aprender a utilizar las capacidades multimodales de Gemini para que analice imágenes (como mockups de UI, diagramas o capturas de pantalla de errores) y genere código o explicaciones a partir de ellas.

## ¿Puede Gemini "ver" imágenes?

Sí. Los modelos de Gemini son **multimodales**, lo que significa que pueden procesar información de diferentes fuentes, incluyendo texto e imágenes. `gemini-cli` te permite pasar una o más imágenes como parte de tu prompt. La IA puede entonces "ver" la imagen y usar esa información visual para realizar una tarea.

Esta es una de las ventajas más espectaculares sobre los asistentes de solo texto y tiene aplicaciones prácticas inmediatas en el desarrollo de software.

**Casos de uso:**
- **De Mockup a Código:** Dale una imagen de una interfaz de usuario y pídele que escriba el código HTML/CSS o de un framework como React/Flutter para replicarla.
- **De Diagrama a Código:** Proporciónale un diagrama de arquitectura o de base de datos y pídele que genere el "boilerplate" de las clases o los scripts SQL.
- **De Captura de Error a Explicación:** Pásale una captura de pantalla de un error en una aplicación y pídele que te explique la posible causa.

## Ejercicio Práctico: De un Mockup de UI a Código HTML

1.  **Consigue una Imagen de Mockup:**
    Guarda una imagen de una interfaz de usuario simple en esta carpeta. Para este ejemplo, vamos a suponer que tienes una imagen llamada `login_mockup.png` que muestra un formulario de inicio de sesión con un título, dos campos de texto (usuario y contraseña) y un botón.

    *(Como no puedo crear la imagen por ti, por favor, busca en Google "simple login form UI" y guarda una imagen con ese nombre en esta carpeta).*

2.  **Inicia Gemini y Haz la Petición Visual:**
    Asegúrate de que la imagen `login_mockup.png` esté en el directorio.
    ```bash
    gemini
    ```
    **Tu petición:**
    ```
    analiza la imagen 'login_mockup.png'. Basándote en su diseño, crea un único archivo HTML llamado 'login.html' que replique esta estructura y estilo. Incluye el CSS dentro de una etiqueta <style> en el mismo archivo. Concéntrate en que se parezca visualmente, no necesita ser funcional.
    ```

3.  **Analiza el Resultado:**
    Gemini procesará tanto tu texto como la imagen. "Verá" los componentes en el mockup (el título, los inputs, el botón) y generará un archivo `login.html` usando la herramienta `write_file`.

4.  **Verifica el Código Generado:**
    Sal de Gemini (`exit`). Ahora deberías tener un archivo `login.html` en tu carpeta. Ábrelo en un navegador web.

    El resultado será una página HTML estática que se asemeja visualmente al mockup que le proporcionaste. La calidad del CSS y la precisión del layout pueden variar, pero la estructura básica estará ahí, ahorrándote una cantidad de tiempo considerable en la maquetación inicial.

## Puntos Clave
- Gemini es multimodal. Puedes incluir una o más rutas de archivo a imágenes directamente en tu prompt.
- Esta capacidad es un "game-changer" para el desarrollo de UI, permitiéndote pasar de un diseño visual a código funcional mucho más rápido.
- Úsalo para interpretar diagramas, explicar errores visuales o cualquier otra tarea donde el contexto visual sea importante.
- La calidad del código generado dependerá de la claridad de la imagen y de la especificidad de tu petición.
