# Shared Responsibility Model

Modelo que define **qué es responsabilidad de AWS y qué es responsabilidad del cliente** en la nube.

---

## Concepto clave

- AWS es responsable de la **seguridad DE la nube**.
- El cliente es responsable de la **seguridad EN la nube**.

---

## Responsabilidad de AWS (Security OF the Cloud)

AWS gestiona:
- Centros de datos físicos.
- Hardware y networking.
- Infraestructura global.
- Seguridad física.

Ejemplos:
- Edificios
- Servidores
- Almacenamiento físico

---

## Responsabilidad del cliente (Security IN the Cloud)

El cliente gestiona:
- Configuración de servicios.
- Gestión de identidades (IAM).
- Parches del sistema operativo (en EC2).
- Configuración de seguridad de S3.
- Datos y cifrado.

---

## Ejemplos prácticos

- Bucket S3 público por error → **cliente**
- Acceso IAM mal configurado → **cliente**
- Fallo de hardware → **AWS**
- Seguridad del datacenter → **AWS**

---

## Variación según el servicio

- EC2 → el cliente gestiona el SO.
- RDS / S3 / DynamoDB → AWS gestiona más capas.
- Servicios serverless → menos responsabilidad del cliente.

---

## Claves de examen

- AWS ≠ responsable de la configuración.
- El cliente protege datos y accesos.
- Cuanto más administrado el servicio, menos responsabilidad del cliente.
