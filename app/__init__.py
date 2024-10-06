from flask import Flask
from app.aws_cred import aws_credentials_bp
from app.ec2 import ec2_bp
from app.scan import scan_bp
from app.secgroup import security_bp
from flask_cors import CORS


# Create the Flask app
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(aws_credentials_bp)
    app.register_blueprint(ec2_bp)
    app.register_blueprint(scan_bp)
    app.register_blueprint(security_bp)

    return app
