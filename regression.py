from base import BasePlot
from matplotlib.widgets import Button, RadioButtons, Slider
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


class RegressionPlot(BasePlot):
    def __init__(self):
        super(RegressionPlot, self).__init__()
        self.new_x = 0

        self.linreg = LinearRegression()

        self.est = None

        left, width = self.ax.get_position().bounds[0:2]
        k_space = plt.axes([left, 0.05, width * 2.4, 0.05])
        k_slider = Slider(k_space, "New point X", 0, 40, 0)
        k_slider.on_changed(self.move_new_point)

        new_space = plt.axes([0.02, 0.8, 0.25, 0.05])
        new_btn = Button(new_space, "Make new point")
        new_btn.on_clicked(self.estimate_new_point)

        train_space = plt.axes([0.02, 0.7, 0.25, 0.05])
        train_btn = Button(train_space, "Train Regression")
        train_btn.on_clicked(self.train)
        plt.show()



    def train(self, val):
        X = np.reshape(self.x, (-1, 1))
        self.est = self.linreg.fit(X, self.y)
        m = self.linreg.coef_
        b = self.linreg.intercept_
        x_line = np.linspace(0, 40)
        self._ = self.ax.plot(x_line, x_line * m + b)

    def move_new_point(self, val):
        self.new_x = val

    def estimate_new_point(self, _):
        print(f"evalutating x val {self.new_x}")
        X = np.reshape([self.new_x], (1, -1))
        print(X)
        new_y = self.est.predict(X)
        print(new_y)
        self.new_point((self.new_x, new_y))

    def clear(self, val):
        print("clear")
        self.x.clear()
        self.y.clear()
        self.reset_plot()

    def remove_last(self, val):
        l = len(self.x)
        self.x.pop(l - 1)
        self.y.pop(l - 1)
        self.reset_plot()

    def onclick(self, event):
        if event.inaxes == self.ax:
            self.new_point((event.xdata, event.ydata))

    def new_point(self, coor):
        self.x.append(coor[0])
        self.y.append(coor[1])
        self.reset_plot()

    def reset_plot(self):
        self.p.remove()
        self.p = self.ax.scatter(self.x, self.y, s=500, c=[.2 for _ in range(len(self.x))], alpha=0.5)
        self.fig.canvas.draw()

if __name__ == "__main__":
    rp = RegressionPlot()
