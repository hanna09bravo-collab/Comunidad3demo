import streamlit as st
import pandas as pd
import numpy as np
st.title('Agendar cita')



import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
appointment = st.slider(
"Programe la asesoria:",
value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)


import streamlit as st
import pandas as pd
import numpy as np
import datetime
d = st.date_input(
"Seleccione Fecha",
datetime.date(2019, 7, 6))
st.write('La fecha seleccionada es:', d)


import streamlit as st
option = st.selectbox(
'¿Cómo desearía ser contactado/a?',
('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)
