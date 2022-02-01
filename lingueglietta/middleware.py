import logging
import time

logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class GPFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before_timestamp = time.time()
        # logger.info(f"Tracking {before_timestamp}")
        ip_address = get_client_ip(request)

        logger.info(str(ip_address)+"-"+str(request))

        response = self.get_response(request)

        # after_timestamp = time.time()
        # delta = after_timestamp - before_timestamp
        # logger.info(f"Tracking {after_timestamp} for a delta of {delta}")

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        logger.info(f"Running {view_func.__name__} view")
