import streamlit as st
import Dataframe as df
import pandas as pd
import plotly.express as px

## getting data 
inputData = st.sidebar.file_uploader("Upload the data frame here",accept_multiple_files=False,type=['xlsx'])

if inputData is not None:    
    myData = pd.read_excel(inputData) 
    ##initialising the class
    data = df.Dataframe(myData)
    
    data.min()
    data.max()


    def Line():
        lineGraph = data.lineGraph()
        st.header("Generated Line graph")
        st.write(lineGraph)
        
    def Bar():  
        barGraph = data.barGraph()
        st.header("Generated Bar graph")
        st.write(barGraph)

    def Dtable():
        table = data.getData()
        st.header("Table")
        st.write(table)


    st.sidebar.button('dataframe ',on_click=Dtable)
    st.sidebar.button('line graph',on_click=Line)
    st.sidebar.button('bar graph',on_click=Bar)
       

else:
    st.title("FREE CHART APP")
    st.subheader("Welcome to free chart app you number one data visualisation application")
    st.write("Please upload you data set to continue")



    
     




    

 
   
    
