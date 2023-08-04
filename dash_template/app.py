""" Setting up loggers with a config dict """
import logging
import logging.config

import pandas as pd
import plotly.express as px
from dash import Dash, dash_table, dcc, html

from logging_conf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

# Create logger
logger = logging.getLogger("file")

# Incorporate data
logger.info("Reading data")
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app
logger.info("Starting app")
app = Dash(__name__)

# App layout
app.layout = html.Div(
    [
        html.Div(children="My First App with Data and a Graph"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg")),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
