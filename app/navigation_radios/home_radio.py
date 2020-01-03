import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio


class HomeRadio(AbstractNavigationRadio):

    name = "Home"
    _display_header = False

    def _action(self):
        st.markdown("""
        # ThatScotDataSci Streamlit Example App

        This is a super simple, starter for 10 Streamlit app with the purpose of demoing functionality, and documenting 
        how to run and deploy a Stremlit app to Heroku using GitHub.
        
        I've also been working on creating re-usable objects to aid with creating and organising multi-page Streamlit 
        apps in a clean manor.
        
        Use the radio buttons in the sidebar to select a page to view.
        """)
