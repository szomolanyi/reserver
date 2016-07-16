from app.user import user
from flask_security import roles_required

@user.route('/user')
@roles_required('customer')
def first():
	return "Ahoj svet"
