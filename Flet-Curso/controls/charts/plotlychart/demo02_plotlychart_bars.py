import plotly.express as px

import flet as flt
from flet.plotly_chart import PlotlyChart


def main(page: flt.Page):
    page.title = "Plotly Chart Demo"

    df = px.data.gapminder().query("continent=='Oceania'")

    fig  = px.bar(
        df,
        x='year',
        y='pop',
        hover_data=['lifeExp', 'gdpPercap'],
        color='country',
        labels={'pop':'population of Canada'},
        height=400
    )

    page.add(PlotlyChart(fig, expand=True))


if __name__ == "__main__":
    flt.app(target=main)
