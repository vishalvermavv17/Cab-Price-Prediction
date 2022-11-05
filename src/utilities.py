import pandas as pd
import numpy as np
import datetime

from src.CONSTANTS import DATETIME_COL, PICKUP_LAT, DROPOFF_LAT, DROPOFF_LONG, PICKUP_LONG, FEATURE_COLUMNS


def add_datetime_features(df, col):
    dt = pd.to_datetime(df[col])
    df['day_of_week'] = dt.dt.dayofweek
    df['minute'] = dt.dt.minute
    df['hr_of_day'] = dt.dt.hour
    df['month'] = dt.dt.month
    df['year'] = dt.dt.year
    df['day'] = dt.dt.day
    return df


def haversine_distance(df):
    R = 6371  # radius of earth in kilometers
    # R = 3959 #radius of earth in miles
    phi1 = np.radians(df[PICKUP_LAT])
    phi2 = np.radians(df[DROPOFF_LAT])

    delta_phi = np.radians(df[DROPOFF_LAT] - df[PICKUP_LAT])
    delta_lambda = np.radians(df[DROPOFF_LONG] - df[PICKUP_LONG])

    # a = sin²((φB - φA)/2) + cos φA . cos φB . sin²((λB - λA)/2)
    a = np.sin(delta_phi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0) ** 2

    # c = 2 * atan2( √a, √(1−a) )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # d = R*c
    d = (R * c)  # in kilometers
    df['h_distance'] = d
    return df


def prepare_inference_df(df):
    df = add_datetime_features(df, DATETIME_COL)
    df = haversine_distance(df)
    return df[FEATURE_COLUMNS]
