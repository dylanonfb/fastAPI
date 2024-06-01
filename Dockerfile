FROM python:3
WORKDIR /app

COPY ./requirement.txt ./requirement.txt

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 80

CMD ["fastapi","run", "--port","80"]
