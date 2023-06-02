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
