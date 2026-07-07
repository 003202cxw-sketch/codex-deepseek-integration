# Codex-DeepSeek Integration

🚀 **Complete integration of OpenAI Codex with DeepSeek API for code generation, completion, review, optimization, and bug detection.**

## Features

✨ **Core Capabilities:**
- 📝 **Code Completion** - Generate code completions based on prompts
- 🛠️ **Code Generation** - Generate complete production-ready code
- 📚 **Code Explanation** - Explain and understand existing code
- 🔍 **Code Review** - Review code with quality and security insights
- ⚡ **Code Optimization** - Optimize code for performance and readability
- 🐛 **Bug Detection** - Identify potential bugs and suggest fixes

## Tech Stack

- **Backend:** Python (Flask) & Node.js (Express)
- **API:** DeepSeek AI
- **Models:** DeepSeek Coder
- **Configuration:** Environment variables via `.env`

## Prerequisites

- Python 3.8+ or Node.js 14+
- DeepSeek API Key ([Get one here](https://platform.deepseek.com))

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/003202cxw-sketch/codex-deepseek-integration.git
cd codex-deepseek-integration
```

### 2. Setup Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your DeepSeek API Key:

```env
DEEPSEEK_API_KEY=your_actual_api_key_here
DEEPSEEK_API_BASE=https://api.deepseek.com/v1
DEEPSEEK_MODEL=deepseek-coder
MAX_TOKENS=2048
TEMPERATURE=0.7
PORT=8000
```

### 3a. Python Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python3 -m flask --app src.app run
```

### 3b. Node.js Setup

```bash
# Install dependencies
npm install

# Run the Express server
npm start
```

## API Endpoints

### Health Check

```bash
GET /health
```

Response:
```json
{
  "status": "healthy",
  "service": "codex-deepseek-integration"
}
```

### 1. Code Completion

```bash
POST /api/code-completion
Content-Type: application/json

{
  "prompt": "Write a function to calculate factorial",
  "context": "Python function (optional)"
}
```

### 2. Code Generation

```bash
POST /api/code-generation
Content-Type: application/json

{
  "description": "A Python class for managing a todo list with add, remove, and list methods"
}
```

### 3. Code Explanation

```bash
POST /api/code-explanation
Content-Type: application/json

{
  "code": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
}
```

### 4. Code Review

```bash
POST /api/code-review
Content-Type: application/json

{
  "code": "your code here"
}
```

### 5. Code Optimization

```bash
POST /api/code-optimization
Content-Type: application/json

{
  "code": "your code here"
}
```

### 6. Bug Detection

```bash
POST /api/bug-detection
Content-Type: application/json

{
  "code": "your code here"
}
```

## Usage Examples

### Python

```python
from src.deepseek_client import DeepSeekClient

client = DeepSeekClient()

# Code Completion
result = client.code_completion("Write a sorting function")
print(result)

# Code Generation
result = client.code_generation("A weather API client")
print(result)

# Code Explanation
code = "def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)"
result = client.code_explanation(code)
print(result)

# Code Review
result = client.code_review(code)
print(result)

# Code Optimization
result = client.code_optimization(code)
print(result)

# Bug Detection
result = client.bug_detection(code)
print(result)
```

Run example:
```bash
python3 examples/python_example.py
```

### Node.js

```javascript
const axios = require('axios');

const api = axios.create({
  baseURL: 'http://localhost:8000'
});

// Code Completion
api.post('/api/code-completion', {
  prompt: 'Write a sorting function'
}).then(res => console.log(res.data.result));

// Code Generation
api.post('/api/code-generation', {
  description: 'A weather API client'
}).then(res => console.log(res.data.result));
```

Run example:
```bash
node examples/node_example.js
```

## Testing with cURL

### Health Check

```bash
curl -X GET http://localhost:8000/health
```

### Code Completion

```bash
curl -X POST http://localhost:8000/api/code-completion \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a function to calculate factorial"
  }'
```

### Code Generation

```bash
curl -X POST http://localhost:8000/api/code-generation \
  -H "Content-Type: application/json" \
  -d '{
    "description": "A Python class for managing a todo list"
  }'
```

### Code Review

```bash
curl -X POST http://localhost:8000/api/code-review \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def sum_list(lst):\n    total = 0\n    for i in range(len(lst)):\n        total = total + lst[i]\n    return total"
  }'
```

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| `DEEPSEEK_API_KEY` | - | Your DeepSeek API key (required) |
| `DEEPSEEK_API_BASE` | `https://api.deepseek.com/v1` | DeepSeek API endpoint |
| `DEEPSEEK_MODEL` | `deepseek-coder` | Model to use |
| `MAX_TOKENS` | `2048` | Maximum response length |
| `TEMPERATURE` | `0.7` | Response creativity (0-1) |
| `PORT` | `8000` | Server port |
| `HOST` | `0.0.0.0` | Server host |
| `ENVIRONMENT` | `development` | Environment (development/production) |

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── app.py                 # Flask application
│   ├── config.py              # Configuration management
│   ├── deepseek_client.py     # DeepSeek API client
│   ├── server.js              # Express server
│   └── deepseekClient.js      # Node.js DeepSeek client
├── examples/
│   ├── python_example.py      # Python usage examples
│   └── node_example.js        # Node.js usage examples
├── .env.example               # Environment template
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
├── package.json               # Node.js dependencies
└── README.md                  # This file
```

## Error Handling

### Missing API Key

```json
{
  "error": "DEEPSEEK_API_KEY environment variable is not set"
}
```

### Invalid Request

```json
{
  "error": "prompt is required"
}
```

### API Error

```json
{
  "error": "DeepSeek API Error: ..."
}
```

## Performance Tips

- Adjust `MAX_TOKENS` based on your needs (higher = slower but more detailed)
- Use `TEMPERATURE` 0.3-0.5 for consistent results, 0.7-1.0 for creative results
- Cache responses when possible
- Use streaming for large requests (if supported)

## Security Considerations

- Never commit `.env` file with real API keys
- Use environment variables in production
- Implement rate limiting
- Validate user inputs
- Use HTTPS in production

## Troubleshooting

### Connection Refused

```bash
# Check if server is running
lsof -i :8000

# Kill process if needed
kill -9 <PID>
```

### API Key Errors

```bash
# Verify API key
echo $DEEPSEEK_API_KEY

# Test API connectivity
curl -X POST https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-coder","messages":[{"role":"user","content":"test"}]}'
```

### Module Import Errors

```bash
# Python
pip install -r requirements.txt --force-reinstall

# Node.js
rm -rf node_modules package-lock.json
npm install
```

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

- 📧 Email: 003202cxw@gmail.com
- 🔗 GitHub: [003202cxw-sketch](https://github.com/003202cxw-sketch)
- 📚 DeepSeek Docs: [https://platform.deepseek.com/docs](https://platform.deepseek.com/docs)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Changelog

### v1.0.0 (Initial Release)
- ✅ Code Completion support
- ✅ Code Generation support
- ✅ Code Explanation support
- ✅ Code Review support
- ✅ Code Optimization support
- ✅ Bug Detection support
- ✅ Python (Flask) implementation
- ✅ Node.js (Express) implementation
- ✅ Complete documentation

---

**Made with ❤️ by 003202cxw-sketch**
