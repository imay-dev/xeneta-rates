FROM  postgres:13

COPY rates.sql /docker-entrypoint-initdb.d/

EXPOSE 5432