import plotly.graph_objects as go


class Plot:
    def draw(self, hours, temperatures):
        fig = go.Figure(data=[go.Scatter(x=hours, y=temperatures)])
        fig.show()
