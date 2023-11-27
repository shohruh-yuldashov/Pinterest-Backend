FROM python:3.11-alpine

WORKDIR /app

COPY . .
COPY entrypoint.sh /app/entrypoint.sh
#RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN  /app/entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]

