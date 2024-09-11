import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
gold_data = pd.read_csv('gld_price_data.csv')

def show_explore_page():
    st.title("Explore Details of Gold Price")

    # Warning message on Streamlit
    st.warning("Gold Price Data Exploration")

    # Distribution plot for GLD price
    st.write("#### Distribution of GLD Price")
    fig, ax = plt.subplots()
    sns.histplot(gold_data['GLD'], color='Purple', ax=ax)  # Use sns.histplot instead of sns.displot for direct plotting on ax
    st.pyplot(fig)

    # Correlation heatmap
    st.write("#### Correlation Heatmap")
    correlation = gold_data.drop('Date', axis=1).corr()

    # Constructing a heatmap
    fig1, ax1 = plt.subplots(figsize=(10, 10))  # Define figsize in subplots
    sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap="Greens", ax=ax1)
    st.pyplot(fig1)