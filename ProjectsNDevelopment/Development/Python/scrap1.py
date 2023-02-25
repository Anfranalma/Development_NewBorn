
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##Get the website

webpage=requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

##parse the website

soup= BeautifulSoup(webpage.content,"html.parser")



##get the tags for ratings
all_ratings=soup.find_all(attrs={'class':'Rating'})

##get the tags for company name
all_companies=soup.find_all(attrs={'class':'Company'})

##get the cocoa percent
all_cocoaPercent=soup.find_all(attrs={'class':'CocoaPercent'})

##get only the text on each tag
ratings=[]
##get only the company names on each tag
companies=[]
##get only the cocoapercent on each tag
cocoap=[]
for rating in all_ratings[1:]:
  ratings.append(float(rating.string))

for company in all_companies[1:]:
  companies.append(company.string)

for cocoa in all_cocoaPercent[1:]:
  cocoap.append(int(float(cocoa.string[:-1])))

print(cocoap)


#Checking historigram from chacolate ratings
plt.hist(ratings)
plt.show()

#create the data frame for companies and ratings
d={"Company": companies, "Rating": ratings, "CocoaPercent": cocoap}
graphic=pd.DataFrame.from_dict(d)
graphic.head()

avg_ratings=graphic.groupby("Company").Rating.mean()
top_10=avg_ratings.nlargest(10)
print(top_10)
plt.cla()
plt.scatter(graphic.CocoaPercent,graphic.Rating)
plt.show()
plt.cla()
z = np.polyfit(graphic.CocoaPercent, graphic.Rating, 1)
line_function = np.poly1d(z)
plt.plot(graphic.CocoaPercent, line_function(graphic.CocoaPercent), "r--")


##We have explored a couple of the questions about chocolate that inspired us when we looked at this chocolate table.

##What other kinds of questions can you answer here? Try to use a combination of BeautifulSoup and Pandas to explore some more.

##For inspiration: Where are the best cocoa beans grown? Which countries produce the highest-rated bars?



