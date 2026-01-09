# Seguridad en la red en AWS

Servicios y mecanismos para proteger el tráfico y la conectividad en AWS.

---

## Conceptos clave

- Security Groups → **stateful**
- NACL → **stateless**

---

## AWS Network Firewall

Firewall administrado para proteger VPC.

Equivalente en Azure: **Azure Firewall**

---

## AWS WAF

Protección contra ataques web (SQL Injection, XSS).

Equivalente en Azure: **Azure Web Application Firewall**

---

## AWS Shield

Protección contra ataques DDoS.

Equivalente en Azure: **Azure DDoS Protection**

---

## Security Groups

Firewall a nivel de instancia.

Equivalente en Azure: **Network Security Groups (NSG)**

---

## NACL

Firewall a nivel de subnet.

Equivalente en Azure: **NSG + Azure Firewall**

---

## Claves de examen

- Security Groups = stateful
- NACL = stateless
- WAF protege aplicaciones web
- Shield protege contra DDoS