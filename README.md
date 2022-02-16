**Project Directory:**

- backend
  - requirements.txt
- frontend
- .env
- docker-compose.yml
- **django-rest framework:**
  Create backend django project:
- cd backend
- `django-admin startproject [project name]`
- `cd [project name]`
- `django-admin startapp [app name]`
- add environment files
  - create .env file and add the variables included in the .env-example file
- Building api endpoints:
  - model
  - url
  - router
  - view
  - endpoints
  - makemigrations
  - migrate

**vue**
Create Vue project:

- cd frontend
- `vue create [project name]`
- Optionally:
  - to add storybook`npx init`
    Start containers:
    `docker-compose up`
- building components

**Postgres**
configure

docker run -d --name container-name pyhton3 manage.py migrate

gitworkflow
