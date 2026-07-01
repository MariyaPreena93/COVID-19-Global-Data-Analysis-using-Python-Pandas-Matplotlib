# COVID-19 Global Data Analysis using Python, Pandas & Matplotlib

## Project Overview

This project analyzes a real-world COVID-19 dataset using **Python**, **Pandas**, and **Matplotlib**. It demonstrates data cleaning, transformation, aggregation, and visualization techniques commonly used in ETL and data analysis workflows.

The analysis includes continent-wise case summaries, country-level statistics, trend analysis, and multiple visualizations to better understand the spread and impact of COVID-19.

---

## Technologies Used

* Python 3
* Pandas
* Matplotlib

---

## Dataset

The dataset contains global COVID-19 statistics with columns such as:

* ISO Code
* Continent
* Country (Location)
* Date
* Total Cases
* New Cases
* Total Deaths
* New Deaths
* Total Tests
* New Tests
* Total Vaccinations
* People Vaccinated
* Median Age
* Population Statistics

---

## Features

### Data Cleaning

* Removed duplicate records.
* Removed records with missing continent, location, or date values.
* Converted the **date** column to datetime format.
* Converted numeric columns using `pd.to_numeric()` with `errors="coerce"`.

### Data Analysis

* Total COVID-19 cases by continent.
* Top 10 countries by total confirmed cases.
* Top 10 countries by total deaths.
* Monthly COVID-19 new case trend in Canada.
* Daily death trend in India.
* Scatter plot comparing total cases and total deaths.
* Dataset summary before and after cleaning.

### Data Visualization

* Bar Chart
* Horizontal Bar Chart
* Line Chart
* Scatter Plot

---

## Project Workflow

1. Read the CSV dataset.
2. Clean and validate the data.
3. Convert data types.
4. Perform aggregations using Pandas.
5. Create visualizations using Matplotlib.
6. Display summary statistics.

---

## Visualizations Included

* COVID-19 Total Cases by Continent
* Top 10 Countries by Total Cases
* Top 10 Countries by Total Deaths
* Monthly New Cases Trend in Canada
* Daily Death Trend in India
* Total Cases vs Total Deaths Scatter Plot

---

## Key Pandas Concepts Used

* `read_csv()`
* `drop_duplicates()`
* `dropna()`
* `groupby()`
* `sort_values()`
* `nlargest()`
* `to_numeric()`
* `to_datetime()`
* `.dt.to_period()`
* Boolean Filtering
* Aggregation Functions

---

## Key Matplotlib Concepts Used

* `plt.figure()`
* `plt.bar()`
* `plt.barh()`
* `plt.plot()`
* `plt.scatter()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.title()`
* `plt.xticks()`
* `plt.show()`

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Cleaning real-world datasets
* Working with date and time data in Pandas
* Handling missing and duplicate records
* Data aggregation using `groupby()`
* Trend analysis using time-series data
* Creating informative charts with Matplotlib
* Building an end-to-end data analysis workflow

---

## Future Enhancements

* Add pie charts for continent-wise case distribution.
* Analyze vaccination trends by country and continent.
* Calculate case fatality and recovery rates.
* Export summary reports to CSV or Excel.
* Build an interactive dashboard using Plotly or Power BI.
* Load cleaned data into a MySQL database for reporting.

---

## Sample Output

* Total records before and after data cleaning
* Total COVID-19 cases by continent
* Top 10 countries by confirmed cases
* Top 10 countries by deaths
* Monthly COVID-19 trends
* Daily death trends
* Scatter plot showing the relationship between total cases and total deaths

---

## Skills Demonstrated

* Python Programming
* Data Cleaning
* Data Transformation
* Exploratory Data Analysis (EDA)
* Data Visualization
* Time-Series Analysis
* Pandas
* Matplotlib
* Analytical Thinking

---

## Author

**Mariya Preena**

This project is part of my Python and Data Analytics portfolio, showcasing practical skills in data cleaning, analysis, and visualization using real-world datasets.
