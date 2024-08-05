import matplotlib.pyplot as plt
from Black_scholes import BSOptionPricing
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def plot_with_time(time_max, strike_price, current_price, riskfree_rate, volatility):
    time_range = np.arange(1, time_max)
    Call_put_list = [BSOptionPricing(current_price, strike_price, time, riskfree_rate, volatility).price()
                     for time in time_range]
    call_option = [i['call'] for i in Call_put_list]
    put_option = [i['put'] for i in Call_put_list]
    plt.plot(time_max - time_range, call_option)
    # plt.show()
    plt.plot(time_range, put_option)
    plt.legend(["Call", "Put"], loc="lower right")
    plt.show()


def plot_with_current_price(time, strike_price, current_price_max, current_price_min, riskfree_rate, volatility):
    price_range = np.arange(current_price_min, current_price_max)
    Call_put_list = [BSOptionPricing(price, strike_price, time, riskfree_rate, volatility).price()
                     for price in price_range]
    call_option = [i['call'] for i in Call_put_list]
    put_option = [i['put'] for i in Call_put_list]
    plt.plot(price_range, call_option)
    # plt.show()
    plt.plot(price_range, put_option)
    plt.legend(["Call", "Put"], loc="lower right")
    plt.show()


def plot_with_time_current_price(time_range, strike_price, current_price_max, current_price_min, riskfree_rate,
                                 volatility):
    time_range = np.arange(1, time_range)
    current_price_range = np.arange(current_price_min, current_price_max)
    current_price_grid, time_grid = np.meshgrid(current_price_range, time_range)
    # print(len(current_price_grid))
    call_price = np.array([[BSOptionPricing(S, strike_price, T, riskfree_rate, volatility).price()['call']
                                         for S in current_price_range] for T in time_range])
    put_price = np.array([[BSOptionPricing(S, strike_price, T, riskfree_rate, volatility).price()['put']
                                         for S in current_price_range] for T in time_range])
    sns.set(style="whitegrid")

    # Plotting
    fig = plt.figure(figsize=(14, 6))

    # Plot Call Option Prices
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(current_price_grid, time_grid, call_price, cmap='viridis')
    ax1.set_title('Call Option Prices: Strike Price = 100', fontsize=14)
    ax1.set_xlabel('Current Price', fontsize=12)
    ax1.set_ylabel('Time to Maturity', fontsize=12)
    ax1.set_zlabel('Call Price', fontsize=12)
    ax1.tick_params(axis='both', which='major', labelsize=10)

    # Plot Put Option Prices
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(current_price_grid, time_grid, put_price, cmap='plasma')
    ax2.set_title('Put Option Prices: Strike Price = 100', fontsize=14)
    ax2.set_xlabel('Current Price', fontsize=12)
    ax2.set_ylabel('Time to Maturity', fontsize=12)
    ax2.set_zlabel('Put Price', fontsize=12)
    ax2.tick_params(axis='both', which='major', labelsize=10)

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # plot_with_time(1000, 100, 110, 0.005, 0.1)
    plot_with_time_current_price(time_range=100, strike_price=100, current_price_max=150, current_price_min=50, riskfree_rate=0.005,
                            volatility=0.1)
