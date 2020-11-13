import streamlit as st

from app.abstract_classes.abstract_navigation_radio import AbstractNavigationRadio
from app.content.utils import get_git_content


HEROKU_TERRAFORM_GIT_REPO_URL = "https://github.com/thatscotdatasci/heroku-terraform/main/"
RAW_HEROKU_TERRAFORM_GIT_REPO_URL = "https://raw.githubusercontent.com/thatscotdatasci/heroku-terraform/main/"
TF_APPS_URL = "".join((RAW_HEROKU_TERRAFORM_GIT_REPO_URL, "apps.tf"))
GITHUB_ACTION_URL = "".join((RAW_HEROKU_TERRAFORM_GIT_REPO_URL, ".github/workflows/main.yml"))


class HerokuRadio(AbstractNavigationRadio):

    name = "Heroku Hosting"

    def _action(self):
        st.markdown(f"""
        
        ## What is Heroku?
        
        Direct from the [Heroku website](https://www.heroku.com):
        
        > Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Our platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market.
        
        ## Why use it?
        
        I use Heroku as it provides the following for free (figures below are for verified accounts - more info about the free offering can be found [here](https://www.heroku.com/free)):
        
        - 100 apps (which will take me a long time to reach)
        - 1000 free 'dyno' hours per month (i.e. a total runtime of 1000 hours, where each app is 'awoken' when a web request is recieved, and sleep after 30 minutes of inactivity)
        - 512 MB RAM per dyno (not much, put plenty for simple apps)
        
        As long as the Streamlit app is packaged as a Docker image, it can be deployed to Heroku in a matter of minutes - as is discussed below.
        
        ## Creating a new app
        
        A new Heroku app needs to be created whenever you want to deploy a new Streamlit app.
        This can be done easily via the UI or [CLI](https://devcenter.heroku.com/articles/creating-apps), however  I use [Terraform](https://www.terraform.io/) to manage my Heroku apps.
        
        I manage this via my [heroku-terraform]({HEROKU_TERRAFORM_GIT_REPO_URL}) repo. Each Heroku app has an entry in `apps.tf`:
        
        """)

        with st.beta_expander(label="Content of apps.tf", expanded=False):
            st.code(get_git_content(TF_APPS_URL), language="terraform")

        st.markdown("""
        
        To create a new app, I simply need to add a new entry to the file.
        
        Once committed, the following GitHub action will automatically run Terraform apply.
        
        """)

        with st.beta_expander(label="Terraform apply GitHub Action", expanded=False):
            st.code(get_git_content(GITHUB_ACTION_URL), language="yaml")

        st.markdown("""
        
        Current job status: ![Terraform Workflow](https://github.com/thatscotdatasci/heroku-terraform/workflows/Terraform%20Workflow/badge.svg?branch=main)
        
        Previous executions can be seen [here](https://github.com/thatscotdatasci/heroku-terraform/actions).
        
        ## Deploying the App
        
        Full documentation can be found [here](https://devcenter.heroku.com/articles/container-registry-and-runtime),
        however the following three commands are all that's needed:
        
        - login to the container registry (run `heroku login` to login via a web browser first, or set the `HEROKU_API_KEY`environment variable)
        
          `heroku container:login`
          
        - build the Docker image defined by the Dockerfile and push it to the container registry (note the dyno is being called `web` here - any name could be used):
        
          `heroku container:push web -a "$HEROKU_APP"`
        
        - release the new image to the Heroku app
        
          `heroku container:release web -a "$HEROKU_APP"`
        
        """)

