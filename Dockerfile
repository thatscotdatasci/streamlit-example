FROM python:3.7

# Create dir for the app
WORKDIR /app/

# Install the requirements
COPY requirements.txt ./
RUN pip install update && pip install -r requirements.txt

# Add the required code
COPY setup.sh tsds.py ./

# Run the image as a non-root user - Heroku will not run as root
RUN useradd -m myuser
USER myuser

# Run the app - Heroku uses the CMD
# Execute setup.sh at runtime - needs to have the correct port
CMD sh setup.sh && streamlit run tsds.py --server.port "$PORT"
