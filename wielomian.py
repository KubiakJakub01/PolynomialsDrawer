# Importowanie bibliotek
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure


# %matplotlib qt

# Obiekt wilomianu
class Wielomian():

    def __init__(self, coefficients, min_x, max_x):
        # Inicjalizacja zmienych
        self.coefficients = coefficients
        self.min_x = min_x
        self.max_x = max_x
        self.pattern = self.wzor()
        self.zero_places = []
        self.X = np.arange(self.min_x, self.max_x + 0.1, 0.1)
        self.zakres = len(self.X)
        self.dervative_coefficients = self.derivative()
        self.Y = [self(round(x, 2), self.coefficients) for x in self.X]
        self.Y_dervative = [self(round(x, 2), self.dervative_coefficients) for x in self.X]

    def __call__(self, x, coefficients):
        # Wyliczanie wartosci funkcji
        res = 0.0
        power = len(coefficients) - 1
        for coeff in coefficients:
            res += coeff * (x ** power)
            power -= 1
        # print('x: {} y: {}'.format(x,res))
        return res

    def derivative(self):
        # wyliczanie wspolczynikow pochodnej funkcji
        dervative_coffe = []
        potega = len(self.coefficients) - 1

        for coeff in self.coefficients[:-1]:
            a = coeff * potega
            dervative_coffe.append(a)
            potega -= 1
        # print(dervative_coffe)
        return dervative_coffe

    def wzor(self):
        # Wyznaczanie wzoru funkcji w postaci ogolnej
        pattern = ''
        size = len(self.coefficients) - 1
        wspolczyniki = []

        for coeff in self.coefficients:
            if coeff == 0:
                wspolczyniki.append('0')
            elif coeff != 0:
                if len(wspolczyniki) == 0:
                    if coeff == 1:
                        wspolczyniki.append('')
                    elif coeff == -1:
                        wspolczyniki.append('-')
                    else:
                        wspolczyniki.append(str(coeff))
                elif coeff > 0:
                    wspolczyniki.append('+' + str(coeff))
                elif coeff < 0:
                    wspolczyniki.append(coeff)

        for coeff in wspolczyniki:
            if coeff != '0':
                if size == 0:
                    pattern += '{}'.format(coeff)
                elif size == 1:
                    pattern += '{}x '.format(coeff)
                else:
                    pattern += '{}x$^{}$ '.format(coeff, size)
            size -= 1

        # print(pattern)

        return pattern

    def __repr__(self):
        return "Wilomian: " + self.pattern

    def plot(self):
        # Rysowanie funkcji

        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111)

        plt.plot(self.X, self.Y, label='f(x)')
        plt.plot(self.X, self.Y_dervative, label="f'(x)")

        left, right = ax.get_xlim()
        low, high = ax.get_ylim()
        plt.arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15, color='red')
        plt.arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15, color='red')

        ax.set_title(self.pattern, color='white')
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        plt.grid()
        plt.legend()

        return fig
        # plt.show()

    def create_figure(self):
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        xs = self.X
        ys = self.Y
        axis.plot(xs, ys)
        return fig

