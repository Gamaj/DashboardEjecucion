import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Base.csv')

data = [go.Scatter(x = df['SEMANA'], y = df['OBJ'], text = df['NUM MES'], mode = 'markers', marker = dict(size = df['REAL'] ))]

layout = go.Layout(title = 'Bubble Chart')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)