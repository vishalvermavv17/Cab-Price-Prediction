# Data Science Project Report : Machine Learning regression problem of Cab fare prediction.
This file contains information about project being executed in this case 'Cab fare prediction'. It is organized according to the Team Data Science Process (TDSP [Lifecycle stages](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/lifecycle-detail.md).
![template_screenshot](https://user-images.githubusercontent.com/20114106/200154152-54f11b9a-7b3f-4365-b534-4a0bf772e8b1.PNG)

# 1. Business Understanding
* NOTE: This is a sample for a tutorial, so scope, plan etc., does not necessarily correspond to an actual data science project addressing a specific business question. In an actual project, the problem definition, scope, plan, personnel sections are likely to be much more detailed, based on discussions with the client (or business owner), the structure of the data science team etc.
### Problem Definition
The purpose of this project is to demonstrate the skills required to successfully execute a machine learning regression problem.

The dataset for this project is from the Kaggle competition sponsored by Google Cloud [[link]](https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction/data). The dataset contains New York city cab ride details. Based on ride features, the machine learning task is to predict the fare amount of given ride within New York city (regression problem).

### Scope
 * The scope of this project is to create a regression machine learning model which address the above prediction problem. 
 * We execute the project in Machine Learning using Sklearn library.
 * We used GPU's and CuML library to build model on large dataset (~5GB & over 55 million rows).
 * We operationalize the solution in docker Container Services for single-mode fare amount prediction.
 
 ## Plan
We follow the stages for the TDSP lifecycle, and organize documentation and code according to the stages of the lifecycle. Documentation about the work and findings in each of the lifecycle stages is included below. The code is organized into folders that follow the lifecycle stages.

### Metrics
Performance of the machine learning models will be evaluated on the test set provided by the Kaggle [[link]](https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction/data). MSE is measured and reported using RMSE. RMSE of < $5 will be considered acceptable and suitable for deployment.

## 2. [**Data Acquisition and Understanding**](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/01_data_acquisition_and_understanding)

### Raw Data
For detailed information about the data, please see the [description](https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction/data) in the Kaggle competition page.  

There are a total of 55.4 million instances (prior to any filtering), mix of continuous and discrete.

TARGET: fare_amount.

FEATURES: pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, day_of_week, minute, hr_of_day, month, year, day, h_distance.

### Data Exploration
Data exploration is performed using the Python 3 using pandas, numpy, matplotlib and seaborn library that helps to generate standardized data exploration reports for data containing numerical and categorical features and target. 

The details of data exploration and visualisation are present in project notebook and visulations are stored in visualisation directory.
