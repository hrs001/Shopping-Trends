import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/harshsrivastava/Downloads/archive (2)/shopping_trends_updated.csv')

#First 5 rows
print(df.head(5))

# Columns Names
print(df.columns)

# Generalised info of the dataset
print(df.shape)
print(df.size)
print(df.dtypes)
print(df.describe())


# Finding the Duplicate and the null value 
print(df.duplicated())
print(df.isnull())

# Age Histogram
p = np.arange(0,100,15)

plt.title("Histogram of Age : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Maroon'})
plt.hist(df['Age'], bins = p, )
plt.xlabel("Age : ")
plt.ylabel('Frequency : ')
plt.xticks(p)

# Gender Distribution Bar chart
a = df.groupby('Gender').count()['Customer ID']
print(a.index)
plt.title("Gender Distribution : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.bar(a.index, a, color = 'Maroon')
plt.xlabel("Gender : ")
plt.ylabel('Frequency : ')
plt.show()

# Pie Chart of Subscription Status
b = df.groupby('Subscription Status').count()['Customer ID']
plt.pie(b, labels= b.index)
plt.show()

# Create a pie chart of Color distribution (show only top 5)
c = df.groupby('Color').count()['Customer ID']
d = c.sort_values( ascending= False).head(5)
plt.pie(d, labels= d.index)
plt.show()

# Create a bar plot for count of purchases by Season
e = df.groupby('Season').count()['Customer ID']
plt.bar(e.index, e)
plt.xticks(e.index)
plt.show()

# Create a pie chart for distribution of Purchase Category
f = df.groupby('Category').count()['Customer ID']
plt.pie(f,labels = f.index)
plt.show()

# Group by Category and calculate mean Purchase Amount. Sort and show: Top 2 categories, Bottom 2 categories
g = df.groupby('Category')['Purchase Amount (USD)'].mean()
print(g)

# Group by Season and calculate the sum of Purchase Amount.
h = df.groupby('Season')['Purchase Amount (USD)'].sum()
print(h)

# Group by Size and calculate the mean of Purchase Amount.
i = df.groupby('Size')['Purchase Amount (USD)'].mean()
print(i)

# Group by Payment Method and calculate the total Purchase Amount
j = df.groupby('Payment Method')['Purchase Amount (USD)'].sum()
print(j)

# Group by Discount Applied and calculate: Maximum Review Rating, Mean Review Rating
j = df.groupby('Discount Applied')['Review Rating'].max()
k = df.groupby('Discount Applied')['Review Rating'].min()
print(j)
print(k)

# Group by Color and count how many times each Category appears.
l = df.groupby('Color')['Customer ID'].count().sort_index(ascending= False)
print(l)

# Group by Frequency of Purchases and calculate the median of Previous Purchases.
m = df.groupby('Item Purchased')['Previous Purchases'].median()
print(m)

# Group by Season and calculate the mean of Review Rating.
n = df.groupby('Season')['Review Rating'].mean()
print(n)

# Create a scatter plot: Previous Purchases vs Review Rating
plt.title("Scatter Plot : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.scatter(df.groupby('Previous Purchases')['Previous Purchases'].mean(), df.groupby('Previous Purchases')['Review Rating'].median(), color = 'Maroon')
plt.show()

# Create a histogram of Purchase Amount (with 10 bins
plt.title("Scatter Plot : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.hist(df['Purchase Amount (USD)'], bins = 10,color = 'Maroon')
plt.show()

# Create a bar plot: Mean Review Rating for each Color (top 5 only).
p = df.groupby('Color')['Review Rating'].mean().sort_values(ascending = False).head(5)
print(p)
plt.title("Scatter Plot : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.bar(p.index, p)
plt.show()

# Create a pie chart: Total Purchase Amount by Payment Method.
p = df.groupby('Payment Method')['Customer ID'].count()
print(p)
plt.title("Scatter Plot : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.pie(p, labels= p.index)
plt.show()

# Create a pie chart: Total Purchase Amount by Season.
p = df.groupby('Season')['Purchase Amount (USD)'].sum()
print(p)
plt.title("Scatter Plot : ", fontdict={'fontsize': 30, 'fontstyle' : 'oblique', 'color' : 'Grey'})
plt.pie(p, labels= p.index)
plt.show()