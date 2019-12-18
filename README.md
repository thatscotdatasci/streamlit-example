# Streamlit Example App

Very simple Streamlit example app to test functionality and CI/CD deployment.

## Local Execution
Ensure that you have Docker installed, and then run the following command from the command line:

`sh local.sh`

This will build and run a Docker image. The Streamlit app will be available at:

`http://localhost:8501`

The directory containing the app code (`tsds.py`) is mounted inside the running container, and so any modifications made
will be reflected in the app when the page is refreshed/the app is re-run.
