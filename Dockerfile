FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

COPY . /code

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
