FROM python:3.7

WORKDIR /app/

COPY requirements.txt ./
RUN pip install update && pip install -r requirements.txt

COPY docker_entrypoint.sh tsds.py ./

ENV PORT=80
CMD chmod +x docker_entrypoint.sh && ./docker_entrypoint.sh
