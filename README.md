simple-flask-app-on-dokku
=========================
1. Log in to digital ocean instance:

exp2: ssh -i ~/.ssh/id_rsa_digitalocean root@95.85.49.94

2. Run worker:

dokku run little-flask-app python worker.py
