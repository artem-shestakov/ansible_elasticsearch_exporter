import testinfra.utils.ansible_runner
import os
import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('es_exporter')

@pytest.fixture()
def AnsibleDefaults(host) -> dict: 
    "Get defaults roles's variables"
    return host.ansible("include_vars","../../defaults/main.yml")['ansible_facts']

def test_service(host):
    "If service started and enabled"
    service = host.service("elasticsearch_exporter.service")
    assert service.is_enabled
    assert service.is_running

def test_port(host, AnsibleDefaults):
    "If exporter port is opened"
    web_listen_address = AnsibleDefaults['web_listen_address']
    if web_listen_address.split(':')[0] == "":
        assert host.socket(f"tcp://{web_listen_address.split(':')[1]}").is_listening
    else:
        assert host.socket(f"tcp://{web_listen_address}").is_listening

def test_url(host, AnsibleDefaults):
    "If metrics path return 200 code"
    if AnsibleDefaults['web_listen_address'].split(':')[0] == "":
        exporter_address = f"127.0.0.1:{AnsibleDefaults['web_listen_address'].split(':')[1]}"
    else:
        exporter_address = AnsibleDefaults['web_listen_address']
    exporter_path = AnsibleDefaults['web_telemetry_path']
    cmd = host.run(f"curl http://{exporter_address}{exporter_path} -I")
    assert "200 OK" in cmd.stdout