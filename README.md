simple-flask-app-on-dokku
=========================
1. Log in to digital ocean instance:

exp2: ssh -i ~/.ssh/id_rsa_digitalocean root@95.85.49.94

2. Run worker:

dokku run little-flask-app python worker.py

3. Deploy on digitalocean with dokku:

ssh-add ~/.ssh/id_rsa_digitalocean
git push dokku master

4. HOWTOs:

docker images # list available docker images
docker ps # list running containers

docker run <image> python /app/worker.py # run worker

5. cron:

open crontab for edit:

crontab -e

put a cron record:

# m h  dom mon dow   command
55,57 * * * * docker run 178f480dee41 python /app/worker.py

