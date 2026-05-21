import os
import subprocess

def pull_models():
    # Fixed: changed list [] to dict {}
    # Fixed: removed all deprecated models
    # Fixed: added latest replacement models
    models = {
        "Llama 3.3-70B Versatile":          "llama-3.3-70b-versatile",        # replaces llama3-70b-8192
        "Llama 3.1-8B Instant":             "llama-3.1-8b-instant",           # replaces gemma2-9b-it
        "Llama 4 Maverick 17B":             "meta-llama/llama-4-maverick-17b-128e-instruct",  # new
        "Llama 4 Scout 17B":                "meta-llama/llama-4-scout-17b-16e-instruct",      # new
        "Qwen3 32B":                        "qwen/qwen3-32b",                  # new
        "GPT-OSS 120B":                     "openai/gpt-oss-120b",             # new
    }

    for model_name, model_id in models.items():
        print(f"Pulling model: {model_name} ({model_id})")
        subprocess.run(["ollama", "pull", model_id])

if __name__ == "__main__":
    pull_models()

                       
