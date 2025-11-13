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

Examples: <br>
<br>
Alphabet: abcdefghijklmnopqrstuvwxyz <br>
Number of clauses: 3. <br>
Number of literals per clause: MAX 4. <br>
CNF: <br>
-a <br>
h x <br>
-s <br>

------------ <br>

Alphabet: 1234567890 <br>
Number of clauses: 2. <br>
Number of literals per clause: EXACT 3. <br>
CNF: <br>
1 2 4 <br>
-4 9 -9 <br>

------------ <br>

Testing solving a SAT CNF problem. <br>
Alphabet: 1234567890 <br>
SAT: <br>
-0 1 -7 <br>
2 -4 5 <br>
<br>
Solution: <br>
{'0': 0, '1': 1, '7': 1, '2': 1, '5': 1, '4': 1} <br>

------------ <br>

Testing solving an UNSAT CNF problem. <br>
Alphabet: 123 <br>
UNSAT: <br>
1 2 3
1 2 -3
1 -2 3
1 -2 -3
-1 2 -3
-1 2 3
-1 -2 -3
-1 -2 3 
<br>
Solution: <br>
None <br>
