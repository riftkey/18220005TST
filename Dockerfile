FROM python:3.10.4
WORKDIR /TST
COPY requirements.txt /TST/requirements.txt
RUN pip install -r requirements.txt
COPY . /TST
EXPOSE 8080
CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]