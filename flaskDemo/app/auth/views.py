from flask import redirect, request, url_for, flash
from flask import render_template
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm


# 登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    meta_title = "登录"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password',)
    return render_template(
        'auth/index.html.j2',
        meta_title=meta_title,
        form=form)
