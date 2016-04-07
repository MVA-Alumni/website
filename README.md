Dans /etc/rc.local :

/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log --pidfile=/tmp/uwsgi.pid


Lien de mvaalumni_uwsgi.ini -> /srv/uwsgi/vassals

Lien de mvaalumni_nginx.conf -> /etc/nginx/sites-enabled


