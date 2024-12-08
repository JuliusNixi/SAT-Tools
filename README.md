# SAT-Tools
Generate and solve SAT (boolean satisfiability problem) formulas.

This script generates a SAT problem in CNF format. 
The CNF is generated with a given alphabet, number of clauses, and number of literals per clause. 
The literals are randomly chosen from the alphabet and negated with a 50% chance.
The negated literals are prefixed with a hyphen.
The CNF is converted to a string with each clause on a separate line and each literal separated by a space.

The CNF could be resolved with a brute force algorithm that tries all possible bit configurations. 
The algorithm returns the assignments that satisfy the CNF.
THIS IS A BRUTE FORCE IMPLEMENTATION. IT IS NOT EFFICIENT FOR LARGE CNF.
HAS BEEN MADE ONLY FOR DEMONSTRATION PURPOSES.    