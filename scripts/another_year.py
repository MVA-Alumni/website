# Use this script to add a new promo in the database.
#
# Before, always activate the virtual env :
#   source ../venv-mvaalumni/bin/activate
#
# Then, run the script :
#   python manage.py shell
#   execfile('scripts/another_year.py')
#
# Maybe better : execute line by line in the python shell.

from directory.models import Year
Year.objects.create(pk=2016)
