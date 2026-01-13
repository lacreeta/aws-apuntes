# Introducción a AWS

## ¿Qué es AWS?

**Amazon Web Services (AWS)** es la plataforma de servicios en la nube más completa y ampliamente adoptada del mundo, ofrecida por Amazon.

Lanzado en 2006, AWS ofrece más de 200 servicios completos desde centros de datos distribuidos globalmente.

**Equivalente en Azure**: Microsoft Azure

---

## ¿Qué es Cloud Computing?

Cloud Computing (computación en la nube) es la **entrega bajo demanda** de recursos de TI a través de Internet con precios de pago por uso.

### Características Principales

1. **Bajo demanda (On-demand)**: Acceso instantáneo a recursos sin intervención humana
2. **Acceso a través de red**: Accesible desde cualquier lugar con Internet
3. **Pool de recursos**: Recursos compartidos entre múltiples clientes
4. **Elasticidad rápida**: Escalado automático según necesidades
5. **Servicio medido**: Pago solo por lo que usas

---

## Modelos de Servicio Cloud

### IaaS (Infrastructure as a Service)
**Máximo control, máxima responsabilidad**

- Infraestructura virtualizada
- Tú gestionas: OS, middleware, runtime, datos, aplicaciones
- AWS gestiona: hardware físico, networking, virtualización

**Ejemplos en AWS**: EC2, VPC, EBS

**Equivalente Azure**: Azure Virtual Machines

---

### PaaS (Platform as a Service)
**Balance entre control y gestión**

- Plataforma de desarrollo completa
- Tú gestionas: aplicaciones y datos
- AWS gestiona: todo lo demás (OS, runtime, middleware, etc.)

**Ejemplos en AWS**: Elastic Beanstalk, RDS, Lambda

**Equivalente Azure**: Azure App Service, Azure SQL Database

---

### SaaS (Software as a Service)
**Mínimo control, mínima responsabilidad**

- Software completo gestionado por el proveedor
- Tú solo usas la aplicación
- El proveedor gestiona todo

**Ejemplos**: Gmail, Office 365, Salesforce

**En AWS**: WorkMail, Chime, WorkDocs

---

## Modelos de Implementación Cloud

### Nube Pública
- Recursos propiedad y operados por un proveedor cloud
- Compartidos entre múltiples organizaciones
- Acceso a través de Internet

**Ejemplo**: AWS, Azure, GCP

---

### Nube Privada
- Infraestructura dedicada a una sola organización
- Mayor control y seguridad
- Puede estar on-premises o hosted

**En AWS**: AWS Outposts (trae AWS a tu datacenter)

---

### Nube Híbrida
- Combinación de nube pública y privada
- Datos y aplicaciones compartidos entre ellas
- Mayor flexibilidad

**En AWS**: AWS Direct Connect, Storage Gateway

---

## Ventajas de AWS Cloud

### 1. Costos Variables vs Costos Fijos
- **Antes**: Comprar servidores (CAPEX)
- **Con AWS**: Pagar solo por uso (OPEX)

### 2. Economías de Escala
- AWS compra a gran escala → precios más bajos
- Los ahorros se transfieren a los clientes

### 3. Sin Gestión de Capacidad
- No necesitas adivinar capacidad
- Escala automática según demanda

### 4. Velocidad y Agilidad
- Recursos en minutos, no semanas/meses
- Experimenta rápido y falla rápido

### 5. No Mantener Datacenters
- AWS gestiona el hardware
- Tú te enfocas en tu negocio

### 6. Alcance Global en Minutos
- Despliega en múltiples regiones mundiales
- Baja latencia para usuarios globales

---

## AWS vs Modelo Tradicional

| Aspecto | Tradicional On-Premises | AWS Cloud |
|---------|-------------------------|-----------|
| **Inversión inicial** | Alta (CAPEX) | Baja (OPEX) |
| **Escalado** | Semanas/meses | Minutos |
| **Capacidad** | Fija, puede sobrar/faltar | Elástica, ajustable |
| **Mantenimiento** | Tu responsabilidad | AWS gestiona infraestructura |
| **Alcance global** | Costoso y lento | Rápido y económico |
| **Innovación** | Ciclos largos | Experimentación rápida |

---

## Tipos de Clientes AWS

AWS sirve a todo tipo de organizaciones:

- **Startups**: Infraestructura sin inversión inicial
- **Empresas**: Modernización de aplicaciones legacy
- **Gobierno**: Cumplimiento y seguridad (AWS GovCloud)
- **ONGs**: Costos reducidos para impacto social

---

## Servicios Principales de AWS (Overview)

### Compute
EC2, Lambda, ECS, EKS, Fargate, Elastic Beanstalk

### Storage
S3, EBS, EFS, Glacier, Storage Gateway

### Databases
RDS, DynamoDB, ElastiCache, Redshift, Aurora

### Networking
VPC, CloudFront, Route 53, Direct Connect, API Gateway

### Security & Identity
IAM, Cognito, KMS, Shield, WAF, GuardDuty

### Management & Governance
CloudWatch, CloudTrail, Config, Systems Manager, CloudFormation

---

## 6 Pilares del Well-Architected Framework

1. **Operational Excellence**: Operaciones que soportan el negocio
2. **Security**: Protección de información y sistemas
3. **Reliability**: Recuperación de fallos y escalado según demanda
4. **Performance Efficiency**: Uso eficiente de recursos
5. **Cost Optimization**: Evitar costos innecesarios
6. **Sustainability**: Minimizar impacto ambiental

Más detalles en [Well-Architected Framework](operations/well-architected.md)

---

!!! tip "Para el Examen"
    - Entiende las **ventajas de la nube** (6 ventajas principales)
    - Conoce la diferencia entre **IaaS, PaaS, SaaS**
    - Comprende **CAPEX vs OPEX**
    - Familiarízate con el **Well-Architected Framework**

---

## Siguientes Pasos

Ahora que entiendes los conceptos fundamentales, continúa con:

1. [Infraestructura Global de AWS](global-infrastructure.md)
2. [Modelo de Responsabilidad Compartida](security/shared-responsibility.md)
3. [IAM - Identity and Access Management](security/iam.md)