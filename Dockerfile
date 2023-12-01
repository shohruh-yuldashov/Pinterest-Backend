FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
