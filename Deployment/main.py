import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('EDA', 'Predict Price'))
if navigation == 'EDA' :
    eda.run()
else :
    prediction.run()