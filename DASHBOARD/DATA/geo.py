
import pandas as pd
import numpy as np

Ciutat_Vella=[41.38022] 
Ciutat_Vella_2=[2.17319]
def map_dis(dist):
    if dist == "Ciutat Vella":
        df = pd.DataFrame(list(zip(Ciutat_Vella, Ciutat_Vella_2)),
                columns =['lat', 'lon'])
    return df           
    
