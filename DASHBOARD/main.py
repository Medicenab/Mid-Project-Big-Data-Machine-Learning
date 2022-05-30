import streamlit as st 
from DATA.get_data import get_dis, get_year, get_all, data_reduce
from DATA.graph import pieChart
from DATA.geo import map_dis
import itertools

st.title('Inmigracion en Barcelona')
st.text('Distribucion de nacionalidades por distrito en BCN, durante 2015, 2016 y 2017')
year=get_year()
year_select = st.multiselect('Selecciona algun año:', [x for x in year])

BCN=get_dis()

dist = st.selectbox('Selecciona un distrito', [x for x in BCN])



for_graph={}
for_graph_1={}
for_graph_2={}

all_data=get_all()

if len(year_select)==1:
    data_base={}
    for_graph={}
    
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    data_base[x['Nationality']]=(x['Number'])
    data_base=dict( sorted(data_base.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base, lambda k: 'All the rest' if (data_base[k]<70) else k):
        for_graph[key] = sum([data_base[k] for k in list(group)]) 
    print(for_graph)
    pieChart(for_graph)       





if len(year_select)==2:
    data_base={}
    for_graph={}
    
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    data_base[x['Nationality']]=(x['Number'])
    data_base=dict( sorted(data_base.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base, lambda k: 'All the rest' if (data_base[k]<70) else k):
        for_graph[key] = sum([data_base[k] for k in list(group)]) 
    print(for_graph)
    pieChart(for_graph)    

    data_base_1={}
    for_graph_1={}
    for x in all_data:
        if x["Year"]==year_select[1]:
                if x['District Name']==dist:
                    data_base_1[x['Nationality']]=(x['Number'])
    data_base_1=dict( sorted(data_base_1.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base_1, lambda k: 'All the rest' if (data_base_1[k]<70) else k):
        for_graph_1[key] = sum([data_base_1[k] for k in list(group)])                       
    pieChart(for_graph_1)





if len(year_select)==3:
    data_base={}
    for_graph={}
    
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    data_base[x['Nationality']]=(x['Number'])
    data_base=dict( sorted(data_base.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base, lambda k: 'All the rest' if (data_base[k]<70) else k):
        for_graph[key] = sum([data_base[k] for k in list(group)]) 
    print(for_graph)
    pieChart(for_graph)    

    data_base_1={}
    for_graph_1={}
    for x in all_data:
        if x["Year"]==year_select[1]:
                if x['District Name']==dist:
                    data_base_1[x['Nationality']]=(x['Number'])
    data_base_1=dict( sorted(data_base_1.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base_1, lambda k: 'All the rest' if (data_base_1[k]<70) else k):
        for_graph_1[key] = sum([data_base_1[k] for k in list(group)])                       
    pieChart(for_graph_1)

    data_base_2={}
    for_graph_2={}
    for x in all_data:
        if x["Year"]==year_select[1]:
                if x['District Name']==dist:
                    data_base_2[x['Nationality']]=(x['Number'])
    data_base_2=dict( sorted(data_base_2.items(),
                           key=lambda item: item[1],
                           reverse=True))
    for key, group in itertools.groupby(data_base_2, lambda k: 'All the rest' if (data_base_2[k]<70) else k):
        for_graph_2[key] = sum([data_base_2[k] for k in list(group)])                       
    pieChart(for_graph_2)



df=map_dis(dist)
st.map(df)