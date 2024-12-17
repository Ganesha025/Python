from flask import Flask, request, jsonify, render_template_string
import math

app = Flask(__name__)

# HTML Template for Calculator
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #calculator {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #result {
            width: 100%;
            height: 40px;
            text-align: right;
            margin-bottom: 10px;
            font-size: 24px;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        }
        button {
            width: 60px;
            height: 60px;
            font-size: 20px;
            margin: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Virtual Calculator</h1>
    <div id="calculator">
        <input type="text" id="result" disabled>
        <div>
            <button onclick="clearResult()">C</button>
            <button onclick="appendToResult('/')">/</button>
            <button onclick="appendToResult('*')">*</button>
            <button onclick="appendToResult('-')">-</button>
        </div>
        <div>
            <button onclick="appendToResult('7')">7</button>
            <button onclick="appendToResult('8')">8</button>
            <button onclick="appendToResult('9')">9</button>
            <button onclick="appendToResult('+')">+</button>
        </div>
        <div>
            <button onclick="appendToResult('4')">4</button>
            <button onclick="appendToResult('5')">5</button>
            <button onclick="appendToResult('6')">6</button>
            <button onclick="calculateResult()">=</button>
        </div>
        <div>
            <button onclick="appendToResult('1')">1</button>
            <button onclick="appendToResult('2')">2</button>
            <button onclick="appendToResult('3')">3</button>
        </div>
        <div>
            <button onclick="appendToResult('0')">0</button>
        </div>
    </div>

    <script>
        function appendToResult(value) {
            document.getElementById('result').value += value;
        }

        function clearResult() {
            document.getElementById('result').value = '';
        }

        async function calculateResult() {
            const resultField = document.getElementById('result');
            const expression = resultField.value;
            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ expression })
                });
                const data = await response.json();
                resultField.value = data.result;
            } catch (error) {
                resultField.value = 'Error';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        expression = data.get('expression', '')
        
        # Securely evaluate the expression
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": "Error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
