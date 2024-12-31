# ETL Pipeline Básica

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para extraer datos climáticos de la API de OpenWeather, transformarlos en un formato estructurado y cargarlos en una base de datos relacional.

## Características
- **Extracción**: Obtención de datos climáticos actuales desde la API de OpenWeather.
- **Transformación**: Limpieza y normalización de los datos en un formato tabular utilizando pandas.
- **Carga**: Inserción de los datos transformados en una base de datos SQL (SQLite o PostgreSQL).

## Tecnologías Utilizadas
- **Lenguaje**: Python 3.8+
- **Base de Datos**: SQLite o PostgreSQL
- **Bibliotecas Clave**:
  - `requests` para la interacción con la API.
  - `pandas` para la transformación de datos.
  - `sqlalchemy` para la conexión con la base de datos.

## Requisitos Previos
- Tener una API Key de OpenWeather. Puedes registrarte [aquí](https://openweathermap.org/api).
- Tener Python 3.8+ instalado en tu sistema.
- Configurar un entorno virtual (opcional pero recomendado).

## Instalación
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/etl-pipeline-basica.git
   cd etl-pipeline-basica
