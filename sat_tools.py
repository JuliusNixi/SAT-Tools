from random import choice, seed

# Returns a random literal from the alphabet string. The literal may be negated with a 50% chance.
# The negated literals are prefixed with a hyphen.
def generateLiteral(alphabet):
    if alphabet == "":
        raise ValueError("Alphabet cannot be empty.")
    literal = choice(alphabet)
    if choice([True, False]):
        return literal
    return "-" + literal

# Returns a list of literals from the alphabet.
# The number of literals is randomly chosen from 1 to n if exactNOrMaxN is False.
# The number of literals is exactly n if exactNOrMaxN is True.
def generateClause(alphabet, n = 3, exactNOrMaxN = True):
    if n < 1:
        raise ValueError("Number of literals per clause must be greater than 0.")
    clause = []
    if not exactNOrMaxN:
        n = choice(range(1, n + 1))
    for _ in range(n):
        while True:
            literal = generateLiteral(alphabet)
            if literal in clause or "-" + literal in clause:
                continue
            clause.append(literal)
            break
    return clause

# Returns a list of k clauses.
def generateCNF(alphabet, k, n = 3, exactNOrMaxN = True):
    if k < 1:
        raise ValueError("Number of clauses must be greater than 0.")
    cnf = []
    for _ in range(k):
        clause = generateClause(alphabet, n, exactNOrMaxN)
        clause.sort()
        cnf.append(clause)
    return cnf

# Converts a CNF list to a string to be printed.
def stringifyCNF(cnf):
    return "\n".join([" ".join(clause) for clause in cnf])

# Returns a set of all possible binary strings of length n.
def generateBitsConfigurations(n):
    total_configurations = 2 ** n

    configurations = set()
    
    for i in range(total_configurations):
        binary_string = format(i, f'0{n}b')
        configurations.add(binary_string)
    
    return configurations

# Returns a set of all the variables in the CNF, only the variable names without the negation.
def getCNFVariables(cnf):
    variables = set()
    for clause in cnf:
        for literal in clause:
            if literal[0] == "-":
                variables.add(literal[1:])
            else:
                variables.add(literal)
    return variables

# Evaluates the CNF with the given bits configuration.
# Returns a dictionary with the variables as keys and the bit as value if the CNF is satisfiable.
# Returns None if the CNF is unsatisfiable with the given bits configuration.
def evaluateCNF(cnf, bitsConfiguration, cnfVariables):

    # Returns a dictionary with the variables as keys and the bit as value.
    def mapBitsToVariables(bits, variables):
        variables = list(variables)
        return {variables[i]: int(bits[i]) for i in range(len(bits))}
    
    # Returns a new CNF list of clauses with the assignments applied.
    # Each clause is a list of 0 or 1. So each literal is now a boolean.
    def translateAssignmentsInCNF(assignments, cnf):
        translatedCNF = []
        for clause in cnf:
            translatedClause = []
            for literal in clause:
                if literal[0] == "-":
                    translatedClause.append(not assignments[literal[1:]])
                else:
                    translatedClause.append(assignments[literal])
            translatedCNF.append(translatedClause)
        return translatedCNF
    
    # Evaluates the entire translated CNF.
    # Returns True if the CNF is satisfiable.
    # Returns False if the CNF is unsatisfiable.
    def evaluateTranslatedCNF(translatedCNF):
        for clause in translatedCNF:
            sat = False
            for literal in clause:
                if literal:
                    sat = True
                    break
            if not sat:
                return False
        return True
    
    assignments = mapBitsToVariables(bitsConfiguration, cnfVariables)
    translatedCNF = translateAssignmentsInCNF(assignments, cnf)
    if evaluateTranslatedCNF(translatedCNF):
        return assignments
    return None

# Resolves the CNF SAT problem.
# THIS IS A BRUTE FORCE IMPLEMENTATION. IT IS NOT EFFICIENT FOR LARGE CNF.
# HAS BEEN MADE ONLY FOR DEMONSTRATION PURPOSES.
def resolveCNF(cnf):
    cnfVars = getCNFVariables(cnf)
    bitsConfigurations = generateBitsConfigurations(len(cnfVars))
    for bits in bitsConfigurations:
        result = evaluateCNF(cnf, bits, cnfVars)
        if result != None:
            return result
    return None

# Converts a CNF string to a CNF list.
def cnfFromCNFString(cnfString):
    cnf = []
    for line in cnfString.split("\n"):
        clause = line.split()
        cnf.append(clause)
    return cnf

if __name__ == "__main__":

    seed(42)

    print("""
SAT Generator

This script generates a SAT problem in CNF format. 
The CNF is generated with a given alphabet, number of clauses, and number of literals per clause. 
The literals are randomly chosen from the alphabet and negated with a 50% chance.
The negated literals are prefixed with a hyphen.
The CNF is converted to a string with each clause on a separate line and each literal separated by a space.

The CNF could be resolved with a brute force algorithm that tries all possible bit configurations. 
The algorithm returns the assignments that satisfy the CNF.
THIS IS A BRUTE FORCE IMPLEMENTATION. IT IS NOT EFFICIENT FOR LARGE CNF.
HAS BEEN MADE ONLY FOR DEMONSTRATION PURPOSES.         

Examples:
          """)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print("Alphabet:", alphabet)
    print("Number of clauses: 3.")
    print("Number of literals per clause: MAX 4.")
    print("CNF:")
    cnf = generateCNF(alphabet, 3, 4, False)
    print(stringifyCNF(cnf), "\n")

    print("------------", "\n")

    alphabet = "1234567890"
    print("Alphabet:", alphabet)
    print("Number of clauses: 2.")
    print("Number of literals per clause: EXACT 3.")
    print("CNF:")
    cnf = generateCNF(alphabet, 2)
    print(stringifyCNF(cnf), "\n")  

    print("------------", "\n")

    print("Testing solving a SAT CNF problem.")
    cnf = generateCNF(alphabet, 2)
    print("SAT:")
    print(stringifyCNF(cnf), "\n") 
    print("Solution:")
    result = resolveCNF(cnf)
    print(result, "\n")

    print("------------", "\n")

    print("Testing solving a UNSAT CNF problem.")
    unsatTest = """1 2 3
1 2 -3
1 -2 3
1 -2 -3
-1 2 -3
-1 2 3
-1 -2 -3
-1 -2 3"""
    print("UNSAT:")
    print(unsatTest, "\n")
    print("Solution:")
    cnf = cnfFromCNFString(unsatTest)
    result = resolveCNF(cnf)
    print(result)




