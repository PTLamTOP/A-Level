from datetime import timedelta, datetime
import pytz

from django.contrib.auth import logout


class LastActionCheckMiddleware(object):
    """
    Middleware checks when authorized user (NOT admin) makes the last request.
    If the last request was 5 minutes ago from current request -> logout.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # STEP 1: check if user: 1) is NOT admin; 2) is authenticated
        if not request.user.is_superuser and request.user.is_authenticated:
            local = pytz.timezone('Europe/Kiev')
            # STEP 2: Try to get last_action in session:
            # 2.1: if there is not last_action in the session -> add new key 'last_action' with current time
            if not request.session.get('last_action'):
                request.session['last_action'] = datetime.now().timestamp()
            else:
                # 2.2: if there is key 'last action' in the session -> compare current time with 'last_action' time
                # 2.2.1: If MORE than 5 minutes -> delete 'last_action' from the session and logout
                local_time_now = local.localize(datetime.now())
                last_action_time = local.localize(datetime.fromtimestamp(request.session.get('last_action')))
                if (local_time_now - last_action_time) >= timedelta(minutes=5):
                    del request.session['last_action']
                    logout(request)
                else:
                    # 2.2.2: if NOT MORE than 5 minutes -> update time of 'last_action' to new current time
                    request.session['last_action'] = datetime.now().timestamp()
        response = self.get_response(request)
        return response
