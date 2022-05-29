import matplotlib.pyplot as plt
import streamlit as st 

def pieChart(x):
    fig = plt.figure(figsize=(22, 16))
    plt.pie(x.values(), labels = x.keys(),autopct='%1.1f%%',startangle=90,labeldistance=1.05)
    st.balloons()
    st.pyplot(fig)


