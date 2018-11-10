 #! /usr/bin/python


import os
import sys
import json

from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy
from paramiko.ssh_exception import SSHException

SERVERS = None

def load_config(config_file="~/.servers_config"):
    global SERVERS
    config_file = os.path.expanduser(config_file)
    try:
        with open(config_file) as f:
            SERVERS = json.load(f)
    except FileNotFoundError:
        print("No configuration exists. exiting...")
        sys.exit(1)

load_config()

def run_commands_on_servers():
    if SERVERS is None:
        return

    for server in SERVERS['servers']:
        print("{:^30s}".format(server['hostname']))
        hostname = server['hostname']
        username = server['username']
        password = server['password']

        with SSHClient() as client:
            client.set_missing_host_key_policy(AutoAddPolicy)
            client.load_system_host_keys()

            client.connect(hostname, username=username, password=password)

            for command in server['commands']:
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read().decode("utf-8"))
                print(stderr.read().decode("utf-8"))

run_commands_on_servers()
