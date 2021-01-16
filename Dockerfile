FROM python:3.9

WORKDIR /code
COPY requirements.txt ./

RUN pip install -r requirements.txt

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh
CMD [ "./wait-for-it.sh" ]