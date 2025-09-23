# up_bi_2025_Sept/Modules/Utils/headr.py
#Encabezado de mi interfaz grafica de mi app

import streamlit as st

def show_header(text_title: str):
  #layout: logo + title side by side
  col1, col2 = st.columns([1, 6)]

  with col1:
    st.image("assets/up_logo.jpg", width=200)
  
  with col2:
    st.title(text_title)
    st.caption("Developed for: *Business Intelligence (Graduate Level)*")
    st.caption("Instructor: Edgar Avalos-Ganua (2025), Universidad Panamericana")

  
