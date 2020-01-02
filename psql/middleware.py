from lib.psql.session import db_session


class PsqlMiddleware:
    def __init__(self, app):
        self.app = app

        app.after_request(self.after_request)

    def after_request(self, response):
        db_session.close()
        return response
