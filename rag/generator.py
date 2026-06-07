"""
Ollama generation wrapper.
"""

import ollama

from config import OLLAMA_MODEL


class Generator:
    """
    Wrapper around Ollama for text generation.
    """

    def generate(self, prompt):
        """
        Send the prompt to Ollama and
        return the generated response.
        """

        response = ollama.chat(
            model=OLLAMA_MODEL,
            options={
                "temperature": 0,
            },
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return (
            response["message"]
            ["content"]
        )
    
