import plotly.express as px
import pandas as pd


df = pd.read_csv("austpop.csv")

# Line graphs
fig = px.line(df, x="year", y="Aust", title="Australian Population")
fig.write_html("cats.html")