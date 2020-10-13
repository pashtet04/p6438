Mandatory envs:
    - APP_SETTINGS
    - DATABASE_URL

production: docker-compose up

debug: docker-compose -f docker-compose.debug.yml up

POST VALUE:
```
curl --location --request POST 'http://127.0.0.1:8080/post-value' \
--header 'Content-Type: application/json' \
--data-raw '{"value": "1", "lang": "Python"}'
```

➜ docker exec -it interview_db_1 bash
postgres=# \c postgres
postgres=# select * from results;
