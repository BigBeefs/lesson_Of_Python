import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def main():
    uploaded_file = st.file_uploader("Scegli un File")
    if uploaded_file is not None:
        dfup =pd.read_csv(uploaded_file)
        column_headers = list(dfup.columns.values)
        target = st.selectbox('Scegli la Target:',column_headers,index=3)
        if target is not None:
            X=dfup.iloc[:,:-1]
            #y=dfup.iloc[:,-1]
            y=dfup[target]
            st.dataframe(dfup.head())
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=667)
            model=LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test).round(2)
            
            y_pred = model.predict(X_test).round(2)
            X_test[target]= y_test
            X_test['Prediction']= y_pred
            X_test['Error'] = y_test - X_test['Prediction']
            r2score = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write('DataFrame con la Prediction')
            st.dataframe(X_test)
            st.write('Media di errore:',X_test['Error'].mean().round(2))
            st.write('R2 Score:',r2score.round(2))
            st.write('Mean Absolute Error:',mae.round(2))
            st.write('Mean Squared Error:',mse.round(2))
            st.write('Rout Mean Error:',rmse.round(2))
            

if __name__ == "__main__":
    main()