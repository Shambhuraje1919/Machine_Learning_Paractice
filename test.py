#import pandas
import pandas as pd

data = {
    "name": ["Amit", "Ravi", "Neha","SAm"],
    "age": [21, 22, 20,22],
    "marks": [85, 90, 78,99]
}

df = pd.DataFrame(data)
print(df)
