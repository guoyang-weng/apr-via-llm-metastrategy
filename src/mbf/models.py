import os
import json
import requests

completion_tokens = prompt_tokens = 0

KEY_FILE = os.getenv("AZURE_OPENAI_API_KEY", "")

# Load the service key
def load_key():
    if KEY_FILE != "":
        with open(KEY_FILE, "r") as key_file:
            svc_key = json.load(key_file)
        return svc_key
    else:
        print("Warning: AZURE_OPENAI_API_KEY is not set")

# Get Token
def get_token(svc_key):
    svc_url = svc_key["url"]
    client_id = svc_key["uaa"]["clientid"]
    client_secret = svc_key["uaa"]["clientsecret"]
    uaa_url = svc_key["uaa"]["url"]

    params = {"grant_type": "client_credentials" }
    resp = requests.post(f"{uaa_url}/oauth/token",
                        auth=(client_id, client_secret),
                        params=params)

    token = resp.json()["access_token"]

    return token

def make_request(data):
    my_svc_key = load_key()
    my_token = get_token(my_svc_key)

    headers = {
        "Authorization":  f"Bearer {my_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f'{my_svc_key["url"]}/api/v1/completions',
                         headers=headers,
                         json=data)
    return response

def gpt(prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

def chatgpt(messages, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    global completion_tokens, prompt_tokens
    outputs = []
    while n > 0:
        cnt = min(n, 20)
        data = {
            "deployment_id": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": 0.95,
            "n": cnt,
            "stop": stop
        }
        n -= cnt
        response = make_request(data)
        json_response = response.json()
        if "choices" in json_response:
            outputs.extend([choice["message"]["content"] for choice in json_response["choices"]])
            # log completion tokens
            completion_tokens += json_response["usage"]["completion_tokens"]
            prompt_tokens += json_response["usage"]["prompt_tokens"]
        else:
            outputs.extend([])
    return outputs
    
def gpt_usage(backend="gpt-4"):
    global completion_tokens, prompt_tokens
    if backend == "gpt-4":
        cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
    elif backend == "gpt-3.5-turbo":
        cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.002
    return {"completion_tokens": completion_tokens, "prompt_tokens": prompt_tokens, "cost": cost}
