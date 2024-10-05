from flask import Blueprint, jsonify, request
import nmap

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/ports', methods=['POST'])
def scan_instance_ports():
    data = request.json
    ip_address = data.get('ip_address')

    if not ip_address:
        return jsonify({"error": "Missing IP address"}), 400

    try:
        nm = nmap.PortScanner()
        nm.scan(ip_address, '22-1024')

        open_ports = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    if nm[host][proto][port]['state'] == 'open':
                        open_ports.append(port)

        return jsonify({"ip_address": ip_address, "open_ports": open_ports})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
