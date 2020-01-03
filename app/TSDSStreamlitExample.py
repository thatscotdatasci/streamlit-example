import requests
from PIL import Image
from io import BytesIO

import streamlit as st

from app.navigation_radios.home_radio import HomeRadio
from app.navigation_radios.streamlit_radio import StreamlitRadio
from app.navigation_radios.heroku_radio import HerokuRadio
from app.navigation_radios.github_radio import GitHubRadio
from app.navigation_manager.navigation_manager import NavigationManager

TSDS_ICON_URL = "https://raw.githubusercontent.com/thatscotdatasci/thatscotdatasci.github.io/master/assets/icons/tsds.ico"


# Display the TSDS logo in the sidebar
tsds_icon_data = requests.get(TSDS_ICON_URL)
tsds_icon = Image.open(BytesIO(tsds_icon_data.content))
st.sidebar.image(tsds_icon)

# App title in sidebar
st.sidebar.markdown("""
# TSDS Streamlit Example

Simple example of Streamlit features, as well as how to run and deploy a Streamlit app to Heroku using GitHub
""")

# Instantiate navigation radio options
navigation_radio_options = (HomeRadio, StreamlitRadio, HerokuRadio, GitHubRadio)

# Content manager
content_manager = NavigationManager(navigation_radio_options, HomeRadio)
