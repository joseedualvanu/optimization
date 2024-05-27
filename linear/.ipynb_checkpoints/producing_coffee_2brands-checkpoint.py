# To summarize, this optimization model aims to determine the optimal amounts of coffee1 and coffee2 to produce in order to maximize profit, 
# while satisfying the given constraints on coffee consumption, labor, and machine availability. 
# The code sets up the problem, defines the objective function and constraints, solves the problem, and displays the optimal solution.

from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value

# Create the problem instance
problem = LpProblem("ProfitMaximization", LpMaximize)

# Define the decision variables
# coffee1 kg
x1 = LpVariable("x1", lowBound=0) 
# coffee2 kg
x2 = LpVariable("x2", lowBound=0)

# Define the objective function
# profit per coffee1 kg and coffee2 kg
objective = 700 * x1 + 900 * x2
problem += objective

# Define the constraints
# coffee consumption
problem += 3 * x1 + 5 * x2 <= 3600
# labor
problem += x1 + 2 * x2 <= 1600
# machine
problem += 50 * x1 + 20 * x2 <= 48000

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print(f"coffee 1 kg (x1) = {value(x1)}")
print(f"coffee 2 kg (x2) = {value(x2)}")
print(f"Maximum Profit ($)= {value(objective)}")
