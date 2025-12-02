# Lección 1: Configuración es Poder - `/init` y Cambio de Modelos

## Objetivo
Aprender a crear una configuración local para un proyecto usando `/init`, entender su propósito y cómo modificarla para cambiar el modelo de IA subyacente.

## ¿Qué es `/init` y cuándo debo usarlo?

`gemini-cli` tiene una configuración global, pero a menudo querrás que se comporte de manera diferente para proyectos específicos. Quizás un proyecto requiere un modelo de IA más potente, mientras que para otro basta con un modelo más rápido y económico.

Aquí es donde entra `/init`.

`/init` es un comando especial que se ejecuta **dentro de una sesión de `gemini`**. Su única función es crear un subdirectorio `.gemini/` en tu proyecto actual, con un archivo de configuración local `config.toml`.

**Debes ejecutar `/init` cuando quieras:**
1.  Establecer una configuración específica para un proyecto que sea diferente de la global.
2.  Cambiar el modelo de IA para un solo proyecto.
3.  Definir un `GEMINI.md` (un "agente" o "persona") que solo se aplique a ese proyecto.

## Ejercicio Práctico: Cambiando el Modelo de IA

Vamos a configurar este proyecto para que use un modelo específico, como `gemini-1.5-flash-001`.

1.  **Inicia Gemini y Ejecuta `/init`:**
    Dentro de la carpeta de esta lección, inicia `gemini`.
    ```bash
    gemini
    ```
    Una vez dentro, escribe el comando especial:
    ```
    /init
    ```
    Gemini creará un directorio `.gemini` con un `config.toml` dentro. Puedes salir de la sesión con `exit`.

2.  **Explora la Configuración:**
    Ahora, en tu terminal normal, lista el contenido de la nueva carpeta:
    ```bash
    ls -F .gemini/
    ```
    Verás el archivo `config.toml`. Vamos a leerlo:
    ```bash
    cat .gemini/config.toml
    ```
    Tendrá un contenido similar a este, probablemente con el modelo por defecto:
    ```toml
    # Default model to use.
    # Run `gemini models list` to see all available models.
    model = "gemini-1.5-pro-latest"
    ```

3.  **Cambia el Modelo:**
    Edita el archivo `.gemini/config.toml` con tu editor preferido (o usando `gemini-cli` en un paso posterior) y cambia la línea del modelo. Por ejemplo:
    ```toml
    # Model changed to Flash for speed
    model = "models/gemini-1.5-flash-001"
    ```
    *Nota: Los nombres exactos de los modelos pueden variar. `gemini-1.5-flash-001` es un ejemplo común.*

4.  **Verifica el Cambio:**
    La próxima vez que inicies `gemini` **desde este directorio o cualquiera de sus subdirectorios**, usará automáticamente `gemini-1.5-flash-001` en lugar del modelo global. No necesitas hacer nada más. `gemini-cli` detecta el `.gemini/config.toml` local y le da prioridad.

## Puntos Clave
- `/init` crea una configuración local para tu proyecto en un archivo `.gemini/config.toml`.
- La configuración local **siempre tiene prioridad** sobre la configuración global cuando ejecutas `gemini` desde dentro de ese proyecto.
- La forma más directa de cambiar el modelo de IA para un proyecto es editar el campo `model` en el `config.toml` local.
- Esto te permite usar el potente y costoso `gemini-1.5-pro` para tareas complejas en un proyecto, y el rápido y económico `gemini-1.5-flash` para tareas más simples en otro.

---

## Anexo: Instalación de `gemini-cli`

Para poder realizar este tutorial, necesitas tener `gemini-cli` instalado.

**Requisito previo:** Debes tener **Python 3.9+** y **pip** (el gestor de paquetes de Python) instalados en tu sistema.

Se recomienda encarecidamente instalar la herramienta en un **entorno virtual** para evitar conflictos con otros paquetes de Python.

### Linux y macOS

1.  **Abre tu terminal.**
2.  **Crea y activa un entorno virtual (opcional pero recomendado):**
    ```bash
    # Crea el entorno
    python3 -m venv gemini-cli-env

    # Activa el entorno
    source gemini-cli-env/bin/activate
    ```
    *Tu prompt debería cambiar para indicar que estás dentro del entorno.*

3.  **Instala `gemini-cli` usando pip:**
    ```bash
    pip install google-gemini-cli
    ```

### Windows

1.  **Abre PowerShell o el Símbolo del sistema (cmd).**
2.  **Crea y activa un entorno virtual (opcional pero recomendado):**
    ```powershell
    # Crea el entorno
    python -m venv gemini-cli-env

    # Activa el entorno en PowerShell
    .\gemini-cli-env\Scripts\Activate.ps1
    
    # O si usas cmd.exe
    # .\gemini-cli-env\Scripts\activate.bat
    ```

3.  **Instala `gemini-cli` usando pip:**
    ```bash
    pip install google-gemini-cli
    ```

### Verificación de la Instalación

Una vez instalado, puedes verificar que todo funciona correctamente ejecutando el comando de ayuda:

```bash
gemini --help
```

Si ves la lista de comandos disponibles, ¡`gemini-cli` está listo para usarse!