# syntax=docker/dockerfile:1

FROM python:3.9.5

WORKDIR /code

COPY ./requirements.txt /journee/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app



HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/status || exit 1

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]