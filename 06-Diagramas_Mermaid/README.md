# Ejercicio 06: Generación y Compilación de Diagramas con Mermaid

Este directorio contiene un script de Python (`generar_diagramas.py`) diseñado para ilustrar cómo se pueden documentar procesos de software complejos utilizando diagramas de Mermaid.

Los diagramas generados corresponden a flujos que son notoriamente difíciles de entender y explicar solo con texto.

## Procesos Documentados

1.  **Flujo de Autorización OAuth 2.0 (Authorization Code):** Muestra la interacción entre el usuario, el cliente y los servidores para una autenticación segura.
2.  **Patrón de Diseño "Saga" en Microservicios:** Ilustra cómo se mantiene la consistencia de los datos a través de transacciones locales y compensaciones en caso de fallo.
3.  **Operación `git rebase --interactive`:** Visualiza cómo se re-escribe el historial de commits en Git.

---

## 1. Instalación de Herramientas (Requisito)

Para compilar los diagramas a un formato de imagen como SVG, necesitas la herramienta de línea de comandos de Mermaid (`mmdc`).

**Requisito previo:** Debes tener **Node.js y npm** instalados. Puedes verificarlo con `node -v` y `npm -v`.

Una vez confirmado, instala `mmdc` de forma global en tu sistema ejecutando:

```bash
npm install -g @mermaid-js/mermaid-cli
```

---

## 2. ¿Cómo usarlo?

### Paso A: Generar los archivos de diagrama

Primero, ejecuta el script de Python para generar los archivos de definición de Mermaid (`.mmd`).

```bash
python3 generar_diagramas.py
```

Esto creará tres archivos en el directorio actual:
- `01_oauth2_flow.mmd`
- `02_saga_pattern.mmd`
- `03_git_rebase_interactive.mmd`

### Paso B: Compilar los diagramas a SVG

Ahora, usa `mmdc` para convertir estos archivos `.mmd` en imágenes vectoriales `.svg`.

Puedes hacerlo uno por uno:
```bash
mmdc -i 01_oauth2_flow.mmd -o 01_oauth2_flow.svg
mmdc -i 02_saga_pattern.mmd -o 02_saga_pattern.svg
mmdc -i 03_git_rebase_interactive.mmd -o 03_git_rebase_interactive.svg
```

O puedes usar un bucle `for` en tu terminal para compilarlos todos a la vez:
```bash
# Para bash o zsh
for file in *.mmd; do mmdc -i "$file" -o "${file%.mmd}.svg"; done
```

---

## 3. Visualización de los Diagramas

Tienes dos formas de ver los diagramas:

1.  **Opción recomendada (SVG):** Abre los archivos `.svg` generados directamente en cualquier navegador web (Chrome, Firefox, Safari) o en un visor de imágenes. Esta es la mejor manera de ver una imagen estática de alta calidad.

2.  **Opción alternativa (Live Preview):** Abre los archivos fuente `.mmd` en un editor que tenga un pre-visualizador de Mermaid. Por ejemplo, Visual Studio Code con la extensión **"Markdown Preview Mermaid Support"** o similar. Esto te permite ver el diagrama renderizado en tiempo real mientras editas el código.