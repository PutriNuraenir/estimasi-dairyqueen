import pickle
import streamlit as st

model = pickle.load(open('estimasi_dairyqueen.sav', 'rb'))

st.title('Estimasi Jumlah Kalori Di Menu Dairy Queen')

Cholesterols = st.number_input('Input Jumlah Kolesterol (mg)')
carbohydrates = st.number_input('Input Total Karbohidrat (g)')
Sugars = st.number_input('Input Jumlah Gula (g)')
Protein = st.number_input('Input Jumlah Protein (g)')
Total_Fat = st.number_input('Input Total Lemak (g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Cholesterols, carbohydrates, Sugars, Protein, Total_Fat]]
        )
    st.write ('Estimasi Jumlah Kalori Menu Makanan Dairy Queen : ', predict)