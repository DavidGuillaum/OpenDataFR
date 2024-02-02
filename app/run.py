import requests
import pandas as pd
from pandas import json_normalize

from dash import Dash, dcc
import dash_bootstrap_components as dbc
import dash_html_components as html



#Extract
#SELECT annee, distric
response_API = requests.get('https://opendata.fr.ch/api/explore/v2.1/catalog/datasets/01_02_age_5_sex_natio_etatcivil/records?select=annee%2C%20district%2C%20commune%2C%20genre%2C%20nationalite_categorie_fr%2C%20classe_etat_civil_fr&where=commune%20like%20%22Corminboeuf%22&limit=100')
print(response_API.status_code)
df_json = response_API.json()
df = pd.json_normalize(df_json["results"])

#Transform
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["annee"] = df["annee"].astype(int)
for col in df.columns[1:]:
    df[col] = str(df[col])

observations_by_year = df.groupby('annee').size().reset_index(name='count')



#web-app

app = Dash(__name__)

app.layout = html.Div([
    dcc.Markdown(children=f"Population of Canton Fribourg by Year"),
    dcc.Graph(
        figure={
            'data': [
                {'x': observations_by_year['annee'], 'y': observations_by_year['count'], 'type': 'bar', 'name': 'Observations'},
            ],
            'layout': {
                'title': 'Number of Observations by Year',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Count'},
            }
        }
    ),
])

#run 
if __name__=='__main__':
    app.run_server(debug=True, port=8054)