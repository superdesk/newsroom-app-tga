from flask import Blueprint, render_template

blueprint = Blueprint('tga_public', __name__)


@blueprint.route('/terms')
def terms():
    return render_template('terms.html')


@blueprint.route('/about')
def about():
    return render_template('about.html')


@blueprint.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
