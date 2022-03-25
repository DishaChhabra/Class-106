import pandas
import plotly.express as px

data=pandas.read_csv('https://raw.githubusercontent.com/whitehatjr/correlation/master/data/cups%20of%20coffee%20vs%20hours%20of%20sleep.csv')

graph = px.scatter(data, x='Coffee in ml',y='sleep in hours')
graph.show()

print(data.corr())

data2 = pandas.read_csv('https://raw.githubusercontent.com/whitehatjr/correlation/master/data/Size%20of%20TV%2C%09Average%20time%20spent%20watching%20TV%20in%20a%20week%20(hours).csv')
graph2 = px.scatter(data2, x='Size of TV',	y='\tAverage time spent watching TV in a week (hours)')
graph2.show()

print(data2.corr())