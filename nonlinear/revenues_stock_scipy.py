from scipy.optimize import minimize

# Define the objective function
def objective(x):
    x1, x2, x3 = x
    return 100 * x1**2 + 1600 * x2**2 + 100 * x3**2

# Define the inequality constraint function
def constraint(x):
    x1, x2, x3 = x
    return [50 * x1 + 40 * x2 + 25 * x3 - 100000]

# Define the inequality constraint bounds
bounds = [(0, None), (0, None), (0, None)]

# Define the R value for the inequality constraint
R = 0  # Replace with the desired value

# Define the inequality constraint bounds with R
inequality_constraint = {'type': 'ineq', 'fun': constraint}
inequality_constraint_bounds = [(None, None)]

# Solve the optimization problem
initial_guess = [0, 0, 0]
solution = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=inequality_constraint_bounds)

# Print the optimal solution
print("Optimal Solution:")
print(f"x1 = {solution.x[0]}")
print(f"x2 = {solution.x[1]}")
print(f"x3 = {solution.x[2]}")
print(f"Minimum Value = {solution.fun}")
