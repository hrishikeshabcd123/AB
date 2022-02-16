FROM python:3.7
LABEL maintainer="Alexander Pankov <ap@wdevs.ru>"

ARG environment=production

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/* ./
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=${environment}

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
