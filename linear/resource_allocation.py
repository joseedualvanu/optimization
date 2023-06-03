#In this example, we have three resources (resource 1, resource 2, and resource 3) that can be allocated. 
#The objective is to maximize the total value obtained from allocating these resources. 
#The decision variables x1, x2, and x3 represent the amounts of resource 1, resource 2, and resource 3 allocated, respectively.

#The constraints specify the limits on the available resources. 
#In this case, we have three constraints that restrict the total allocation of each resource.

from pulp import *

# Create the LP problem
prob = LpProblem("Resource Allocation", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=0)  # Amount of resource 1 allocated
x2 = LpVariable("x2", lowBound=0)  # Amount of resource 2 allocated
x3 = LpVariable("x3", lowBound=0)  # Amount of resource 3 allocated

# Define the objective function
prob += 5*x1 + 8*x2 + 3*x3  # Maximize the total value

# Define the constraints
prob += 2*x1 + 3*x2 + 1*x3 <= 100  # Resource 1 constraint
prob += 1*x1 + 2*x2 + 2*x3 <= 90   # Resource 2 constraint
prob += 4*x1 + 1*x2 + 2*x3 <= 80   # Resource 3 constraint

# Solve the LP problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Print the optimal solution
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the optimal objective value
print("Total value =", value(prob.objective))
