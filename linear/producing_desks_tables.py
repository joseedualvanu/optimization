from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value

# Create the problem instance
problem = LpProblem("ProfitMaximization", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

# Define the objective function
objective = 700 * x1 + 900 * x2
problem += objective

# Define the constraints
problem += 3 * x1 + 5 * x2 <= 3600
problem += x1 + 2 * x2 <= 1600
problem += 50 * x1 + 20 * x2 <= 48000

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print(f"x1 = {value(x1)}")
print(f"x2 = {value(x2)}")
print(f"Maximum Profit = {value(objective)}")
