# IAM (Identity and Access Management)
IAM es el servicio de AWS que permite **gestionar identidades y controlar el acceso** a los recursos de AWS de forma segura.

Controla:
- Quién puede acceder (identidad)
- A qué recursos puede acceder
- Qué acciones puede realizar

Equivalente en Azure: **Microsoft Entra ID (Azure AD) + RBAC**

---

## Características principales de IAM
- Servicio **global** (no depende de una región).
- Integración nativa con todos los servicios de AWS.
- Basado en el principio de **menor privilegio**.
- Autenticación y autorización centralizadas.

---

## Componentes principales de IAM
### Usuarios IAM
- Representan personas o aplicaciones
- Tipos de acceso:

> - Acceso a consola (usuario + contraseña)

> - Acceso programático (Access Key + Secret Key)

- No se recomienda usar el **usuario root** para tareas diarias.

Equivalente en Azure: **Usuarios de Entra ID**

---

### Grupos IAM
- Colecciones de usuarios IAM.
- Los permisos se asignan al grupo, no al usuario.
- Facilitan la administración de permisos.

Ejemplos:
- Admins
- Developers
- ReadOnly

Equivalente en Azure: **Grupos de Entra ID**

---

### Roles IAM
- Identidades que no pertenecen a una persona concreta.
- Se asumen de forma **temporal**.
- Muy utilizados por servicios AWS y acceso entre cuentas.

**Casos de uso**:
- EC2 accede a S3 sin credenciales.
- Lambda accede a DynamoDB.
- Acceso cross-account.

Equivalente en Azure: **Managed Identities**

---

### Políticas IAM
- Definen los permisos.
- Escritas en formato **JSON**.
- Se pueden asociar a:
> - Usuarios
> - Grupos
> - Roles

**Tipos de políticas**:
- AWS Managed Policies
- Customer Managed Policies
- Inline Policies (menos recomendadas)

Equivalente en Azure: **RBAC Roles + Azure Policy (parcial)**

---

## Estructura básica de una política IAM
**Una política define**:
- Effect: Allow o Deny
- Action: acciones permitidas
- Resource: recursos afectados

---

## Autenticación en IAM
- Usuario + contraseña → acceso a la consola.
- Access Key + Secret Key → acceso por CLI / SDK / API.
- Roles → credenciales temporales (recomendado).

**Buenas prácticas**:
- Evitar Access Keys en usuarios.
- Usar roles siempre que sea posible.

---

## Seguridad en IAM
### Root User
- Tiene acceso total a la cuenta.
- Usar solo para:
> - Crear la cuenta
> - Configuraciones críticas

- Recomendaciones:
> - Activar MFA
> - No usar para tareas diarias

---

### MFA (Multi-Factor Authentication)
- Añade una capa extra de seguridad.
- Recomendado para:
> - Root user
> - Usuarios con permisos elevados

Equivalente en Azure: **MFA en Entra ID**

---

## Buenas prácticas de IAM (examen)
- Principio de menor privilegio.
- Usar roles en lugar de credenciales embebidas.
- Habilitar MFA.
- No compartir usuarios.
- Revisar permisos periódicamente.

---

## IAM y AWS Organizations
- IAM gestiona identidades dentro de una cuenta.
- AWS Organizations permite aplicar \*\*SCPs\*\* (Service Control Policies).
- Los SCPs no conceden permisos, \*\*solo los restringen\*\*.

Equivalente en Azure:
- Organizations + SCPs ↔ Management Groups + Azure Policy

---

## Claves de examen
- IAM es un servicio global.
- Los roles usan credenciales temporales.
- Las políticas definen permisos.
- Root user ≠ usuario IAM.
- MFA mejora la seguridad.
- Los SCPs limitan permisos incluso si IAM los permite.