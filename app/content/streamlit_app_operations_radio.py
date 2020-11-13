import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio
from app.content.utils import get_git_content

RAW_GIT_URL = "https://raw.githubusercontent.com/thatscotdatasci/streamlit-example/master/"
DOCKERFILE_URL = "".join((RAW_GIT_URL, "Dockerfile"))
DOCKER_COMPOSE_URL = "".join((RAW_GIT_URL, "docker-compose.yml"))
SETUP_SCRIPT_URL = "".join((RAW_GIT_URL, "setup.sh"))
LOCAL_SCRIPT_URL = "".join((RAW_GIT_URL, "local.sh"))


class StreamlitAppOperationsRadio(AbstractNavigationRadio):

    name = "Streamlit App Operations"

    def _action(self):
        dockerfile_content = get_git_content(DOCKERFILE_URL)
        docker_compose_content = get_git_content(DOCKER_COMPOSE_URL)
        setup_script_content = get_git_content(SETUP_SCRIPT_URL)
        local_script_content = get_git_content(LOCAL_SCRIPT_URL)

        st.markdown("""
        
        ## Running from the Command Line
        
        Running a Streamlit app locally is as simple as executing the following terminal command:
        
        ```
        streamlit run <path_to_app>
        ```
        
        The Streamlit process monitors files for changes, so it's not necessary to restart it each time a modificaiton is made.
        
        Various arguments can be passed to the run command; the one I most commonly use is to change the port Streamlit 
        listens to connections on (the default is `8501`):
        
        ```
        streamlit run <path_to_app> --server.port "$PORT"
        ```
        
        ## Docker Containerisation
        
        To give my Streamlit apps portability (that is, the ability to be run on multiple different platforms - such as 
        Heroku, AWS ECS, etc.) I have containerised them using [Docker](https://www.docker.com/). By always running the apps locally using the same
        Docker image that will eventually be deployed, I can have confidence that the deployed app should work as
        expected.
        
        ### Dockerfile
        
        The required Dockerfile is very simple; just ensure that the `requirements.txt` includes all necessary
        libraries, including Streamlit. The purpose of `setup.sh` is described below.
        
        """)

        st.code(dockerfile_content, language="docker")

        st.markdown("""
        
        ### docker-compose.yml

        Not required for the Heroku deployment, but convenient for defining how containers should be executed (what
        volumes should be mounted, what ports exposed, etc.). If the application comprises many services, Docker Compose
        is recommend by Heroku for local development (see 
        [here](https://devcenter.heroku.com/articles/local-development-with-docker-compose)).

        This will normally be a very simple file, given Streamlit is usually going to be the only service. In 
        certain circumstances, it may be desired to also run a database, or even some scheduler + workers, but that's
        almost certainly going to be overkill for a Streamlit app.

        The port Streamlit listens on needs to be exposed (see `local.sh` below). The code repository is mounted as the
        working directory defined in the `Dockerfile` so that modifications are immediately reflected in the app,
        without needing to restart the container.
        """)

        st.code(docker_compose_content, language="docker")

        st.markdown("""

        ### setup.sh

        The purpose of this script is to create a Streamlit config file. See the 
        [Streamlit Configuration](https://docs.streamlit.io/en/stable/streamlit_configuration.html) documentation for
        information on the available parameters.
        
        Running previous versions of Streamlit on Docker/Heroku required various parameters to be set. Now, the only 
        flag I set is `headless=True` to prevent Streamlit from attempting to open a browser window on start.

        """)

        st.code(setup_script_content, language="bash")

        st.markdown("""
        
        ### local.sh
        
        This file sets the port Streamlit should listen for connections on (which is used by both the Dockerfile and
        docker-compose.yml) and starts a container running the Streamlit app.
        
        By specifying the `--build` flag the image will be updated with any changes before a container is started.
        
        """)

        st.code(local_script_content, language="bash")
