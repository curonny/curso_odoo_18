
from odoo.http import Session

class LoginSession(Session):
    def authenticate(self, db, credential):
        return super().authenticate(db, credential)
