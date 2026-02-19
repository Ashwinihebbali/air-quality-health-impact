
# 🌍 Air Quality Health Impact Prediction System

Professional data project for exploring associations between air pollution and health outcomes. This repository includes a Streamlit dashboard for interactive exploration, a Jupyter notebook with reproducible analysis, and the dataset used for demonstrations.

view Streamlit App here 👉 https://air-quality-health-impact-paqj6wjwnob2zfc5wssav2.streamlit.app/

Overview:
- Objective: Provide tools to explore, visualize, and model relationships between air quality indicators (e.g., PM2.5, NO2) and health metrics (e.g., respiratory hospitalizations, mortality) using a single, shareable dataset.
- Audience: data scientists, public-health analysts, policy researchers, and educators who need an interactive demo and reproducible analysis.

Features:
- Interactive Streamlit dashboard for filtering, plotting, and summarizing the dataset.
- Exploratory Data Analysis and example modeling workflow in `Air_quality_Health_Impact.ipynb`.
- Minimal, reproducible environment described in `requirements.txt`.

Repository structure:
- `app.py` — Streamlit application (dashboard and visualizations).
- `Air_quality_Health_Impact.ipynb` — Jupyter notebook with EDA and modeling examples.
- `air_quality_health_impact_data.csv` — Example dataset used by the app and notebook.
- `requirements.txt` — Python dependencies to reproduce the environment.
- `README.md` — This document.

Data description:
- The example dataset is `air_quality_health_impact_data.csv`. It should contain the primary variables used by the notebook and app. Typical columns the project expects (adjust to your real data):
	- `date` — observation date (YYYY-MM-DD)
	- `location` — geographic unit (city/region)
	- `pm25` — PM2.5 concentration (µg/m³)
	- `no2` — NO2 concentration (ppb)
	- `ozone` — O3 concentration (ppb)
	- `resp_hosp` — respiratory hospitalizations (count)
	- `population` — population for rate calculations




