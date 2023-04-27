import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    st.title("Numeri Casuali")
    generate_random = np.random.RandomState(667)

    rng = np.random.default_rng()
    
    inpRand = st.slider('Inserisci valore della x e y',0,100,50)
    
    coefAng = st.slider('Inserisci coefficente angolare',0,10,3)
    
    noise = rng.normal(0,0.5,inpRand)
    
    x = 10 * generate_random.rand(inpRand)
    y =  coefAng * x + noise
    X = x.reshape(-1,1)
    
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    y_pred  = model.predict(X)
    
    fig = plt.figure(figsize=(18,10))
    plt.scatter(x,y)
    plt.axis([0, 10, 0, 50])
    plt.plot(x,y_pred,'-r')
    st.pyplot(fig)
    st.write(f"Il valore dell'equazione y= {round(model.intercept_,2)} + {round(model.coef_[0],2)}*x  ")
    
    
    
    
if __name__ == "__main__":
    main()
