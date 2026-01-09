# Elastic Load Balancing en AWS

Servicios para distribuir tráfico entre recursos.

---

## Application Load Balancer (ALB)

**Capa OSI:** Nivel 7 (Aplicación)  
**Protocolos:** HTTP, HTTPS, WebSocket

### Características
- Enrutamiento por host y ruta.
- Ideal para aplicaciones web y APIs.
- Integración con AWS WAF.

### Casos de uso
- Microservicios
- Aplicaciones web modernas
- ECS / EKS

---

## Network Load Balancer (NLB)

**Capa OSI:** Nivel 4 (Transporte)  
**Protocolos:** TCP, UDP, TLS

### Características
- Ultra baja latencia.
- IP estática por AZ.
- Alto rendimiento.

### Casos de uso
- Gaming
- Streaming
- IoT

---

## Gateway Load Balancer (GWLB)

**Capa OSI:** Nivel 3 (Red)

### Características
- Integración con firewalls e IDS/IPS.
- Inspección de tráfico.

### Casos de uso
- Seguridad avanzada
- Network Virtual Appliances

---

## Claves de examen

- ALB = capa 7
- NLB = capa 4
- GWLB = seguridad