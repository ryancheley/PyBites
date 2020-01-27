from collections import namedtuple
from datetime import date, datetime

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    # 1

    c = pd.read_csv(DATA_FILE)
    # convert date column from str to datetime
    c['Date'] = pd.to_datetime(c['Date'])

    # 2
    the_day = c['Date'].dt.strftime('%m%d')
    c['The_Day'] = the_day

    c_max = c.iloc[c.groupby(['ID', 'The_Day'])['Data_Value'].agg(pd.Series.idxmax)]
    # c_max = c_max.drop(index=c_max[c['The_Day'] == '0229'].index.values)

    c_min = c.iloc[c.groupby(['ID', 'The_Day'])['Data_Value'].agg(pd.Series.idxmin)]
    # c_min = c_min.drop(index=c_min[c['The_Day'] == '0229'].index.values)


    # 3
    c_min_2015 = c_min[c_min.Date.dt.year == 2015]

    c_max_2015 = c_max[c_max.Date.dt.year == 2015]

    # 4
    idx_min = c_min_2015[['Data_Value']].idxmin()
    low_2015 = STATION(
        c_min_2015.loc[[idx_min[0]]].ID.values[0],
        datetime.utcfromtimestamp(c_min_2015.loc[[idx_min[0]]].Date.values[0].astype(date) * 1e-9).date(),
        c_min_2015.loc[[idx_min[0]]].Data_Value.values[0] / 10
    )

    idx_max = c_max_2015[['Data_Value']].idxmax()
    high_2015 = STATION(
        c_max_2015.loc[[idx_max[0]]].ID.values[0],
        datetime.utcfromtimestamp(c_max_2015.loc[[idx_max[0]]].Date.values[0].astype(date) * 1e-9).date(),
        c_max_2015.loc[[idx_max[0]]].Data_Value.values[0] / 10
    )

    return high_2015, low_2015


p = high_low_record_breakers_for_2015()
high = p[0]

print((high.Date))