# AWS Organizations

Servicio para la **gestión multi-cuenta** en AWS.

Equivalente en Azure: **Management Groups + Azure Policy**

---

## Qué hace AWS Organizations

- Centraliza la gestión de múltiples cuentas AWS.
- Permite consolidar la facturación.
- Aplica políticas de control a nivel organizativo.

---

## Service Control Policies (SCPs)

- Definen **qué está permitido a nivel máximo**.
- No conceden permisos, solo los restringen.
- Se aplican a cuentas u OU (Organizational Units).

---

## Casos de uso

- Separación de entornos (prod, dev, test).
- Control de costes.
- Gobierno centralizado.

---

## Claves de examen

- Gestión multi-cuenta.
- SCP ≠ IAM Policy.
- SCP limita incluso si IAM permite.