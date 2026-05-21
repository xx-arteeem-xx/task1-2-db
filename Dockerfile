FROM python:3.12-slim

WORKDIR /app

COPY task/films.db ./films.db
COPY task/music.db ./music.db
COPY solution/ ./solution/

RUN chmod +x /app/solution/run_all.sh

CMD ["bash", "/app/solution/run_all.sh"]
