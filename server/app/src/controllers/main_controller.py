from flask import Blueprint, request, render_template, make_response, redirect
from http import HTTPStatus

from ..models.session_model import Session
from .backofficer_controller import backofficer_bp
from .collector_controller import collector_bp
from .janitor_controller import janitor_bp
from .mcp_controller import mcp_bp

main_bp = Blueprint('main', __name__)

@main_bp.before_request
def auth():
    access_token = request.cookies.get('access_token')
    if not Session.has(access_token):
        return redirect('/login')

@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('/layout/main.html', content='index.html')

main_bp.register_blueprint(backofficer_bp, url_prefix='/backofficer')
main_bp.register_blueprint(collector_bp, url_prefix='/collector')
main_bp.register_blueprint(janitor_bp, url_prefix='/janitor')
main_bp.register_blueprint(mcp_bp, url_prefix='/mcp')
