FROM python:3.11-slim

RUN pip install pyserial paho-mqtt

COPY mb7062.py /mb7062.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]