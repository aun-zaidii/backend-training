# 🧟‍♂️ Zombie Apocalypse Survival Calculator API

## 🎯 **Main Learning Focus: Expression Parsing & Mathematical Libraries**
Learn how to integrate and use mathematical expression parsers, handle complex string-based input, and work with mathematical computation libraries in backend APIs.

## 🌍 The Scenario
The year is 2024, and a zombie apocalypse has ravaged the world. As the lead engineer for the last remaining survivor bunker, you must create a **smart Calculator API** that helps survivors make critical calculations for resource management, survival planning, and complex mathematical operations needed in the apocalypse.

## 📋 Mission Details
Build a powerful REST API that can evaluate mathematical expressions and maintains a complete history of all calculations. This advanced calculator will help survivors with everything from basic arithmetic to complex scientific calculations using a single, flexible endpoint.

### Core Features Required:
- **Expression Evaluation**: Parse and calculate mathematical expressions
- **Basic Operations**: `+`, `-`, `*`, `/`, `%`, `^` (power)
- **Scientific Functions**: `sin()`, `cos()`, `tan()`, `sqrt()`, `log()`, `ln()`, `abs()`, `factorial()`
- **Memory Variables**: Store and use variables in expressions (e.g., `x = 5`, `x * 2`) - BONUS (Ask Lead if this should be done)
- **Calculation History**: Store all expressions and results with timestamps
- **Error Handling**: Handle invalid expressions, division by zero, domain errors

### API Endpoints Needed:
```
Calculation:
POST /calculate
Body: { "expression": "2 + 3 * sin(45)" }
Response: { 
  "expression": "2 + 3 * sin(45)", 
  "result": 4.121, 
  "id": 1, 
  "timestamp": "2024-01-01T10:00:00Z" 
}

POST /calculate
Body: { "expression": "x = 10" }
Response: { 
  "expression": "x = 10", 
  "result": 10, 
  "id": 2, 
  "message": "Variable x set to 10" 
}

POST /calculate
Body: { "expression": "x * 2 + sqrt(16)" }
Response: { 
  "expression": "x * 2 + sqrt(16)", 
  "result": 24, 
  "id": 3, 
  "variables": { "x": 10 } 
}

History Management:
GET /history
Response: [
  { 
    "id": 1, 
    "expression": "2 + 3 * sin(45)", 
    "result": 4.121, 
    "timestamp": "2024-01-01T10:00:00Z" 
  }
]

GET /history/{id}
Response: { 
  "id": 1, 
  "expression": "2 + 3 * sin(45)", 
  "result": 4.121, 
  "timestamp": "2024-01-01T10:00:00Z" 
}

DELETE /history
Response: { "message": "History cleared" }

DELETE /history/{id}
Response: { "message": "Calculation deleted" }

Variables:
GET /variables
Response: { "x": 10, "survival_days": 45, "team_size": 8 }

POST /variables/clear
Response: { "message": "All variables cleared" }
```

### Supported Expression Examples:
```
Basic: "5 + 3", "10 * 2.5", "100 / 4", "15 % 4", "2 ^ 8"
Scientific: "sin(90)", "cos(0)", "sqrt(25)", "log(100)", "ln(2.718)"
Complex: "2 + 3 * sin(45) - sqrt(16)", "factorial(5) + abs(-10)"
Variables: "x = 50", "y = x * 2", "survival_ratio = team_size / zombie_count"
Functions: "max(5, 10, 3)", "min(1, 2, 3)", "round(3.14159, 2)"
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Expression Parser**: Use a math expression library (Math.js, SymPy, etc.)
- **Database**: SQLite for calculation history and variables
- **Framework**: Express, Flask, Spring Boot, etc.
- **Error Handling**: Graceful handling of invalid expressions and math errors
- **Validation**: Ensure expressions are safe (no code injection)

### Database Schema:
```
Calculations:
- id, expression, result, timestamp, variables_used (JSON)

Variables:
- name, value, last_updated

Supported Functions:
Basic: +, -, *, /, %, ^ (power)
Scientific: sin, cos, tan, asin, acos, atan, sqrt, log, ln, abs
Utility: factorial, max, min, round, ceil, floor
```

### Expression Parser Features:
- **Operator Precedence**: Correct mathematical order of operations
- **Function Support**: Built-in mathematical functions
- **Variable Assignment**: Store and reuse named values
- **Error Recovery**: Clear error messages for invalid expressions
- **Security**: Prevent code injection and unsafe operations

## ⏱️ **Exact Development Time: 2.5 days**
- **Setup & Expression Parser Integration**: 1 day
- **API Endpoints & Variable Management**: 1 day  
- **History & Error Handling**: 0.5 day

## 🎯 Survival Success Criteria
- Single endpoint can evaluate complex mathematical expressions
- Supports all basic arithmetic and scientific functions
- Variables can be stored and used in subsequent calculations
- Complete calculation history is maintained
- Proper error handling for invalid expressions and math errors
- Variables persist across calculations
- Clear error messages for syntax errors
- Performance is good for complex expressions

## 📚 Learning Objectives
- Expression parsing and evaluation
- Mathematical library integration
- Variable state management across requests
- Advanced error handling for dynamic input
- Security considerations for user input
- API design with flexible input handling
- Working with mathematical computation libraries

*Build the smartest calculator the apocalypse survivors have ever seen!* 🧟‍♀️⚡
