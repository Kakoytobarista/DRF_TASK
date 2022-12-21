FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code
ADD . /code
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8000
CMD [ "sh", "-c", \
"cd drf_task \
python3 manage.py migrate \
&& \
python manage.py runserver 0:8000" \
]
