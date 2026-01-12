# AWS X-Ray

AWS X-Ray es un servicio de AWS para **trazabilidad (tracing)** en aplicaciones distribuidas.
Permite seguir una petición “de punta a punta” (end-to-end) a través de múltiples servicios.

---

## Qué problema resuelve
En microservicios o arquitecturas distribuidas, cuando algo va lento o falla, es difícil saber:
- ¿Dónde está el cuello de botella?
- ¿Qué servicio está causando el error?
- ¿Qué dependencias externas fallan?

X-Ray te da visibilidad del “camino” de una request.

---

## Qué hace X-Ray
- Recoge trazas (traces) de solicitudes.
- Muestra un **Service Map** (mapa de servicios y dependencias).
- Identifica:
  - Latencia por servicio
  - Errores
  - Retries
  - Bottlenecks

---

## Conceptos clave (examen-friendly)

### Trace
La traza completa de una petición (end-to-end).

### Segment
Parte de la traza generada por un servicio AWS (ej. Lambda, API Gateway).

### Subsegment
Detalles dentro de un segmento (ej. llamada a DynamoDB o a un servicio externo).

### Service Map
Diagrama visual de cómo se conectan los servicios y dónde hay latencia/errores.

---

## Integraciones típicas
- AWS Lambda
- Amazon API Gateway
- Amazon ECS/EKS
- Elastic Load Balancing (ALB)
- Aplicaciones en EC2 (con SDK/agent)
- Servicios downstream (DynamoDB, SQS, etc.) como dependencias en la traza

---

## Casos de uso
- Depurar latencia en microservicios.
- Encontrar fallos en cadena (un servicio lento afecta a otros).
- Root cause de errores intermitentes.
- Observabilidad avanzada en arquitecturas serverless.

---

## Pistas de examen
- X-Ray = **tracing** (seguimiento de requests).
- CloudWatch ≠ X-Ray:
  - CloudWatch: métricas/logs/alertas
  - X-Ray: trazas y dependencias (end-to-end)
- Si preguntan por “service map” o “request tracing” → X-Ray.

---

## Resumen rápido
X-Ray = **tracing end-to-end para apps distribuidas**
