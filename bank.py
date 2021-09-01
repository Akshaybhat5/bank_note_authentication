import pandas as pd
import streamlit as st

import pickle

model = pickle.load(open('bank_authentication.pkl', 'rb'))

@st.cache()
def prediction(variance, skewness, curtosis, entropy):
    prediction = model.predict([[variance, skewness, curtosis, entropy]])

    if prediction == 0:
        return 'Duplicate Note'
    else:
        return 'Original Note'


def main():
    html_temp = """ 
    <div style ="background-color:black;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Bank Note Authentication</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)


    # st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    variance = st.number_input('enter the variance')
    skewness = st.number_input('enter skewness') 
    curtosis = st.number_input('enter curtosis') 
    entropy = st.number_input('enter entropy')
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(variance, skewness, curtosis, entropy) 
        st.success(result)
        



if __name__ == '__main__':
    main()