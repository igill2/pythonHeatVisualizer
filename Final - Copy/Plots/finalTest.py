import pandas as pd
df = pd.read_csv('../Datasets/crimeRates.csv')

import plotly.express as px

fig1 = px.choropleth(df, locations='State',
                            locationmode="USA-states",
                            color ="homicideRate2017",
                           color_continuous_scale="Viridis_r",
                           range_color=(0, 14),
                           scope="usa",
                           labels={'homicideRate2017':'Homicide Rate'},
                            title ='Homicide Rates by State in 2017',
                            height = 750
                          )

fig2 = px.choropleth(df, locations='State',
                     locationmode="USA-states",
                     color="firearmDeathRate",
                     color_continuous_scale="Viridis_r",
                     range_color=(0, 20),
                     scope="usa",
                     labels={'firearmDeathRate': 'Firearm Death Rate'},
                     title ='Firearm Death Rates by State in 2017',
                     height = 750
                     
                     )

fig3 = px.choropleth(df, locations='State',
                     locationmode="USA-states",
                     color="firearmDeaths",
                     color_continuous_scale="Viridis_r",
                     range_color=(0, 4000),
                     scope="usa",
                     labels={'firearm Deaths': 'FirearmDeaths'},
                    title ='Firearm Deaths by State in 2017',
                     height = 750
                     )

with open('graph.html', 'a') as f:
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))