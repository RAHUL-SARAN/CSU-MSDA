#########################################################################
#Python Statistical Data Visualization - Plotting data for presentation
#########################################################################
# import matplotlib library and assign it to a simple alias for later use
# matplotlib is a library to generate different kind of data visualisations.
import matplotlib.pyplot as plt
# import pandas library and assign it to a simple alias for later use
# pandas is a library to transform data into required form
import pandas as pd
# import seaborn library and assign it to a simple alias for later use
# seaborn is another data visualisation library built on matplotlib
import seaborn as sns

"""
Create Data_Frame from a sample array. 
This dataframe will have different faculties as rows and their attributes as columns 
"""
df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','F','M','F','M'],
    'state':['CA','DC','CA','DC','VA','NY','NY'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})
print(df)
#1 Generate a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.show()

#2 Generate a simple bar plot between name and age
df.plot(kind='bar',x='name',y='age')
plt.show()

#3 Generate more than 1 line plots. Different line plots are distinguished with their color
ax = plt.gca()
df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)
plt.show()

#4 Generate Stacked bar plot to show count of people for different state and split by gender
df.groupby(['state','gender'])['name'].size().unstack().plot(kind='bar',stacked=True)
df.sample(n=3)
plt.show()

#5 Generate a stacked bar Plot with count of people by gender, spliting by state:
df.groupby(['gender','state'])['age'].size().unstack().plot(kind='bar',stacked=True)
plt.show()

#6 Generate a violinplot for age
fig, ax = plt.subplots()
ax.violinplot(df["age"], vert=False)
plt.show()

#7 Generate a Plot of the distribution of faculty children
num_bins = 10
# Attribute normed is depricated and replaced by density
#plt.hist(df['num_children'], num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.hist(df['num_children'], num_bins, density=1, facecolor='blue', alpha=0.5)
plt.show()

#8 Use Seaborn Library to contruct a pet plot
sns.set()
# Set context to `"paper"`
sns.set_context("paper")
# Construct pets plot
sns.swarmplot(x="num_pets", y="age", data=df)
# Show plot
plt.show()

#9 Save last plot to a file with Permanent link
# the plot gets saved to 'graphoutput.png' image file
plt.savefig('graphoutput.png')
