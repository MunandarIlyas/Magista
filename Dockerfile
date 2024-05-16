FROM python:3.9

# Copy all project files
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Running migrations
RUN python manage.py migrate

# Create superuser using Django shell
RUN echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='satria').exists() or \
User.objects.create_superuser('satria', 'satria@email.com', 'satria123')" \
| python manage.py shell

# Gunicorn command
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
