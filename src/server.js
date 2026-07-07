const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config();
const DeepSeekClient = require('./deepseekClient');

const app = express();
const PORT = process.env.PORT || 8000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Initialize DeepSeek client
const client = new DeepSeekClient();

// Health check
app.get('/health', (req, res) => {
    res.json({ status: 'healthy', service: 'codex-deepseek-integration' });
});

// Code Completion
app.post('/api/code-completion', async (req, res) => {
    try {
        const { prompt, context } = req.body;
        if (!prompt) {
            return res.status(400).json({ error: 'prompt is required' });
        }
        const result = await client.codeCompletion(prompt, context);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Code Generation
app.post('/api/code-generation', async (req, res) => {
    try {
        const { description } = req.body;
        if (!description) {
            return res.status(400).json({ error: 'description is required' });
        }
        const result = await client.codeGeneration(description);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Code Explanation
app.post('/api/code-explanation', async (req, res) => {
    try {
        const { code } = req.body;
        if (!code) {
            return res.status(400).json({ error: 'code is required' });
        }
        const result = await client.codeExplanation(code);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Code Review
app.post('/api/code-review', async (req, res) => {
    try {
        const { code } = req.body;
        if (!code) {
            return res.status(400).json({ error: 'code is required' });
        }
        const result = await client.codeReview(code);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Code Optimization
app.post('/api/code-optimization', async (req, res) => {
    try {
        const { code } = req.body;
        if (!code) {
            return res.status(400).json({ error: 'code is required' });
        }
        const result = await client.codeOptimization(code);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Bug Detection
app.post('/api/bug-detection', async (req, res) => {
    try {
        const { code } = req.body;
        if (!code) {
            return res.status(400).json({ error: 'code is required' });
        }
        const result = await client.bugDetection(code);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// 404 Handler
app.use((req, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 Codex-DeepSeek server running on http://localhost:${PORT}`);
    console.log(`📚 Available endpoints:`);
    console.log(`   - POST /api/code-completion`);
    console.log(`   - POST /api/code-generation`);
    console.log(`   - POST /api/code-explanation`);
    console.log(`   - POST /api/code-review`);
    console.log(`   - POST /api/code-optimization`);
    console.log(`   - POST /api/bug-detection`);
});

module.exports = app;
