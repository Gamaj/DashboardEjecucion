import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as geek





app = dash.Dash()

df = pd.read_csv('Base.csv')

available_indicators = df['Plataforma'].unique()


app.layout = html.Div([
    html.Div([dcc.Dropdown(
                id='Actividades',
                options=[{'label': i, 'value': i} for i in available_indicators],
            )],
        style={'width': '100%', 'display': 'inline-block'}),
    html.Div([ dcc.Graph(
            id='crossfilter-indicator-scatter',
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='pieAltipal',
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='barWeek',
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'})
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
        piedata = go.Pie(labels= ['Ejecucion' , 'Faltante' ],values=[geek.nansum(lista2),geek.nansum(lista1)-geek.nansum(lista2)])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }
    else:    
        dff = df[df['Plataforma'] == actividad]
        lista1 = dff['OBJ']
        lista2 = dff['REAL']
        print(geek.nansum(lista1)-geek.nansum(lista2))
        print (geek.nansum(lista1))
        print(geek.nansum(lista2))

        piedata = go.Pie(labels= ['Ejecucion' , 'Faltante' ],values=[geek.nansum(lista2),geek.nansum(lista1)-geek.nansum(lista2)])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }
@app.callback(
    dash.dependencies.Output('pieAltipal','figure'),
    [dash.dependencies.Input('Actividades','value')])        
def graphbar(actividad):
    if actividad is None:
        altipal = df[df['Distribuidor']== 'Altipal']
        dialsa =  df[df['Distribuidor']== 'Dialsa']
        meico =  df[df['Distribuidor']== 'Meico']
        piedata = go.Bar(x = ['Altipal' , 'Dialsa','Meico' ],y=[(geek.nansum(altipal['REAL'])/geek.nansum(altipal['OBJ']))*100,(geek.nansum(dialsa['REAL'])/geek.nansum(dialsa['OBJ']))*100,(geek.nansum(meico['REAL'])/geek.nansum(meico['OBJ']))*100])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }
    else:    
        dff = df[df['Plataforma'] == actividad]
        altipal = dff[dff['Distribuidor']== 'Altipal']
        dialsa =  dff[dff['Distribuidor']== 'Dialsa']
        meico =  dff[dff['Distribuidor']== 'Meico']
        piedata = go.Bar(x = ['Altipal' , 'Dialsa','Meico' ],y=[(geek.nansum(altipal['REAL'])/geek.nansum(altipal['OBJ']))*100,(geek.nansum(dialsa['REAL'])/geek.nansum(dialsa['OBJ']))*100,(geek.nansum(meico['REAL'])/geek.nansum(meico['OBJ']))*100])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }

@app.callback(
    dash.dependencies.Output('barWeek','figure'),
    [dash.dependencies.Input('Actividades','value')])        
def graphweek(actividad):
    if actividad is None:
        altipal = df[df['Distribuidor']== 'Altipal']
        dialsa =  df[df['Distribuidor']== 'Dialsa']
        meico =  df[df['Distribuidor']== 'Meico']
        piedata = go.Bar(x = ['Altipal' , 'Dialsa','Meico' ],y=[(geek.nansum(altipal['REAL'])/geek.nansum(altipal['OBJ']))*100,(geek.nansum(dialsa['REAL'])/geek.nansum(dialsa['OBJ']))*100,(geek.nansum(meico['REAL'])/geek.nansum(meico['OBJ']))*100])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }
    else:    
        dff = df[df['Plataforma'] == actividad]
        semana = dff
        semana1 = semana [semana['SEMANA'] == '1']
        semana2 = semana [semana['SEMANA'] == '2']
        semana3 = semana [semana['SEMANA'] == '3']
        semana4 = semana [semana['SEMANA'] == '4']
        print ((geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100)
        piedata = go.Scatter(x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
        
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION'}
        }



if __name__ == '__main__':
    app.run_server(debug=True)

