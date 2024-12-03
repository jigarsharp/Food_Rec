import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps

print(tf.__version__)
st.markdown("""
    #  :orange[Indian Food Recognition]
             """
           )
    

models=[]
model1 = tf.keras.models.load_model('my_Mobilenet.h5')
model2 = tf.keras.models.load_model('my_Mobilenet.h5')
models.append(model1)
models.append(model2)


file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    st.image(image,width=175)
    size = (224,224)    
    image = ImageOps.fit(image, size, Image.LANCZOS)
    image = image.convert('RGB')
    image = np.asarray(image)
    image = np.expand_dims(image,axis=0)
    image = tf.keras.applications.mobilenet_v3.preprocess_input(image)
    pred=[model.predict(image) for model in models]
    pred=np.sum(np.array(pred),axis=0)
    

    #pred = model.predict(image)
     
    if np.argmax(pred) == 0:
        st.markdown(''':orange[It is Burger!]''')
        
        st.markdown(''' :red[Ingredients:	Onion, cheese slices, powdered garam masala powder, refined oil, ginger paste,burger buns, tomato ketchup, garlic paste, tomato,powdered red chilli, salt, breadcrumbs, lemon juice, butter, coriander leaves, lettuce leaf]''')
        st.markdown(''':violet[Method : Grilled or Not-Grilled]''')

    elif np.argmax(pred) == 1:
	    st.markdown(''' :orange[It is Butter Naan!]''')
	    st.markdown(''' :red[Ingredients: Maida(flour), Fresh curd, Baking soda, Sugar, Salt, Oil,Ghee/butter]''')
	    st.markdown(''' :violet[Method: Toasting]''')
       
    elif np.argmax(pred) == 2:
	    st.markdown(''':orange[It is Chai!]''')
    elif np.argmax(pred) == 3:
	    st.markdown(''':orange[It is Chapati!]''')
	
    elif np.argmax(pred) == 4:
	    st.markdown(''':orange[It is Chole Bhature!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 5:
	    st.markdown(''':orange[It is Dal Makhni!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 6:
	    st.markdown(''':orange[It is Franky!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 7:
	    st.markdown(''':orange[It is Fried Rice!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 8:
	    st.markdown(''':orange[It is Gajar Halwa!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 9:
	    st.markdown(''' :orange[It is Gulab Jamun!]''')
	    st.markdown(''' :red[Ingredients: paneer, Edible oil, water, lemon juice, sugar, green cardamom, mashed khoya, ghee, saffron]''')
	    st.markdown(''' :violet[Method: Fry]''')

    elif np.argmax(pred) == 10:
	    st.markdown(''':orange[It is Idli!]''')
	    st.markdown(''':red[Ingredients : basmati rice,fenugreek seeds,sesame oil,urad dal,salt,water]''')
	    st.markdown(''':violet[Method : Fermentation & Steaming]''')

    elif np.argmax(pred) == 11:
	    st.markdown(''':orange[It is Jalebi!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 12:
	    st.markdown(''':orange[It is Kadai Paneer!]''')	
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 13:
	    st.markdown(''':orange[It is Khaman!]''')
	    st.markdown(''' :red[Ingredients : flour (besan),sugar,salt,refined oil,mustard seeds, water,lemon juice, baking soda, curry leave]''')
	    st.markdown(''' :violet[Method : Fermentation & Steaming]''')

    elif np.argmax(pred) == 14:
	    st.markdown(''':orange[It is Kulfi!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 15:
	    st.markdown(''':orange[It is Masala Dosa!]''')
	    st.markdown(''' :red[Ingredients:	urad dal,fenugreek (methi) seed, raw rice (chawal),par-boiled rice, thick beaten rice (poha), ghee,coconut chutney]''')
	    st.markdown(''' :violet[Method : Fermentation & Baking]''')


    elif np.argmax(pred) == 16:
	    st.markdown(''':orange[It is Meduvada!]''')
	    st.markdown(''' :red[Ingredients:urad dal,peppercorns,refined oil,garlic,asafoetida,onion,curry leaves,ginger,salt,water]''')
	    st.markdown(''' :violet[Method: Fermentation & Fry]''')

    elif np.argmax(pred) == 17:
	    st.markdown(''':orange[It is Mirchi Vada!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 18:
	    st.markdown(''':orange[It is Momos!]''')
	    st.markdown(''' :red[Ingredients:soya sauce,mushroom,cabbage,tofu, ginger, water, flour, garlic, onion, chille]''')
	    st.markdown(''' :violet[Method: Steam or Fry]''')

    elif np.argmax(pred) == 19:
	    st.markdown(''':orange[It is Pani Puri!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 20:
	    st.markdown(''':orange[It is Pakoda!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 21:
	    st.markdown(''':orange[It is Pizza!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 22:
	    st.markdown(''':orange[It is Poha!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    elif np.argmax(pred) == 23:
	    st.markdown(''':orange[It is Rasgulla!]''')
	    st.markdown(''' :red[Ingredients: milk,sugar,rose water,lime juice,water,powdered green cardamom]''')
	    st.markdown(''':violet[Method : Coagulation of milk or curding]''')

    elif np.argmax(pred) == 24:
	    st.markdown(''':orange[It is samosa!]''')
	    
	    st.markdown(''' :red[Ingredients: flour,cumin seeds, ginger, potato,coriander powder, chilli powder, kasoori methi leaves, carom seeds,  oil, coriander seeds, green chilli, cumin powder, garam masala powder, salt,  coriander leaves, peanuts]''')
	    st.markdown(''':violet[Method : Fry]''')

    elif np.argmax(pred) == 25:
	    st.markdown(''':orange[It is Vadapav!]''')
	    st.markdown(''' :red[]''')
	    st.markdown(''':violet[]''')

    else :
        st.write("It is a not Food!")


