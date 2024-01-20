FROM python:3.9-slim
COPY . /backend
WORKDIR /backend
RUN python -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]