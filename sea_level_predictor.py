import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(32,10))
    ax = df.plot(ax=ax, kind='scatter', x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    first_best_fit = pd.Series(list(range(df['Year'].min(), 2051)))
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(first_best_fit, result.intercept + result.slope * first_best_fit)

    # Create second line of best fit
    second_best_fit = pd.Series(list(range(2000, 2051)))
    df_adjusted = df[df['Year'] > 1999]
    result = linregress(df_adjusted['Year'], df_adjusted['CSIRO Adjusted Sea Level'])
    plt.plot(second_best_fit, result.intercept + result.slope * second_best_fit)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()