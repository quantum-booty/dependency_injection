from datetime import datetime
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from matplotlib_plot import Plot

def test_draw(monkeypatch):
    plot_date_mock = MagicMock()
    show_mock = MagicMock()
    monkeypatch.setattr(plt, 'plot_date', plot_date_mock)
    monkeypatch.setattr(plt, 'show', show_mock)

    plot = Plot()
    hour = [datetime.now().isoformat()]
    temperature = [14.52]
    plot.draw(hour, temperature)

    _, called_temperatures = plot_date_mock.call_args[0]
    assert called_temperatures == temperature
    show_mock.assert_called()

    
