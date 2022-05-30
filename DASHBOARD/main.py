import streamlit as st 
from DATA.get_data import get_dis, get_year, get_all, data_clean
from DATA.graph import pieChart
from DATA.geo import map_dis


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
    for_graph={}
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    for_graph[x['Nationality']]=(x['Number'])
    for_graph=dict( sorted(for_graph.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph)                                       
if len(year_select)==2:
    for_graph={}
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    for_graph[x['Nationality']]=(x['Number'])
    for_graph=dict( sorted(for_graph.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph)  
    for_graph_1={}
    for x in all_data:
        if x["Year"]==year_select[1]:
                if x['District Name']==dist:
                    for_graph_1[x['Nationality']]=(x['Number'])
    for_graph_1=dict( sorted(for_graph_1.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph_1)
if len(year_select)==3:
    for_graph={}
    for x in all_data:
        if x["Year"]==year_select[0]:
                if x['District Name']==dist:
                    for_graph[x['Nationality']]=(x['Number'])
    for_graph=dict( sorted(for_graph.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph)  
    for_graph_1={}
    for x in all_data:
        if x["Year"]==year_select[1]:
                if x['District Name']==dist:
                    for_graph_1[x['Nationality']]=(x['Number'])
    for_graph_1=dict( sorted(for_graph_1.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph_1)
    for_graph_2={}
    for x in all_data:
        if x["Year"]==year_select[2]:
                if x['District Name']==dist:
                    for_graph_2[x['Nationality']]=(x['Number'])
    for_graph_2=dict( sorted(for_graph_2.items(),
                           key=lambda item: item[1],
                           reverse=True))
    pieChart(for_graph_2)



df=map_dis(dist)
st.map(df)