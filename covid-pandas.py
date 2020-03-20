import pandas as pd
import numpy
import plotly.graph_objects as go

file = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
country = 'US'
title = "Confirmed Cases as function of Time in " + country
data = pd.read_csv(file)
df = pd.DataFrame(data)
dates = list(df.columns.values)
dates = dates[4:]
cases = []
# a = tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5)]
# >>> numpy.sum(a)[1]
# poop = df[(df['Country/Region'] == 'Italy') & (df[date])]
for date in dates:
    poop = df[(df['Country/Region'] == country) & (df[date])]
for date in dates:
    cases.append(numpy.sum(poop)[date])
print(cases)

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=cases,
                    mode='lines+markers'))
fig.update_layout(title=title,
                font={"size": 20},
                xaxis_title='',
                yaxis_title="Confirmed Cases"
        )
fig.show()