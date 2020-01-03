import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio


class HerokuRadio(AbstractNavigationRadio):

    name = "Heroku Hosting"

    def action(self):
        st.markdown("""
        
        Run Heroku web app locally:
        
        ```
        heroku local web
        ```
        """)

