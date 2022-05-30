from re import X
import requests
import itertools

def get_dis():
    return requests.get(f"https://api-midproject.herokuapp.com/district").json()

def get_year():
    return requests.get(f"https://api-midproject.herokuapp.com/year").json()

def get_all():
    return requests.get(f"https://api-midproject.herokuapp.com/all/data").json()

def data_clean(data,year_select,dist):
    for_graph={}
    for x in data:
        for fecha in year_select:
            if x["Year"]==fecha:
                if x['District Name']==dist:
                    for_graph[x['Nationality']]=(x['Number'])
        return  for_graph           
    for_graph=dict( sorted(for_graph.items(),
                           key=lambda item: item[1],
                           reverse=True))
    return for_graph

def data_reduce(data):
    x={}
    for key, group in itertools.groupby(data, lambda k: 'All the rest' if (data[k]<70) else k):
        x[key] = sum([data[k] for k in list(group)]) 

    return x