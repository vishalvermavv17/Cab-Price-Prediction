# Data Science Project Report : Machine Learning regression problem of Cab fare prediction.
This file contains information about project being executed in this case 'Cab fare prediction'. It is organized according to the Team Data Science Process (TDSP) [Lifecycle stages](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/lifecycle-detail.md).
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

## 3. **Modeling**

### Feature Engineering
**Data cleanup: Removing columns and rows**
We have performed feature engineering on random sub-sample without replacing of given data set having 1.2 million rows (~10%) because given dataset is quite large and can be sufficiently represented with sub-sample.

We have performed validation checks on each sample and removed samples that violates the validation condition. Below are the mentioned validations performed on training dataset.
1. fare amount > $0 and fare amount <= $500
2. passenger count > 0
3. valid range is -90 to 90 for latitude and -180 to 180 for longitude
4. pickup and dropoff geolocations should be different
5. harvensine distance between two geolocation should be >= 1km

**Feature creation from pickup datetime variable**
Pickup datetime variable is distributed into sub variable like day_of_week, minute, hr_of_day, month, year, day.

**Haversine distance**
Feature engineered a h_distance variable using haversine formula that computes distance between pickup and dropoff geolocations for each sample.

**Saving processed data sets for modeling input**
Training and test data sets were stored in feather file format and saved as .feather files for input into modeling (training data), and model evaluation or deployment (test data). We chose feather file format as these are light weight and fast on-disk file format especially to store dataframes.

### Modeling training
We created Random Forest regressor model with 3-fold cross-validation. We used [HyperOpt](http://hyperopt.github.io/hyperopt/) for  as a strategy for cross-validation. 

### Model evaluation
Performance of the models were measured using [RMSE](https://en.wikipedia.org/wiki/Root-mean-square_deviation) on the test data set. RMSE of Random Forest models were < 3.4. We saved model in pickled.pkl files, and output the RMSE validation score for model. In addition, for model interpretation, feature importance for the Random Forest model are output in a .csv file and plotted below. 

Importance of features from the Random Forest model is shown below:

![feature_importance](https://user-images.githubusercontent.com/20114106/200174871-499bddca-3f17-4404-acb8-3186a85b7b73.png)

## 4. **Deployment**
We deployed the Random Forest Model. Deployment is performed using Heroku App Services using github workflows. 
Here is a webapp link to use prediction service.
[`https://cab-fare-prediction-v1.herokuapp.com/`](https://cab-fare-prediction-v1.herokuapp.com/)

## Version Control Repository
An empty Git repository is needed to version control contents of this project. 

#### Deployment
Service is run in the Azure Container Service (ACS). The operationalization environment provisions Docker and Kubernetes in the cluster to manage the web service deployment.

#### Code Execution
Executing a Flask server in Docker environment is easy:

 ```
 docker build -t cab-fare-prediction .
 
 docker run -p 5000:5000 cab-fare-prediction
 ```

IPython notebook files can be double-clicked from the project structure and run in the Jypyter Notebook Server.
