import streamlit as st

from app.abstract_classes.abstract_navigation_button import AbstractNavigationButton


class HerokuButton(AbstractNavigationButton):

    name = "Heroku Hosting"

    def action(self):
        st.markdown("""
        
        Run Heroku web app locally:
        
        ```
        heroku local web
        ```
        """)

