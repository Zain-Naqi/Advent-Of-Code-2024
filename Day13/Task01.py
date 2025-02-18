import pulp

with open('input.txt', 'r') as file:
    input_data = file.read()

machine_data = input_data.split("\n\n")

machines = []

for machine_str in machine_data:
    lines = machine_str.splitlines()
    
    button_a_line = lines[0]
    _, button_a_values = button_a_line.split(": ")
    button_a_x, button_a_y = map(int, [val[2:] for val in button_a_values.split(", ")])
    
    button_b_line = lines[1]
    _, button_b_values = button_b_line.split(": ")
    button_b_x, button_b_y = map(int, [val[2:] for val in button_b_values.split(", ")])
    
    prize_line = lines[2]
    _, prize_values = prize_line.split(": ")
    prize_x, prize_y = map(int, [val[2:] for val in prize_values.split(", ")])
    
    machines.append([ [button_a_x, button_a_y], [button_b_x, button_b_y], [prize_x, prize_y] ])
    
res = 0
for m in machines:
    dx1, dy1 = m[0][0], m[0][1]
    dx2, dy2 = m[1][0], m[1][1]
    x1_target, y1_target = m[2][0], m[2][1]

    cost_A = 3
    cost_B = 1

    prob = pulp.LpProblem("Minimize Cost", pulp.LpMinimize)

    x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
    x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')

    prob += cost_A * x1 + cost_B * x2
    prob += dx1 * x1 + dx2 * x2 == x1_target
    prob += dy1 * x1 + dy2 * x2 == y1_target

    prob.solve()

    if pulp.LpStatus[prob.status] == "Optimal":
        cost = pulp.value(prob.objective)
    else:
        cost = 0

    res += int(cost)

print(res)
