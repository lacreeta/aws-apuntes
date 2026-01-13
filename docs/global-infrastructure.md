# Infraestructura Global de AWS

AWS tiene la **infraestructura global de nube más extensa y confiable** del mundo, diseñada para proporcionar alta disponibilidad, tolerancia a fallos y baja latencia.

---

## 🌍 Componentes de la Infraestructura

La infraestructura global de AWS se compone de:

1. **Regiones (Regions)**
2. **Zonas de Disponibilidad (Availability Zones - AZs)**
3. **Edge Locations (Puntos de Presencia)**
4. **Local Zones**
5. **Wavelength Zones**

---

## 📍 Regiones (Regions)

### ¿Qué es una Región?

Una **región** es un área geográfica que contiene múltiples centros de datos aislados (Availability Zones).

- Cada región es completamente **independiente** y **aislada**
- Los datos **NO se replican automáticamente** entre regiones (salvo configuración explícita)
- Actualmente hay **33+ regiones** en todo el mundo

### Ejemplos de Regiones

| Código | Nombre | Ubicación |
|--------|--------|-----------|
| `us-east-1` | US East (N. Virginia) | Virginia, EE.UU. |
| `us-west-2` | US West (Oregon) | Oregon, EE.UU. |
| `eu-west-1` | Europe (Ireland) | Irlanda |
| `ap-southeast-1` | Asia Pacific (Singapore) | Singapur |
| `sa-east-1` | South America (São Paulo) | Brasil |

### ¿Cómo Elegir una Región?

!!! tip "Factores para Elegir una Región"
    
    1. **Compliance/Cumplimiento**: Requisitos legales (ej: GDPR en Europa)
    2. **Latencia**: Proximidad a usuarios finales
    3. **Servicios Disponibles**: No todos los servicios están en todas las regiones
    4. **Costos**: Los precios varían según la región

**Ejemplo**: Si tus usuarios están en Europa, elige una región europea (eu-west-1) para reducir latencia.

---

## 🏢 Zonas de Disponibilidad (Availability Zones - AZs)

### ¿Qué es una AZ?

Una **Availability Zone** es uno o más centros de datos discretos con energía, red y conectividad redundantes dentro de una región.

### Características Clave

- Cada región tiene **mínimo 3 AZs** (generalmente 3-6)
- Las AZs están **físicamente separadas** (varios kilómetros)
- Conectadas con **redes de alta velocidad y baja latencia**
- Aisladas de fallos en otras AZs (inundación, incendio, etc.)

### Nomenclatura

- Región: `us-east-1`
- AZs dentro: `us-east-1a`, `us-east-1b`, `us-east-1c`, etc.

!!! warning "Importante"
    Las letras de AZ son **aleatorias por cuenta AWS**.
    Tu `us-east-1a` puede ser diferente físicamente al `us-east-1a` de otra cuenta.

### Alta Disponibilidad con Multi-AZ

Para lograr **alta disponibilidad**, despliega recursos en **múltiples AZs**:


Si una AZ falla, las otras siguen funcionando.

**Equivalente en Azure**: Availability Zones

---

## ⚡ Edge Locations (Puntos de Presencia)

### ¿Qué son las Edge Locations?

**Edge Locations** son puntos de presencia de AWS distribuidos globalmente que almacenan contenido en caché para reducir latencia.

### Características

- Hay **400+ Edge Locations** en más de 90 ciudades
- **Más numerosas** que las regiones
- Usadas principalmente por **CloudFront** (CDN) y **Route 53** (DNS)

### ¿Cómo Funcionan?

1. Usuario en Madrid solicita un archivo
2. CloudFront busca el archivo en la Edge Location más cercana (Madrid)
3. Si está en caché → entrega inmediata
4. Si no → descarga desde región origen y almacena en caché

**Resultado**: Latencia ultra-baja para usuarios globales

### Servicios que Usan Edge Locations

- **CloudFront**: CDN para contenido estático/dinámico
- **Route 53**: DNS global
- **AWS WAF**: Filtrado de tráfico web
- **AWS Shield**: Protección DDoS

**Equivalente en Azure**: Azure CDN, Azure Front Door

---

## 🌐 Comparación: Regiones vs AZs vs Edge Locations

| Concepto | Cantidad | Propósito | Ejemplos de Uso |
|----------|----------|-----------|-----------------|
| **Regions** | 33+ | Separación geográfica y compliance | Ejecutar EC2, alojar bases de datos |
| **Availability Zones** | 100+ | Alta disponibilidad y tolerancia a fallos | Multi-AZ para RDS, ELB entre AZs |
| **Edge Locations** | 400+ | Baja latencia global mediante caché | CloudFront, Route 53 |

---

## 🏗️ Local Zones

### ¿Qué son?

**Local Zones** extienden AWS a grandes áreas metropolitanas específicas, más cerca de usuarios finales.

### Características

- Extensión de una región cerca de poblaciones grandes
- Para aplicaciones de **latencia ultra-baja** (< 10ms)
- Subconjunto de servicios AWS disponibles

**Ejemplo**: AWS Local Zone en Los Ángeles (extensión de us-west-2)

**Caso de uso**: Gaming en tiempo real, streaming de video en vivo, workstations virtuales

---

## 📡 Wavelength Zones

### ¿Qué son?

**Wavelength Zones** integran servicios AWS dentro de redes 5G de operadores de telecomunicaciones.

### Características

- Para aplicaciones **5G de latencia ultra-baja** (< 5ms)
- Incrusta compute y storage en el borde de redes 5G
- Ideal para IoT, realidad aumentada, streaming

**Caso de uso**: Aplicaciones móviles que requieren respuesta instantánea

---

## 🔄 AWS Outposts

### ¿Qué es?

**AWS Outposts** lleva servicios AWS a tu **datacenter on-premises**.

### Características

- Hardware y software AWS instalados en tu ubicación
- Gestión unificada con AWS Cloud
- Para cargas híbridas o compliance estricto

**Equivalente en Azure**: Azure Stack

---

## 🌍 Alcance de Servicios AWS

Los servicios AWS tienen diferentes alcances:

### Servicios Globales
No dependen de región específica:

- **IAM**: Gestión de identidades
- **Route 53**: DNS
- **CloudFront**: CDN
- **WAF**: Firewall web

### Servicios Regionales
Operan dentro de una región específica:

- **EC2**: Compute
- **S3**: Storage (buckets son regionales)
- **RDS**: Bases de datos
- **Lambda**: Funciones serverless

!!! tip "Para el Examen"
    Conoce qué servicios son **globales** vs **regionales**.
    Pista: Los de **networking global** (CloudFront, Route 53) y **seguridad/identidad** (IAM) son globales.

---

## 🎯 Diseño para Alta Disponibilidad

### Buenas Prácticas

1. **Multi-AZ**: Despliega en al menos 2 AZs
2. **Multi-Region**: Para disaster recovery crítico
3. **CloudFront**: Distribuye contenido globalmente
4. **Route 53**: Enrutamiento basado en salud y latencia


---

## 📊 Tolerancia a Fallos vs Alta Disponibilidad

### Alta Disponibilidad (High Availability)
- Sistema disponible la mayor parte del tiempo
- **Minimiza downtime** pero puede tener interrupciones breves
- Ejemplo: Multi-AZ deployment

### Tolerancia a Fallos (Fault Tolerance)
- Sistema continúa operando **sin interrupción** ante fallos
- **Zero downtime** incluso con fallos de componentes
- Ejemplo: Multi-region con failover automático

!!! tip "Para el Examen"
    - **Alta Disponibilidad** = Multi-AZ
    - **Tolerancia a Fallos** = Multi-Region + Failover automático

---

## 🔍 Servicios por Alcance: Resumen

### Globales
- IAM
- Route 53
- CloudFront
- WAF
- Shield

### Regionales
- EC2
- Lambda
- RDS
- S3 (buckets son regionales)
- VPC
- ELB
- DynamoDB

### AZ-Específicos
- Subnets
- Instancias EC2 individuales
- Volúmenes EBS

---

## 💡 Ejemplos para el Examen

**Pregunta**: "Una empresa quiere garantizar que su aplicación siga funcionando incluso si un datacenter falla completamente. ¿Qué debe hacer?"

**Respuesta**: Desplegar en **múltiples Availability Zones**

---

**Pregunta**: "¿Qué servicio AWS reduce la latencia para usuarios globales almacenando contenido en caché?"

**Respuesta**: **CloudFront** (usa Edge Locations)

---

**Pregunta**: "¿Qué componente de infraestructura AWS contiene múltiples centros de datos con energía y red redundantes?"

**Respuesta**: **Availability Zone (AZ)**

---

## 📚 Recursos Adicionales

- [Mapa de Infraestructura Global de AWS](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)

---

!!! success "Checklist para el Examen"
    - [ ] Entiendo qué es una Región y cómo elegirla
    - [ ] Sé qué es una Availability Zone y su propósito
    - [ ] Conozco las Edge Locations y qué servicios las usan
    - [ ] Entiendo Multi-AZ vs Multi-Region
    - [ ] Puedo diferenciar servicios globales vs regionales
    - [ ] Comprendo Alta Disponibilidad vs Tolerancia a Fallos

---

Siguiente tema recomendado: [Modelo de Responsabilidad Compartida](security/shared-responsibility.md)
