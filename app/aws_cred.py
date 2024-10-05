from flask import Blueprint, jsonify, request
import boto3

aws_credentials_bp = Blueprint('aws_credentials', __name__)

# Global dictionary to store AWS credentials
aws_credentials = {}

@aws_credentials_bp.route('/aws/set', methods=['POST'])
def set_aws_credentials():
    data = request.json
    aws_access_key = data.get('aws_access_key')
    aws_secret_key = data.get('aws_secret_key')
    aws_region = data.get('aws_region')

    if not aws_access_key or not aws_secret_key or not aws_region:
        return jsonify({"error": "Missing AWS credentials"}), 400

    # Store the credentials in a global dictionary
    aws_credentials['aws_access_key'] = aws_access_key
    aws_credentials['aws_secret_key'] = aws_secret_key
    aws_credentials['aws_region'] = aws_region
    

    return jsonify({"message": "AWS credentials stored successfully!"}), 200

# Helper function to get AWS credentials
def get_aws_client(service):
    if not aws_credentials:
        return None, "AWS credentials not set"

    try:
        client = boto3.client(service,
                              aws_access_key_id=aws_credentials['aws_access_key'],
                              aws_secret_access_key=aws_credentials['aws_secret_key'],
                              region_name=aws_credentials['aws_region'])
        return client, None
    except Exception as e:
        return None, str(e)
