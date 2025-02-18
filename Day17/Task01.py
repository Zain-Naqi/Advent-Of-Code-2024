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

Registers = {'A': 37293246, 'B': 0, 'C': 0}
Program = [2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Instructions = {0: lambda operand: adv(Registers, findComboOperand(operand)), 
                1: lambda operand: bxl(Registers, operand), 
                2: lambda operand: bst(Registers, findComboOperand(operand)), 
                3: lambda operand: jnz(Registers, operand), 
                4: lambda operand: bxc(Registers), 
                5: lambda operand: out(findComboOperand(operand)), 
                6: lambda operand: bdv(Registers, findComboOperand(operand)), 
                7: lambda operand: cdv(Registers, findComboOperand(operand))}


print(runProgram(Program, Instructions))
