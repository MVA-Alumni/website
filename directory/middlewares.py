from django.utils.timezone import now

class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing.
            al = request.user.alumnus
            al.last_visit = now()
            al.save()
        return response
