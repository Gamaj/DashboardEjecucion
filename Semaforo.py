import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as geek

app = dash.Dash()

df = pd.read_csv('Base.csv')

available_indicators = df['Plataforma'].unique()
mes_indicators = df['MES'].unique()
semana_indicators = df['SEMANA'].unique()
departamento_indicators = df['Departamento'].unique()
distribuidor_indicators = df['Distribuidor'].unique()
canal_indicators = df['Canal'].unique()
segmento_indicators = df['Segmento'].unique()

app.layout = html.Div([
    html.Div([html.Div(
                    [
                        html.H2(
                            'Semáforo de ejecución',
                            style={'text-align': 'center'}
                        )
                    ],

                ),
            html.Div(
                    [
                        html.H3(
                            'Plataforma',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Actividades',
                            options=[{'label': i, 'value': i} for i in available_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        
                    ],
                     style={'width': '2%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        html.H3(
                            'Mes',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Mes',
                            options=[{'label': i, 'value': i} for i in mes_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        
                    ],
                     style={'width': '2%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        html.H3(
                            'Semana',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='semana',
                            options=[{'label': 1, 'value': 1} , {'label': 2, 'value': 2} ,{'label': 3, 'value': 3} ,{'label': 4, 'value': 4},{'label': 5, 'value': 5} ],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        
                    ],
                     style={'width': '2%', 'display': 'inline-block'}
                ),
            html.Div(
                    [
                        html.H3(
                            'Departamento',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Departamento',
                            options=[{'label': i, 'value': i} for i in departamento_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
             html.Div(
                    [
                        html.H3(
                            'Distribuidor',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Distribuidor',
                            options=[{'label': i, 'value': i} for i in distribuidor_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
                 html.Div(
                    [
                        
                    ],
                     style={'width': '2%', 'display': 'inline-block'}
                ),
                html.Div(
                    [
                        html.H3(
                            'Canal',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Canal',
                            options=[{'label': i, 'value': i} for i in canal_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
                html.Div(
                    [
                        
                    ],
                     style={'width': '2%', 'display': 'inline-block'}
                ),
                html.Div(
                    [
                        html.H3(
                            'Segmento',
                            style={'text-align': 'center'}
                        ),
                         dcc.Dropdown(
                            id='Segmento',
                            options=[{'label': i, 'value': i} for i in segmento_indicators],
                        )
                    ],
                     style={'width': '23.5%', 'display': 'inline-block'}
                ),
                html.Div(
                    [
                        
                    ],
                     style={'width': '25.5%', 'display': 'inline-block'}
                ),   
           ],
       ),
    html.Div([ dcc.Graph(
            id='crossfilter-indicator-scatter',
        )
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='pieAltipal',
        )
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='barWeek',
        )
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='barChannel',
        )
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div(
                    [
                        
                    ],
                     style={'width': '10%', 'display': 'inline-block'}
                ),
    html.Div([ dcc.Graph(
            id='barSegment',
        )
    ], style={'width': '80%', 'display': 'inline-block', 'padding': '0 20'}),
   
     html.Div([ dcc.Graph(
            id='barFaltante',
            config={
			'displayModeBar':True,
			'queueLength':0
		    },
        )
    ], style={'width': '100%', 'height': '200%', 'display': 'inline-block', 'padding': '0 20'}),
    ])

@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])
def graph(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]
  
                  
    lista1 = dff['OBJ']
    lista2 = dff['REAL']
    print (geek.nansum(lista1))
    print(geek.nansum(lista2))
    print(geek.nansum(lista1)-geek.nansum(lista2))
    piedata = go.Pie(labels= ['Ejecucion' , 'Faltante' ],values=[geek.nansum(lista2),geek.nansum(lista1)-geek.nansum(lista2)])
        
    return {
        'data':[piedata],'layout': {'title': 'EJECUCION'}
    }


@app.callback(
    dash.dependencies.Output('pieAltipal','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])        
def graphbar(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]
  
    altipal = dff[dff['Distribuidor']== 'Altipal']
    dialsa =  dff[dff['Distribuidor']== 'Dialsa']
    meico =  dff[dff['Distribuidor']== 'Meico']
    piedata = go.Bar(x = ['Altipal' , 'Dialsa','Meico' ],y=[(geek.nansum(altipal['REAL'])/geek.nansum(altipal['OBJ']))*100,(geek.nansum(dialsa['REAL'])/geek.nansum(dialsa['OBJ']))*100,(geek.nansum(meico['REAL'])/geek.nansum(meico['OBJ']))*100])
        
    return {
        'data':[piedata],'layout': {'title': 'EJECUCION x DISTRIBUIDOR'}
    }
 
@app.callback(
    dash.dependencies.Output('barWeek','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])        
def graphweek(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]

    semana = dff
    semana1 = semana[semana['SEMANA'] == 1]
    semana2 = semana[semana['SEMANA'] == 2]
    semana3 = semana[semana['SEMANA'] == 3]
    semana4 = semana[semana['SEMANA'] == 4]
    lineGeneraldata = go.Scatter(name= 'Total', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
    semana = dff[dff['Distribuidor']== 'Altipal']
    semana1 = semana[semana['SEMANA'] == 1]
    semana2 = semana[semana['SEMANA'] == 2]
    semana3 = semana[semana['SEMANA'] == 3]
    semana4 = semana[semana['SEMANA'] == 4]
    lineAltipaldata = go.Scatter(name= 'Altipal', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
    semana = dff[dff['Distribuidor']== 'Dialsa']
    semana1 = semana[semana['SEMANA'] == 1]
    semana2 = semana[semana['SEMANA'] == 2]
    semana3 = semana[semana['SEMANA'] == 3]
    semana4 = semana[semana['SEMANA'] == 4]
    lineDialsadata = go.Scatter(name= 'Dialsa', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
    semana = dff[dff['Distribuidor']== 'Meico']
    semana1 = semana[semana['SEMANA'] == 1]
    semana2 = semana[semana['SEMANA'] == 2]
    semana3 = semana[semana['SEMANA'] == 3]
    semana4 = semana[semana['SEMANA'] == 4]
    lineMeicodata = go.Scatter(name= 'Meico', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])

    return {
        'data':[lineGeneraldata , lineAltipaldata, lineDialsadata, lineMeicodata],'layout': {'title': 'EJECUCION x SEMANA'}
    }
    
@app.callback(
    dash.dependencies.Output('barChannel','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])  
def graphChannel(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]

    ontrade = dff[dff['Canal']== 'On Trade']
    offtrade = dff[dff['Canal'] == 'Off Trade']
    piedata = go.Bar(y = ['On Trade' , 'Off Trade'],x=[(geek.nansum(ontrade['REAL'])/geek.nansum(ontrade['OBJ']))*100,(geek.nansum(offtrade['REAL'])/geek.nansum(offtrade['OBJ']))*100], orientation = 'h')
    return {
        'data':[piedata],'layout': {'title': 'EJECUCION x CANAL'}
    }


@app.callback(
    dash.dependencies.Output('barSegment','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])  
def graphSegmento(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]

    bares = dff[dff['Segmento Según Scorecard']== 'BARES']
    Conveniencia = dff[dff['Segmento Según Scorecard']== 'Conveniencia']
    Discotecas = dff[dff['Segmento Según Scorecard']== 'DISCOTECAS']
    Drogueria = dff[dff['Segmento Según Scorecard']== 'Droguerías']
    Hiperysuper = dff[dff['Segmento Según Scorecard']== 'Hiper y Supermercados']
    licoreras = dff[dff['Segmento Según Scorecard'] == 'LICORERAS']
    mayorista = dff[dff['Segmento Según Scorecard'] == 'MAYORISTAS']
    restaurantes = dff[dff['Segmento Según Scorecard'] == 'RESTAURANTES']
    store = dff[dff['Segmento Según Scorecard'] == 'Store']
    supermercado = dff[dff['Segmento Según Scorecard'] == 'SUPERMERCADOS']
    tat = dff[dff['Segmento Según Scorecard'] == 'TAT (TIENDAS)']
    piedata = go.Bar(y = ['BARES' , 'Conveniencia','DISCOTECAS','Droguerías','Hiper y Supermercados','LICORERAS','MAYORISTAS','RESTAURANTES','Store','SUPERMERCADOS', 'TAT'],x=[(geek.nansum(bares['REAL'])/geek.nansum(bares['OBJ']))*100,(geek.nansum(Conveniencia['REAL'])/geek.nansum(Conveniencia['OBJ']))*100,(geek.nansum(Discotecas['REAL'])/geek.nansum(Discotecas['OBJ']))*100,(geek.nansum(Drogueria['REAL'])/geek.nansum(Drogueria['OBJ']))*100,(geek.nansum(Hiperysuper['REAL'])/geek.nansum(Hiperysuper['OBJ']))*100,(geek.nansum(licoreras['REAL'])/geek.nansum(licoreras['OBJ']))*100,(geek.nansum(mayorista['REAL'])/geek.nansum(mayorista['OBJ']))*100,(geek.nansum(restaurantes['REAL'])/geek.nansum(restaurantes['OBJ']))*100,(geek.nansum(store['REAL'])/geek.nansum(store['OBJ']))*100,(geek.nansum(supermercado['REAL'])/geek.nansum(supermercado['OBJ']))*100,(geek.nansum(tat['REAL'])/geek.nansum(tat['OBJ']))*100], orientation = 'h' )
    return {
        'data':[piedata],'layout': {'title': 'EJECUCION x SEGMENTO SC', 'yaxis': {'autorange': True,  'automargin': True, 'animate': True}}
    }

@app.callback(
    dash.dependencies.Output('barFaltante','figure'),
    [dash.dependencies.Input('Actividades','value'),
    dash.dependencies.Input('Mes','value'),
    dash.dependencies.Input('semana','value'),
    dash.dependencies.Input('Departamento','value'),
    dash.dependencies.Input('Distribuidor','value'),
    dash.dependencies.Input('Canal','value'),
    dash.dependencies.Input('Segmento','value')])  
def graphPlatf(actividad,mes,semana,departamento,distri,canal,segmento):
    dff = df

    if mes is not None:
        dff = dff[dff['MES'] == mes]
    if semana is not None:
        dff = dff[dff['SEMANA'] == semana]
    if departamento is not None:
        dff = dff[dff['Departamento'] == departamento]
    if distri is not None:
        dff = dff[dff['Distribuidor'] == distri]
    if canal is not None:
        dff = dff[dff['Canal'] == canal]
    if segmento is not None:
        dff = dff[dff['Segmento'] == segmento]
    if actividad is not None:
        dff = dff[dff['Plataforma'] == actividad]
        dfff = dff
        column = [[],[]]
        reales = geek.nansum(dfff['REAL'])
        objt = geek.nansum(dfff['OBJ'])
        falta = 100 - ((reales/objt)*100)
        if falta > 0:
            if (reales/objt) <= 1:
                column[0].append(actividad)
                column[1].append(falta) 
        piedata = go.Bar(x = column[0],y=column[1], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION FALTANTE x ACTIVIDAD', 'yaxis': {'autorange': True,'title': 'X Axis',  'automargin': True, 'animate': True}}
        }
    if actividad is None:
        plat = dff['Plataforma'].unique()
        column = [[],[]]
        for row in plat:
            print(row)
            print(dff['Plataforma'] == row)
            dfff = dff[dff['Plataforma'] == row]
            reales = geek.nansum(dfff['REAL'])
            objt = geek.nansum(dfff['OBJ'])
            falta = 100 - ((reales/objt)*100) 
            if falta > 0:
                if (reales/objt) <= 1:
                    column[0].append(row)
                    column[1].append(falta)

        piedata = go.Bar(y = column[0],x=column[1], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION FALTANTE x ACTIVIDAD', 'yaxis': {'autorange': True,  'automargin': True, 'animate': True}}
        }
    
    



if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
