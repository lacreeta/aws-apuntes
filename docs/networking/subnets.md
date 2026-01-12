# Subnets, Internet Gateway y NAT Gateway

Servicios fundamentales para **organizar y controlar el tráfico** dentro de una VPC.

---

## Subnets

### Qué son
Segmentos de red dentro de una VPC.

### Características clave
- Asociadas a **una sola Availability Zone**.
- Definen si un recurso es público o privado.
- Usan rangos IP del CIDR de la VPC.

### Tipos
- **Public Subnet** → acceso a Internet.
- **Private Subnet** → sin acceso directo a Internet.

---

## Internet Gateway (IGW)

### Qué es
Permite la comunicación entre la VPC e Internet.

### Claves
- Se asocia a una VPC.
- Necesario para subnets públicas.
- Permite tráfico **entrante y saliente**.

---

## NAT Gateway

### Qué es
Permite que instancias en **subnets privadas** accedan a Internet **sin recibir tráfico entrante**.

### Claves
- Servicio totalmente gestionado.
- Se despliega en una subnet pública.
- Solo tráfico saliente.

---

## Casos de uso
- Web servers en subnets públicas.
- Bases de datos en subnets privadas.
- Acceso seguro a Internet desde recursos privados.

---

## Pistas de examen
- Subnet pública = ruta a IGW.
- Subnet privada = usa NAT Gateway.
- NAT ≠ Internet Gateway.

---

## Resumen rápido
- Subnet = segmento de red  
- IGW = acceso a Internet  
- NAT = salida a Internet desde privado