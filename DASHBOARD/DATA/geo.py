
import pandas as pd
import numpy as np

Ciutat_Vella=[[41.38022,2.17319]]
Eixample=[[41.38896, 2.16179]]
Gràcia=[[41.40237, 2.15641]]
Horta_Guinardó=[[41.41849, 2.1677]]
Les_Corts=[[41.38712, 2.13007]]
Nou_Barris=[[41.44163, 2.17727]]
Sant_Andreu=[[41.43541, 2.18982]]
Sant_Martí=[[41.41814, 2.19933]]
Sants_Montjuïc=[[41.37263, 2.1546]]
Sarrià_Sant_Gervasi=[[41.40104, 2.1394]]





def map_dis(dist):
    if dist == "Ciutat Vella":
        df = pd.DataFrame(Ciutat_Vella,
                columns =['lat', 'lon'])    
    if dist == "Eixample":
        df = pd.DataFrame(Eixample,
                columns =['lat', 'lon'])
    if dist == "Gràcia":
        df = pd.DataFrame(Gràcia,
                columns =['lat', 'lon'])
    if dist == "Horta-Guinardó":
        df = pd.DataFrame(Horta_Guinardó,
                columns =['lat', 'lon'])
    if dist == "Les Corts":
        df = pd.DataFrame(Les_Corts,
                columns =['lat', 'lon'])
    if dist == "Nou Barris":
        df = pd.DataFrame(Nou_Barris,
                columns =['lat', 'lon'])     
    if dist == "Sant Andreu":
        df = pd.DataFrame(Sant_Andreu,
                columns =['lat', 'lon'])            
    if dist == "Sant Martí":
        df = pd.DataFrame(Sant_Martí,
                columns =['lat', 'lon'])    
    if dist == "Sants-Montjuïc":
        df = pd.DataFrame(Sants_Montjuïc,
                columns =['lat', 'lon'])      
    if dist == "Sarrià-Sant Gervasi":
        df = pd.DataFrame(Sarrià_Sant_Gervasi,
                columns =['lat', 'lon'])                                              
    return df           
