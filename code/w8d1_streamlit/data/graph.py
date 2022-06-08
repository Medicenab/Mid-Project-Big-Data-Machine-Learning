import plotly.io as pio
import plotly.graph_objs as go
import plotly_express as px
import matplotlib.pyplot as plt


def radar_plot(stats, name):
    theta = [stat["stat"]["name"].title() for stat in stats]
    values = [s["base_stat"] for s in stats]
    
    radar = go.Scatterpolar(
            r = values,
            theta = theta,
            name = name,
            fill = "toself"
        )
    return radar