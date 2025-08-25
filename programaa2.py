import streamlit as st
import pandas as pd
import numpy as np
st.title("Titulo")
num = st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))
