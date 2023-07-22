# Backend Dockerfile
FROM python:3.9

WORKDIR /final-pjt-back

COPY ./final-pjt-back/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./final-pjt-back .

CMD ["python", "manage.py", "runserver"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py loaddata initial_data.json && python manage.py runserver 0.0.0.0:8000"

# Frontend Dockerfile
FROM node:20

WORKDIR /final-pjt-front

COPY ./final-pjt-front/package*.json ./
RUN npm install

COPY ./final-pjt-front .

CMD ["npm", "run", "serve"]
