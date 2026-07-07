/**
 * Node.js example for using Codex-DeepSeek Integration
 */

require('dotenv').config();
const axios = require('axios');

const BASE_URL = process.env.BASE_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

async function runExamples() {
    console.log('='.repeat(50));
    console.log('Codex-DeepSeek Integration Examples');
    console.log('='.repeat(50));
    
    try {
        // Example 1: Code Completion
        console.log('\n1. Code Completion');
        console.log('-'.repeat(50));
        const completionResponse = await api.post('/api/code-completion', {
            prompt: 'Write a function to calculate factorial',
            context: 'Python function'
        });
        console.log('Result:', completionResponse.data.result);
        
        // Example 2: Code Generation
        console.log('\n2. Code Generation');
        console.log('-'.repeat(50));
        const generationResponse = await api.post('/api/code-generation', {
            description: 'A JavaScript class for managing a simple todo list'
        });
        console.log('Result:', generationResponse.data.result);
        
        // Example 3: Code Explanation
        console.log('\n3. Code Explanation');
        console.log('-'.repeat(50));
        const code = `
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
        `;
        const explanationResponse = await api.post('/api/code-explanation', {
            code: code
        });
        console.log('Result:', explanationResponse.data.result);
        
        // Example 4: Code Review
        console.log('\n4. Code Review');
        console.log('-'.repeat(50));
        const codeToReview = `
function sumList(list) {
    let total = 0;
    for (let i = 0; i < list.length; i++) {
        total = total + list[i];
    }
    return total;
}
        `;
        const reviewResponse = await api.post('/api/code-review', {
            code: codeToReview
        });
        console.log('Result:', reviewResponse.data.result);
        
        // Example 5: Code Optimization
        console.log('\n5. Code Optimization');
        console.log('-'.repeat(50));
        const codeToOptimize = `
function findMax(arr) {
    let maxVal = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}
        `;
        const optimizationResponse = await api.post('/api/code-optimization', {
            code: codeToOptimize
        });
        console.log('Result:', optimizationResponse.data.result);
        
        // Example 6: Bug Detection
        console.log('\n6. Bug Detection');
        console.log('-'.repeat(50));
        const buggyCode = `
function divideNumbers(a, b) {
    return a / b;
}

function processList(items) {
    for (let i = 0; i <= items.length; i++) {
        console.log(items[i]);
    }
}
        `;
        const bugDetectionResponse = await api.post('/api/bug-detection', {
            code: buggyCode
        });
        console.log('Result:', bugDetectionResponse.data.result);
        
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
}

// Run examples
if (process.env.DEEPSEEK_API_KEY) {
    runExamples();
} else {
    console.error('Error: DEEPSEEK_API_KEY environment variable is not set');
    process.exit(1);
}
