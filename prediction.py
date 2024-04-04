import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import sqlite3

#load model
model = load_model('model.h5')

#load pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# # Fungsi untuk menyimpan data ke dalam file CSV
# def save_to_csv(data):
#     # Membaca dataframe kosong
#     df_empty = pd.read_csv('data_raw.csv')

#     # Mengubah data inputan menjadi dataframe
#     df_input = pd.DataFrame(data, index=[0])

#     # Menggabungkan dataframe kosong dengan dataframe inputan
#     df_combined = pd.concat([df_empty, df_input], ignore_index=True)

#     # Menyimpan dataframe gabungan ke dalam file CSV
#     df_combined.to_csv('data_raw.csv', index=False)

conn = sqlite3.connect('property_database.db')

def run():
    # Membuat Judul
    st.title('House Pricing Prediction')
    # Membuat subheader
    st.subheader('Prediction')

    def preprocess_image(uploaded_image, target_size=(64, 64)):
        # Open the uploaded image file
        img = Image.open(uploaded_image)
        # Resize the image
        img = img.resize(target_size)
        # Convert the image to array
        img_array = np.array(img)
        # Expand dimensions to match the model's expected input shape
        img_array_expanded_dims = np.expand_dims(img_array, axis=0)
        return img_array_expanded_dims

    # buat form inputan
    with st.form('inputUser'):
    #    name = st.text_input('Nama', help='Nama Penjual')
       image = st.file_uploader("Upload the House Image", type=["jpg", "png", "jpeg"])
       street = st.text_input('street', help='Street name in California')
       citi = st.selectbox('citi',('Salton City', 'Brawley', 'Imperial', 'Calexico', 'Gorman',
       'Frazier Park', 'Rosamond', 'Kernville', 'Tehachapi', 'Arvin',
       'California City', 'Bakersfield', 'Delano', 'Lebec',
       'Pine Mountain Club', 'Inyokern', 'Mojave', 'Boron',
       'Stallion Springs', 'Ridgecrest', 'Keene', 'Caliente',
       'Bear Valley Springs', 'Wofford Heights', 'Studio City',
       'Glendale', 'Eagle Rock', 'Rancho Palos Verdes', 'Woodland Hills',
       'Montebello', 'Los Angeles', 'Culver City', 'Long Beach', 'Walnut',
       'Rowland Heights', 'Porter Ranch', 'Newhall', 'Covina',
       'Santa Monica', 'San Marino', 'Agoura Hills', 'Stevenson Ranch',
       'La Canada Flintridge', 'Arcadia', 'Pasadena', 'El Segundo',
       'El Monte', 'Torrance', 'Altadena', 'Encino', 'Downey',
       'Sherman Oaks', 'Monrovia', 'Northridge', 'Sunland', 'Azusa',
       'Valley Glen', 'Castaic', 'Tarzana', 'Burbank', 'Diamond Bar',
       'Hacienda Heights', 'Canyon Country', 'Van Nuys', 'West Covina',
       'Sierra Madre', 'Alhambra', 'Beverly Hills', 'Venice', 'Inglewood',
       'Westchester', 'Valley Village', 'Glendora', 'San Gabriel',
       'La Verne', 'Malibu', 'Redondo Beach', 'Playa del Rey',
       'Palos Verdes Estates', 'Whittier', 'Pomona', 'Toluca Lake',
       'Shadow Hills', 'Hermosa Beach', 'Claremont', 'South Pasadena',
       'Pacific Palisades', 'Calabasas', 'West Hollywood', 'Temple City',
       'Lancaster', 'Littlerock', 'Palmdale', 'Pearblossom',
       'Lake Los Angeles', 'North Hollywood', 'Sylmar', 'Lake Hughes',
       'Santa Clarita', 'Llano', 'Acton', 'Reseda', 'La Mirada',
       'Lake Elizabeth', 'Paramount', 'San Pedro', 'Green Valley',
       'Compton', 'Huntington Park', 'Juniper Hills', 'Quartz Hill',
       'Leona Valley', 'Agua Dulce', 'San Fernando', 'Pico Rivera',
       'Hawaiian Gardens', 'Mt Baldy', 'Gardena', 'La Puente', 'Artesia',
       'Baldwin Park', 'Norwalk', 'Tujunga', 'Bell Gardens', 'Carson',
       'Pacoima', 'Bellflower', 'Bell', 'Lynwood', 'East Los Angeles',
       'South El Monte', 'Canoga Park', 'Chatsworth', 'Granada Hills',
       'South Gate', 'Lakewood', 'Wilmington', 'Val Verde', 'Saugus',
       'Commerce', 'Valencia', 'Santa Fe Springs', 'Topanga', 'Arleta',
       'Sun Valley', 'La Crescenta', 'Winnetka', 'Rosemead',
       'Panorama City', 'Monterey Park', 'Hawthorne', 'Phillips Ranch',
       'Mission Hills', 'Duarte', 'North Hills', 'San Dimas',
       'West Hills', 'Lake Balboa', 'Hollywood', 'Lawndale', 'Cerritos',
       'Los Feliz', 'Lakeview Terrace', 'Lomita', 'Harbor City',
       'Highland Park', 'Montrose', 'View Park', 'Echo Park',
       'Costa Mesa', 'Fullerton', 'Laguna Beach',
       'Rancho Santa Margarita', 'Ladera Ranch', 'Huntington Beach',
       'Anaheim Hills', 'Newport Beach', 'San Juan Capistrano',
       'Lake Forest', 'Orange', 'Laguna Niguel', 'Aliso Viejo', 'Irvine',
       'Garden Grove', 'Placentia', 'Los Alamitos', 'San Clemente',
       'Dana Point', 'Mission Viejo', 'Coto de Caza', 'La Habra',
       'Westminster', 'Rossmoor', 'Laguna Hills', 'Yorba Linda',
       'Fountain Valley', 'North Tustin', 'Trabuco Canyon',
       'La Habra Heights', 'Santa Ana', 'Seal Beach', 'Brea', 'Cypress',
       'Villa Park', 'Tustin', 'Newport Coast', 'Corona del Mar',
       'Laguna Woods', 'Anaheim', 'Buena Park', 'Silverado', 'Stanton',
       'La Palma', 'Midway City', 'Modjeska Canyon', 'La Quinta',
       'Temecula', 'Rancho Mirage', 'Palm Desert', 'Indian Wells',
       'Palm Springs', 'Canyon Lake', 'Winchester', 'Murrieta',
       'Bermuda Dunes', 'Mountain Center', 'Corona', 'Riverside', 'Indio',
       'Banning', 'Thermal', 'Menifee', 'Norco', 'Homeland', 'Hemet',
       'Cherry Valley', 'Wildomar', 'Coachella', 'San Jacinto',
       'Desert Hot Springs', 'Lake Elsinore', 'Perris', 'Moreno Valley',
       'Anza', 'Blythe', 'Cathedral City', 'Cabazon', 'Nuevo',
       'Idyllwild', 'Thousand Palms', 'Beaumont', 'Whitewater',
       'Sun City', 'Aguanga', 'Belltown', 'Calimesa', 'Mira Loma',
       'Romoland', 'Chino Hills', 'Rancho Cucamonga', 'Lake Arrowhead',
       'Yucaipa', 'Redlands', 'Joshua Tree', 'Big Bear', 'Upland',
       'Bloomington', 'San Bernardino', 'Colton', 'Chino', 'Alta Loma',
       'Oak Glen', 'Lucerne Valley', 'Fontana', 'Wrightwood',
       'Big Bear Lake', 'Needles', 'Running Springs', 'Hesperia',
       'Pinon Hills', 'Pioneertown', 'Ontario', 'Yucca Valley',
       'Apple Valley', 'Cedarpines Park', 'Victorville', 'Helendale',
       'Crestline', 'Morongo Valley', '29 Palms', 'Sugarloaf', 'Landers',
       'Angelus Oaks', 'Adelanto', 'Green Valley Lake', 'Big Bear City',
       'Mentone', 'Rimforest', 'Phelan', 'Oro Grande', 'Fawnskin',
       'Barstow', 'Cedar Glen', 'Twin Peaks', 'Forest Falls', 'Highland',
       'Big River', 'Loma Linda', 'Rialto', 'Newberry Springs',
       'Oak Hills', 'Grand Terrace', 'Montclair', 'El Mirage', 'Blue Jay',
       'San Diego', 'San Marcos', 'Carlsbad', 'Encinitas', 'Jamul',
       'Del Mar', 'Chula Vista', 'Poway', 'Oceanside', 'Solana Beach',
       'Fallbrook', 'Bonita', 'Bonsall', 'La Mesa', 'Ramona', 'Coronado',
       'Vista', 'Cardiff by the Sea', 'El Cajon', 'Escondido',
       'Valley Center', 'Alpine', 'Rancho Santa Fe', 'La Jolla',
       'Imperial Beach', 'Pacific Beach', 'Cardiff', 'Borrego Springs',
       'Julian', 'Lakeside', 'Spring Valley', 'Boulevard',
       'Warner Springs', 'National City', 'Santee', 'Ranchita', 'Jacumba',
       'Campo', 'Palomar Mountain', 'Pauma Valley', 'Descanso',
       'Santa Ysabel', 'Pine Valley', 'Lemon Grove', 'Dulzura',
       'Rancho Bernardo', 'Paradise Hills', 'Potrero', 'Ocean Beach',
       'Pismo Beach', 'Paso Robles', 'Los Osos', 'Templeton', 'Cambria',
       'Morro Bay', 'Nipomo', 'Arroyo Grande', 'San Luis Obispo',
       'Avila Beach', 'Cayucos', 'Creston', 'Atascadero', 'San Miguel',
       'Santa Margarita', 'Oceano', 'Shandon', 'Grover Beach',
       'Parkfield', 'Santa Barbara', 'Carpinteria', 'Lompoc',
       'Santa Maria', 'Montecito', 'Santa Ynez', 'Cuyama', 'New Cuyama',
       'Los Alamos', 'Solvang', 'Guadalupe', 'Vandenberg Village',
       'Buellton', 'Goleta', 'Westlake Village', 'Ventura', 'Camarillo',
       'Santa Paula', 'Thousand Oaks', 'Newbury Park', 'Lake Sherwood',
       'Simi Valley', 'Ojai', 'Somis', 'Oxnard', 'Oak Park', 'Moorpark',
       'Fillmore', 'Oak View', 'Port Hueneme', 'Piru', 'La Conchita'), help='City name in California')
    #    buildingage = st.slider('buildingage', min_value = 5, max_value = 25, help='Usia Bangunan(range 5 until 25)')
    #    houselevel = st.slider('houselevel', min_value = 1, max_value = 5, help='Tingkat Rumah(range 1 until 5)')
       n_citi = st.slider('n_citi', min_value = 1, max_value = 414, help='Kodepos')
       bed = st.slider('bed', min_value = 1, max_value = 12, help='Number of Bedrooms(range 1 until 12)')
       bath = st.slider('bath', min_value = 1, max_value = 12, help='Number of Bathrooms(range 1 until 12)')
       sqft = st.slider('sqft', min_value = 280, max_value = 17700, help='House Area(range 1 until 12)')
    #    image = st.file_uploader("Upload the House Image", type=["jpg", "png", "jpeg"])
       st.markdown('---')

       # submit button
       submitted = st.form_submit_button('Predict')

       if submitted:
        st.markdown('---')
        if image == None:
            st.markdown('### **Please Upload Your House Image** :warning:')
        else:
            st.image(image)
            image_array = preprocess_image(image)

        data_inf = {
           'street': street,
           'citi': citi,
           'n_citi': n_citi,
           'bed': bed,
           'bath': bath,
           'sqft': sqft
        }

        data_inf_df = pd.DataFrame([data_inf])  # Create DataFrame from data_inf
        # data_inf_df['image'] = [image_array]  # Add the preprocessed image array to the DataFrame
        data_inf_process = pipeline.transform(data_inf_df)  # Transform data using pipeline
        combined_input = [data_inf_process, image_array]

        # Make prediction
        prediction = model.predict(combined_input)
        st.write(f"Your house price : {prediction[0][0]:.2f} USD")
        data_inf_df['price'] = prediction[0][0]
        data_inf_df.to_csv('data_raw.csv')
        # data_inf_df.to_sql('properties', conn, if_exists='append', index=False)


if __name__ == "__main__":
    run()
