import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Black_scholes import BSOptionPricing


def plot_time_graph(time_max, strike_price, current_price, riskfree_rate, volatility):
    time_range = np.arange(1, time_max)
    Call_put_list = [BSOptionPricing(current_price, strike_price, time, riskfree_rate, volatility).price()
                     for time in time_range]
    call_option = [i['call'] for i in Call_put_list]
    put_option = [i['put'] for i in Call_put_list]
    df = pd.DataFrame({
        'Time to Maturity': time_range,
        'Call Option Price': call_option,
        'Put Option Price': put_option
    })
    return df


def plot_price_graph(time, strike_price, current_price_max, current_price_min, riskfree_rate, volatility):
    price_range = np.arange(current_price_min, current_price_max)
    Call_put_list = [BSOptionPricing(price, strike_price, time, riskfree_rate, volatility).price()
                     for price in price_range]
    call_option = [i['call'] for i in Call_put_list]
    put_option = [i['put'] for i in Call_put_list]
    df = pd.DataFrame({
        'Price Range': price_range,
        'Call Option Price': call_option,
        'Put Option Price': put_option
    })
    return df


def plot_time_price(time_range, strike_price, current_price_max, current_price_min, riskfree_rate,
                    volatility):
    time_range = np.arange(1, time_range)
    current_price_range = np.arange(current_price_min, current_price_max)
    current_price_grid, time_grid = np.meshgrid(current_price_range, time_range)
    call_price = np.array([[BSOptionPricing(S, strike_price, T, riskfree_rate, volatility).price()['call']
                            for S in current_price_range] for T in time_range])
    put_price = np.array([[BSOptionPricing(S, strike_price, T, riskfree_rate, volatility).price()['put']
                           for S in current_price_range] for T in time_range])
    return time_grid, current_price_grid, call_price, put_price


def plot_3d_surface(X, Y, Z, title, zlabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('Stock Price')
    ax.set_ylabel('Time to Maturity')
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    return fig
