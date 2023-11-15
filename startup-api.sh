cd .docker
docker compose up -d --build

cd ../api
python -m flask --app app --debug run --port 5050
