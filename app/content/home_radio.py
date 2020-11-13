import numpy as np
import streamlit as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio


class HomeRadio(AbstractNavigationRadio):

    name = "Home"
    _display_header = False

    def _action(self):


        st.markdown("""
        # Streamlit Example App

        This is a very simple, starter for 10 [Streamlit](https://www.streamlit.io/) app with the purpose of demonstrating functionality, and 
        documenting how to run and deploy a Stremlit app to [Heroku](https://www.heroku.com/) using [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions).

        I've also been working on creating re-usable objects to aid with creating and organising multi-page Streamlit 
        apps in a clean manor. Use the radio buttons in the sidebar to select a page to view.
        
        ## Standard Normal Distribution Playground
        """)

        n_dists = st.selectbox(label="Number of Distributions", options=range(1, 6), index=2)
        no_points = st.slider(label="Number of Data Points", min_value=10, max_value=300, value=200, step=10)
        st.button("Refresh")

        # Show some example data
        hist_data = [np.random.randn(no_points) + i*2 for i in range(n_dists)]
        group_labels = sorted([f'Group {i+1}' for i in range(n_dists)], reverse=True)

        # fig = go.Figure(data=go.Scatter(x=x1, y=x2, mode="markers", marker=dict(size=np.abs(x3)*10)))
        # st.plotly_chart(fig, use_container_width=True)

        fig = ff.create_distplot(hist_data, group_labels, bin_size=.3)
        st.plotly_chart(fig, use_container_width=True)

