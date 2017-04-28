from flask import request, jsonify, url_for
from . import api
from ..models import User
from .. import db


@api.route('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return jsonify(user.to_json())


@api.route('/user/<int:user_id>', methods=['PUT'])
def edit_profile(user_id):
    user = User.query.get_or_404(user_id)
    raw = request.json
    user.name = raw.get('name', user.name)
    user.location = raw.get('location', user.location)
    user.about_me = raw.get('about_me', user.about_me)
    db.session.add(user)
    return jsonify(user.to_json())
