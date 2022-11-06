TRAINED_MODEL_NAME = "rf_model.pkl.gz"

TARGET_LABEL = ['fare_amount']
FEATURE_COLUMNS = [
    'pickup_longitude',
    'pickup_latitude',
    'dropoff_longitude',
    'dropoff_latitude',
    'passenger_count',
    'day_of_week',
    'hr_of_day',
    'day',
    'month',
    'year',
    'h_distance'
]

REQUEST_COLUMNS = [
    'pickup_longitude',
    'pickup_latitude',
    'dropoff_longitude',
    'dropoff_latitude',
    'datetime',
    'passenger_count'
]

float_cols = [
    'pickup_longitude',
    'pickup_latitude',
    'dropoff_longitude',
    'dropoff_latitude',
]

"""
   --- Constant Strings ---
"""
DATETIME_COL = 'datetime'
PICKUP_LONG = 'pickup_longitude'
PICKUP_LAT = 'pickup_latitude'
DROPOFF_LONG = 'dropoff_longitude'
DROPOFF_LAT = 'dropoff_latitude'

