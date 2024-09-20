import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
x=(1,2,3,4,5)
y=(2,4,6,8,10)
df=pd.DataFrame({"in":x,"out":y})
sns.scatterplot(x="in",y='out',data=df,color="red",marker="o")

plt.plot(df["in"],df['out'],color="red",marker="o")
plt.xlabel("x data")
plt.ylabel("y data")
plt.grid(True)
plt.show()

data=pd.read_csv("elections.csv")
print(data["Party"])
count=data["Party"].value_counts()
print(count)
plt.figure(figsize=(10,7))
plt.pie(count,labels=count.index,autopct='%4.2f%%',startangle=140)
plt.show()

data={'name':["A","B","C","D"],'rank':[2,3,4,5]}
df=pd.DataFrame(data)
print(df)
explode_data=(0,0,0.1,0)
colors_data=("blue","pink","orange",'yellow')
plt.figure(figsize=(10,7))
plt.pie(df["rank"],labels=df["name"],explode=explode_data,colors=colors_data,autopct='%5.3f%%',startangle=140)
plt.show()

np.random.seed(50)
good=np.random.normal(size=100)
df=pd.DataFrame(good,columns=["good_data"])
print(df)

bad=np.random.normal(size=100)
bad=np.append(bad,[20,30,10])
print(bad)
df1=pd.DataFrame(bad,columns=["bad_data"])
print(df1)


plt.subplot(1,2,2)
plt.boxplot(df['good_data'],vert=False)
plt.title("good data")


plt.subplot(1,2,1)
plt.boxplot(df1['bad_data'],vert=False)
plt.title("bad data")
plt.tight_layout()
plt.show()








