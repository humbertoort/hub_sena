import streamlit as st
from PIL import Image, ImageOps
from datetime import datetime
import paho.mqtt.client as paho
import time
import json
from datetime import datetime
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

broker="broker.mqttdashboard.com"
port=1883


def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass


def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    print(message_received)

client1=paho.Client("Python")
client1.on_publish = on_publish    
client1.subscribe("remote")
client1.on_message = on_message
client1.connect(broker,port)

image0 = Image.open('senalogo.png')
st.image(image0, caption='SENA')

st.subheader('Operación Robot sobre Internet')

image2 = Image.open('descarga_magician.jpg')
st.image(image2, caption='Robot')

st.markdown("Código RFID")

#codrfid = st.text_input('RFID código', max_chars=10)
#st.write(' Ejecutar Proceso: ', codrfid)


placeholder = st.empty()
codrfid = placeholder.text_input('text', max_chars=10, key=1)
click_clear = st.button('Limpiar', key=3)
if click_clear:
    input = placeholder.text_input('text', value='', key=2)

#st.write(input)

st.write('Ejecutar Proceso: ',codrfid)


if (codrfid=="0405829753"): # verde
   image = Image.open('camisetaverde.jpg')
   st.image(image, caption=' Proceso Equipo2')
   client1.publish("accion","on")  


if (codrfid=="0407926893"): # Negro
   image = Image.open('camisetanegra.jpg')
   st.image(image, caption='Proceso Equipo2')
   client1.publish("accion","off") 
