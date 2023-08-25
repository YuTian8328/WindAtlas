import pandas as pd
import numpy as np

from windpowerlib import ModelChain, WindTurbine, create_power_curve, wind_speed


def hellman(
    wind_speed,
    wind_speed_height,
    hub_height,
    roughness_length=None,
    hellman_exponent=None
):
    hellman_exponent = 1 / 7
    return wind_speed * (hub_height / wind_speed_height) ** hellman_exponent


wind_speed.hellman = hellman


def speed_to_power(weather_df, my_turbine):

    mc_my_turbine = ModelChain(
        my_turbine,
        power_output_model='power_curve',
        wind_speed_model='hellman')
    mc_my_turbine.run_model(weather_df)
    # write power output time series to WindTurbine object
    my_turbine.power_output = mc_my_turbine.power_output.values
    return my_turbine.power_output


if __name__ == "__main__":
    from config import my_turbine
    weather_df = pd.read_csv('data/Kumpula2021.csv')
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
    # weather_df['wind_speed', '10'] = pd.to_numeric(
    #     weather_df['wind_speed', '10'], errors='coerce')
    weather_df["roughness_length"] = None

    speed_to_power(weather_df, my_turbine=my_turbine)
