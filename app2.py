import numpy as py
import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("sample_pivot.csv")
st.set_page_config(layout="wide")
fh=df.drop(columns=["Region"]).columns
st.title("HIGH FASHION :green[Analysis] 👕👔🧥💹:")
st.markdown("This Analysis Dashboard that gives a Relationship Between **Region** and other various attributes used in the production of Designer of **High Fashion** Wears, Based on Four Regions which are (East,West,North,South)") 

st.sidebar.markdown("## The Piechart And Barchart: Relationship Between:Relationship Between Regions And Sales.")
x_axis=st.sidebar.selectbox("X AXIS",fh)
y_axis=st.sidebar.selectbox("Y AXIS",fh)
color_encode=st.sidebar.checkbox(label="COLOR ENCODED BY REGION")
container=st.container()
chart1,chart2=container.columns(2)

with chart1:
    if x_axis and y_axis:
        fig=px.bar(df,x=x_axis, y=y_axis, color="Region" if color_encode else None, title="{} VS {}".format(x_axis.upper(),y_axis.upper()))
        st.plotly_chart(fig, use_container_width=True)

with chart2:
     if x_axis and y_axis:
        st.markdown("SELECT X AXIS TO BE ONLY CATEGORY AND Y AXIS SHOULD BE NUMBERS.")
        fig2=px.pie(df,names=x_axis,values=y_axis,title= "{} vs {}".format(x_axis.upper(),y_axis.upper()),template="seaborn", hole = 0.5)
        pull_values=[0,0,0,0]
        fig2.update_traces(pull = pull_values, textposition="inside", textinfo="percent + label")
        st.plotly_chart(fig2, use_container_width=True)
show_df=st.checkbox("SHOW DATAFRAME")
if show_df:
    st.dataframe(df)

st.header("CHICKEN REPUBLIC 🥤🍔🍗🍟")
st.markdown("Analyzing the Relationship Between Customer and other Attributes like(Total bill,Tips,Gende) with Each Day")
df3=pd.read_csv("tips.csv")
fig6=px.sunburst(df3,path=["Day","Time","Sex","Smoker"], values="Total_bill")
st.plotly_chart(fig6,use_container_width=True)

show_df3=st.checkbox("SHOW DATAFRAME", key="show_df3")
if show_df3:
    st.dataframe(df3)