# In this example, we have a production planning problem where 
# we want to determine the quantities of two products (product 1 and product 2) to produce. 
# The objective is to minimize the total production cost.

# The decision variables x1 and x2 represent the quantities of product 1 and product 2 to produce, respectively. 
# Note that I've set the cat parameter to 'Integer' to indicate that the decision variables should be integer values.

# The constraints specify the availability of resources required for production.
# In this case, we have three constraints that ensure that the resources are sufficient to meet the production requirements.

from pulp import *

# Create the LP problem
prob = LpProblem("Production Planning", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=0, cat='Integer')  # Quantity of product 1 to produce
x2 = LpVariable("x2", lowBound=0, cat='Integer')  # Quantity of product 2 to produce

# Define the objective function
prob += 5 * x1 + 8 * x2  # Minimize the total production cost

# Define the constraints
prob += 2 * x1 + 3 * x2 >= 100  # Resource 1 constraint
prob += 1 * x1 + 2 * x2 >= 90   # Resource 2 constraint
prob += 4 * x1 + 1 * x2 >= 80   # Resource 3 constraint

# Solve the LP problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Print the optimal solution
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the optimal objective value
print("Total cost =", value(prob.objective))