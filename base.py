import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class BasePlot:
    def __init__(self):
        self.x = []
        self.y = []

        self.fig = plt.figure()
        self.ax = self.fig.subplots()
        plt.subplots_adjust(left = 0.3, bottom = 0.25)
        plt.xlim([0, 40])
        plt.ylim([0, 40])
        self.p = self.ax.scatter(self.x, self.y, s=500, c=[], alpha=0.5)

        ax_button = plt.axes([0.25, 0.1, 0.08, 0.05])
        clear_button = Button(ax_button, 'Clear', color='white', hovercolor='grey')
        clear_button.on_clicked(self.clear)

        ax_button2 = plt.axes([0.45, 0.1, 0.18, 0.05])
        rm_button = Button(ax_button2, 'Remove last', color='white', hovercolor='grey')
        rm_button.on_clicked(self.remove_last)

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.show()

    def reset_plot(self):
        pass

    def clear(self, val):
        pass

    def remove_last(self, val):
        pass

    def onclick(self, event):
        pass

    def new_point(self, event, cls):
        pass


if __name__ == "__main__":
    bp = BasePlot()





