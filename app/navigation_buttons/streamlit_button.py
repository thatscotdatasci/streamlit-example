import time

import numpy as np
import pandas as pd
import streamlit as st

from app.abstract_classes.abstract_navigation_button import AbstractNavigationButton


class StreamlitButton(AbstractNavigationButton):

    name = "Streamlit Code"

    def action(self):
        st.markdown("""
        
        Run Streamlit:
        
        ```
        streamlit run <path_to_app>
        ```
        
        # My first app

        ## Table
        Here's our first attempt at using data to create a table:
        """)

        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]
        })

        df

        st.markdown("""
        ## User input
        This is a test of user input
        """)

        user_input = st.text_input("Input:")

        st.markdown(f"""
        The following value was specified: {user_input} 

        ## Checkbox Example
        Lets play around with a checkbox
        """)

        if st.checkbox('Show dataframe'):
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

            st.line_chart(chart_data)

        st.markdown("""
        ## Animation
        Lets looks at something more creative...
        """)

        progress_bar = st.progress(0)
        status_text = st.empty()
        chart = st.line_chart(np.random.randn(10, 2))

        for i in range(100):
            # Update progress bar.
            progress_bar.progress(i)

            new_rows = np.random.randn(10, 2)

            # Update status text.
            status_text.text(
                'The latest random number is: %s' % new_rows[-1, 1])

            # Append data to the chart.
            chart.add_rows(new_rows)

            # Pretend we're doing some computation that takes time.
            time.sleep(0.1)

        status_text.text('Done!')
        st.balloons()
        st.success("Success!")
