import streamlit as st 
from DATA.get_data import get_dis, get_year, get_all, data_clean
from DATA.graph import pieChart
from DATA.geo import map_dis


st.title('Inmigracion en Barcelona')
st.text('Distribucion de nacionalidades por distrito en BCN')


BCN=get_dis()
print (type((BCN)))
dist = st.selectbox('Esgoje un distrito', [x for x in BCN])
print (dist)

year=get_year()
year_select = st.selectbox('Esgoje un año', [x for x in year])
print(year_select)
print(type(year_select))

all_data=get_all()

for_graph=data_clean(all_data,year_select,dist)

pieChart(for_graph)

df=map_dis(dist)
st.map(df)