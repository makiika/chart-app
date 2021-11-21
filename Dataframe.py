import plotly.express as px
import streamlit as st

class Dataframe:
    def __init__(self,df):
        self.df = df
        self.cleanDf = self.df
        self.cleanDf.dropna(inplace=True)
        self.cleanDf.drop_duplicates(inplace = True)
        self.X = st.sidebar.selectbox('X-axis',(self.cleanDf.columns))
        self.Y = st.sidebar.selectbox('Y-axis',(self.cleanDf.columns))
        
     #Getting the dataframe of the cleaned data  
    def getData(self):
        return self.cleanDf
    
    #Generating a line graph
    def lineGraph(self): 
         self.line_graph = px.line(self.cleanDf,
                            text=self.Y,
                            y=self.Y,
                            x=self.X,
                            width=1000,
                            height=700,                            
                            line_shape='spline')
         return self.line_graph
     
    #Generating a bargraph from the cleaned data set 
    def barGraph(self):
         self.bar_graph = px.bar(self.cleanDf,
                           y=self.Y,
                           x=self.X,                          
                           width=1000, 
                           height=700)
         return self.bar_graph
         
    def max(self): 
        return self.df.max()
        
    def min(self):
        return self.df.min()
        