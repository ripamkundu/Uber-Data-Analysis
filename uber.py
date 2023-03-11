import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data=pd.read_csv('uber_dataset.csv')
plt.plot(data['humidity'])
plt.show()
print(data.describe())

a=data.shape
print(a)
##The Name of the driver and the the total number of trips done by that driver
n=pd.DataFrame(data['driver_name_en'].value_counts())
print(n)

##The Name of the city and the number of times the cities were visited in trips
c=pd.DataFrame([data['city'].value_counts()],index=[1])
print(c)


fig=plt.figure()
k=plt.axes(projection='3d')
x1=data['surge_multiplier'].values
y1=data['temperature_value'].values
z1=data['feels_like'].values
k.scatter(x1,y1,z1,c='Indigo')
k.set_title('3d Scatter Plot')
g=plt.show()
print(g)

x2=data['rub_usd_exchange_rate'].values
y2=data['price_rub'].values
z2=np.loadtxt('uber_dataset.csv')
fig1=plt.figure()
t=fig.add_subplot(111,projection='3d')
t.contour3D(x2,y2,z2,cmap='ocean')
p=plt.show()
print(p)





