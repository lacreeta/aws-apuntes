# Tips para el Examen AWS Cloud Practitioner

Esta página contiene consejos estratégicos para maximizar tus posibilidades de aprobar el examen.

---

## 📝 Formato del Examen

### Tipos de Preguntas

**1. Opción Múltiple (1 respuesta correcta de 4)**
- La mayoría de las preguntas son de este tipo
- 3 distractores incorrectos

**2. Respuesta Múltiple (2+ respuestas correctas de 5)**
- Indica cuántas respuestas seleccionar
- Ejemplo: "Seleccione DOS opciones"

### Características
- Sin penalización por respuesta incorrecta → **responde todas las preguntas**
- Puedes marcar preguntas para revisar después
- 90 minutos es suficiente tiempo
- Calculadora disponible en preguntas de costos

---

## 🎯 Estrategia General

### Durante el Estudio

!!! tip "Enfoque Conceptual"
    El examen evalúa **comprensión conceptual**, no memorización de detalles técnicos.
    
    - ✅ Entiende CUÁNDO usar cada servicio
    - ✅ Conoce casos de uso típicos
    - ❌ No necesitas memorizar límites específicos
    - ❌ No necesitas saber sintaxis de código

### Durante el Examen

1. **Lee la pregunta completa** antes de ver las opciones
2. **Identifica palabras clave** (alta disponibilidad, bajo costo, serverless, etc.)
3. **Elimina respuestas obviamente incorrectas** primero
4. **Si dudas**, marca y continúa (no pierdas tiempo)
5. **Revisa marcadas** al final si hay tiempo

---

## 🔑 Palabras Clave y Sus Servicios

Aprende a reconocer qué pide cada pregunta:

| Palabra Clave | Probablemente la respuesta sea... |
|---------------|-----------------------------------|
| **Serverless** | Lambda, DynamoDB, S3, API Gateway, Fargate |
| **Cost optimization / Lowest cost** | Spot Instances, S3 Glacier, Reserved Instances |
| **High availability** | Multi-AZ, ELB, Auto Scaling, Route 53 |
| **Global performance / CDN** | CloudFront |
| **File storage / Shared storage** | EFS |
| **Object storage** | S3 |
| **Block storage** | EBS |
| **Archival** | S3 Glacier |
| **DNS** | Route 53 |
| **DDoS protection** | Shield (Standard/Advanced) |
| **WAF / Web filtering** | AWS WAF |
| **Encryption at rest** | KMS |
| **Identity management** | IAM, Cognito |
| **Monitoring** | CloudWatch |
| **Auditing / Compliance** | CloudTrail, Config |
| **Cost management** | Cost Explorer, Budgets |
| **Migration** | DMS, DataSync, Snow Family |
| **Machine Learning** | SageMaker, Rekognition, Comprehend |
| **Hybrid cloud** | Storage Gateway, Direct Connect |

---

## ⚠️ Confusiones Comunes

### Storage: S3 vs EBS vs EFS

| Servicio | Tipo | Uso | Acceso |
|----------|------|-----|--------|
| **S3** | Object storage | Archivos, backups, sitios estáticos | Internet/API |
| **EBS** | Block storage | Disco duro de EC2 | Solo una instancia |
| **EFS** | File storage | Compartido entre EC2 | Múltiples instancias |

!!! warning "Clave del Examen"
    - ¿Necesitas compartir entre instancias? → **EFS**
    - ¿Es un archivo/objeto individual? → **S3**
    - ¿Es el disco de una VM? → **EBS**

---

### Security Groups vs NACLs

| Aspecto | Security Groups | NACLs |
|---------|----------------|--------|
| **Nivel** | Instancia (ENI) | Subnet |
| **Estado** | Stateful | Stateless |
| **Reglas** | Solo ALLOW | ALLOW y DENY |
| **Orden** | No importa | Evaluación secuencial |

---

### CloudWatch vs CloudTrail

| Servicio | Propósito | Qué Registra |
|----------|-----------|--------------|
| **CloudWatch** | Monitoreo de performance | Métricas (CPU, memoria, logs) |
| **CloudTrail** | Auditoría de acciones | API calls, quién hizo qué y cuándo |

!!! tip "Recuerda"
    - Performance/métricas → **CloudWatch**
    - Auditoría/compliance → **CloudTrail**

---

### IAM Users vs IAM Roles

| Concepto | Uso | Credenciales |
|----------|-----|--------------|
| **IAM User** | Personas o aplicaciones específicas | Permanentes (Access Keys) |
| **IAM Role** | Servicio AWS o acceso temporal | Temporales (asumidos) |

**Regla de oro**: Servicios AWS usan Roles, NO Users

---

### Reserved vs Spot vs Savings Plans

| Modelo | Descuento | Compromiso | Interrupción |
|--------|-----------|------------|--------------|
| **Reserved** | Hasta 72% | 1 o 3 años | No |
| **Spot** | Hasta 90% | Ninguno | Sí (puede terminar) |
| **Savings Plans** | Hasta 72% | 1 o 3 años (flexibilidad) | No |

---

## 📊 Dominio por Dominio

### 1. Conceptos de Nube (24%)

**Enfócate en:**
- ✅ 6 ventajas de la nube
- ✅ CAPEX vs OPEX
- ✅ Modelos: IaaS, PaaS, SaaS
- ✅ Infraestructura global (Regiones, AZs, Edge Locations)
- ✅ Well-Architected Framework (6 pilares)

**Preguntas típicas:**
- "¿Cuál es una ventaja de la nube?"
- "¿Qué significa escalabilidad?"
- "¿Cuál es la diferencia entre alta disponibilidad y tolerancia a fallos?"

---

### 2. Seguridad y Cumplimiento (30%)

**Enfócate en:**
- ✅ Modelo de Responsabilidad Compartida (crucial!)
- ✅ IAM (Users, Groups, Roles, Policies)
- ✅ MFA (Multi-Factor Authentication)
- ✅ Servicios de seguridad: GuardDuty, Inspector, Macie, Shield, WAF
- ✅ Encryption: KMS
- ✅ Compliance: Artifact

**Preguntas típicas:**
- "¿De qué es responsable AWS en el modelo compartido?"
- "¿Qué servicio detecta amenazas en tiempo real?"
- "¿Cómo dar permisos a una aplicación en EC2?"

!!! warning "Crucial para el Examen"
    El **Modelo de Responsabilidad Compartida** aparece MUCHO. Memoriza:
    - **AWS**: Seguridad DE la nube (hardware, facilities, red)
    - **Cliente**: Seguridad EN la nube (datos, IAM, encriptación, SO)

---

### 3. Tecnología y Servicios (34%)

**Enfócate en:**
- ✅ Compute: EC2, Lambda, ECS/EKS, Elastic Beanstalk
- ✅ Storage: S3, EBS, EFS, Glacier
- ✅ Databases: RDS, DynamoDB, ElastiCache, Redshift
- ✅ Networking: VPC, Subnets, Route 53, CloudFront, ELB
- ✅ Analytics: Athena, EMR, Kinesis
- ✅ Migration: DMS, DataSync, Snow Family
- ✅ ML: SageMaker, Rekognition, Comprehend

**Preguntas típicas:**
- "¿Qué servicio usar para...?"
- "¿Cuál es serverless?"
- "¿Qué base de datos para...?"

---

### 4. Facturación y Precios (12%)

**Enfócate en:**
- ✅ Modelos de precios (On-Demand, Reserved, Spot, Savings Plans)
- ✅ Free Tier
- ✅ Herramientas: Cost Explorer, Budgets, Cost & Usage Reports
- ✅ Support Plans (Basic, Developer, Business, Enterprise)
- ✅ Trusted Advisor
- ✅ Consolidación de facturación (AWS Organizations)

**Preguntas típicas:**
- "¿Cómo reducir costos?"
- "¿Qué plan de soporte incluye...?"
- "¿Qué herramienta para monitorear gastos?"

---

## 🎓 Últimos Consejos

### Semana Antes del Examen

- [ ] Repasa el **Modelo de Responsabilidad Compartida**
- [ ] Revisa casos de uso de cada servicio principal
- [ ] Haz al menos 2 exámenes de práctica completos
- [ ] Identifica tus áreas débiles y refuérzalas
- [ ] Lee las preguntas de muestra oficiales de AWS

### Día del Examen

- Descansa bien la noche anterior
- Lee cada pregunta COMPLETA antes de responder
- Si dudas, elimina opciones y escoge la mejor restante
- Gestiona tu tiempo (≈1.4 min por pregunta)
- No dejes preguntas en blanco

### Durante el Examen

!!! tip "Estrategia de Eliminación"
    Si dudas entre opciones:
    
    1. Elimina las claramente incorrectas
    2. Entre las restantes, elige la más **simple** y **económica**
    3. AWS suele favorecer soluciones managed/serverless sobre auto-gestionadas
    4. Cuando hable de seguridad, elige la opción MÁS segura

---

## 📚 Recursos de Práctica

- **Oficiales AWS**: [Preguntas de Muestra](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Sample-Questions.pdf)
- **AWS Skill Builder**: Examen de práctica oficial ($20)
- **Tutorialsdojo**: Exámenes de práctica muy similares al real
- **Udemy**: Cursos de Stephane Maarek o Neal Davis
- **Whizlabs**: Simuladores de examen

---

## ✅ Checklist Final

Antes de programar tu examen, asegúrate de poder:

- [ ] Explicar las 6 ventajas de AWS Cloud
- [ ] Diferenciar IaaS, PaaS y SaaS
- [ ] Explicar el Modelo de Responsabilidad Compartida
- [ ] Conocer los servicios principales de cada categoría
- [ ] Identificar cuándo usar S3 vs EBS vs EFS
- [ ] Entender IAM (Users, Groups, Roles, Policies)
- [ ] Conocer los modelos de precios de EC2
- [ ] Explicar los 6 pilares del Well-Architected Framework
- [ ] Diferenciar CloudWatch vs CloudTrail
- [ ] Conocer las diferencias entre planes de soporte

---

## 🎉 Después del Examen

- Resultados disponibles **inmediatamente** (Pass/Fail)
- Score detallado disponible en 5 días laborables
- Certificado digital disponible en tu cuenta AWS Certification
- Válido por **3 años**

---

¡Mucha suerte!