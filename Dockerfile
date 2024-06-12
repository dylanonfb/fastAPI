FROM python:3 as build
WORKDIR /app

COPY ./requirement.txt ./requirement.txt

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 80

CMD ["fastapi","run", "--port","80"]
