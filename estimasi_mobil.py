#untuk load SAV
import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

#untuk Judul Web
st.title('Estimasi Harga Mobil Bekas')

#membuat form input

year = st.number_input('input Tahun Mobil')
mileage = st.number_input('input Km Mobil')
tax = st.number_input('input Pajak Mobil')
mpg = st.number_input('input Konsumsi Mobil')
engineSize = st.number_input('input Engine Size Mobil')

#MOdel prediksi

predict = ''
#button
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )

    #keterangan
    st.write ('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :', predict*19000)