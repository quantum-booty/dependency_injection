from datetime import datetime
from unittest.mock import MagicMock

import plotly.graph_objects as go
from plotly_plot import Plot


def test_draw(monkeypatch):
    figure_mock = MagicMock()
    monkeypatch.setattr(go, 'Figure', figure_mock)
    scatter_mock = MagicMock()
    monkeypatch.setattr(go, 'Scatter', scatter_mock)

    plot = Plot()
    hours = [datetime.now()]
    temperatures = [14.52]
    plot.draw(hours, temperatures)

    call_kwargs = scatter_mock.call_args[1]
    assert call_kwargs['y'] == temperatures
    figure_mock().show.assert_called()
