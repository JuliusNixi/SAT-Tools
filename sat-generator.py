from random import choice, seed

def generateLiteral(alphabet):
    if alphabet == "":
        raise ValueError("Alphabet cannot be empty.")
    literal = choice(alphabet)
    if choice([True, False]):
        return literal
    return "-" + literal

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

def generateCNF(alphabet, k, n = 3, exactNOrMaxN = True):
    if k < 1:
        raise ValueError("Number of clauses must be greater than 0.")
    cnf = []
    for _ in range(k):
        clause = generateClause(alphabet, n, exactNOrMaxN)
        clause.sort()
        cnf.append(clause)
    return cnf

def stringifyCNF(cnf):
    return "\n".join([" ".join(clause) for clause in cnf])

if __name__ == "__main__":

    seed(42)

    print("""
SAT Generator

This script generates a SAT problem in CNF format. 
The CNF is generated with a given alphabet, number of clauses, and number of literals per clause. 
The literals are randomly chosen from the alphabet and negated with a 50% chance.
The negated literals are prefixed with a hyphen.
The CNF is converted to a string with each clause on a separate line and each literal separated by a space.
          
Examples:
          """)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cnf = generateCNF(alphabet, 3, 4, False)
    print(stringifyCNF(cnf), "\n")

    print("------------", "\n")

    alphabet = "1234567890"
    cnf = generateCNF(alphabet, 2)
    print(stringifyCNF(cnf), "\n")  

