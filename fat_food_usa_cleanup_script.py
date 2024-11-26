"""
Name: Muna Mohamed
CS230: Section 5
Data: fast_food_usa.csv
"""

# Importing Libraries
import pandas as pd

# Reading the csv to a dataframe
df = pd.read_csv('fast_food_usa.csv')

# Printing out the head of the dataframe
df.head()


# Importing libraries 
import streamlit as st
import pandas as pd


# Cleaning up data for Streamlit app
df = pd.read_csv('fast_food_usa.csv')

# Renaming columns so its easier to use in Streamlit App
df.rename(columns = {'city': 'City', 'province': 'State', 'postalCode': 'Postal Code', 'longitude':'Longitude', 
'latitude':'Latitude', 'name': 'Restaurant Name'}, inplace=True) # Setting inplace true to keep changes in df



# Cleaning/Normalizing Restaurant Name values for McDonald's
mcd_variations = ['Mcdonalds', 'McDonalds', "Mcdonald's", 'Mc Donalds', "McDonalds's", 
"Mcdonalds Whitehouse", "McDonald's of Rolesville", "The Arch at McDonald's Campus Office Building"]
df['Restaurant Name'] = df['Restaurant Name'].replace(mcd_variations, "McDonald's")

# Cleaning/Normalizing Restaurant Name values for Arbys
ar_variations = ['Arbys', "Arby's"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ar_variations, "Arby's")

# Cleaning/Normalizing Restaurant Name values for Auntie Anne's
aap_variations = ["Auntie Anne's", "Auntie Anne's Pretzels"]
df['Restaurant Name'] = df['Restaurant Name'].replace(aap_variations, "Auntie Anne's")

# Cleaning/Normalizing Restaurant Name values for combination Tacobell/KFC
tbk_variations = ["Taco Bell/KFC", "Taco Bell/KFC", "KFC/Taco Bell", "TacoBell/KFC",
"TacoBell / KFC"]
df['Restaurant Name'] = df['Restaurant Name'].replace(tbk_variations, "Tacobell/KFC")

# Cleaning/Normalizing Restaurant Name values for KFC
tbk_variations = ["KFC", "KFC Kentucky Fried Chicken"]
df['Restaurant Name'] = df['Restaurant Name'].replace(tbk_variations, "KFC")

# Cleaning/Normalizing Restaurant Name values for Burger King
bk_variations = ["Burger King", "Burger King¬Æ"]
df['Restaurant Name'] = df['Restaurant Name'].replace(bk_variations, "Burger King")

# Cleaning/Normalizing Restaurant Name values for B-Good
bg_variations = ["B Good", "B.GOOD", "B-Good","b.good"]
df['Restaurant Name'] = df['Restaurant Name'].replace(bg_variations, "B.Good")

# Cleaning/Normalizing Restaurant Name values for Bakers Drive Thru
bdt_variations = ["Baker's Drive Thru", "Baker's Drive-thru"]
df['Restaurant Name'] = df['Restaurant Name'].replace(bdt_variations, "Bakers Drive Thru")

# Cleaning/Normalizing Restaurant Name values for Chic-fil-a
cfa_variations = ["Chick-Fil-A", "Chick-fil-A"]
df['Restaurant Name'] = df['Restaurant Name'].replace(cfa_variations, "Chick-fil-a")

# Cleaning/Normalizing Restaurant Name values for Dairy Queen
dq_variations = ["Dairy Queen", "Dairy Queen (Treat Only)" , "Wolf's Dairy Queen"]
df['Restaurant Name'] = df['Restaurant Name'].replace(dq_variations, "Dairy Queen")

# Cleaning/Normalizing Restaurant Name values for Qdoba
q_variations = ["Qdoba Mexican Eats", "QDOBA Mexican Eats", "Qdoba Mexican Grill"]
df['Restaurant Name'] = df['Restaurant Name'].replace(q_variations, "QDOBA")

# Cleaning/Normalizing Restaurant Name values for Zaxby's
zx_variations = ["Zaxby's", "Zaxby's Chicken Fingers & Buffalo Wings"]
df['Restaurant Name'] = df['Restaurant Name'].replace(zx_variations, "Zaxby's")

# Cleaning/Normalizing Restaurant Name values for Foster's Freeze
ff_variations = ["Foster's Freeze", "Fosters Freeze"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ff_variations, "Fosters's Freeze")

# Cleaning/Normalizing Restaurant Name values for Jimmy Johns
jj_variations = ["Jimmy John's", "Jimmy Johns"]
df['Restaurant Name'] = df['Restaurant Name'].replace(jj_variations, "Jimmy John's")

# Cleaning/Normalizing Restaurant Name values for Little Caesar's
lc_variations = ["Little Caesar's Pizza", "Little Caesars","Little Caesars Pizza"]
df['Restaurant Name'] = df['Restaurant Name'].replace(lc_variations, "Little Caesar's")

# Cleaning/Normalizing Restaurant Name values for Long John 
ljs_variations = ["Long John Silvers", "Long John Silver's"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ljs_variations, "Long John Silver's")

# Cleaning/Normalizing Restaurant Name values for combination Long Jouhn Silver and AW
ljsaw_variations = ["Long John Silver's/AW", "Long John Silvers/A&W", "Long John Silvers / A&W", 
"Long John Silver's / AW"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ljsaw_variations, "Long John Silver's/A&W")

# Cleaning/Normalizing Restaurant Name values for Mr Hero
mh_variations = ["Mr Hero", "Mr.Hero"]
df['Restaurant Name'] = df['Restaurant Name'].replace(mh_variations, "Mr.Hero")

# Cleaning/Normalizing Restaurant Name values for Panda Express
pe_variations = ["Panda Express", "Panda Express Innovation Kitchen"]
df['Restaurant Name'] = df['Restaurant Name'].replace(pe_variations, "Panda Express")

# Cleaning/Normalizing Restaurant Name values for PepperJax Grill
pjg_variations = ["PepperJax Grill", "Pepperjax Grill"]
df['Restaurant Name'] = df['Restaurant Name'].replace(pjg_variations, "PepperJax Grill")

# Cleaning/Normalizing Restaurant Name values for Popeyes
pe_variations = ["Popeyes", "Popeyes Chicken & Biscuits", "Popeyes Chicken Biscuits", "Popeyes Louisiana Kitchen", 
"Popeye's Louisiana Kitchen"]
df['Restaurant Name'] = df['Restaurant Name'].replace(pe_variations, "Popeyes")

# Cleaning/Normalizing Restaurant Name values for Quiznos
qs_variations = ["Quizno's", "Quiznos", "Quiznos Sub"]
df['Restaurant Name'] = df['Restaurant Name'].replace(qs_variations, "Quizno's")

# Cleaning/Normalizing Restaurant Name values for Rausing Canes
rc_variations = ["Raising Cane's", "Raising Canes", "Raising Cane's Chicken Fingers"]
df['Restaurant Name'] = df['Restaurant Name'].replace(rc_variations, "Raising Cane's")

# Cleaning/Normalizing Restaurant Name values for Rally's
r_variations = ["Rally's","Rallys", "Rally's Hamburgers"]
df['Restaurant Name'] = df['Restaurant Name'].replace(r_variations, "Rally's")

# Cleaning/Normalizing Restaurant Name values for Roma Pizza
rp_variations = ["Roma Pizza", "Romas Pizza"]
df['Restaurant Name'] = df['Restaurant Name'].replace(rp_variations, "Roma Pizza")

# Cleaning/Normalizing Restaurant Name values for Subway
s_variations = ["SUBWAY", "SUBWAY¬Æ"]
df['Restaurant Name'] = df['Restaurant Name'].replace(s_variations, "Subway")

# Cleaning/Normalizing Restaurant Name values for Sonic
sdi_variations = ["SONIC Drive In", "SONIC Drive-In", "Sonic", "Sonic Drive In",
"Sonic Drive in", "Sonic Drive-In", "Sonic America's Drive-In"]
df['Restaurant Name'] = df['Restaurant Name'].replace(sdi_variations, "Sonic")

# Cleaning/Normalizing Restaurant Name values for Steak N Shake
ss_variations = ["Steak 'n Shake", "Steak N Shake", "Steak N Shake "]
df['Restaurant Name'] = df['Restaurant Name'].replace(ss_variations, "Steak N Shake")

# Cleaning/Normalizing Restaurant Name values for Wingstop
ws_variations = ["Wingstop", "Wingstop Restaurant"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ws_variations, "Wingstop")

# Cleaning/Normalizing Restaurant Name values for Wienerschnitzel
wss_variations = ["Wienerschitzel", "Wienerschnitzel"]
df['Restaurant Name'] = df['Restaurant Name'].replace(wss_variations, "Wienerschnitzel")

# Cleaning/Normalizing Restaurant Name values for Captain D's
cds_variations = ["Captain D's", "Captain D's Seafood"]
df['Restaurant Name'] = df['Restaurant Name'].replace(cds_variations, "Captain D's")

# Cleaning/Normalizing Restaurant Name values for Capri Italian Restaurant
cir_variations = ["Capri Italian Restaurant", "Capri Italian Restaurant"]
df['Restaurant Name'] = df['Restaurant Name'].replace(cir_variations, "Capri Italian Restaurant")

# Cleaning/Normalizing Restaurant Name values for Carls Jr
cj_variations = ["Carl's Jr", "Carl's Jr."]
df['Restaurant Name'] = df['Restaurant Name'].replace(cj_variations, "Carls Jr")

# Cleaning/Normalizing Restaurant Name values for combination Carls Jr/Green Burrito
ccj_variations = ["Carl's Jr", "Carl's Jr./Green Burrito", "Carl's Jr./The Green Burrito",
"Carl's Jr./ Green Burrito", "Carl's Jr. / Green Burrito"]
df['Restaurant Name'] = df['Restaurant Name'].replace(ccj_variations, "Carls Jr")

# Cleaning/Normalizing Restaurant Name values for Chipotle
cmg_variations = ["Chipotle","Chipotle Mexican Grill"]
df['Restaurant Name'] = df['Restaurant Name'].replace(cmg_variations, "Chipotle")

# Cleaning/Normalizing Restaurant Name values for Dunkin
dds_variations = ["Dunkin' Donuts","Dunkin Donuts", "Dunkin"]
df['Restaurant Name'] = df['Restaurant Name'].replace(dds_variations, "Dunkin Donuts")

# Cleaning/Normalizing Restaurant Name values for Five Guys
fg_variations = ["Five Guys", "Five Guys Burger and Fries", "Five Guys Burgers Fries"]
df['Restaurant Name'] = df['Restaurant Name'].replace(fg_variations, "Five Guys")

# Cleaning/Normalizing Restaurant Name values for Hardees
h_variations = ["Hardee's", "Hardees"]
df['Restaurant Name'] = df['Restaurant Name'].replace(h_variations, "Hardee's")

# Cleaning/Normalizing Restaurant Name values for Combo Hardees/Red Burrito
hrb_variations = ["Hardee's/Red Burrito", "Hardee's/red Burrito", "Hardee's/ Red Burrito", 
"Hardee's / Red Burrito"]
df['Restaurant Name'] = df['Restaurant Name'].replace(hrb_variations, "Hardee's/Red Burrito")

# Cleaning/Normalizing Restaurant Name values for Jack in the Box
jitb_variations = ["Jack In The Box", "Jack in the Box", "Jack in the Box -"]
df['Restaurant Name'] = df['Restaurant Name'].replace(jitb_variations, "Jack in the Box")

# Cleaning/Normalizing Restaurant Name values for Toppers Pizza
tp_variations = ["Topper's Pizza", "Toppers Pizza"]
df['Restaurant Name'] = df['Restaurant Name'].replace(tp_variations, "Topper's Pizza")


# Removing restaurants with 'closed' in the name
df = df[~df['Restaurant Name'].str.contains('closed', case=False, na=False)]
df = df[~df['Restaurant Name'].str.contains('Closed', case=False, na=False)]

# Removing T-Mobile
df = df[~df['Restaurant Name'].str.contains('T-Mobile', case=False, na=False)]

# Removing Walmart
df = df[~df['Restaurant Name'].str.contains('Walmart', case=False, na=False)]
df = df[~df['Restaurant Name'].str.contains('Walmart Supercenter', case=False, na=False)]




# Exporting data frame so I can use this in the Streamlit App
df.to_csv('fast_food_usa_cleaned.csv', index=False)
