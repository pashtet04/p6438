Mandatory envs:
    - APP_SETTINGS
    - DATABASE_URL

production: docker-compose up
debug: docker-compose -f docker-compose.debug.yml up

