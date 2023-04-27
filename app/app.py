import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
import io
from sklearn.linear_model import LogisticRegression
import openpyxl

def CreaPlotNumCas():
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

def CreaHMComp():
    figHMComp = plt.figure(figsize=(18,10))
    dfComp= pd.read_csv('app/Company.csv')
    sns.heatmap(data=dfComp.corr(),annot=True)
    st.pyplot(figHMComp)
    
def CreaHMStart():
    figHMStartUp = plt.figure(figsize=(18,10))
    dfStart= pd.read_csv('app/Startup.csv')
    sns.heatmap(data=dfStart.corr(),annot=True)
    st.pyplot(figHMStartUp)
    
def CreaPlotError():
    dfCompError=pd.read_csv('app/Company.csv')
    X=dfCompError.drop(columns='Sales')
    y=dfCompError['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=667)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    res_df = pd.DataFrame(data=list(zip(y_pred, y_test)),columns=['predicted', 'real']) 
    res_df['error'] = res_df['real'] - res_df['predicted']
    res_df.round(1)
    
    lenght = y_pred.shape[0]
    x = np.linspace(0,lenght,lenght)

    figureError = plt.figure(figsize=(10,7))
    plt.plot(x,y_test,label='Y Reale')
    plt.plot(x,y_pred, label='Y Predetto') 
    plt.legend(loc=1)
    st.pyplot(figureError)   
    
def confrontaFile(uploaded_file,):
    dfup =pd.read_csv(uploaded_file)
                
    df  = pd.read_csv('app/iris.data',header=None)
    df.columns=['sepal length','sepal width','petal length','petal width','class']
    X=df.drop(columns='class')
    y=df['class']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=667)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(dfup.to_numpy())
    dfup['Prediction']=y_pred
    st.dataframe(dfup)
    
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()

        st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='Risultati.xlsx',
            mime='application/vnd.ms-excel')

def main():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Crea Plot", "HeatMapCompany", "HeatMapStartUp","Plot Errori","Confronta File"])
    with tab1:
        # st.button('Crea il Plot', on_click= CreaPlotNumCas)
        CreaPlotNumCas()
    with tab2:
        # st.button('Crea HeatMap di "Company.csv"',on_click=CreaHMComp)
        CreaHMComp()
    with tab3:
        # st.button('Crea HeatMap di "Startup.csv"',on_click=CreaHMStart)
        CreaHMStart()
    with tab4:
        # st.button('Crea Plot differenza errori Company',on_click=CreaPlotError)
        CreaPlotError()
    with tab5:
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            confrontaFile(uploaded_file)

                
                
if __name__ == "__main__":
    main()
