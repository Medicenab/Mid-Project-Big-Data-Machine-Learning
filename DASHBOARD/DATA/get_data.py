import re
import requests
def get_dis():
    return requests.get(f"https://api-midproject.herokuapp.com/district").json()

def get_year():
    return requests.get(f"https://api-midproject.herokuapp.com/year").json()

def get_all():
    return requests.get(f"https://api-midproject.herokuapp.com/all/data").json()

def data_clean(data,year_select,dist):
    for_graph={}
    for x in data:
        if x["Year"]==year_select:
            if x['District Name']==dist:
                for_graph[x['Nationality']]=(x['Number'])
    for_graph=dict( sorted(for_graph.items(),
                           key=lambda item: item[1],
                           reverse=True))
    return for_graph
