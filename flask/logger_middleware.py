from flask import g, request
import time


class LoggerMiddleware:
    def __init__(self, app):
        self.app = app

        app.before_request(self.before_request)
        app.after_request(self.after_request)

    def before_request(self):
        g.request_started = time.time()

    def after_request(self, response):
        duration = round(time.time() - g.request_started, 5)
        ip_address = request.headers.get(
            "X-Forwarded-For",
            request.remote_addr,
        )
        print(f"🌐 {request.path} from: {ip_address} took {duration} seconds and returned status {response.status_code}")
        return response
