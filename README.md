# EC2 Inspector

**EC2 Inspector** is a Flask-based application that allows users to inspect their AWS EC2 instances for potential security vulnerabilities, such as open ports and security groups that allow traffic from all IP addresses (0.0.0.0/0). This tool aims to help cloud engineers and developers ensure their EC2 instances are configured securely and in line with best practices.

## Features

- **Security Group Inspection**: Check the security groups attached to an EC2 instance and flag any rules that allow unrestricted access (0.0.0.0/0).
- **Port Scanning**: Scan the EC2 instance’s public IP for open ports.
- **Modular Design**: Built with Flask Blueprints, making it easy to extend and maintain.

> **Note**: This project is still under development. We welcome contributions and collaboration from developers and cloud engineers to enhance its features.

## Requirements

- Python 3.8+
- Flask
- Boto3 (AWS SDK for Python)
- Nmap (for port scanning)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iamtoyosee/EC2-inspector.git
   cd EC2-inspector
   ```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```
3. Set up AWS credentials (either as environment variables or via AWS CLI):

```bash
export AWS_ACCESS_KEY_ID='your-access-key'
export AWS_SECRET_ACCESS_KEY='your-secret-key'
export AWS_DEFAULT_REGION='your-region' 
```

## Usage

1. Start the Flask server:

```bash
python run.py
```

2. Set AWS Credentials: Make a POST request to /aws/set with your AWS credentials.

Example request body:

```json
{
  "aws_access_key": "YOUR_ACCESS_KEY",
  "aws_secret_key": "YOUR_SECRET_KEY",
  "aws_region": "us-east-1"
}
```

3. Inspect an EC2 Instance's Security Groups: Make a POST request to /security-groups with the instance_id of the EC2 instance you want to inspect.

Example request body:

```json
{
  "instance_id": "i-0123456789abcdef0"
}
```

4. Scan an EC2 Instance for Open Ports: Make a POST request to /scan/ports with the public IP address of the EC2 instance.

Example request body:

```json
{
  "ip_address": "54.123.45.67"
}
```

## Roadmap
 Improve error handling and edge case management.
 Add detailed vulnerability descriptions and recommendations.
 Implement authentication for the API.
 Add more AWS services to inspect (e.g., S3, RDS).
 Integrate AWS Trusted Advisor for advanced checks.


## Contributing
We welcome contributions from the community! Whether it's improving existing features, adding new ones, or suggesting improvements, feel free to:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -m 'Add feature name').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

Please make sure to follow the coding style and standards set in this project. If you have any questions, feel free to open an issue or reach out.


## Contact
For any inquiries or suggestions, please reach out to blacktechiegirl@gmail.com

## Disclaimer
This tool is intended for use in testing and inspecting your own AWS resources. Ensure you have proper permissions before scanning any EC2 instances or AWS resources.