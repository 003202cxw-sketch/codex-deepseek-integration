import requests
from typing import List, Dict, Optional
from src.config import Config


class DeepSeekClient:
    """Client for interacting with DeepSeek API"""
    
    def __init__(self):
        self.api_key = Config.DEEPSEEK_API_KEY
        self.api_base = Config.DEEPSEEK_API_BASE
        self.model = Config.MODEL_NAME
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> Dict:
        """Call DeepSeek Chat Completion API"""
        
        temperature = temperature or Config.TEMPERATURE
        max_tokens = max_tokens or Config.MAX_TOKENS
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(
                Config.CHAT_ENDPOINT,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": response.status_code}
    
    def code_completion(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate code completion based on prompt"""
        
        system_message = {
            "role": "system",
            "content": "You are an expert code assistant. Write clean, efficient, and well-documented code."
        }
        
        user_message_content = prompt
        if context:
            user_message_content = f"Context:\n{context}\n\nRequest:\n{prompt}"
        
        messages = [
            system_message,
            {"role": "user", "content": user_message_content}
        ]
        
        response = self.chat_completion(messages)
        
        if "error" in response:
            return f"Error: {response['error']}"
        
        return response["choices"][0]["message"]["content"]
    
    def code_generation(self, description: str) -> str:
        """Generate complete code based on description"""
        
        prompt = f"Generate complete, production-ready code for: {description}"
        return self.code_completion(prompt)
    
    def code_explanation(self, code: str) -> str:
        """Explain given code"""
        
        prompt = f"Explain the following code in detail:\n\n```\n{code}\n```"
        return self.code_completion(prompt)
    
    def code_review(self, code: str) -> str:
        """Review and provide feedback on code"""
        
        prompt = f"""Please review the following code and provide:
1. Code quality assessment
2. Performance suggestions
3. Security concerns (if any)
4. Best practices recommendations
5. Refactoring suggestions

Code:\n```\n{code}\n```"""
        return self.code_completion(prompt)
    
    def code_optimization(self, code: str) -> str:
        """Optimize the given code"""
        
        prompt = f"""Optimize the following code for performance and readability:

```\n{code}\n```

Provide the optimized version with explanations."""
        return self.code_completion(prompt)
    
    def bug_detection(self, code: str) -> str:
        """Detect potential bugs in code"""
        
        prompt = f"""Analyze the following code for potential bugs, errors, and issues:

```\n{code}\n```

Provide detailed analysis and suggested fixes."""
        return self.code_completion(prompt)
