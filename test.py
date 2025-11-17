import pandas as pd

# Load the CSV file
df = pd.read_csv('C:\\Users\\Mahi2\\capstone\\capstone_healthpredictors\\data\\patients.csv')
print(df.head().to_string())  # shows table format in terminal
df.head()
import pandas as pd

providers1 = pd.read_csv(
    'C:\\Users\\Mahi2\\capstone\\capstone_healthpredictors\\data\\providers.csv'
)
# View a few rows (table)
print(providers1.head().to_string())
