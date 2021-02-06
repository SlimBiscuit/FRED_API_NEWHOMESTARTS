from fredapi import Fred
from pandas.core.frame import DataFrame
fred = Fred(api_key='xxxx') #insert your API key instead of 'xxxx'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
import matplotlib.dates as mdates

def HouseData(months):

    if months > 36:
        print ('You have exceeded the threshold, please select a lesser values')
    return 

    # Fetch the series from the fred API and convert to a Dataframe
    series_latest_release = fred.get_series_latest_release('HOUST')
    data = series_latest_release.to_frame('New_Home_Starts')

    # Create a new 'Date' column using the index values and apply formatting
    data['Date'] = data.index
    data['Date'] = data['Date'].dt.strftime('%m-%Y')

    # Get the most recent date
    most_recent = data.index.max()

    # Starting from the most recent date in the data, select the last n months of data
    filtered_data = data.loc[f"{(most_recent - relativedelta(months=months - 1))}":f"{most_recent}"]

    # PLOT THE FIGURE AND FORMAT
    filtered_data.plot.bar(y='New_Home_Starts', x='Date')

    # Rotate x labels
    plt.xticks(rotation=45)

    # Set the y-axis label
    plt.ylabel('New Housing Starts')

    # Set the title
    plt.title('New Housing Starts for US - FRED')

    # Calculate and set the limit values of the Y-Axis
    stats = filtered_data['New_Home_Starts'].describe()
    y_min = stats['min'] - 200
    y_max = stats['max'] + 200
    plt.ylim(y_min, y_max)

    plt.show()
    return filtered_data

print(HouseData(37))