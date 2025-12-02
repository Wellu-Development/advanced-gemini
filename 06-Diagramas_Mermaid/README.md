# Ejercicio 06: Generación de Diagramas Complejos con Mermaid

Este directorio contiene un script de Python (`generar_diagramas.py`) diseñado para ilustrar cómo se pueden documentar procesos de software complejos utilizando diagramas de Mermaid.

Los diagramas generados corresponden a flujos que son notoriamente difíciles de entender y explicar solo con texto.

## Procesos Documentados

1.  **Flujo de Autorización OAuth 2.0 (Authorization Code):** Muestra la interacción entre el usuario, el cliente y los servidores para una autenticación segura.
2.  **Patrón de Diseño "Saga" en Microservicios:** Ilustra cómo se mantiene la consistencia de los datos a través de transacciones locales y compensaciones en caso de fallo.
3.  **Operación `git rebase --interactive`:** Visualiza cómo se re-escribe el historial de commits en Git, una operación potente pero peligrosa.

## ¿Cómo usarlo?

1.  Abre una terminal en el directorio `06-Diagramas_Mermaid`.
2.  Ejecuta el script de Python:
    ```bash
    python3 generar_diagramas.py
    ```
3.  El script generará tres archivos:
    - `01_oauth2_flow.md`
    - `02_saga_pattern.md`
    - `03_git_rebase_interactive.md`
4.  Abre estos archivos `.md` en un visor compatible con Mermaid (como el de GitHub, GitLab o VS Code con la extensión "Markdown Preview Mermaid Support") para ver los diagramas renderizados.
