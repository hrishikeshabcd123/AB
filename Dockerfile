FROM centos:centos7

COPY ./requirements.txt /app/requirements.txt
RUN yum install -y python3 python3-pip python3-devel

WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py" ]
