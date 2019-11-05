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
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='barChannel',
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([ dcc.Graph(
            id='barSegment',
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
     html.Div([ dcc.Graph(
            id='barFaltante',
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
        semana = df
        semana1 = semana[semana['SEMANA'] == 1]
        semana2 = semana[semana['SEMANA'] == 2]
        semana3 = semana[semana['SEMANA'] == 3]
        semana4 = semana[semana['SEMANA'] == 4]
        lineGeneraldata = go.Scatter(name= 'Total', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
        semana = df[df['Distribuidor']== 'Altipal']
        semana1 = semana[semana['SEMANA'] == 1]
        semana2 = semana[semana['SEMANA'] == 2]
        semana3 = semana[semana['SEMANA'] == 3]
        semana4 = semana[semana['SEMANA'] == 4]
        lineAltipaldata = go.Scatter(name= 'Altipal', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
        semana = df[df['Distribuidor']== 'Dialsa']
        semana1 = semana[semana['SEMANA'] == 1]
        semana2 = semana[semana['SEMANA'] == 2]
        semana3 = semana[semana['SEMANA'] == 3]
        semana4 = semana[semana['SEMANA'] == 4]
        lineDialsadata = go.Scatter(name= 'Dialsa', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])
        semana = df[df['Distribuidor']== 'Meico']
        semana1 = semana[semana['SEMANA'] == 1]
        semana2 = semana[semana['SEMANA'] == 2]
        semana3 = semana[semana['SEMANA'] == 3]
        semana4 = semana[semana['SEMANA'] == 4]
        lineMeicodata = go.Scatter(name= 'Meico', x = ['1','2','3','4'],y=[(geek.nansum(semana1['REAL'])/geek.nansum(semana1['OBJ']))*100,(geek.nansum(semana2['REAL'])/geek.nansum(semana2['OBJ']))*100,(geek.nansum(semana3['REAL'])/geek.nansum(semana3['OBJ']))*100,(geek.nansum(semana4['REAL'])/geek.nansum(semana4['OBJ']))*100])

        return {
            'data':[lineGeneraldata , lineAltipaldata, lineDialsadata, lineMeicodata],'layout': {'title': 'EJECUCION'}
        }
    else:    
        dff = df[df['Plataforma'] == actividad]
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
            'data':[lineGeneraldata , lineAltipaldata, lineDialsadata, lineMeicodata],'layout': {'title': 'EJECUCION'}
        }

@app.callback(
    dash.dependencies.Output('barChannel','figure'),
    [dash.dependencies.Input('Actividades','value')])  
def graphChannel(actividad):
    if actividad is None:
        ontrade = df[df['Canal']== 'On Trade']
        offtrade = df[df['Canal'] == 'Off Trade']
        piedata = go.Bar(y = ['On Trade' , 'Off Trade'],x=[(geek.nansum(ontrade['REAL'])/geek.nansum(ontrade['OBJ']))*100,(geek.nansum(offtrade['REAL'])/geek.nansum(offtrade['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x CANAL'}
        }
    else:
        dff = df[df['Plataforma'] == actividad]
        ontrade = dff[dff['Canal']== 'On Trade']
        offtrade = dff[dff['Canal'] == 'Off Trade']
        piedata = go.Bar(y = ['On Trade' , 'Off Trade'],x=[(geek.nansum(ontrade['REAL'])/geek.nansum(ontrade['OBJ']))*100,(geek.nansum(offtrade['REAL'])/geek.nansum(offtrade['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x CANAL'}
        }

@app.callback(
    dash.dependencies.Output('barSegment','figure'),
    [dash.dependencies.Input('Actividades','value')])  
def graphChannel(actividad):
    if actividad is None:
        bares = df[df['Segmento Según Scorecard']== 'BARES']
        Conveniencia = df[df['Segmento Según Scorecard']== 'Conveniencia']
        Discotecas = df[df['Segmento Según Scorecard']== 'DISCOTECAS']
        Drogueria = df[df['Segmento Según Scorecard']== 'Droguerías']
        Hiperysuper = df[df['Segmento Según Scorecard']== 'Hiper y Supermercados']
        licoreras = df[df['Segmento Según Scorecard'] == 'LICORERAS']
        mayorista = df[df['Segmento Según Scorecard'] == 'MAYORISTAS']
        restaurantes = df[df['Segmento Según Scorecard'] == 'RESTAURANTES']
        store = df[df['Segmento Según Scorecard'] == 'Store']
        supermercado = df[df['Segmento Según Scorecard'] == 'SUPERMERCADOS']
        tat = df[df['Segmento Según Scorecard'] == 'TAT (TIENDAS)']
        piedata = go.Bar(y = ['BARES' , 'Conveniencia','DISCOTECAS','Droguerías','Hiper y Supermercados','LICORERAS','MAYORISTAS','RESTAURANTES','Store','SUPERMERCADOS', 'TAT'],x=[(geek.nansum(bares['REAL'])/geek.nansum(bares['OBJ']))*100,(geek.nansum(Conveniencia['REAL'])/geek.nansum(Conveniencia['OBJ']))*100,(geek.nansum(Discotecas['REAL'])/geek.nansum(Discotecas['OBJ']))*100,(geek.nansum(Drogueria['REAL'])/geek.nansum(Drogueria['OBJ']))*100,(geek.nansum(Hiperysuper['REAL'])/geek.nansum(Hiperysuper['OBJ']))*100,(geek.nansum(licoreras['REAL'])/geek.nansum(licoreras['OBJ']))*100,(geek.nansum(mayorista['REAL'])/geek.nansum(mayorista['OBJ']))*100,(geek.nansum(restaurantes['REAL'])/geek.nansum(restaurantes['OBJ']))*100,(geek.nansum(store['REAL'])/geek.nansum(store['OBJ']))*100,(geek.nansum(supermercado['REAL'])/geek.nansum(supermercado['OBJ']))*100,(geek.nansum(tat['REAL'])/geek.nansum(tat['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x SEGMENTO SC'}
        }
    else:
        dff = df[df['Plataforma'] == actividad]
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
        piedata = go.Bar(y = ['BARES' , 'Conveniencia','DISCOTECAS','Droguerías','Hiper y Supermercados','LICORERAS','MAYORISTAS','RESTAURANTES','Store','SUPERMERCADOS', 'TAT'],x=[(geek.nansum(bares['REAL'])/geek.nansum(bares['OBJ']))*100,(geek.nansum(Conveniencia['REAL'])/geek.nansum(Conveniencia['OBJ']))*100,(geek.nansum(Discotecas['REAL'])/geek.nansum(Discotecas['OBJ']))*100,(geek.nansum(Drogueria['REAL'])/geek.nansum(Drogueria['OBJ']))*100,(geek.nansum(Hiperysuper['REAL'])/geek.nansum(Hiperysuper['OBJ']))*100,(geek.nansum(licoreras['REAL'])/geek.nansum(licoreras['OBJ']))*100,(geek.nansum(mayorista['REAL'])/geek.nansum(mayorista['OBJ']))*100,(geek.nansum(restaurantes['REAL'])/geek.nansum(restaurantes['OBJ']))*100,(geek.nansum(store['REAL'])/geek.nansum(store['OBJ']))*100,(geek.nansum(supermercado['REAL'])/geek.nansum(supermercado['OBJ']))*100,(geek.nansum(tat['REAL'])/geek.nansum(tat['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x SEGMENTO SC'}
        }

@app.callback(
    dash.dependencies.Output('barFaltante','figure'),
    [dash.dependencies.Input('Actividades','value')])  
def graphChannel(actividad):
    if actividad is None:
        dff = df['Plataforma'].unique()
        print(dff)
        bares = df[df['Segmento Según Scorecard']== 'BARES']
        Conveniencia = df[df['Segmento Según Scorecard']== 'Conveniencia']
        Discotecas = df[df['Segmento Según Scorecard']== 'DISCOTECAS']
        Drogueria = df[df['Segmento Según Scorecard']== 'Droguerías']
        Hiperysuper = df[df['Segmento Según Scorecard']== 'Hiper y Supermercados']
        licoreras = df[df['Segmento Según Scorecard'] == 'LICORERAS']
        mayorista = df[df['Segmento Según Scorecard'] == 'MAYORISTAS']
        restaurantes = df[df['Segmento Según Scorecard'] == 'RESTAURANTES']
        store = df[df['Segmento Según Scorecard'] == 'Store']
        supermercado = df[df['Segmento Según Scorecard'] == 'SUPERMERCADOS']
        tat = df[df['Segmento Según Scorecard'] == 'TAT (TIENDAS)']
        piedata = go.Bar(y = ['BARES' , 'Conveniencia','DISCOTECAS','Droguerías','Hiper y Supermercados','LICORERAS','MAYORISTAS','RESTAURANTES','Store','SUPERMERCADOS', 'TAT'],x=[(geek.nansum(bares['REAL'])/geek.nansum(bares['OBJ']))*100,(geek.nansum(Conveniencia['REAL'])/geek.nansum(Conveniencia['OBJ']))*100,(geek.nansum(Discotecas['REAL'])/geek.nansum(Discotecas['OBJ']))*100,(geek.nansum(Drogueria['REAL'])/geek.nansum(Drogueria['OBJ']))*100,(geek.nansum(Hiperysuper['REAL'])/geek.nansum(Hiperysuper['OBJ']))*100,(geek.nansum(licoreras['REAL'])/geek.nansum(licoreras['OBJ']))*100,(geek.nansum(mayorista['REAL'])/geek.nansum(mayorista['OBJ']))*100,(geek.nansum(restaurantes['REAL'])/geek.nansum(restaurantes['OBJ']))*100,(geek.nansum(store['REAL'])/geek.nansum(store['OBJ']))*100,(geek.nansum(supermercado['REAL'])/geek.nansum(supermercado['OBJ']))*100,(geek.nansum(tat['REAL'])/geek.nansum(tat['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x SEGMENTO SC'}
        }
    else:
        dff = df[df['Plataforma'] == actividad]
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
        piedata = go.Bar(y = ['BARES' , 'Conveniencia','DISCOTECAS','Droguerías','Hiper y Supermercados','LICORERAS','MAYORISTAS','RESTAURANTES','Store','SUPERMERCADOS', 'TAT'],x=[(geek.nansum(bares['REAL'])/geek.nansum(bares['OBJ']))*100,(geek.nansum(Conveniencia['REAL'])/geek.nansum(Conveniencia['OBJ']))*100,(geek.nansum(Discotecas['REAL'])/geek.nansum(Discotecas['OBJ']))*100,(geek.nansum(Drogueria['REAL'])/geek.nansum(Drogueria['OBJ']))*100,(geek.nansum(Hiperysuper['REAL'])/geek.nansum(Hiperysuper['OBJ']))*100,(geek.nansum(licoreras['REAL'])/geek.nansum(licoreras['OBJ']))*100,(geek.nansum(mayorista['REAL'])/geek.nansum(mayorista['OBJ']))*100,(geek.nansum(restaurantes['REAL'])/geek.nansum(restaurantes['OBJ']))*100,(geek.nansum(store['REAL'])/geek.nansum(store['OBJ']))*100,(geek.nansum(supermercado['REAL'])/geek.nansum(supermercado['OBJ']))*100,(geek.nansum(tat['REAL'])/geek.nansum(tat['OBJ']))*100], orientation = 'h')
        return {
            'data':[piedata],'layout': {'title': 'EJECUCION x SEGMENTO SC'}
        }



if __name__ == '__main__':
    app.run_server(debug=True)
