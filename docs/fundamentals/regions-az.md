# Regiones, Availability Zones y Edge Locations

Conceptos fundamentales de la infraestructura global de AWS que afectan a **disponibilidad, latencia y resiliencia**.

---

## Región (Region)

Una **región** es un área geográfica que contiene múltiples centros de datos de AWS.

- Cada región es independiente.
- Los recursos se despliegan en una región concreta.
- No todos los servicios están disponibles en todas las regiones.

Ejemplos:
- eu-west-1 (Irlanda)
- us-east-1 (N. Virginia)

---

## Availability Zones (AZ)

Una **Availability Zone** es uno o más centros de datos dentro de una región.

- Cada AZ está aislada físicamente.
- Conectadas mediante redes de alta velocidad.
- Diseñadas para evitar fallos simultáneos.

### Uso principal
- Alta disponibilidad.
- Tolerancia a fallos.

Ejemplo:
- Región: eu-west-1  
- AZs: eu-west-1a, eu-west-1b, eu-west-1c

---

## Edge Locations

Ubicaciones utilizadas para **entrega de contenido y baja latencia**.

- Usadas principalmente por CloudFront.
- Distribuidas globalmente.
- No sirven para desplegar recursos como EC2.

---

## Relación entre Region, AZ y Edge

- Región → ámbito geográfico.
- AZ → alta disponibilidad dentro de una región.
- Edge → optimización de latencia global.

---

## Claves de examen

- Las regiones son independientes.
- Las AZ son aisladas entre sí.
- Alta disponibilidad = múltiples AZ.
- CloudFront usa Edge Locations.
