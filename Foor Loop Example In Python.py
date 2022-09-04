#!/usr/bin/env python
# coding: utf-8

# # Basic Python_Loop

# In[1]:


fruits=["apple"],["banana"],["cherry"]
for x in fruits:
    print (x)


# In[5]:


for x in "apple":
     print(x)


# In[6]:


for x in range(10):
    print (x)


# In[7]:


for x in range(2,30,3):
    print (x)


# In[9]:


for x in range(10):
   print (x)
else:
       print("End")


# In[13]:


first=["red","big","tasty"]
second=["apple","banana","cherry"]
for x in first:
    for y in second:
        print(x)


# In[14]:


first=["red","big","tasty"]
second=["apple","banana","cherry"]
for x in first:
    for y in second:
        print(x,y)


# In[19]:


num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")


# # Write a Python program to construct the following pattern, using a nested for loop.

# In[2]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	


# # Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

# In[5]:


lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)
	


# # Write a Python program to print alphabet pattern 'A'.

# In[ ]:


# result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);


# # Write a Python program to display astrological sign for given date of birth.

# In[9]:


day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)


# # Python program to draw square

# In[1]:


import turtle
skk = turtle.Turtle()

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()


# # Python program to draw star

# In[4]:


import turtle
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
	star.right(144)
	star.forward(100)
	
turtle.done()


# # Python program to draw hexagon

# In[ ]:


import turtle
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)
	
turtle.done()


# # Python program to draw Spiral Helix Pattern

# In[ ]:


import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.exitonclick()


# In[ ]:




