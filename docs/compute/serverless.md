## Servicios Serverless (Core)

Los servicios serverless permiten ejecutar código o procesos **sin gestionar servidores**.
AWS se encarga automáticamente de:
- Infraestructura
- Escalado
- Alta disponibilidad

El usuario paga **solo por el uso real**.

---

## AWS Lambda

AWS Lambda es un servicio serverless que permite **ejecutar código en respuesta a eventos**.

No es necesario aprovisionar ni administrar servidores.

Equivalente en Azure: **Azure Functions**

---

### Características principales de Lambda

- Ejecución bajo demanda.
- Escalado automático.
- Pago por número de ejecuciones y tiempo de ejecución.
- Integración nativa con otros servicios AWS.

---

### Casos de uso de Lambda

- Procesamiento de eventos S3.
- APIs backend.
- Automatización y tareas programadas.
- Procesamiento de streams y logs.

---

### Claves de examen Lambda

- Serverless.
- Escala automáticamente.
- Pago por ejecución.
- No se gestionan servidores.

---

## Amazon API Gateway

Amazon API Gateway es un servicio totalmente administrado para **crear, publicar y gestionar APIs**.

Suele usarse junto con AWS Lambda.

Equivalente en Azure: **Azure API Management (básico)**

---

### Características principales de API Gateway

- Soporte para APIs REST y HTTP.
- Autenticación y control de acceso.
- Integración directa con Lambda y otros servicios AWS.
- Escalado automático.

---

### Casos de uso de API Gateway

- Exponer funciones Lambda como APIs.
- Backend para aplicaciones web y móviles.
- Arquitecturas serverless.

---

### Claves de examen API Gateway

- Servicio gestionado.
- Se integra con Lambda.
- Ideal para arquitecturas serverless.

---

## Servicios de mensajería (Serverless)

### Amazon SQS (Simple Queue Service)

Servicio de colas totalmente administrado para **desacoplar aplicaciones**.

Equivalente en Azure: **Azure Queue Storage / Service Bus (colas)**

---

#### Características de SQS

- Almacenamiento temporal de mensajes.
- Escalado automático.
- Alta disponibilidad.
- Dos tipos:
  - Standard
  - FIFO (orden garantizado)

---

#### Casos de uso SQS

- Comunicación entre microservicios.
- Procesamiento asíncrono.
- Gestión de picos de carga.

---

### Amazon SNS (Simple Notification Service)

Servicio de mensajería basado en **publicación/suscripción**.

Equivalente en Azure: **Azure Event Grid**

---

#### Características de SNS

- Envío de mensajes a múltiples suscriptores.
- Soporte para múltiples protocolos (email, SMS, Lambda, SQS).
- Alta disponibilidad.

---

#### Casos de uso SNS

- Notificaciones.
- Alertas.
- Arquitecturas orientadas a eventos.

---

### Claves de examen SQS vs SNS

- SQS = colas (uno a uno).
- SNS = pub/sub (uno a muchos).
- Ambos son serverless.

---