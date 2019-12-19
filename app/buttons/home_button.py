from app.abstract_classes.abstract_button import AbstractButton

import streamlit as st


class HomeButton(AbstractButton):

    name = "Home"

    def action(self):
        st.markdown("""
        # ThatScotDataSci Streamlit Example App

        This is a super simple, starter for 10 Streamlit app with the purpose of demoing functionality, and documenting how to
        do some cool stuff.
        """)
