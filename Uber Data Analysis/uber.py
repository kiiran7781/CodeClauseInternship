import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('UBER_DATA_ANALYSIS.csv')

import streamlit as st
import plotly.express as px


st.title("Trip Analysis")

st.header("Task 1: Most Frequent Starting Places")
st.plotly_chart(px.bar(
    df['START*'].value_counts().nlargest(10),
    x=df['START*'].value_counts().nlargest(10).index,
    y=df['START*'].value_counts().nlargest(10).values,
    labels={'x': 'The Starting Places For our Trips', 'y': 'Number of Trips'},
    title='Most Frequent Starting Places For our Trips'
))

st.header("Task 2: Mean of Miles for Each Purpose")
sns_plot = sns.barplot(
    x=df['MILES*'],
    y=df['PURPOSE*'],
    order=df.groupby('PURPOSE*')['MILES*'].mean().sort_values(ascending=False).index,
    color="blue"
)
sns_plot.set(xlabel="The Mean of Miles", ylabel="Trip Purpose", title="The Mean of Miles for Each Purpose")
st.pyplot(sns_plot.figure)

st.header("Task 3: Mean of Miles for Each Ending Point")
sns_plot = sns.barplot(
    x=df['MILES*'],
    y=df['STOP*'],
    order=df.groupby('STOP*')['MILES*'].mean().sort_values(ascending=False).nlargest(10).index,
    color="blue"
)
sns_plot.set(xlabel="The Mean of Miles", ylabel="Trips Ending point", title="The Mean of Miles for Each Ending Point")
st.pyplot(sns_plot.figure)

st.header("Task 4: Mean of Miles for Each Starting Point")
sns_plot = sns.barplot(
    x=df['MILES*'],
    y=df['START*'],
    order=df.groupby('START*')['MILES*'].mean().sort_values(ascending=False).nlargest(10).index,
    color="blue"
)
sns_plot.set(xlabel="The Mean of Miles", ylabel="Trips Starting Point", title="The Mean of Miles for Each Starting Point")
st.pyplot(sns_plot.figure)

st.header("Task 5: Most Frequent Ending Places")
st.plotly_chart(px.bar(
    df['STOP*'].value_counts().nlargest(10),
    x=df['STOP*'].value_counts().nlargest(10).index,
    y=df['STOP*'].value_counts().nlargest(10).values,
    labels={'x': 'The Ending Places For our Trips', 'y': 'Number of Trips'},
    title='Most Frequent Ending Places For our Trips'
))

st.header("Task 6: Mean of Miles for Each Category")
sns_plot = sns.barplot(
    x=df['MILES*'],
    y=df['CATEGORY*'],
    order=df.groupby('CATEGORY*')['MILES*'].mean().sort_values(ascending=False).index,
    color="blue"
)
sns_plot.set(xlabel="The Mean of Miles", ylabel="Trip Category", title="The Mean of Miles for Each Category")
st.pyplot(sns_plot.figure)

