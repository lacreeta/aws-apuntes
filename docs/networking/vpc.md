# Amazon VPC (Virtual Private Cloud)

Amazon VPC es el servicio de AWS que permite crear **redes virtuales privadas y aisladas** dentro de la nube de AWS.

---

## Qué problema resuelve
Permite controlar **red, direccionamiento IP, seguridad y conectividad** de los recursos desplegados en AWS.

---

## Características clave
- Red **aislada** por cuenta.
- Definición de rangos IP mediante **CIDR**.
- Diseño **regional** (abarca varias AZ).
- Control total del tráfico de red.
- Integración con la mayoría de servicios AWS.

---

## Componentes principales
- Subnets
- Route Tables
- Internet Gateway
- NAT Gateway
- Security Groups
- Network ACLs

---

## Casos de uso
- Aislar entornos (prod / dev / test).
- Controlar acceso a Internet.
- Arquitecturas seguras y escalables.
- Conectividad híbrida.

---

## Pistas de examen
- VPC es **regional**.
- Subnets son **zonales**.
- Toda instancia EC2 vive dentro de una VPC.
- Security Groups = stateful.
- NACL = stateless.

---

## Resumen rápido
VPC = **red privada en AWS**