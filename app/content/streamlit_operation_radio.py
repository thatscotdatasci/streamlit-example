import time

import numpy as np
import pandas as pd
import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio


class StreamlitOperationRadio(AbstractNavigationRadio):

    name = "Streamlit Operation"

    def _action(self):
        st.markdown("""
        
        Run Streamlit:
        
        ```
        streamlit run <path_to_app>
        ```
        """)
