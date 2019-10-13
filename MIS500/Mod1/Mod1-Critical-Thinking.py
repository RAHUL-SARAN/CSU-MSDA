#########################################################################
#Python Statistical Data Visualization - Plotting data for presentation
#########################################################################
# import matplotlib library and assign it to a simple alias for later use
# matplotlib is a library to generate different kind of data visualisations.
import matplotlib.pyplot as mplt
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
faculty_df = pd.DataFrame({
    'faculty_name':['Peter','Lisa','John','Jose','Bill','Mary','Jeff'],
    'faculty_age':[22,77,21,18,44,32,19],
    'faculty_gender':['M','F','M','F','M','F','M'],
    'faculty_state':['CA','DC','CA','DC','VA','NY','NY'],
    'faculty_children':[3,1,0,2,3,2,4],
    'faculty_pets':[4,2,0,6,1,2,3]
})
print(faculty_df)
#1 Generate a scatter plot comparing faculty_children and faculty_pets
faculty_df.plot(kind='scatter',x='faculty_children',y='faculty_pets',color='red')
mplt.show()

#2 Generate a simple bar plot between faculty_name and faculty_age
faculty_df.plot(kind='bar',x='faculty_name',y='faculty_age')
mplt.show()

#3 Generate more than 1 line plots. Different line plots are distinguished with their color
ax = mplt.gca()
faculty_df.plot(kind='line',x='faculty_name',y='faculty_children',ax=ax)
faculty_df.plot(kind='line',x='faculty_name',y='faculty_pets', color='red', ax=ax)
mplt.show()

#4 Generate Stacked bar plot to show count of people for different state and split by faculty gender
faculty_df.groupby(['faculty_state','faculty_gender'])['faculty_name'].size().unstack().plot(kind='bar',stacked=True)
faculty_df.sample(n=3)
mplt.show()

#5 Generate a stacked bar Plot with count of people by faculty gender, spliting by faculty state:
faculty_df.groupby(['faculty_gender','faculty_state'])['faculty_age'].size().unstack().plot(kind='bar',stacked=True)
mplt.show()

#6 Generate a violinplot for faculty age
fig, ax = mplt.subplots()
ax.violinplot(faculty_df["faculty_age"], vert=False)
mplt.show()

#7 Generate a Plot of the distribution of faculty children
num_bins = 10
# Attribute normed is depricated and replaced by density
#plt.hist(df['num_children'], num_bins, normed=1, facecolor='blue', alpha=0.5)
mplt.hist(faculty_df['faculty_children'], num_bins, density=1, facecolor='blue', alpha=0.5)
mplt.show()

#8 Use Seaborn Library to contruct a pet plot
sns.set()
# Set context to `"paper"`
sns.set_context("paper")
# Construct pets plot
sns.swarmplot(x="faculty_pets", y="faculty_age", data=faculty_df)
# Show plot
mplt.show()

#9 Save last plot to a file with Permanent link
# the plot gets saved to 'graphoutput.png' image file
mplt.savefig('graphoutput.png')
