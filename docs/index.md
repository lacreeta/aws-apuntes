# AWS Certified Cloud Practitioner - Guía de Estudio

Bienvenido a esta guía de estudio para la certificación **AWS Certified Cloud Practitioner (CLF-C02)**.

Estos apuntes están organizados por dominios del examen e incluyen equivalencias con Azure para facilitar el aprendizaje si ya tienes experiencia con esa plataforma.

---

## 📋 Sobre el Examen

El examen AWS Certified Cloud Practitioner valida tu comprensión de:

- Conceptos fundamentales de la nube de AWS
- Servicios principales de AWS
- Seguridad y cumplimiento
- Facturación y precios
- Arquitecturas básicas

### Detalles del Examen

| Aspecto | Detalle |
|---------|---------|
| **Código** | CLF-C02 |
| **Duración** | 90 minutos |
| **Preguntas** | 65 (aproximadamente) |
| **Formato** | Opción múltiple y respuesta múltiple |
| **Puntaje mínimo** | 700/1000 |
| **Idiomas** | Español, Inglés, y otros |
| **Costo** | $100 USD |

---

## 📊 Dominios del Examen

El examen se divide en cuatro dominios principales:

| Dominio | Peso | Temas |
|---------|------|-------|
| **1. Conceptos de Nube** | 24% | Valor de la nube, arquitectura, economía cloud |
| **2. Seguridad y Cumplimiento** | 30% | Modelo de responsabilidad compartida, IAM, servicios de seguridad |
| **3. Tecnología y Servicios** | 34% | Servicios core (compute, storage, networking, databases) |
| **4. Facturación y Precios** | 12% | Modelos de precios, herramientas de facturación |

---

## 🗺️ Guía de Estudio Recomendada

### Semana 1-2: Fundamentos
- [ ] Leer [Introducción a AWS](introduction.md)
- [ ] Entender la [Infraestructura Global](global-infrastructure.md)
- [ ] Estudiar el [Modelo de Responsabilidad Compartida](security/shared-responsibility.md)
- [ ] Dominar [IAM](security/iam.md)

### Semana 3-4: Servicios Core
- [ ] **Compute**: [EC2](compute/ec2.md), [Lambda](compute/serverless.md), [ECS/EKS](compute/containers.md)
- [ ] **Storage**: [S3](storage/s3.md), [EBS](storage/ebs.md), [EFS](storage/efs.md)
- [ ] **Databases**: Revisar [opciones de bases de datos](databases/databases.md)
- [ ] **Networking**: [VPC](networking/vpc.md), [Route 53](networking/route-53.md), [CloudFront](networking/cloudfront.md)

### Semana 5: Seguridad y Operaciones
- [ ] Servicios de seguridad: [KMS](security/kms.md), [GuardDuty](security/guardduty.md), [Inspector](security/inspector.md)
- [ ] Monitoreo: [CloudWatch](operations/cloudwatch.md), [CloudTrail](operations/config.md)
- [ ] Infraestructura como código: [CloudFormation](operations/cloudformation.md)

### Semana 6: Facturación y Preparación Final
- [ ] [Modelos de Facturación](cost/billing.md)
- [ ] [Cost Explorer](cost/cost-explorer.md) y [Budgets](cost/budgets.md)
- [ ] [Planes de Soporte](support/support.md) y [Trusted Advisor](support/trusted-advisor.md)
- [ ] Repasar [Tips para el Examen](exam-tips.md)
- [ ] Realizar exámenes de práctica

---

## 🎯 Recursos Adicionales

### Oficiales de AWS
- [Guía del examen oficial](https://aws.amazon.com/certification/certified-cloud-practitioner/)
- [AWS Training and Certification](https://aws.amazon.com/training/)
- [AWS Skill Builder](https://skillbuilder.aws/)
- [Preguntas de muestra oficiales](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Sample-Questions.pdf)

### Práctica
- AWS Free Tier para práctica hands-on
- Simuladores de examen (Udemy, Whizlabs, TutorialsDojo)

---

## 💡 Consejos Generales

!!! tip "Enfoque del Estudio"
    - Entiende **conceptos** más que memorizar detalles técnicos
    - Conoce **cuándo usar cada servicio** (casos de uso)
    - Familiarízate con los **modelos de precios** básicos
    - El examen es de nivel **foundational**, no necesitas ser experto técnico

!!! warning "Común Confusión"
    No confundir servicios similares:
    - EBS vs EFS vs S3
    - Security Groups vs NACLs
    - IAM Roles vs IAM Users
    - CloudWatch vs CloudTrail

---

## 📚 Navegación

Usa el menú lateral para navegar por los diferentes temas. Los temas están organizados siguiendo la estructura del examen y las mejores prácticas de estudio.

¡Buena suerte con tu preparación! 