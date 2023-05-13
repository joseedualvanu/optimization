from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value

# Create the problem instance
problem = LpProblem("MinimizationProblem", LpMinimize)

# Define the decision variables
x = [LpVariable(f"x{i}", lowBound=0) for i in range(1, 8)]

# Define the objective function
objective = lpSum(x)
problem += objective

# Define the constraints
problem += lpSum([x[0], x[3], x[4], x[5], x[6]]) >= 110
problem += lpSum([x[0], x[1], x[4], x[5], x[6]]) >= 80
problem += lpSum([x[0], x[1], x[2], x[5], x[6]]) >= 150
problem += lpSum([x[0], x[1], x[2], x[3], x[6]]) >= 30
problem += lpSum([x[0], x[1], x[2], x[3], x[4]]) >= 70
problem += lpSum([x[1], x[2], x[3], x[4], x[5]]) >= 160
problem += lpSum([x[2], x[3], x[4], x[5], x[6]]) >= 120

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
for var in x:
    print(f"{var.name} = {value(var)}")
print(f"Minimum Value = {value(objective)}")
