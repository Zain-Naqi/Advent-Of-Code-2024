
def adv(Registers, comboOperand):
    Registers['A'] = Registers['A'] // (2**comboOperand)
    return ""

def bxl(Registers, literalOperand):
    Registers['B'] = Registers['B'] ^ literalOperand
    return ""

def bst(Registers, ComboOperand):
    Registers['B'] = ComboOperand % 8
    return ""

def jnz(Registers, literalOperand):
    global instructionPointer
    if Registers['A'] != 0:
        instructionPointer = literalOperand
        return ""
    return ""

def bxc(Registers):
    Registers['B'] = Registers['B'] ^ Registers['C']
    return ""

def out(comboOperand):
    return str(comboOperand % 8)

def bdv(Registers, comboOperand):
    Registers['B'] = Registers['A'] // (2**comboOperand)
    return ""

def cdv(Registers, comboOperand):
    Registers['C'] = Registers['A'] // (2**comboOperand)
    return ""

def findComboOperand(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return Registers['A']
    elif operand == 5:
        return Registers['B']
    elif operand == 6:
        return Registers['C']
    else:
        raise ValueError("Invalid combo operand")

def runProgram(Program, Instructions): 
    global instructionPointer
    instructionPointer = 0
    output = ""   
    while instructionPointer < len(Program):
        opcode = Program[instructionPointer]
        operand = Program[instructionPointer + 1]
        
        if res := Instructions[opcode](operand):
            output += res + ","
        if opcode != 3 or Registers['A'] == 0:
            instructionPointer += 2
            
    return output

Registers = {'A': 0, 'B': 0, 'C': 0}
from multiprocessing import Pool, Manager

# Function to run the program for a specific range of counts
def findCountInRange(start, end, target, shared_result):
    for count in range(start, end):
        Registers = {'A': count, 'B': 0, 'C': 0}  # Reset registers for each count
        if runProgram(Program, Instructions)[:-1] == target:
            shared_result.value = count  # Store the result
            return count
    return None

# Main function to parallelize the search
def parallelSearch(target, max_count, num_workers=4):
    step = max_count // num_workers
    ranges = [(i * step + 1, (i + 1) * step + 1) for i in range(num_workers)]

    with Manager() as manager:
        shared_result = manager.Value('i', -1)  # Shared result between processes
        with Pool(num_workers) as pool:
            # Run workers in parallel
            results = [
                pool.apply_async(findCountInRange, (start, end, target, shared_result))
                for start, end in ranges
            ]

            # Wait for all workers to complete
            for r in results:
                r.wait()
                if shared_result.value != -1:  # Early termination if result found
                    pool.terminate()
                    pool.join()
                    return shared_result.value

    return -1  # If no result found

# Define your program and instructions
Program = [0, 3, 5, 4, 3, 0]  # Example program
Instructions = {
    0: lambda operand: adv(Registers, findComboOperand(operand)),
    1: lambda operand: bxl(Registers, operand),
    2: lambda operand: bst(Registers, findComboOperand(operand)),
    3: lambda operand: jnz(Registers, operand),
    4: lambda operand: bxc(Registers),
    5: lambda operand: out(findComboOperand(operand)),
    6: lambda operand: bdv(Registers, findComboOperand(operand)),
    7: lambda operand: cdv(Registers, findComboOperand(operand)),
}

# Target program output
P = ','.join(str(item) for item in Program)

# Search for the count
max_count = 10**6  # Define the maximum range
result = parallelSearch(P, max_count)

if result != -1:
    print(f"Found count: {result}")
else:
    print("No valid count found within the range.")

