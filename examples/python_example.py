#!/usr/bin/env python3
"""
Python example for using Codex-DeepSeek Integration
"""

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))

from src.deepseek_client import DeepSeekClient
from src.config import Config

# Load environment variables
load_dotenv()

def main():
    print("=" * 50)
    print("Codex-DeepSeek Integration Examples")
    print("=" * 50)
    
    # Initialize client
    client = DeepSeekClient()
    
    # Example 1: Code Completion
    print("\n1. Code Completion")
    print("-" * 50)
    prompt = "Write a function to calculate factorial"
    result = client.code_completion(prompt)
    print(f"Prompt: {prompt}")
    print(f"Result:\n{result}")
    
    # Example 2: Code Generation
    print("\n2. Code Generation")
    print("-" * 50)
    description = "A Python class for managing a simple todo list with add, remove, and list methods"
    result = client.code_generation(description)
    print(f"Description: {description}")
    print(f"Result:\n{result}")
    
    # Example 3: Code Explanation
    print("\n3. Code Explanation")
    print("-" * 50)
    code = '''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''
    result = client.code_explanation(code)
    print(f"Code:\n{code}")
    print(f"Explanation:\n{result}")
    
    # Example 4: Code Review
    print("\n4. Code Review")
    print("-" * 50)
    code_to_review = '''
def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    return total
'''
    result = client.code_review(code_to_review)
    print(f"Code:\n{code_to_review}")
    print(f"Review:\n{result}")
    
    # Example 5: Code Optimization
    print("\n5. Code Optimization")
    print("-" * 50)
    code_to_optimize = '''
def find_max(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
'''
    result = client.code_optimization(code_to_optimize)
    print(f"Code:\n{code_to_optimize}")
    print(f"Optimization:\n{result}")
    
    # Example 6: Bug Detection
    print("\n6. Bug Detection")
    print("-" * 50)
    buggy_code = '''
def divide_numbers(a, b):
    result = a / b
    return result

def process_list(items):
    for i in range(len(items) + 1):
        print(items[i])
'''
    result = client.bug_detection(buggy_code)
    print(f"Code:\n{buggy_code}")
    print(f"Bug Detection:\n{result}")


if __name__ == "__main__":
    try:
        Config.DEEPSEEK_API_KEY
        main()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set DEEPSEEK_API_KEY in .env file")
        sys.exit(1)
