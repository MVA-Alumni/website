# Installation steps for production

* Create a virtual env (see mvaalumni_uwsgi.ini)
* Add the following command in /etc/rc.local :
`/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log --pidfile=/tmp/uwsgi.pid`
* Create some symbolic links :
  * mvaalumni_uwsgi.ini -> /etc/uwsgi/vassals
  * mvaalumni_nginx.conf -> /etc/nginx/sites-enabled
  * settings_prod.py -> settings.py
* Copy settings_local.py.example to settings.local.py

