import matplotlib.dates
import matplotlib.pyplot as plt


class Plot:
    def draw(self, hours, temperatures):
        hours = matplotlib.dates.date2num(hours)
        plt.plot_date(hours, temperatures, linestyle='-')
        plt.show(block=True)

