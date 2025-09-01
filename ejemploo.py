import streamlit as st
import pandas as pd
import numpy as np
st.title('Titulo del Proyecto')


st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")


import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
appointment = st.slider(
"Programe la asesoria:",
value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)
