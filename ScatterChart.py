import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')  # to get seaborn scatter plot

# read the csv file to extract data
df = pd.read_csv('pricevsmileage.csv')

# store to panda table
Honda_mileage = df['Mileage']
Honda_price = df['Price']

Seat_mileage = df['Mileage.1']
Seat_price = df['Price.1']


# Plot  seaborn scatter chart
sns.regplot(x=Honda_mileage, y=Honda_price, scatter = True, label = 'Honda', color = 'red', ci= None, data=df)
sns.regplot(x=Seat_mileage, y=Seat_price, scatter = True, label = 'Seat', color = 'green', ci = None, data=df)

plt.title('Price vs mileage')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.legend()

plt.show()


