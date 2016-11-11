# Get emails of a promotion
# Not tested, may contain errors

from directory.models import Alumnus

year = 2015

promo = Alumnus.objects.filter(year=year)
mails = [al.user.email for al in promo]
mail_list = ', '.join(mails)

print(mail_list)

