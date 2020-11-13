import requests
from PIL import Image
from io import BytesIO

import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio

TSDS_BANNER_URL = "https://raw.githubusercontent.com/thatscotdatasci/thatscotdatasci.github.io/master/assets/images/homepage_1800.jpg"


class HomeRadio(AbstractNavigationRadio):

    name = "Home"
    _display_header = False

    def _action(self):


        st.markdown("""
        # ThatScotDataSci Streamlit Example App
        """)

        # Display the TSDS banner
        tsds_banner_data = requests.get(TSDS_BANNER_URL)
        tsds_banner = Image.open(BytesIO(tsds_banner_data.content))
        st.image(tsds_banner, use_column_width=True)

        st.markdown("""
        This is a very simple, starter for 10 [Streamlit](https://www.streamlit.io/) app with the purpose of demonstrating functionality, and 
        documenting how to run and deploy a Stremlit app to [Heroku](https://www.heroku.com/) using [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions).
        
        I've also been working on creating re-usable objects to aid with creating and organising multi-page Streamlit 
        apps in a clean manor. Use the radio buttons in the sidebar to select a page to view.
        """)
