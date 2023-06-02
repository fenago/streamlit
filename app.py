# https://docs.streamlit.io/library/cheatsheet
import streamlit as st
st.title('My CE App') # Sets the the title of your page
st.header('Data Visualization Section')  # Sets a header for a section
st.subheader('Subsection: Pie Chart Analysis')  # Sets a subheader for a subsection
st.text('This section focuses on data preprocessing.')
st.markdown('**This is some bold text**')
import pandas as pd

data = {
    'A': [45, 37, 89, 67],
    'B': ['John', 'Max', 'Lisa', 'Chris']
}
df = pd.DataFrame(data)

st.write(df)

age = st.slider('Your age', min_value=0, max_value=100)  # Returns the value selected by the user
if st.button('Say Hello'):  # Returns True if the user clicks the button
    st.write('Hello!')
show_df = st.checkbox('Show DataFrame')  # Returns True if the user checks the box, False otherwise
if show_df:
    st.write(df)

    
import pandas as pd

# Creating a pandas DataFrame
data = {
    'names': ['John', 'Anna', 'George', 'Mia'],
    'ages': [23, 45, 37, 19]
}
df = pd.DataFrame(data)

import streamlit as st

# Display the DataFrame in Streamlit
st.dataframe(df)

# Display descriptive statistics of 'ages'
st.write(df['ages'].describe())

# Add 'Adult' column
df['Adult'] = df['ages'].apply(lambda x: 'Yes' if x >= 18 else 'No')

# Display DataFrame in Streamlit
st.dataframe(df)


import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import streamlit as st

# Load the iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display the DataFrame in Streamlit
st.dataframe(df)

# Show general information about the dataset
st.text(df.info())

# Show statistical information about the dataset
st.write(df.describe())

# Select a feature to display histogram
feature = st.selectbox('Select a feature', df.columns)

# Plot histogram
fig, ax = plt.subplots()
ax.hist(df[feature], bins=20)

# Set the title and labels
ax.set_title(f'Histogram of {feature}')
ax.set_xlabel(feature)
ax.set_ylabel('Frequency')

# Display the plot
st.pyplot(fig)


import matplotlib.pyplot as plt
import seaborn as sns

# Select features to display scatter plot
feature_x = st.selectbox('Select feature for x axis', df.columns)
feature_y = st.selectbox('Select feature for y axis', df.columns)

# Display scatter plot
fig, ax = plt.subplots()
sns.scatterplot(data=df, x=feature_x, y=feature_y, hue=iris.target, ax=ax)
st.pyplot(fig)
