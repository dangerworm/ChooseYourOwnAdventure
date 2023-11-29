cd .docker
docker compose up -d && cd ..

cd api
flask --app app --debug run --port 5050
