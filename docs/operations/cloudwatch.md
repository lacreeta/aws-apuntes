# Amazon CloudWatch

Amazon CloudWatch es el servicio de AWS para **monitorización y observabilidad** de recursos y aplicaciones.
Permite recopilar **métricas, logs y eventos**, además de crear **alarmas**.

---

## Qué problema resuelve
Te permite responder preguntas como:
- “¿Está mi sistema sano?”
- “¿Hay errores o picos de uso?”
- “¿Qué está pasando ahora mismo?”

Sin CloudWatch, operar en AWS a escala es muy difícil.

---

## Qué hace CloudWatch (3 pilares)

### 1) Metrics (métricas)
- Datos numéricos en el tiempo (CPU, latencia, IOPS, etc.).
- Muchas métricas vienen **por defecto** de servicios como EC2.
- Puedes crear **Custom Metrics** (métricas propias).

**Ejemplos típicos**
- CPUUtilization en EC2
- Latency en ALB
- FreeStorageSpace en RDS

---

### 2) Logs (registros)
- Centraliza y almacena logs de aplicaciones y servicios.
- Permite buscar, filtrar y analizar.

**Conceptos**
- Log Group: “contenedor” (por app/servicio)
- Log Stream: “flujo” de logs (por instancia/contendor)

---

### 3) Events / EventBridge (eventos)
CloudWatch Events evolucionó hacia **Amazon EventBridge**.
- Se usa para reaccionar a cambios de estado (ej. “EC2 stopped”).
- Arquitecturas event-driven.

> En examen: “invocar Lambda cuando pasa X” → suele ser **EventBridge** (antes CloudWatch Events).

---

## Alarmas (CloudWatch Alarms)
Permiten crear alertas basadas en métricas:
- Cuando una métrica cruza un umbral, se dispara una alarma.
- Se puede integrar con:
  - SNS (notificaciones)
  - Auto Scaling (escalado)
  - acciones automatizadas

---

## CloudWatch Dashboards
- Paneles visuales con métricas.
- Muy usado para NOC/operaciones.

---

## Casos de uso
- Monitorizar EC2/RDS/ALB/Lambda.
- Alertas (CPU alta, errores, latencia).
- Centralizar logs.
- Dashboards operativos.
- Automatización basada en eventos (vía EventBridge).

---

## Pistas de examen
- CloudWatch = **monitorización y observabilidad**.
- Métricas + logs + alarmas.
- Config ≠ CloudWatch:
  - CloudWatch: “cómo rinde / qué pasa”
  - Config: “cómo está configurado / compliance”
- Para reaccionar a eventos de estado → normalmente **EventBridge**.
