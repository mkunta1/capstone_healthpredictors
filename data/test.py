import pandas as pd

# Load the CSV
df = pd.read_csv("data/procedures.csv")

# Get number of rows and columns
rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")
