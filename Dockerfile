# Use an appropriate base image
FROM python:3.8

# Create the top level directory for the app
WORKDIR /streamlit_app/

# Copy the requirements and setup file; install the requirements
COPY requirements.txt setup.sh ./
RUN pip install update && pip install -r requirements.txt

# Add the app directory to the PYTHONPATH, and copy the app code to the current directory
ENV PYTHONPATH=$PYTHONPATH:app/
COPY app ./app/

# Run the image as a non-root user - Heroku will not allow the app to be run as root
RUN useradd -m myuser
USER myuser

# Run the app - Heroku uses the CMD
# The setup script is executed before the app is run
CMD sh setup.sh && streamlit run app/TSDSStreamlitExample.py --server.port "$PORT"
