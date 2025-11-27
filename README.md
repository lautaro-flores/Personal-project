# E-commerce Data Lake en AWS (RAW → STAGE → CONSUME)

Proyecto personal de data engineering para simular el flujo analítico de un e-commerce en AWS:

- **Ingesta** de archivos CSV a S3  
- **Orquestación** con S3 Events → Lambda → Glue Workflow  
- **Transformaciones** en capas RAW / STAGE / GOLD con Glue Jobs + Crawlers  
- **Consumo** con Athena, Glue Notebooks y un pequeño módulo de **recomendaciones de productos (IA liviana)**

---

## 🎯 Objetivo del proyecto

Construir un mini data lake de e-commerce que muestre, de punta a punta:

1. **Arquitectura de datos en AWS** (capas, catálogo, orquestación).
2. Uso de **Glue** (Jobs, Crawlers, Workflows) y **Lambda** de forma event-driven.
3. Tabla CONSUME con features de clientes y productos.
4. Un módulo simple de Analítica:
---
<img width="988" height="385" alt="image" src="https://github.com/user-attachments/assets/d1734015-df9f-4f36-bc70-d847e4d93fb7" />
