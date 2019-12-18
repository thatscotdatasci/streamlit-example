FROM python:3.7

WORKDIR /app/

COPY requirements.txt ./
RUN pip install update && pip install -r requirements.txt

COPY docker_entrypoint.sh tsds.py ./

CMD sh docker_entrypoint.sh
