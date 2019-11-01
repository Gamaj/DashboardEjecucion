import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as geek





app = dash.Dash()

df = pd.read_csv('Base.csv')

available_indicators = df['Plataforma'].unique()


def defaultgraph():
    lista1 = df['OBJ']
    lista2 = df['REAL']
    print (geek.nansum(lista1))
    print("HOLA...")
    print(geek.nansum(lista2))
    print(lista2)
    piedata = go.Pie(values=[geek.nansum(lista1)-geek.nansum(lista2),geek.nansum(lista2)])
    
    return {
        'data':[piedata],'layout': {'title': 'EJECUCION'}
    }

app.layout = html.Div([
    html.Div([dcc.Dropdown(
                id='Actividades',
                options=[{'label': i, 'value': i} for i in available_indicators],
            )],
        style={'width': '100%', 'display': 'inline-block'}),
    html.Div([ dcc.Graph(
            figure = defaultgraph(),
            id='crossfilter-indicator-scatter',
            
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    ])

@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter','figure'),
    [dash.dependencies.Input('Actividades','value')])
def graph(actividad):
    if actividad is None:
        lista1 = df['OBJ']
        lista2 = df['REAL']
        print (geek.nansum(lista1))
        print(geek.nansum(lista2))
        print(geek.nansum(lista1)-geek.nansum(lista2))
        piedata = go.Pie(values=[geek.nansum(lista1)-geek.nansum(lista2),geek.nansum(lista2)])
    
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }
    else:    
        dff = df[df['Plataforma'] == actividad]
        lista1 = dff['OBJ']
        lista2 = dff['REAL']
        print(actividad)
        print (geek.nansum(lista1))
        print(geek.nansum(lista2))

        piedata = go.Pie(values=[geek.nansum(lista1)-geek.nansum(lista2),geek.nansum(lista2)])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }



if __name__ == '__main__':
    app.run_server(debug=True)

