from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value

# Create the problem instance
problem = LpProblem("QuadraticMinimization", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)

# Define the objective function
objective = 100 * x1*x1 + 1600 * x2*x2 + 100 * x3*x3
problem += objective

# Define the constraints
problem += 50 * x1 + 40 * x2 + 25 * x3 <= 100000
problem += 55 * x1 + 50 * x2 + 20 * x3 >= R  # Replace R with the desired value

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print(f"x1 = {value(x1)}")
print(f"x2 = {value(x2)}")
print(f"x3 = {value(x3)}")
print(f"Minimum Value = {value(objective)}")
