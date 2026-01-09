# Bases de datos en AWS

Servicios de bases de datos totalmente administrados para distintos tipos de cargas de trabajo.

---

## Bases de datos relacionales

### Amazon RDS (Relational Database Service)

Servicio administrado de bases de datos relacionales.

Motores soportados:
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- SQL Server

Equivalente en Azure:
- Azure SQL Database (SQL Server)
- Azure Database for MySQL
- Azure Database for PostgreSQL
- Azure Database for MariaDB

---

## Base de datos relacional cloud-native

### Amazon Aurora

Base de datos relacional **optimizada y gestionada por AWS**.

- Compatible con MySQL y PostgreSQL.
- Mayor rendimiento y escalabilidad que RDS estándar.
- Alta disponibilidad por defecto.

Equivalente en Azure:
- No hay equivalente directo 1:1.
- Se aproxima con **Azure SQL Hyperscale**.

---

## Base de datos NoSQL

### Amazon DynamoDB

Base de datos NoSQL **serverless** de clave-valor.

- Escala automáticamente.
- Alta disponibilidad.
- Baja latencia.

Equivalente en Azure:
- **Azure Cosmos DB**

---

## Data Warehouse

### Amazon Redshift

Servicio de **almacenamiento y análisis de datos a gran escala** (OLAP).

- Orientado a analítica.
- Consultas complejas sobre grandes volúmenes de datos.

Equivalente en Azure:
- **Azure Synapse Analytics**

---

## Caché en memoria

### Amazon ElastiCache

Servicio de caché en memoria totalmente administrado.

Motores:
- Redis
- Memcached

Equivalente en Azure:
- **Azure Cache for Redis**

---

## Base de datos gráfica

### Amazon Neptune

Base de datos **orientada a grafos**.

- Ideal para relaciones complejas.
- Casos de uso: redes sociales, fraude, recomendaciones.

Equivalente en Azure:
- **Azure Cosmos DB (API Gremlin)**

---

## Análisis de series temporales (Time Series)

### Amazon Timestream

Base de datos diseñada para **datos de series temporales**.

- Métricas
- IoT
- Eventos en el tiempo

Equivalente en Azure:
- **Azure Data Explorer**

---

## Claves de examen

- RDS = relacional gestionado.
- Aurora = relacional optimizado por AWS.
- DynamoDB = NoSQL serverless.
- Redshift = analítica / data warehouse.
- ElastiCache = caché en memoria.
- Neptune = grafos.
- Timestream = series temporales.