from scipy.stats import norm
import numpy as np


class BSOptionPricing:
    def __init__(self, current_price, strike_price, time, risk_free_rate, volatility, q=0):
        self.current_price = current_price
        self.strike_price = strike_price
        self.time = time
        self.risk_free_rate = risk_free_rate
        self.q = q
        self.volatility = volatility

    @staticmethod
    def normal_function(x):
        return norm.cdf(x)

    @property
    def params(self):
        return {'Asset Price': self.current_price,
                'Strike Price': self.strike_price,
                'TIme Until Exp': self.time,
                'risk free rate': self.risk_free_rate,
                'q': self.q,
                'Volatility': self.volatility}

    def d1(self):
        return (np.log(self.current_price / self.strike_price) + (
                    self.risk_free_rate - self.q + self.volatility ** 2 / 2) * self.time) \
            / (self.volatility * np.sqrt(self.time))

    def d2(self):
        return self.d1() - self.volatility * np.sqrt(self.time)

    def _call_value(self):
        return self.current_price * np.exp(-self.q * self.time) * self.normal_function(self.d1()) - \
            self.strike_price * np.exp(-self.risk_free_rate * self.time) * self.normal_function(self.d2())

    def _put_value(self):
        return self.strike_price * np.exp(-self.risk_free_rate * self.time) * self.normal_function(-self.d2()) - \
            self.current_price * np.exp(-self.q * self.time) * self.normal_function(-self.d1())

    def price(self, type_='C'):
        return {'call': float(self._call_value()), 'put': float(self._put_value()),
                "Stock Price": float(self.current_price)}


if __name__ == '__main__':
    K = 100
    r = 0.1
    T = 1
    sigma = 0.3
    S = 100
    print(BSOptionPricing(S, K, T, r, sigma).price('B'))
