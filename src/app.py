from flask import Flask, request, jsonify
from src.config import Config, validate_config
from src.deepseek_client import DeepSeekClient

app = Flask(__name__)

# Validate configuration
try:
    validate_config()
except ValueError as e:
    print(f"Configuration Error: {e}")
    exit(1)

# Initialize DeepSeek client
client = DeepSeekClient()


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "codex-deepseek-integration"}), 200


@app.route('/api/code-completion', methods=['POST'])
def code_completion():
    """Code completion endpoint"""
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        context = data.get('context')
        
        if not prompt:
            return jsonify({"error": "prompt is required"}), 400
        
        result = client.code_completion(prompt, context)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/code-generation', methods=['POST'])
def code_generation():
    """Generate complete code endpoint"""
    try:
        data = request.get_json()
        description = data.get('description')
        
        if not description:
            return jsonify({"error": "description is required"}), 400
        
        result = client.code_generation(description)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/code-explanation', methods=['POST'])
def code_explanation():
    """Explain code endpoint"""
    try:
        data = request.get_json()
        code = data.get('code')
        
        if not code:
            return jsonify({"error": "code is required"}), 400
        
        result = client.code_explanation(code)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/code-review', methods=['POST'])
def code_review():
    """Code review endpoint"""
    try:
        data = request.get_json()
        code = data.get('code')
        
        if not code:
            return jsonify({"error": "code is required"}), 400
        
        result = client.code_review(code)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/code-optimization', methods=['POST'])
def code_optimization():
    """Code optimization endpoint"""
    try:
        data = request.get_json()
        code = data.get('code')
        
        if not code:
            return jsonify({"error": "code is required"}), 400
        
        result = client.code_optimization(code)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/bug-detection', methods=['POST'])
def bug_detection():
    """Bug detection endpoint"""
    try:
        data = request.get_json()
        code = data.get('code')
        
        if not code:
            return jsonify({"error": "code is required"}), 400
        
        result = client.bug_detection(code)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
