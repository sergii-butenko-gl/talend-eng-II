FROM python:3.11-buster

WORKDIR /framework
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "pytest" ]
CMD [ "-s", "-v" ]