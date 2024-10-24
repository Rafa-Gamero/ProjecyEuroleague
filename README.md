# Proyecto de Predicción de Resultados en la Euroliga y Análisis de Exposición de Marca

## Descripción del Proyecto

Este proyecto tiene dos componentes principales:

1. **Predicción de Resultados en la Euroliga:** Utilizamos datos históricos de partidos y estadísticas de jugadores para construir un modelo predictivo que determine el equipo con mayores probabilidades de ganar la Euroliga en la próxima temporada.
  
2. **Análisis de Exposición de Marca y Retorno de Inversión (ROI):** Evaluamos el impacto de un patrocinio deportivo sobre equipos de la Euroliga, considerando métricas como exposición mediática, audiencia, rendimiento deportivo y retorno financiero indirecto.

## Objetivos

- **Desarrollar un modelo de machine learning** que prediga qué equipo tiene más probabilidades de ganar la Euroliga.
- **Analizar el retorno de inversión (ROI)** de un patrocinio deportivo mediante Power BI, basándonos en datos de exposición mediática y rendimiento deportivo.
- Presentar un dashboard en **Power BI** con métricas clave sobre la exposición de marca y el rendimiento de los equipos de la Euroliga.

## Datos Utilizados

### 1. **Datos de Partidos de la Euroliga (2023):**
   - Tablas de estadísticas por partido y jugadores.
   - Datos de enfrentamientos directos (`head_to_head`).
   - Variables clave:
     - `team_id_a`, `team_id_b`: Identificadores de los equipos.
     - `points_a`, `points_b`: Puntuación final de los equipos.
     - `rebounds`, `assists`, `steals`, `blocks`, etc.: Estadísticas por jugador.
     - `team_a_win`, `team_b_win`: Indicadores de victoria por equipo.

### 2. **Datos de Exposición de Marca y Medios:**
   - Datos de audiencia y exposición mediática de los equipos patrocinados.
   - Información sobre patrocinios, contratos y métricas de rendimiento financiero.

## Procesos Realizados

### 1. **Análisis Exploratorio de Datos (EDA):**
   - Limpieza de datos, eliminación de valores nulos y duplicados.
   - Transformación de variables (formato de fechas, edades y columnas categóricas).
   - Análisis de tendencias de rendimiento de los equipos y jugadores.

### 2. **Modelado Predictivo:**
   - Utilización de modelos de machine learning como:
     - **KNN**: Para predecir el equipo ganador en función de estadísticas históricas.
     - **Random Forest** y **Gradient Boosting**: Para mejorar la precisión de las predicciones.
   - Variables clave: puntuaciones, asistencias, rebotes, robos, pérdidas, eficiencia ofensiva y defensiva.


### 3. **Análisis de Exposición de Marca en Power BI:**
   - Creación de un dashboard dinámico con métricas clave, incluyendo:
     - Exposición mediática (alcance de redes sociales, transmisiones televisivas, menciones en medios).
     - Rendimiento deportivo (victorias, estadísticas clave).
     - ROI financiero basado en la inversión en patrocinios y la exposición obtenida.
     - Evaluación de riesgos y oportunidades del patrocinio.
   - Uso de filtros y segmentaciones para permitir análisis interactivo.

## Herramientas Utilizadas

- **Python (Pandas, Scikit-learn, Matplotlib, Seaborn):** Para el análisis exploratorio de datos y la creación de modelos predictivos.

- **Power BI:** Para el análisis de exposición de marca y la creación de dashboards dinámicos y visuales.

## Resultados

- Se logró un modelo predictivo con una precisión aceptable para predecir el equipo más probable en ganar la Euroliga.
- El análisis de exposición de marca mostró un ROI positivo para el patrocinador, con métricas claras de rendimiento deportivo y mediático.
  
## Conclusiones

- El análisis de los datos deportivos puede ser una herramienta poderosa para predecir el éxito en competiciones, y combinarlo con análisis de exposición de marca ayuda a maximizar la efectividad de los patrocinios.
- La aplicación de técnicas de machine learning y la visualización dinámica con Power BI permiten obtener insights clave que pueden ayudar a la toma de decisiones estratégicas.

## Próximos Pasos

- Mejorar el modelo predictivo agregando más datos históricos y ajustando hiperparámetros.
- Profundizar en el análisis de audiencia para identificar patrones de comportamiento en los aficionados de la Euroliga.
- Implementar más funcionalidades en la aplicación de Streamlit, como predicciones para múltiples equipos y diferentes escenarios.

## Instrucciones para Ejecutar el Proyecto

### Requisitos:
- Python 3.8+
- Power BI Desktop
- Bibliotecas de Python:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  



### Ver el Dashboard en Power BI:
1. Abrir el archivo `.pbix` en Power BI Desktop.
2. Interactuar con los filtros y segmentaciones para analizar la exposición de marca.

## Contacto

**Rafael Gamero Arrabal**  
  
[LinkedIn: Rafael Gamero Arrabal](https://www.linkedin.com/in/rafael-gamero-arrabal-619200186/)   
