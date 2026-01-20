#import pandas
import pandas as pd

data = {
    "name": ["Amit", "Ravi", "Neha","SAm"],
    "age": [21, 22, 20,22],
    "marks": [85, 90, 78,99]
}

df = pd.DataFrame(data)
print(df)

data2 = {
    "name":["sohit","Ram","Kisho"],
    "age":[22,23,23],
    "Marks":[22,25,88]
}
df1 = pd.DataFrame(data2)
print(df1)
