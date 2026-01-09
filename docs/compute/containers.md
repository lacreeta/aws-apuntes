## Contenedores en AWS

Los contenedores permiten ejecutar aplicaciones empaquetadas con sus dependencias de forma consistente.

AWS ofrece varios servicios para contenedores.

---

## Amazon ECS (Elastic Container Service)

Servicio administrado para **ejecutar y orquestar contenedores Docker**.

No requiere gestionar Kubernetes.

---

### Características principales de ECS

- Integración nativa con AWS.
- Puede ejecutarse sobre:
  - EC2
  - Fargate (serverless)

---

### Casos de uso ECS

- Microservicios.
- Aplicaciones containerizadas.
- Workloads gestionados por AWS.

---

## Amazon EKS (Elastic Kubernetes Service)

Servicio administrado de **Kubernetes** en AWS.

Equivalente en Azure: **Azure Kubernetes Service (AKS)**

---

### Características principales de EKS

- Kubernetes estándar.
- Alta disponibilidad del plano de control.
- Integración con servicios AWS.

---

### Casos de uso EKS

- Orquestación avanzada.
- Portabilidad entre nubes.
- Entornos Kubernetes estándar.

---

## AWS Fargate

AWS Fargate permite ejecutar contenedores **sin gestionar servidores**.

Es un modelo **serverless para contenedores**.

Equivalente en Azure: **Azure Container Instances (ACI)**

---

### Características principales de Fargate

- No se gestionan instancias EC2.
- Escalado automático.
- Pago por uso.

---

### Claves de examen contenedores

- ECS = orquestación propia de AWS.
- EKS = Kubernetes.
- Fargate = contenedores sin servidores.
- Fargate puede usarse con ECS y EKS.