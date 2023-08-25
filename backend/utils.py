import numpy as np
import pandas as pd
import math
from fractions import Fraction
import numpy as np
import json


def convert_time_granularity(time_series, tg1, tg2):
    if not tg1 % tg2 == 0:
        raise ValueError(
            'wrong time granularities, tg1 is not divisible by tg2')
    elif tg1/tg2 == 1:
        return time_series
    else:
        time_series = time_series.reshape([-1, 1])@np.ones((1, int(tg1/tg2)))

        return time_series.flatten(order='C')


def load_process(filepath):
    f = open(filepath, "r")
    return json.load(f)


if __name__ == "__main__":
    process = np.array([364, 196, 196, 796, 196])
    df = pd.read_csv('data/Winddata.csv')
    df['Wind speed (m/s)'] = df['Wind speed (m/s)'].replace('-',
                                                            None).astype(float)
    df['Wind speed (m/s)'].interpolate(method='polynomial',
                                       order=2, inplace=True)
    dfwindspeed = df['Wind speed (m/s)'].values
    # print(would_it_work(process, dfwindspeed, 40, 400, 2000, 1000, 0.0006))
