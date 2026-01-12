# Elastic Load Balancing (ELB)

Servicios para **distribuir tráfico** entre múltiples recursos y mejorar disponibilidad.

---

## Application Load Balancer (ALB)

- Capa OSI: **Nivel 7**
- Protocolos: HTTP / HTTPS
- Enrutamiento por host y path.

### Casos de uso
- Aplicaciones web.
- APIs.
- Microservicios.

---

## Network Load Balancer (NLB)

- Capa OSI: **Nivel 4**
- Protocolos: TCP / UDP / TLS
- Ultra baja latencia.

### Casos de uso
- Alto rendimiento.
- Gaming.
- Streaming.

---

## Gateway Load Balancer (GWLB)

- Capa OSI: **Nivel 3**
- Integración con firewalls e IDS/IPS.

---

## Pistas de examen
- ALB = capa 7.
- NLB = capa 4.
- ELB mejora alta disponibilidad.

---

## Resumen rápido
Load Balancer = **distribuir tráfico y mejorar resiliencia**
