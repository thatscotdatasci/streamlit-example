import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio
from app.content.utils import get_git_content, RAW_GIT_URL

GITHUB_ACTION_URL = "".join((RAW_GIT_URL, ".github/workflows/main.yml"))


class GitHubRadio(AbstractNavigationRadio):

    name = "GitHub Workflow CI/CD"

    def _action(self):
        st.markdown("""
        
        The following [GitHub Action](https://github.com/features/actions) runs unit tests and deploys the latest commit of the Streamlit app to Heroku:
        
        """)

        st.code(get_git_content(GITHUB_ACTION_URL), language="yaml")

        st.markdown("""
        
        The current job status for this Streamlit app is: ![Heroku Workflow](https://github.com/thatscotdatasci/streamlit-example/workflows/Heroku%20Workflow/badge.svg?branch=master)
        
        Previous executions can be seen [here](https://github.com/thatscotdatasci/streamlit-example/actions).
        
        """)

