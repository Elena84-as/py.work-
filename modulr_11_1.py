import numpy as np
from matplotlib.pyplot import show, subplots

#1
fig,ax = subplots()
ax.set_title('график')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.set_xlim((-5,5))
ax.set_ylim((-5,5))
ax.grid()
x = np.linspace(-5,5,100)
y = 1/x
ax.plot(x,y)

show()


import webp


from PIL import (Image, ImageFilter)

#2
image_path = 'C:\\Users\\evama\\Documents\\pythonProject10\\as.jpg'
orig = Image.open(image_path)
print(orig.format,orig.size,orig.mode)

img = orig.filter(ImageFilter.CONTOUR)

img.show()



import requests

#3
url = 'https://www.youtube.com/results'
query = {'search_query': 'barby'}
response = requests.get(url,params=query)

print(response.headers,'headers')
print(response.status_code,'status_code')
print(response.url, 'url')



#4

matrix = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(matrix)
print(matrix.reshape(6,2))
print(np.resize(matrix,(3,2)))
print(np.delete(matrix,1,axis = 1))







