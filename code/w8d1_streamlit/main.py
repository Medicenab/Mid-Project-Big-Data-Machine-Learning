import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objs as go
from data.get_data import get_all_pokemon
from data.graph import radar_plot


st.title('Mi dashboard de pokemon')
st.text('Vamos a mostrar datos sobre los pokemons') 
pokemons = get_all_pokemon(50)
chosen_one = st.multiselect('Elige pokemon', [p["name"] for p in pokemons], key="1")


img = []
stats = []
for p in pokemons:
    for c in chosen_one:
        if p["name"]==c:
            img.append(p["sprites"]["front_default"])
            stats.append((p["name"], p["stats"]))


num_col = 10
num_filas = (len(img)//num_col)+1
i = 0
for fila in range(num_filas):
    for col in st.columns(num_col):
        if i < len(img):
            with col:
                st.image(img[i])
                i+=1

if stats:
    graph = go.Figure()
    for name, stat in stats:
        print(stat)
        print(name)
        graph.add_trace(radar_plot(stat, name))

    st.plotly_chart(graph)


click = st.button('Click me')
print(click)