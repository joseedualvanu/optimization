import cvxpy as cp

# Define the decision variables
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()

# Define the objective function
objective = cp.Minimize(100 * x1**2 + 1600 * x2**2 + 100 * x3**2)

R = 200

# Define the constraints
constraints = [50 * x1 + 40 * x2 + 25 * x3 <= 100000, 55 * x1 + 50 * x2 + 20 * x3 >= R]

# Create the problem instance
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Print the optimal solution
if problem.status == cp.OPTIMAL:
    print("Optimal Solution:")
    print(f"x1 = {x1.value}")
    print(f"x2 = {x2.value}")
    print(f"x3 = {x3.value}")
    print(f"Minimum Value = {problem.value}")
else:
    print("Problem is infeasible or unbounded.")
