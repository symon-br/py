#STEP 1: Import the tools we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



#STEP 2: Create our data
data = {
    'Size': [500, 750, 1000, 1250, 1500, 1700, 1726, 1625, 77],
    'Price': [25, 36, 48, 59, 70, 81, 92, 103, 114]
}

df = pd.DataFrame(data)
print("Our data :")
print(df)



#STEP 3: Sperate the question from the answer
X = df[['Size']]
Y = df[['Price']]



#STEP 4: Keep some data hidden for testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)



#STEP 5: Train the model
model = LinearRegression()
model.fit(X_train, Y_train)
print("\nModel trained")


#STEP 6: Ask it about a brand new house
new_house = pd.DataFrame({'Size': [1600]})
price = model.predict(new_house)

print("\nA 1600 sqft house should cost: ", round(price[0], 2), "lakhs")


#STEP 7: Draw the picture
plt.scatter(df['Size'], df[['Price']], label='Real prices')
plt.plot(df['Size'], model.predict(X), color='red', label='What model learned')
plt.xlabel('Size (sqft)')
plt.ylabel('price (lakhs)')
plt.legend()
plt.show()