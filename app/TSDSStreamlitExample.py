import requests
from PIL import Image
from io import BytesIO

import streamlit as st

from app.content.home_radio import HomeRadio
from app.content.streamlit_examples_radio import StreamlitExamplesRadio
from app.content.streamlit_app_operations_radio import StreamlitAppOperationsRadio
from app.content.heroku_radio import HerokuRadio
from app.content.github_radio import GitHubRadio
from app.navigation_manager.navigation_manager import NavigationManager

TSDS_ICON_URL = "https://raw.githubusercontent.com/thatscotdatasci/thatscotdatasci.github.io/master/assets/icons/tsds.ico"

# Get the TSDS icon
tsds_icon_data = requests.get(TSDS_ICON_URL)
tsds_icon = Image.open(BytesIO(tsds_icon_data.content))

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Example App",
    page_icon=tsds_icon,
    initial_sidebar_state="expanded",
    layout="centered"
)

# Display the TSDS logo in the sidebar
st.sidebar.image(tsds_icon)

# App title in sidebar
st.sidebar.markdown("""
# Streamlit Example App

Simple example of [Streamlit](https://www.streamlit.io/) features, as well as how to run and deploy a Streamlit app to 
[Heroku](https://www.heroku.com/) using [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions).
""")

# Instantiate navigation radio options
navigation_radio_options = (HomeRadio, StreamlitExamplesRadio, StreamlitAppOperationsRadio, HerokuRadio, GitHubRadio)

# Content manager
content_manager = NavigationManager(navigation_radio_options, HomeRadio)
