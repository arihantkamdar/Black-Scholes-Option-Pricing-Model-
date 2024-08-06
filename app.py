import streamlit as st
import plotly.graph_objs as go
from plot_app import *

st.title("Black-Schole Simulation")

st.write("Certain Asssumptions: ")
st.markdown("- No dividends are paid out during the life of the option.")
st.markdown("- Markets are random because market movements can't be predicted.")
st.markdown("- There are no transaction costs in buying the option.")
st.markdown("- The risk-free rate and volatility of the underlying asset are known and constant.")
st.markdown("- The returns of the underlying asset are normally distributed.")
st.markdown("- The option is European and can only be exercised at expiration.")
# st.write("Select Plot type")
plot_type = st.selectbox("Type of Plot", ['Option Price with Time', 'Option Price with Asset Price',
                                          'Option Price with Time and Asset Price'])

if plot_type == 'Option Price with Time':
    strike_price = st.number_input('Strike Price', value=100)
    max_time = st.number_input('Time Range from 1', value=30)
    current_price = st.number_input('Price of Asset', value=110)
    riskfree_rate = st.number_input('Risk-free ate of return per unit time', value=0.005)
    volatility = st.number_input('Volatility', value=0.10)
    df = plot_time_graph(time_max=max_time,
                         strike_price=strike_price,
                         current_price=current_price,
                         riskfree_rate=riskfree_rate,
                         volatility=volatility)
    st.line_chart(df.set_index('Time to Maturity'),
                  x_label='Time to Maturity',
                  y_label='Price')

if plot_type == 'Option Price with Asset Price':
    strike_price = st.number_input('Strike Price', value=100)
    time = st.number_input('Time from expiry', value=10)
    current_price_min = st.number_input('Min Price of Asset', value=110)
    current_price_max = st.number_input('Max Price of Asset', value=110)
    riskfree_rate = st.number_input('Risk-free ate of return per unit time', value=0.005)
    volatility = st.number_input('Volatility', value=0.10)
    df = plot_price_graph(time,
                          strike_price,
                          current_price_max,
                          current_price_min,
                          riskfree_rate,
                          volatility)
    st.line_chart(df.set_index('Price Range'),
                  x_label='Asset Price',
                  y_label='Price')

if plot_type == 'Option Price with Time and Asset Price':
    strike_price = st.number_input('Strike Price', value=100, key="S")
    max_time = st.number_input('Time Range from 1', value=30)
    current_price_min = st.number_input('Min Price of Asset', value=110)
    current_price_max = st.number_input('Max Price of Asset', value=110)
    riskfree_rate = st.number_input('Risk-free ate of return per unit time', value=0.005)
    volatility = st.number_input('Volatility', value=0.10)
    time_grid, current_price_grid, call_price, put_price = plot_time_price(max_time, strike_price, current_price_max,
                                                                           current_price_min, riskfree_rate,
                                                                           volatility)
    st.pyplot(plot_3d_surface(current_price_grid, time_grid, call_price, 'Call Option Price Surface', 'Call Price'))
    st.pyplot(plot_3d_surface(current_price_grid, time_grid, put_price, 'Put Option Price Surface', 'Put Price'))

    # fig = go.Figure(data=[go.Surface(z=df['Call Option Price'].tolist(), x=df['Price Range'].tolist(), y=df['time_range'].tolist())])
    # fig.update_layout(title='3D Plot', scene=dict(
    #     xaxis_title='X AXIS',
    #     yaxis_title='Y AXIS',
    #     zaxis_title='Z AXIS'))

    # Display the plot in the Streamlit app
    # st.plotly_chart(fig)
    # fig = go.Figure(data=[go.Surface(z=df['Put Option Price'], x=df['Price Range'], y=df['time_range'])])
    # fig.update_layout(title='3D Plot', scene=dict(
    #     xaxis_title='X AXIS',
    #     yaxis_title='Y AXIS',
    #     zaxis_title='Z AXIS'))
    #
    # # Display the plot in the Streamlit app
    # st.plotly_chart(fig)
