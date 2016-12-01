# Use this script to add a new admin.
#
# Before, always activate the virtual env :
#   source ../venv-mvaalumni/bin/activate
#
# Then, run the script :
#   python manage.py shell
#   execfile('scripts/new_admin.py')
#
# Better : execute line by line in the python shell.

from directory.models import Alumnus
new_admin = Alumnus.objects.get(user__first_name='Firstname')
new_admin.user.is_staff = True
new_admin.user.save()
