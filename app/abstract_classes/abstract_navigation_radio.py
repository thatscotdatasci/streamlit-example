from abc import ABC

import streamlit as st

from app.abstract_classes.abstract_input_object import AbstractInputObject


class AbstractNavigationRadio(AbstractInputObject, ABC):

    def action(self):
        st.markdown("""
        # Coming Soon!
        
        This is a placeholder page - content to come soon!
        """)
