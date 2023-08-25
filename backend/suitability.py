from concurrent.futures import ProcessPoolExecutor, as_completed
import sys
import os
import time
import threading
from fractions import Fraction
import math
from config import n100, rutland504, automax
from utils import convert_time_granularity, load_process
import pandas as pd
import numpy as np
from wind_power_transformation import speed_to_power


def suitability(power, time_point, max_waiting_time, total_energy):
    """
    Determine the suitability of a given time point for running a process with a initially empty battery.

    This function calculates the accumulated energy generation over a specified
    period, starting from the given time point and extending up to a maximum
    waiting time. If the accumulated energy generation is greater than or equal
    to a predefined total energy threshold, the function returns True, indicating
    that the time point is suitable for the process. Otherwise, it returns False.

    Parameters:
        time_point (int): The starting time point to be evaluated.
        max_waiting_time (int): The maximum duration, in time units, for which
                               energy accumulation is considered.

    Returns:
        bool: True if the accumulated energy generation is sufficient for the process,
              False if the accumulated energy generation is insufficient.

    """
    energy = 0  # start with an empty battery
    for i in range(0, max_waiting_time*6, 6):
        if time_point+i < len(power):
            energy += power[time_point+i]/6

    if energy >= total_energy:
        return True
    return False


def count_starting_points(power, max_waiting_time, total_energy):
    """
    Calculate the count of starting points suitable for a process during a period (e.g. a year).

    This function iterates through the power data array (a time series), evaluating the suitability
    of each time point using the suitability() function. If a time point is
    suitable, it increments the count of suitable starting points. The final count
    of suitable starting points is returned as the result.


    Parameters:
        max_waiting_time (int): The maximum tolerance to wait, in time units, for which energy accumulation is considered.

    Returns:
        int: The count of time points that are suitable for a process.
    """
    count = 0
    for i in range(len(power)):
        if suitability(power, i, max_waiting_time, total_energy):
            count += 1
    return count


# Define a helper function for parallel processing


def process_city(file, max_waiting_time, battery_capacity, total_energy, windturbine):
    wind_data_dir = "./data/windspeed_stations_2021"
    if not file.startswith("."):
        # Read weather data from csv
        weather_df = pd.read_csv(os.path.join(wind_data_dir, file))
        weather_df['Wind speed (m/s)'] = weather_df['Wind speed (m/s)'].replace('-',
                                                                                None).astype(float)
        weather_df['Wind speed (m/s)'].interpolate(method='linear',
                                                   inplace=True)
        weather_df['Wind speed (m/s)'] = weather_df['Wind speed (m/s)'].apply(
            lambda x: np.maximum(x, 0))

        weather_df = weather_df[['Wind speed (m/s)']]

        column_names = pd.MultiIndex.from_arrays(
            [['wind_speed'], ['10']], names=['variable_name', 'height'])

        weather_df.columns = column_names
        weather_df['roughness_length', '0'] = 0.15
        weather_df.fillna(weather_df.mean(
            numeric_only=True).round(2), inplace=True)
        if windturbine == 1:
            my_turbine = rutland504
        elif windturbine == 2:
            my_turbine = automax
        else:
            my_turbine = n100
        power = speed_to_power(weather_df, my_turbine)
        suitable_starting_points = count_starting_points(
            power, max_waiting_time, total_energy)
        return {'city': file[:-4], 'val': suitable_starting_points/len(power)}
    else:
        return None


def get_suitabilities_FMI_parallel(max_waiting_time, battery_capacity, total_energy, windturbine):
    start = time.time()
    print(start)
    workable_fractions = []
    wind_data_dir = "./data/windspeed_stations_2021"
    city_files = [file for file in os.listdir(
        wind_data_dir) if not file.startswith(".")]

    # Create a ProcessPoolExecutor for parallel processing
    with ProcessPoolExecutor() as executor:
        # Submit the city files to the executor for processing
        futures = [executor.submit(process_city, file, max_waiting_time,
                                   battery_capacity, total_energy, windturbine) for file in city_files]

        # Iterate over the completed futures and retrieve the results
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                workable_fractions.append(result)
                # print(result)
    total_time = time.time() - start
    print(total_time)
    return workable_fractions


if __name__ == "__main__":
    from config import automax, Num_turbine
    fractions = get_suitabilities_FMI_parallel(5, 1000, 900, 2)
    print(fractions)
