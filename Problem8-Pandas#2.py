import numpy as np
import pandas as pd
data = {
    "Apple": [10, 200, np.nan, 20, 400],
    "Orange": [5, np.nan, 15, 20, 25]
   
}
df = pd.DataFrame(data)
df.fillna(df.mean(), inplace=True)

print(df)
