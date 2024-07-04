# Life_expectancy_semantic_Project




## Getting started
 - Everything i done using ontop and protege and my all files in semantic_project --> ontop --> every file in there...

## Life Expectancy and Health Indicators Analysis
This project provides an in-depth analysis of life expectancy and various health indicators using data sourced from the World Health Organization and Kaggle. The project aims to create a comprehensive data processing pipeline that transforms raw data into both SQL and RDF formats, facilitating efficient querying and analysis.

## Table of Contents

1. Introduction
2. Data Sources
3. SQL Schema and Data Import
4. Data Processing
5. RDF and Ontology
6. Flask Application for SPARQL Queries
7. Conclusion
8. Appendices


## Introduction
This project explores the integration of different data sources, processing techniques, and tools to generate meaningful insights. The data is standardized and processed using SQL for relational storage and RDF for semantic querying, allowing for flexible data interaction and analysis. The project also leverages Ontop for efficient data transformation and querying.

## Data Sources


### WHO National Life Expectancy Data (who_life_exp.csv)


### Source: Kaggle Life Expectancy Dataset


## Description: Contains information about life expectancy at the national level, including various health indicators.



## Relay World Health Statistics (RELAY_WHS.csv)


### Source: WHO Country Data


## Description: Includes various health statistics for different countries, covering a range of indicators.



## Modified Relay World Health Statistics (relay_whs_modified.csv)


## Source: Generated from the original RELAY_WHS.csv


## Description: Includes a combined indicator column for easier querying and analysis.




## SQL Schema and Data Import

SQL Tables
life_expectancy Table Schema:

DROP TABLE IF EXISTS life_expectancy;

CREATE TABLE life_expectancy (
    Country VARCHAR(100),
    country_code VARCHAR(10),
    region VARCHAR(100),
    Year INT,
    Life_Expectancy FLOAT,
    life_exp60 FLOAT,
    Adult_Mortality FLOAT,
    Infant_Deaths FLOAT,
    age1_4mort FLOAT,
    alcohol FLOAT,
    bmi FLOAT,
    age5_19thinness FLOAT,
    age5_19obesity FLOAT,
    hepatitis FLOAT,
    measles FLOAT,
    polio FLOAT,
    diphtheria FLOAT,
    basic_water FLOAT,
    doctors FLOAT,
    hospitals FLOAT,
    gni_capita FLOAT,
    gghe_d FLOAT,
    che_gdp FLOAT,
    une_pop FLOAT,
    une_infant FLOAT,
    une_life FLOAT,
    une_hiv FLOAT,
    une_gni FLOAT,
    une_poverty FLOAT,
    une_edu_spend FLOAT,
    une_literacy FLOAT,
    une_school FLOAT
);





**`relay_whs` Table Schema:**
```sql

DROP TABLE IF EXISTS relay_whs;

CREATE TABLE relay_whs (
    Country VARCHAR(100),
    IND_NAME VARCHAR(100),
    DIM_SEX VARCHAR(10),
    Value FLOAT,
    Indicator VARCHAR(200)
);


## Data Import Instructions

1. Ensure CSV Files Are Accessible:
    Place your CSV files (who_life_exp.csv and RELAY_WHS.csv) in a location accessible by the psql client.

2. Run the psql Client:
    Open your terminal and start the psql session for your health_data database:


**psql -U healthuser -d health_data**

3. Create the Tables:
    Copy and paste the updated table schema commands into your psql session and execute them.

4. Import Data:
    Use the \copy command to import data from the CSV files:

**
\copy life_expectancy(Country, country_code, region, Year, Life_Expectancy, life_exp60, Adult_Mortality, Infant_Deaths, age1_4mort, alcohol, bmi, age5_19thinness, age5_19obesity, hepatitis, measles, polio, diphtheria, basic_water, doctors, hospitals, gni_capita, gghe_d, che_gdp, une_pop, une_infant, une_life, une_hiv, une_gni, une_poverty, une_edu_spend, une_literacy, une_school) FROM '/full/path/to/who_life_exp.csv' DELIMITER ',' CSV HEADER;
**

** \copy relay_whs(Country, IND_NAME, DIM_SEX, Value) FROM '/full/path/to/RELAY_WHS.csv' DELIMITER ',' CSV HEADER; **

**
-- Combine IND_NAME and DIM_SEX to form the Indicator column
UPDATE relay_whs
SET Indicator = CONCAT(IND_NAME, '_', DIM_SEX); **


## RDF and Ontology

## RDF Datasets
 - life_expectancy_rdf_dataset.ttl
 - relay_whs_rdf_dataset.ttl

## Ontology and Mapping Files
 - life_expectancy_mapping.ttl
 - mapping.obda
 - mapping.ttl
 - ontology2.ttl
 - rdf-dataset.ttl
 - relay_whs_mapping.ttl

## Generating RDF Dataset
 
 1. Generate Direct Mapping Using Ontop CLI:
     ./ontop bootstrap -m mapping.obda -p basic.properties -t ontology.ttl -b http://example.org/

 2. Convert OBDA Mapping to R2RML:
     ./ontop mapping to-r2rml -p basic.properties -i mapping.obda -o mapping.ttl

 3. Materialize Data into RDF Format:
     ./ontop materialize -m life_expectancy_mapping.ttl -p basic.properties -t ontology1.ttl -o life_expectancy_rdf_dataset.ttl -f turtle
     ./ontop materialize -m relay_whs_mapping.ttl -p basic.properties -t ontology1.ttl -o relay_whs_rdf_dataset.ttl -f turtle


## Querying RDF Dataset
   - Use the Ontop CLI and flask app to run SPARQL queries:

   ./ontop query -m life_expectancy_mapping.ttl -p basic.properties -t ontology1.ttl -q query1_list_countries.sparql
   ./ontop query -m relay_whs_mapping.ttl -p basic.properties -t ontology1.ttl -q query11_indicator_and_their_values.sparql



## Flask Application for SPARQL Queries
   # Overview
     -  The Flask-based web application provides a user-friendly interface for performing SPARQL queries on the RDF datasets. It loads the RDF datasets and executes SPARQL queries submitted via the web form.   

## Workflow
    1. Home Page: Displays a form where users can enter their SPARQL queries.
    2. Form Submission: Processes the query and executes it against the RDF datasets.
    3. Query Execution: Uses RDFlib to parse the RDF data and execute the SPARQL query.
    4. Result Rendering: Renders the results in an HTML table.

     - python app.py





## Conclusion
  - In this project, we developed a comprehensive system for analyzing life expectancy and health indicators using data from the World Health Organization and Kaggle. We successfully transformed the data into SQL and RDF formats and built a web application to facilitate SPARQL querying. This project demonstrates the power of combining SQL and RDF to create flexible and efficient data analysis workflows.
