const axios = require('axios');

class DeepSeekClient {
    constructor() {
        this.apiKey = process.env.DEEPSEEK_API_KEY;
        this.apiBase = process.env.DEEPSEEK_API_BASE || 'https://api.deepseek.com/v1';
        this.model = process.env.DEEPSEEK_MODEL || 'deepseek-coder';
        this.maxTokens = parseInt(process.env.MAX_TOKENS) || 2048;
        this.temperature = parseFloat(process.env.TEMPERATURE) || 0.7;
        
        if (!this.apiKey) {
            throw new Error('DEEPSEEK_API_KEY environment variable is not set');
        }
        
        this.client = axios.create({
            baseURL: this.apiBase,
            headers: {
                'Authorization': `Bearer ${this.apiKey}`,
                'Content-Type': 'application/json'
            }
        });
    }
    
    async chatCompletion(messages, temperature = null, maxTokens = null) {
        """Call DeepSeek Chat Completion API"""
        
        temperature = temperature || this.temperature;
        maxTokens = maxTokens || this.maxTokens;
        
        try {
            const response = await this.client.post('/chat/completions', {
                model: this.model,
                messages: messages,
                temperature: temperature,
                max_tokens: maxTokens
            });
            return response.data;
        } catch (error) {
            throw new Error(`DeepSeek API Error: ${error.message}`);
        }
    }
    
    async codeCompletion(prompt, context = null) {
        """Generate code completion based on prompt"""
        
        const systemMessage = {
            role: 'system',
            content: 'You are an expert code assistant. Write clean, efficient, and well-documented code.'
        };
        
        let userContent = prompt;
        if (context) {
            userContent = `Context:\n${context}\n\nRequest:\n${prompt}`;
        }
        
        const messages = [
            systemMessage,
            { role: 'user', content: userContent }
        ];
        
        const response = await this.chatCompletion(messages);
        return response.choices[0].message.content;
    }
    
    async codeGeneration(description) {
        """Generate complete code based on description"""
        
        const prompt = `Generate complete, production-ready code for: ${description}`;
        return this.codeCompletion(prompt);
    }
    
    async codeExplanation(code) {
        """Explain given code"""
        
        const prompt = `Explain the following code in detail:\n\n\`\`\`\n${code}\n\`\`\``;
        return this.codeCompletion(prompt);
    }
    
    async codeReview(code) {
        """Review and provide feedback on code"""
        
        const prompt = `Please review the following code and provide:
1. Code quality assessment
2. Performance suggestions
3. Security concerns (if any)
4. Best practices recommendations
5. Refactoring suggestions

Code:\n\`\`\`\n${code}\n\`\`\``;
        return this.codeCompletion(prompt);
    }
    
    async codeOptimization(code) {
        """Optimize the given code"""
        
        const prompt = `Optimize the following code for performance and readability:\n\n\`\`\`\n${code}\n\`\`\`\n\nProvide the optimized version with explanations.`;
        return this.codeCompletion(prompt);
    }
    
    async bugDetection(code) {
        """Detect potential bugs in code"""
        
        const prompt = `Analyze the following code for potential bugs, errors, and issues:\n\n\`\`\`\n${code}\n\`\`\`\n\nProvide detailed analysis and suggested fixes.`;
        return this.codeCompletion(prompt);
    }
}

module.exports = DeepSeekClient;
