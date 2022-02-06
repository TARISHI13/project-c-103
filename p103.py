import pandas as pd 
import plotly.express as px
df = pd.read_csv("project 103.csv")
fig = px.scatter(df,x = "dates",y = "cases",color = "country")
fig.show()