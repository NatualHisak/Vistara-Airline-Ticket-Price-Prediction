import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

def run():
    #membuat title

    st.title('Vistara Airline price prediction')

    #membuat Sub Header
    st.subheader('EDA untuk analisa Dataset Vistara Airline')

    #Membuat deskripsi
    st.write("Page ini dibuat oleh Muhamad Natual Hisak")

    #Menambahkan gambar

    image = Image.open('Vistara.jpg')
    st.image(image,caption = 'Vistara Airline')

    #membuat garis lurus
    st.markdown('---')

    #Show Dataframe
    data = pd.read_csv(r'C:\Users\Omen\Desktop\Hacktiv8\P1\Milestone 2\Vistara.csv')
    st.dataframe(data)

    #Membuat Piechart class
    st.write('#### Business Class vs Economy Class')
    fig = plt.figure(figsize =(10,6))
    plt.title('Percentage of Economy and Business class Flights', fontsize=15, color='Blue')
    data['class'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel('')
    plt.show()
    st.pyplot(fig)

    # Membuat lineplot days_left
    st.write('#### days_left to price')
    fig2 = plt.figure(figsize=(15,5))
    sns.lineplot(data=data,x='days_left',y='price',color='blue')
    plt.title('Days Left For Departure Versus Ticket Price',fontsize=15)
    plt.xlabel('Days Left for Departure',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.show()
    st.pyplot(fig2)

    # Membuat barchart price vs departure_time
    st.write('#### Ticket price based on the Departure time')
    fig3 = sns.catplot(data=data, kind="bar", x="departure_time", y="price", height=6.5, aspect=12/6.5 ,palette='Paired')
    plt.title('Ticket price based on the Departure time',fontsize=15)
    plt.xlabel('Departure Time',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.show()
    st.pyplot(fig3)

    # Membuat barchart price vs destination_city
    st.write('#### Ticket price based on the Destinantion City')
    fig4 = sns.catplot(data=data, kind="bar", x="destination_city", y="price", height=6.5, aspect=12/6.5 ,palette='Paired')
    plt.title('Ticket price based on the Destinantion City',fontsize=15)
    plt.xlabel('Destinantion City',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.show()
    st.pyplot(fig4)

    # Membuat barchart price vs source_city
    st.write('#### Ticket price based on source_city')
    fig5 = sns.catplot(data=data, kind="bar", x="source_city", y="price", height=6.5, aspect=12/6.5 ,palette='Paired')
    plt.title('Ticket price based on source_city',fontsize=15)
    plt.xlabel('source_city',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.show()
    st.pyplot(fig5)

    # Membuat barchart price vs stops
    st.write('#### Ticket price based on stops')
    fig6 = sns.catplot(data=data, kind="bar", x="stops", y="price", height=6.5, aspect=12/6.5 ,palette='Paired')
    plt.title('Ticket price based on stops',fontsize=15)
    plt.xlabel('Stops',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.show()
    st.pyplot(fig6)
if __name__ == '__main__':
    run()