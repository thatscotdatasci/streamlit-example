from app.abstract_classes.abstract_navigation_button import AbstractNavigationButton

import streamlit as st


class HomeButton(AbstractNavigationButton):

    name = "Home"

    def action(self):
        st.markdown("""
        # ThatScotDataSci Streamlit Example App

        This is a super simple, starter for 10 Streamlit app with the purpose of demoing functionality, and documenting how to
        do some cool stuff.
        """)
