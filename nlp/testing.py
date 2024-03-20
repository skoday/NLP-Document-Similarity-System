import pandas as pd
from normalization import Normalization

df =  pd.DataFrame({"Documento":["el texto de aquí debe esta normalizado", "el gato persiguio a el raton por toda la casa"]})

new = Normalization(df)

print(new.normalize())



#print(isinstance(df, pd.Series))