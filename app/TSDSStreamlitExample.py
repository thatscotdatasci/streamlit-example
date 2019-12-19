import requests
from PIL import Image
from io import BytesIO

import streamlit as st

from app.navigation_buttons.home_button import HomeButton
from app.navigation_buttons.streamlit_button import StreamlitButton
from app.navigation_buttons.heroku_button import HerokuButton
from app.navigation_buttons.github_button import GitHubButton
from app.content_manager.content_manager import ContentManager

TSDS_ICON_URL = "https://raw.githubusercontent.com/thatscotdatasci/thatscotdatasci.github.io/master/assets/icons/tsds.ico"


# Display the TSDS logo in the sidebar
tsds_icon_data = requests.get(TSDS_ICON_URL)
tsds_icon = Image.open(BytesIO(tsds_icon_data.content))
st.sidebar.image(tsds_icon)

# App title in sidebar
st.sidebar.markdown("# TSDS Streamlit Example")

# Instantiate buttons
buttons = (HomeButton, StreamlitButton, HerokuButton, GitHubButton)

# Content manager
content_manager = ContentManager(buttons, HomeButton)
