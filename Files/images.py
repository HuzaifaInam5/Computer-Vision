import cv2

path = '../Images/image_1.jpg'
image = cv2.imread(path)

# Check if the image was successfully loaded
if image is None:
    print("Error loading image")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#EDA Code
#a. Countplot
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
df.head()

#Categorical Data

#sns.countplot(df['Embarked'])
#Plotting a countplot using seaborn library to visualize the distribution of values in the 'Embarked' column
sns.countplot(x='Embarked', data=df)
sns.countplot(x='Pclass', data=df)
df['Survived'].value_counts()
df['Survived'].value_counts().plot(kind='bar')

#b. PieChart
df['Sex'].value_counts().plot(kind='pie')
df['Sex'].value_counts().plot(kind='pie',autopct='%.2f')

# Numerical Data
#a. Histogram

import matplotlib.pyplot as plt
plt.hist(df['Age'],bins=5)

plt.hist(df['Age'])
plt.hist(df['Age'],bins=15)

#b. Distplot

#kernal density estimation (KDE) line. Show data distribution
sns.distplot(df['Age'])

#c. Boxplot

# 5 number sample
#how much data is noise and outliers 
# give you 5 number Summary 
sns.boxplot(df['Age'])
df['Age'].min()
df['Age'].max()
df['Age'].mean()
df['Age'].skew()
