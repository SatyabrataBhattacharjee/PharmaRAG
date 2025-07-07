from langchain.llms.base import LLM
from pydantic import BaseModel, Field
from typing import Optional, List
import requests

class HuggingFaceLLM(LLM, BaseModel):
    model: str = Field(default="microsoft/Phi-3.5-mini-instruct")
    temperature: float = Field(default=0.3)
    max_new_tokens: int = Field(default=300)
    hf_api_key: str = Field(...)

    @property
    def _llm_type(self) -> str:
        return "huggingface_custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.hf_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": self.temperature,
                "max_new_tokens": self.max_new_tokens,
                "return_full_text": False
            }
        }
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{self.model}",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()[0]["generated_text"]
