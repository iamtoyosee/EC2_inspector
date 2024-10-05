from flask import Blueprint, jsonify
from app.aws_cred import get_aws_client

ec2_bp = Blueprint('ec2', __name__)

@ec2_bp.route('/instances', methods=['GET'])
def list_ec2_instances():
    ec2_client, error = get_aws_client('ec2')

    if error:
        return jsonify({"error": error}), 400

    try:
        response = ec2_client.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    "InstanceId": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "PublicIpAddress": instance.get('PublicIpAddress', 'N/A')
                })

        return jsonify({"instances": instances})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
