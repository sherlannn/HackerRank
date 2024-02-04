# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

inp = input()
p = cmath.polar(complex(inp))

print(p[0])
print(p[1])