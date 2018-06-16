from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # user_count = User.query.count()
    if form.validate_on_submit():
        session['name'] = form.name.data

    return render_template(
        'main/index.html.j2',
        name=session.get('name'),
        form=form)
