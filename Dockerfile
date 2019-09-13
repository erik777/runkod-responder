FROM python:3.6

ENV APP_DIR /deploy

RUN mkdir -p ${APP_DIR}

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

RUN pip3 install -r ${APP_DIR}/requirements.txt

EXPOSE 5001

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5001", "--chdir", "./src/responder/web/", "--pythonpath", "${APP_DIR}/src", "app:app"]
