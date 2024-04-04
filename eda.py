import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import phik
import plotly.express as px

st.set_page_config(
    # Bikin judul title page
    page_title= 'Final Project Group 2'
)

def run():
    # Membuat Judul
    st.title('House Pricing Prediction')
    # Membuat subheader
    st.subheader('Exploratory Data Analysis (EDA)')
    # Load Data
    df_eda = pd.read_csv('dataset_tableau_clean_1.csv')
    # Untuk menghilangkan pesan peringatan
    st.set_option('deprecation.showPyplotGlobalUse', False)

    with st.expander("HeatMap Correlation"):
        # Menghitung matriks korelasi menggunakan Phik
        heatmap_corr = df_eda.phik_matrix()
        # Menampilkan heatmap menggunakan Seaborn dan Matplotlib di Streamlit
        st.write("Correlation Heatmap:")
        fig, ax = plt.subplots()
        sns.heatmap(heatmap_corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        plt.title('Correlation Heatmap')
        st.pyplot(fig)

        st.markdown("""
         Insight: There is a fairly high correlation between several features and the target property price (Price) with a threshold of 0.3, namely image_id, citi, street, bed, bath, and sqft. This suggests that characteristics such as the type of drawing, the location of the property (both city and street), and the size and number of bedrooms and bathrooms have the potential to have a significant influence on the price of the property.          
        """)

    with st.expander("Distribution House Category"):
        plt.figure(figsize=(15, 8))
        sns.countplot(data=df_eda, x='house_cat', palette='husl')

        # Menambahkan nilai di setiap bar
        for bar in plt.gca().patches:
            height = bar.get_height()
            plt.gca().annotate(f'{int(height)}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 5),  # 5 points vertical offset
                       textcoords="offset points",
                       ha='center', va='bottom')

        plt.title("Distribution of House Category")
        plt.tight_layout()
        # Menampilkan plot menggunakan Streamlit
        st.pyplot(plt)
        st.markdown("""
         Insight: In the analysis of the three groups of houses created, it was found that intermediate houses had the highest frequency compared to other groups of houses. These findings show that in the data set analyzed, properties with the characteristics of intermediate houses are the most common or most frequently encountered type of property.          
        """)

    with st.expander("Distribution Bedroom by House Category"):
        plt.figure(figsize=(15, 8))
        sns.countplot(data=df_eda, x='bed', hue='house_cat', palette='husl')

        # Menambahkan nilai di setiap bar
        for bar in plt.gca().patches:
            height = bar.get_height()
            plt.gca().annotate(f'{height}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),  # 3 points vertical offset
                       textcoords="offset points",
                       ha='center', va='bottom')

        plt.title("Distribution Bedroom by House Category")
        plt.tight_layout()
        # Menampilkan plot menggunakan Streamlit
        st.pyplot(plt)
        st.markdown("""
         Insight: From the visualization of the data presented, it can be seen that the majority of houses in the intermediate and basic categories have three bedrooms, while the majority of houses in the luxury category have four bedrooms. These findings illustrate a clear pattern in the distribution of the number of bedrooms among the three housing categories          
        """)        

    with st.expander("Distribution Bathroom by House Category"):
        plt.figure(figsize=(15, 8))
        sns.countplot(data=df_eda, x='bath', hue='house_cat', palette='husl')

        # Menambahkan nilai di setiap bar
        for bar in plt.gca().patches:
            height = bar.get_height()
            plt.gca().annotate(f'{height}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),  # 3 points vertical offset
                       textcoords="offset points",
                       ha='center', va='bottom')

        plt.title("Distribution Bathroom by House Category")
        plt.tight_layout()
        # Menampilkan plot menggunakan Streamlit
        st.pyplot(plt)
        st.markdown("""
         Insight: In the data visualization presented, it can be seen that the majority of houses in the intermediate and basic categories have two bathrooms, while the majority of houses in the luxury category have three bathrooms. These findings illustrate a clear pattern in the distribution of the number of bathrooms among the three housing categories.          
        """)        

    with st.expander("Cities with The Highest and Lowest House Prices"):
        # Menghitung harga rata-rata per kota dan mengurutkannya
        mean_prices = df_eda.groupby('citi')['price'].mean().sort_values()

        # Memisahkan 10 kota dengan harga tertinggi dan 10 kota dengan harga terendah
        top_10_highest = mean_prices[-10:]  # 10 kota dengan rata-rata harga tertinggi
        top_10_lowest = mean_prices[:10]    # 10 kota dengan rata-rata harga terendah
        
        st.write("10 Cities with the Lowest Average House Prices")
        st.bar_chart(top_10_lowest)
        st.markdown("""
         Insight: From the data visualization, it can be seen that the 10 cities with the lowest house prices in California include Oro Grande, Delano, Rimforest, Barstow, Sugarloaf, Green Valley Lake, Landers, Lake Los Angeles, California City, and Santa Clarita. These findings suggest that properties in these cities are more affordable compared to the average property in the California region. It is likely that factors such as location, infrastructure and local market needs may influence property prices in these cities.         
        """)  
        st.markdown('---')
        # Membuat barplot untuk 10 kota dengan harga tertinggi
        st.write("10 Cities with the Highest Average House Prices")
        st.bar_chart(top_10_highest)
        st.markdown("""
         Insight: On the other hand, the 10 cities with the highest home prices in California include La Jolla, Venice, West Hollywood, Rancho Santa Fe, Westchester, Villa Park, Palos Verdes Estates, Solvang, Corona del Mar, and Newport Coast. These findings suggest that properties in these cities tend to command higher prices, which may be due to factors such as prestigious locations, luxury amenities and the special appeal of each region.          
        """)

    with st.expander("Example of House Images"):             
        st.image("sample1.png")
        st.markdown('---')
        st.image("sample2.png")
        st.markdown('---')
        st.image("sample3.png")
        st.markdown('---')
        st.image("sample4.png")
        st.markdown('---')
        st.image("sample5.png")
        st.markdown('---')
if __name__ == "__main__":
    run()