import ast
from sklearn.tree import DecisionTreeClassifier

# Sample training data
# Format: [number of lines, number of variables, number of loops]
X_train = [
    [10, 5, 2],   # Example 1: 10 lines, 5 variables, 2 loops
    [20, 10, 4],  # Example 2: 20 lines, 10 variables, 4 loops
    [5, 3, 1],    # Example 3: 5 lines, 3 variables, 1 loop
]
# Optimization suggestions (1 = good, 0 = needs optimization)
y_train = [1, 0, 1]

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Function to analyze code
def analyze_code(code):
    # Parse the code using AST (Abstract Syntax Tree)
    tree = ast.parse(code)
    num_lines = len(code.split('\n'))
    num_vars = sum(isinstance(node, ast.Assign) for node in ast.walk(tree))
    num_loops = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))

    # Predict if optimization is needed
    prediction = model.predict([[num_lines, num_vars, num_loops]])
    return "Needs optimization" if prediction == 0 else "Code is efficient"

# Example code for analysis
code_example = """
for i in range(10):
    x = i * 2
"""

# Analyze the example code
result = analyze_code(code_example)
print(result)
