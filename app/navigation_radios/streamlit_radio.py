import time

import numpy as np
import pandas as pd
import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio


class StreamlitRadio(AbstractNavigationRadio):

    name = "Running Streamlit"

    def action(self):
        st.markdown("""
        
        Run Streamlit:
        
        ```
        streamlit run <path_to_app>
        ```
        """)

        st.markdown("""
                ## Table

                A simple table of data
                """)

        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]
        }, )

        st.write(df)

        st.markdown("""
                ## User Input Example

                Write text in the box below, and see what happens if you include numbers:
                """)

        user_input = str(st.text_input("Input:"))

        if user_input.isalpha():
            st.markdown(f"""
                    The following value was specified: {user_input}
                    """)
        elif user_input:
            st.error(f"""
                    Only alphabetic string is allowed!

                    Rejected input: {user_input}
                    """)

        st.markdown("""
                ## Checkbox Example

                Example of using a checkbox, and displaying a chart
                """)

        chart_checkbox = st.checkbox('Show chart')
        if chart_checkbox:
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

            st.line_chart(chart_data)

        st.markdown("""
                ## Animation

                An example of a chart (from the [docs](https://streamlit.io/docs/advanced_concepts.html#animate-elements)) - 
                apologies for the balloons
                """)

        animation_checkbox = st.checkbox('Show animation')
        if animation_checkbox:
            progress_bar = st.progress(0)
            status_text = st.empty()
            chart = st.line_chart(np.random.randn(10, 2))

            for i in range(11):
                # Update progress bar.
                progress_bar.progress(i * 10)

                new_rows = np.random.randn(10, 2)

                # Update status text.
                status_text.text(
                    'The latest random number is: %s' % new_rows[-1, 1])

                # Append data to the chart.
                chart.add_rows(new_rows)

                # Pretend we're doing some computation that takes time.
                time.sleep(0.1)

            status_text.text('Done!')
            st.success("Success!")
            st.balloons()
