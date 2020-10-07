from random import random as rdn
import matplotlib.pyplot as plt
import streamlit as st
from math import sqrt

def estimate_pi(num_points:int):
    
    points_x = []
    points_y = []
    inside_points = []
    
    for i in range(num_points):
        x = rdn()
        y = rdn()
        points_x.append(x)
        points_y.append(y)
        
        if x**2+y**2 < 1:
            inside_points.append((x,y))
        
    
    circle = plt.Circle((0,0),1,color='blue')
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    
    for i in range(len(points_x)):
        if ((points_x[i]),(points_y[i])) in inside_points:
            ax.plot((points_x[i]),(points_y[i]),'o', color='red')
        else :
            ax.plot((points_x[i]),(points_y[i]),'o', color='black')
            
    st.pyplot(plt.show())
    st.text('Pi estimation:'+str(4*len(inside_points)/len(points_x)))   
num = st.number_input('Number of Points', value=1.)    
if st.button('Estimate'):
    estimate_pi(int(num))
