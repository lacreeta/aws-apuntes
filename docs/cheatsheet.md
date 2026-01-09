# AWS Certified Cloud Practitioner – Cheatsheet Extendido

Este documento resume los **servicios clave de AWS**, cómo elegirlos en el examen y las **trampas más comunes**.

---

## 🧠 Cómo piensa AWS en el examen
AWS evalúa si sabes:
- Elegir el **servicio correcto**
- Diferenciar **serverless vs managed vs IaaS**
- Entender **coste, escalado y responsabilidad**
- Identificar **palabras clave en escenarios**

---

## 📦 STORAGE – Tipos y decisiones

### Qué almacenamiento elegir
| Necesidad | Servicio |
|---------|---------|
| Object storage | Amazon S3 |
| Disco para una EC2 | Amazon EBS |
| File system compartido | Amazon EFS |
| Archivado barato | Amazon S3 Glacier |

---

### Amazon S3
- Object storage
- Serverless
- Escala automáticamente
- Alta durabilidad
- Pago por uso

**Usar cuando**:
- Backups
- Data lakes
- Archivos estáticos

**Frases de examen**:
- Object storage
- Highly durable
- Store files

---

### Amazon EBS
- Block storage
- Se adjunta a **una EC2**
- Vive en una AZ
- Persistente

**Frases de examen**:
- Disk for EC2
- Low latency storage
- Attached volume

---

### Amazon EFS
- File system
- Compartido entre múltiples EC2
- Escala automáticamente
- Multi-AZ

**Frases de examen**:
- Shared file system
- Multiple EC2
- Linux workloads

---

### Amazon S3 Glacier
- Archivado a largo plazo
- Coste muy bajo
- Acceso lento

**Frases de examen**:
- Long-term retention
- Compliance
- Rarely accessed data

---

## ⚙️ COMPUTE – Niveles de abstracción

### Escalera de compute
| Nivel | Servicio |
|----|---------|
| IaaS | EC2 |
| Containers managed | ECS / EKS |
| Serverless | Lambda |
| Serverless containers | Fargate |

---

### Amazon EC2
- Control total
- Gestionas SO y parches
- Pago por instancia

**Frases de examen**:
- Full control
- Custom OS
- Virtual machine

---

### AWS Lambda
- Serverless compute
- Event-driven
- Pago por ejecución

**Frases de examen**:
- Run code without servers
- Event-driven
- Short-lived tasks

---

### AWS Fargate
- Contenedores sin gestionar servidores
- Serverless para containers

**Frases de examen**:
- Containers without managing servers
- ECS / EKS + Fargate

---

## 📡 APPLICATION INTEGRATION – Desacoplar apps

### Amazon SQS
- Cola de mensajes
- Desacopla aplicaciones
- Pull-based

**Frases de examen**:
- Decouple applications
- Queue
- Buffer messages

---

### Amazon SNS
- Pub/Sub
- Push-based
- Fan-out

**Frases de examen**:
- Fan-out
- Push notifications
- Multiple subscribers

---

### Amazon EventBridge
- Event bus
- Arquitecturas event-driven
- Integración serverless

**Frases de examen**:
- Event-driven architecture
- AWS service events

---

## 📊 ANALYTICS – Procesar datos

### Amazon Athena
- SQL sobre S3
- Serverless
- Pago por query

**Frases de examen**:
- Query S3 with SQL
- No infrastructure

---

### AWS Glue
- ETL serverless
- Data Catalog
- Preparación de datos

**Frases de examen**:
- ETL
- Data preparation

---

### Amazon EMR
- Big Data
- Spark / Hadoop
- Usa EC2

**Frases de examen**:
- Clusters
- Big data processing

---

### Amazon Kinesis Data Streams
- Streaming en tiempo real
- Serverless
- AWS-native

**Frases de examen**:
- Real-time streaming
- Low latency

---

### Amazon MSK
- Apache Kafka gestionado
- Usa brokers
- No serverless

**Frases de examen**:
- Apache Kafka
- Managed Kafka

---

## 🗄️ DATABASES – Qué base elegir

### Amazon RDS
- Relacional managed
- SQL
- No serverless

---

### Amazon Aurora
- Relacional AWS-native
- Alta disponibilidad
- Compatible MySQL / PostgreSQL

---

### Amazon DynamoDB
- NoSQL
- Serverless
- Escala automática

**Frases de examen**:
- Key-value
- Serverless database
- Single-digit millisecond latency

---

### Amazon Redshift
- Data warehouse
- Analytics a gran escala
- SQL

**Frases de examen**:
- Data warehouse
- Analytics at scale

---

## 🔐 SECURITY – Muy preguntado

### AWS IAM
- Usuarios, roles y policies
- Control de acceso

**Frases de examen**:
- Least privilege
- Roles for EC2 / Lambda

---

### AWS KMS
- Gestión de claves
- Encryption at rest
- Integrado con AWS

**Frases de examen**:
- Encryption
- Managed keys

---

### Shared Responsibility Model
| AWS | Cliente |
|---|---|
| Infraestructura | Datos |
| Hardware | SO en EC2 |
| Servicios gestionados | Configuración |

**Frase clave**:
- AWS secures the cloud
- Customer secures what’s in the cloud

---

## 💸 BILLING – Siempre cae

### Modelos de pricing
- Pay-as-you-go
- Savings Plans
- Reserved Instances

### Savings Plans
- Compute (EC2, Lambda, Fargate)
- No aplican a S3

---

## 🧠 TRAMPAS CLÁSICAS DE EXAMEN

| Escenario | Respuesta |
|---------|----------|
| Decouple apps | SQS |
| Fan-out | SNS |
| SQL sobre S3 | Athena |
| Data warehouse | Redshift |
| Streaming serverless | Kinesis |
| Kafka | MSK |
| File system compartido | EFS |
| Disco para EC2 | EBS |
| Archivado barato | Glacier |
| Encryption | KMS |

---

## 🏁 Checklist final
Si sabes responder esto, apruebas:
- S3 vs EBS vs EFS
- Athena vs Redshift
- SQS vs SNS
- Kinesis vs MSK
- Serverless vs Managed
- Shared Responsibility Model
