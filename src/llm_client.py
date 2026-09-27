"""LLM client for Ollama integration"""

import requests
from typing import Optional, Dict


class OllamaClient:
    """Client for Ollama LLM"""

    def __init__(self, model: str = "mistral:7b",
                 base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"

    def health_check(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Ollama health check failed: {e}")
            return False

    def generate_response(self, prompt: str, stream: bool = False) -> str:
        """Generate response from LLM"""

        if not self.health_check():
            raise Exception("Ollama is not running. Start with: ollama serve &")

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "temperature": 0.3
        }

        try:
            response = requests.post(
                self.api_endpoint,
                json=payload,
                timeout=300
            )
            response.raise_for_status()

            result = response.json()
            return result.get("response", "")

        except Exception as e:
            print(f"❌ LLM generation failed: {e}")
            return ""

    def enhance_test_description(self, condition: Dict) -> str:
        """Use LLM to enhance test descriptions"""
        prompt = f"""Generate a clear test description for this condition:
Feature: {condition.get('feature')}
Type: {condition.get('type')}
Description: {condition.get('description')}

Provide a concise, actionable test description (1 sentence):"""

        response = self.generate_response(prompt)
        return response.strip().split('\n')[0]  # Get first line


# Test
if __name__ == "__main__":
    client = OllamaClient()

    if client.health_check():
        print("✅ Ollama is running")

        response = client.generate_response(
            "What is behavior driven development? (brief)"
        )
        print(f"Response: {response}")
    else:
        print("❌ Ollama is not running")
