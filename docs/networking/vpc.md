## Amazon VPC (Virtual Private Cloud)

Amazon VPC es el servicio de AWS que permite crear **redes virtuales aisladas** dentro de la nube de AWS.

Equivalente en Azure: **Azure Virtual Network (VNet)**

---

## Características principales de VPC

- Red virtual privada y aislada.
- Definición de rangos IP mediante **CIDR**.
- Control total sobre red y seguridad.
- Integración con la mayoría de servicios AWS.
- Diseño regional (abarca varias Availability Zones).

---

## Componentes principales de VPC

### Subnets

- Segmentos de red dentro de una VPC.
- Asociadas a **una sola Availability Zone**.
- Tipos:
  - **Public Subnet**: tiene acceso a Internet.
  - **Private Subnet**: sin acceso directo a Internet.

Equivalente en Azure: **Subnets en VNet**

---

### Internet Gateway (IGW)

- Permite comunicación entre la VPC e Internet.
- Necesario para que una subnet sea pública.

Equivalente en Azure: **Internet Gateway implícito en VNet**

---

### NAT Gateway

- Permite que instancias en subnets privadas accedan a Internet **sin ser accesibles desde fuera**.
- Servicio administrado.

Equivalente en Azure: **NAT Gateway**

---

### Route Tables

- Definen cómo se enruta el tráfico dentro de la VPC.
- Asociadas a subnets.

Equivalente en Azure: **User Defined Routes (UDR)**

---

### Security Groups

- Firewall a nivel de instancia.
- **Stateful**.
- Permiten reglas de entrada y salida.

Equivalente en Azure: **Network Security Groups (NSG)**

---

### Network ACLs (NACL)

- Firewall a nivel de subnet.
- **Stateless**.
- Reglas de allow y deny explícitas.

Equivalente en Azure: **NSG + Azure Firewall (combinación)**

---

## Conectividad VPC

- **VPC Peering**: conexión privada entre VPCs.
- **VPN Site-to-Site**: conexión cifrada con on-premises.
- **Client VPN**: acceso remoto de usuarios.
- **Direct Connect**: conexión dedicada y privada.

---

## Claves de examen VPC

- VPC es regional.
- Subnets son zonales.
- Security Groups = stateful.
- NACL = stateless.
- Subnet pública necesita Internet Gateway.