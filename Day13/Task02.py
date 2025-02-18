from ortools.linear_solver import pywraplp

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
    
    solver = pywraplp.Solver.CreateSolver('SCIP')

    x1 = solver.IntVar(0.0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0.0, solver.infinity(), 'x2')

    solver.Add(m[0][0] * x1 + m[1][0] * x2 == 10000000000000 + m[2][0])
    solver.Add(m[0][1] * x1 + m[1][1] * x2 == 10000000000000 + m[2][1])

    solver.Minimize(3 * x1 + x2)

    status = solver.Solve()

    cost = 0
    if status == pywraplp.Solver.OPTIMAL:
        res += int(solver.Objective().Value())

print(res)
