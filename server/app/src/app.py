from flask import Flask, request, redirect, render_template, make_response
from http import HTTPStatus

from .models.user_model import User
from .models.session_model import Session
from .controllers.main_controller import main_bp

app = Flask(
    __name__,
    template_folder='./views/',
)

@app.route('/login', methods=['GET', 'POST'])
def login():
    match request.method:
        case 'GET':
            access_token = request.cookies.get('access_token')
            if Session.has(access_token):
                return redirect(request.args.get('returnUrl') or '/', HTTPStatus.OK)
            else:
                return render_template('/layout/main.html', content='login.html')

        case 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            access_token, status = User.login(username, password)

            if access_token is None:
                return make_response({'message': status}, HTTPStatus.UNAUTHORIZED)
            else:
                Session.add(access_token)
                response = make_response(redirect(request.args.get('returnUrl') or '/'))
                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    max_age=(24 * 60 * 60),
                    expires=(24 * 60 * 60),
                    httponly=True,
                    samesite='Strict'
                )
                return response

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
