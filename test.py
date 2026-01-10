#import pandas
import pandas as pd

data = {
    "name": ["Amit", "Ravi", "Neha"],
    "age": [21, 22, 20],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
