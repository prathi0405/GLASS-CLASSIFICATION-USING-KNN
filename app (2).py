import streamlit as st
import pandas as pd
import pickle

from PIL import Image
image = Image.open('bg.jpeg')

st.image(image)

model = pickle.load(open('/Users/ads-16/Desktop/js/bc.pkl','rb'))

def dataframe(head):
    b=pd.DataFrame(head, columns= ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'])
    return b


st.title('Glass Type classification ')

RI = st.text_input(' Enter the RI value:',0)
Na = st.text_input(' Enter the Na value:',0)
Mg = st.text_input(' Enter the Mg value:',0)
Al = st.text_input(' Enter the Al value:',0)
Si = st.text_input(' Enter the Si value:',0)
K = st.text_input(' Enter the K value:',0)
Ca = st.text_input(' Enter the Ca value:',0)
Ba = st.text_input(' Enter the Ba value:',0)
Fe = st.text_input(' Enter the Fe value:',0)

data = [[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]]
newdf = dataframe(data)


predict_value = model.predict(newdf)
result = st.button("Predict")

if result :
    if predict_value == 1:
        st.subheader('The Glass type is used in Building windows (float processed)')
        i = Image.open('df.jpeg')
        st.image(i)
    elif predict_value == 2:
        st.subheader('The Glass type is used in Building windows (non-float processed)')
        i = Image.open('dnf.jpeg')
        st.image(i)
    elif predict_value == 3:
        st.subheader('The Glass type is used in Vehicle windows (float processed)')
        i = Image.open('vf.jpeg')
        st.image(i)
    elif predict_value == 4:
        st.subheader('The Glass type is used in Vehicle windows (non-float processed)')
        i = Image.open('vnf.jpeg')
        st.image(i)
    elif predict_value == 5:
        st.subheader('The Glass type is used in Containers')
        i = Image.open('c.jpeg')
        st.image(i)
    elif predict_value == 6:
        st.subheader('The Glass type is used in Tableware')
        i = Image.open('t.webp')
        st.image(i)
    elif predict_value == 7:
        st.subheader('The Glass type is used in Headlamps')
        i = Image.open('hl.jpeg')
        st.image(i)
    