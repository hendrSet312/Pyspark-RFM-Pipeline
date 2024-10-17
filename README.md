# Pyspark-RFM-Pipeline

This project implements an RFM (Recency, Frequency, Monetary) analysis using PySpark, with data sourced from a PostgreSQL database hosted on Supabase. The pipeline includes data extraction, transformation, and loading processes.

## Project Structure

  - setup.py - Contains database connection details and configuration settings.
  - extract.py - Extracts data from the PostgreSQL database using JDBC.
  - transform.py - Processes the extracted data to calculate RFM metrics.
  - load.py - Writes the transformed data back to the database.
  - main.py - Orchestrates the entire pipeline by executing extract, transform, and load operations.

## Requirements
  - PySpark
  - PostgreSQL JDBC Driver
  - Supabase Account
  - Python 3.x
