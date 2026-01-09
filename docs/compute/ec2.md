## Amazon EC2 (Elastic Compute Cloud)

Amazon EC2 es el servicio de AWS que proporciona **capacidad de cómputo escalable** en la nube mediante máquinas virtuales.

Equivalente en Azure: **Azure Virtual Machines**

---

## Características principales de EC2

- Provisión de máquinas virtuales bajo demanda.
- Control total del sistema operativo.
- Escalado vertical y horizontal.
- Pago por uso (segundos o horas según configuración).
- Integración con otros servicios AWS (IAM, VPC, ELB, CloudWatch).

---

## Componentes clave de EC2

### AMI (Amazon Machine Image)

- Plantilla que define:
  - Sistema operativo
  - Software preinstalado
  - Configuración inicial
- Se utiliza para lanzar instancias EC2.

Equivalente en Azure: **Imágenes de VM**

---

### Tipos de instancias

Clasificación según uso:
- **General Purpose** (ej. t3, t4g)
- **Compute Optimized** (ej. c6)
- **Memory Optimized** (ej. r6)
- **Storage Optimized** (ej. i3)

Para el examen no es necesario memorizar familias concretas.

---

### Modelos de compra

- **On-Demand**: pago por uso, sin compromiso.
- **Reserved Instances**: descuento por compromiso (1 o 3 años).
- **Savings Plans**: descuentos basados en uso.
- **Spot Instances**: uso de capacidad sobrante (más barato, pero puede interrumpirse).

Claves de examen:
- Spot = más barato
- On-Demand = flexible
- Reserved/Savings = ahorro a largo plazo

---

### Seguridad en EC2

- **Security Groups**: firewall a nivel de instancia (stateful).
- Integración con IAM Roles para acceso a otros servicios.
- Uso de pares de claves (Key Pair) para acceso SSH.

---

### Escalabilidad y alta disponibilidad

- **Auto Scaling Groups**: ajustan automáticamente el número de instancias.
- Integración con **Elastic Load Balancing**.
- Uso de **Availability Zones** para alta disponibilidad.

---

## Casos de uso de EC2

- Aplicaciones web tradicionales.
- Servidores empresariales.
- Aplicaciones legacy.
- Entornos de desarrollo y testing.