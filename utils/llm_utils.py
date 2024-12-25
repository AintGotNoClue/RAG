import requests

def query_ollama(prompt: str, model: str = "llama3.2:latest", url: str = "http://localhost:11434/v1/completions"):
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        raise Exception(f"Ошибка подключения к Ollama: {response.status_code} - {response.text}")
