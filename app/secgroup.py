from flask import Blueprint, jsonify, request
from app.aws_cred import get_aws_client

security_bp = Blueprint('security', __name__)

@security_bp.route('/security-groups', methods=['POST'])
def check_security_groups():
    data = request.json
    instance_id = data.get('instance_id')

    if not instance_id:
        return jsonify({"error": "Missing instance ID"}), 400

    ec2_client, error = get_aws_client('ec2')

    if error:
        return jsonify({"error": error}), 400

    try:
        # Fetch the instance details to get the security groups
        instance_response = ec2_client.describe_instances(InstanceIds=[instance_id])
        security_group_ids = []
        for reservation in instance_response['Reservations']:
            for instance in reservation['Instances']:
                security_group_ids.extend([sg['GroupId'] for sg in instance['SecurityGroups']])

        # Fetch the security group details
        if not security_group_ids:
            return jsonify({"error": "No security groups attached to this instance"}), 404

        security_group_response = ec2_client.describe_security_groups(GroupIds=security_group_ids)

        # Inspect the security group rules for vulnerabilities
        vulnerabilities = []
        for sg in security_group_response['SecurityGroups']:
            group_name = sg['GroupName']
            for rule in sg['IpPermissions']:
                if 'IpRanges' in rule:
                    for ip_range in rule['IpRanges']:
                        if ip_range.get('CidrIp') == '0.0.0.0/0':
                            vulnerabilities.append({
                                "GroupId": sg['GroupId'],
                                "GroupName": group_name,
                                "PortRange": f"{rule.get('FromPort')} - {rule.get('ToPort')}",
                                "Protocol": rule.get('IpProtocol'),
                                "CidrIp": ip_range.get('CidrIp'),
                                "Risk": "Open to the world"
                            })

        return jsonify({
            "instance_id": instance_id,
            "vulnerabilities": vulnerabilities if vulnerabilities else "No vulnerabilities found"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
