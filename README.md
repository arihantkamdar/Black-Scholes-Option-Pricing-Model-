# Black-Scholes Option Pricing and Visualization

This Streamlit application allows users to visualize the Black-Scholes option pricing model in 3D interactively. Users can adjust parameters such as current price, strike price, time to maturity, risk-free rate, and volatility to see the corresponding changes in call and put option prices.

## Features

- **Interactive Sliders**: Adjust the model parameters using inputs in the web app.
- **Dynamic 2D 3D Plots**.
- **User-friendly Interface**: Run the streamlit application or just use simple plotting scripts in the repository.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arihantkamdar/Black_Scholes.git
   pip install -r requirements.txt
   # For simple plotting use
   python3 plotting.py
   # For interactive plotting in Streamlit Webapp using
   streamlit run app.py
