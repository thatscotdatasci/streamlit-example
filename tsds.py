import requests
from PIL import Image
from io import BytesIO

import streamlit as st

TSDS_ICON_URL = "https://raw.githubusercontent.com/thatscotdatasci/thatscotdatasci.github.io/master/assets/icons/tsds.ico"


tsds_icon_data = requests.get(TSDS_ICON_URL)
tsds_icon = Image.open(BytesIO(tsds_icon_data.content))
st.image(tsds_icon)

"""
# ThatScotDataSci Streamlit Example App

This is a super simple, starter for 10 Streamlit app.
"""
