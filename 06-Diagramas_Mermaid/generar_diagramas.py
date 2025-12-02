# generar_diagramas.py

def write_mermaid_file(filename, content):
    """Escribe el contenido de un diagrama en un archivo .mmd puro."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Escribimos solo el código del diagrama, sin formato Markdown adicional
            f.write(content.strip())
        print(f"Archivo de diagrama generado: {filename}")
    except IOError as e:
        print(f"Error al escribir en el archivo {filename}: {e}")

def main():
    # --- Definición de Diagramas ---

    # 1. OAuth 2.0 Authorization Code Flow
    oauth_flow = """
sequenceDiagram
    participant User
    participant ClientApp as Cliente App (Navegador)
    participant AuthServer as Servidor de Autorización
    participant ResourceServer as Servidor de Recursos

    User->>ClientApp: Inicia acción (ej. "Login con Google")
    ClientApp->>AuthServer: Redirige al usuario para autorizar (con client_id, redirect_uri)
    activate AuthServer
    AuthServer->>User: Muestra pantalla de login y consentimiento
    User->>AuthServer: Ingresa credenciales y autoriza
    AuthServer-->>ClientApp: Redirige de vuelta con un Código de Autorización (en la URL)
    deactivate AuthServer
    
    activate ClientApp
    Note right of ClientApp: El frontend recibe el código y lo envía al backend de la App
    ClientApp->>AuthServer: Intercambia el Código por un Access Token (petición backend-a-backend)
    deactivate ClientApp
    
    activate AuthServer
    AuthServer->>AuthServer: Valida el código, client_id y client_secret
    AuthServer-->>ClientApp: Devuelve Access Token y Refresh Token
    deactivate AuthServer
    
    ClientApp->>ResourceServer: Solicita recurso protegido (ej. API de Google) con el Access Token
    activate ResourceServer
    ResourceServer->>ResourceServer: Valida el Access Token
    ResourceServer-->>ClientApp: Devuelve el recurso protegido (ej. datos del usuario)
    deactivate ResourceServer
    
    ClientApp->>User: Muestra los datos o confirma el login
"""

    # 2. Patrón Saga para una transacción distribuida
    saga_pattern = """
sequenceDiagram
    participant Client
    participant OrderService as Servicio de Pedidos
    participant PaymentService as Servicio de Pagos
    participant InventoryService as Servicio de Inventario

    Client->>OrderService: Crear Pedido
    activate OrderService
    OrderService->>OrderService: Crea pedido en estado 'PENDIENTE'
    OrderService->>PaymentService: Iniciar Pago (con datos del pedido)
    deactivate OrderService
    
    activate PaymentService
    PaymentService->>PaymentService: Procesa el pago
    alt Pago Exitoso
        PaymentService-->>OrderService: Evento: 'Pago Realizado'
    else Pago Fallido
        PaymentService-->>OrderService: Evento: 'Pago Fallido'
    end
    deactivate PaymentService

    activate OrderService
    OrderService->>OrderService: Recibe evento de pago
    alt Pago Realizado
        OrderService->>InventoryService: Reservar Inventario
        activate InventoryService
        InventoryService->>InventoryService: Decrementa el stock
        alt Stock Disponible
            InventoryService-->>OrderService: Evento: 'Inventario Reservado'
            activate OrderService
            OrderService->>OrderService: Marca Pedido como 'COMPLETADO'
            deactivate OrderService
        else Stock Insuficiente
            InventoryService-->>OrderService: Evento: 'Fallo en Reserva de Inventario'
            activate OrderService
            OrderService->>OrderService: Inicia transacción de compensación
            OrderService->>PaymentService: Compensación: Reembolsar Pago
            OrderService->>OrderService: Marca Pedido como 'FALLIDO'
            deactivate OrderService
        end
        deactivate InventoryService
    else Pago Fallido
        OrderService->>OrderService: Marca Pedido como 'CANCELADO'
    end
    deactivate OrderService
"""

    # 3. Git Rebase Interactivo
    git_rebase = """
graph TD
    subgraph "Antes del Rebase Interactivo"
        A[C1: Commit inicial] --> B(C2: feat A)
        B --> C(C3: feat B)
        C --> D(C4: feat C)
    end

    subgraph "Comando: git rebase -i HEAD~3"
        direction LR
        subgraph "Editor de Rebase"
            i1("pick C2: feat A")
            i2("squash C3: feat B")
            i3("pick C4: feat C")
        end
    end
    
    subgraph "Después del Rebase"
        A --> E(C2': feat A + feat B)
        E --> F(C4': feat C)
    end
    
    D --"re-escribe la historia"--> F
    C --"se fusiona en C2'"--> E
    B --"se convierte en C2'"--> E

    classDef original fill:#f9f,stroke:#333,stroke-width:2px;
    class A,B,C,D original;
"""

    # --- Generación de archivos ---
    diagrams = {
        "01_oauth2_flow.mmd": oauth_flow,
        "02_saga_pattern.mmd": saga_pattern,
        "03_git_rebase_interactive.mmd": git_rebase
    }

    for filename, content in diagrams.items():
        write_mermaid_file(filename, content)

if __name__ == '__main__':
    main()
