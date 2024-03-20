import pandas as pd
from normalization import Normalization

df =  pd.DataFrame({"Documento":["el texto de aquí debe esta normalizado"]})

new = Normalization(df)

print(new.normalize())



#print(isinstance(df, pd.Series))