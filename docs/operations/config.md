# AWS Config

AWS Config es un servicio que permite **evaluar, auditar y registrar la configuración** de los recursos AWS a lo largo del tiempo.

No mide rendimiento ni uso: **mide configuración y cumplimiento**.

---

## Qué problema resuelve
Permite responder preguntas como:
- “¿Quién cambió este recurso?”
- “¿Cumple esta configuración las reglas de seguridad?”
- “¿Cómo estaba configurado este recurso ayer?”

Es clave para **compliance y auditoría**.

---

## Qué hace AWS Config

### 1) Inventario de recursos
- Mantiene un historial de configuraciones.
- Registra cambios en recursos AWS.
- Permite ver el **estado pasado y actual**.

---

### 2) Evaluación de cumplimiento (Compliance)
- Evalúa recursos contra **reglas**.
- Las reglas pueden ser:
  - AWS Managed Rules
  - Custom Rules (Lambda)

Ejemplos de reglas:
- Buckets S3 no públicos
- EBS cifrado
- RDS con backups habilitados

---

### 3) Auditoría y trazabilidad
- Quién hizo el cambio.
- Cuándo ocurrió.
- Qué cambió exactamente.

---

## Qué NO hace AWS Config
- ❌ No monitoriza CPU, memoria ni latencia.
- ❌ No genera alertas de rendimiento.
- ❌ No sustituye a CloudWatch.

---

## Casos de uso
- Auditorías de seguridad.
- Cumplimiento normativo (compliance).
- Gobernanza de cuentas.
- Análisis forense de cambios.
- Entornos regulados.

---

## Integraciones habituales
- CloudTrail (quién hizo el cambio).
- SNS (notificaciones).
- Security Hub (postura de seguridad).
- Organizations (multi-cuenta).

---

## Pistas de examen (muy importantes)
- AWS Config = **configuración y compliance**.
- CloudWatch ≠ Config:
  - CloudWatch → métricas y logs
  - Config → estado y cambios
- Si hablan de:
  - “record configuration changes”
  - “audit resources”
  - “compliance rules”
  
  👉 **AWS Config**

---

## Ejemplos típicos de pregunta
> “Which service tracks configuration changes over time?”

> “Which service checks if resources comply with security rules?”

Respuesta: **AWS Config**

---

## Resumen rápido
AWS Config = **configuración, cambios y cumplimiento**
