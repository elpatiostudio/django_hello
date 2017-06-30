FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
#		mysql-client libmysqlclient-dev \
#		postgresql-client libpq-dev \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app

ADD ./django.prj/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
