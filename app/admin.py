from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import User, id

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(id, db.session))

