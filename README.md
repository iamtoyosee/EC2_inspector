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
   git clone https://github.com/your-username/ec2-inspector.git
   cd ec2-inspector
