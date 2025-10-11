a = 10 > 2 or 30 > 40
print(f"10 > 2 or 30 > 40 = {a} -->Short Circuit Evaluation")
b = 100 > 20 or 30 > 40 or 50 > 40
print(f"100 > 20 or 30 > 40 or 50 > 40 = {b} -->Short Circuit Evaluation")
c = 100 > 300 or 40 > 30 or 50 > 60
print(f"100 > 300 or 40 > 30 or 50 > 60 = {c} -->Short Circuit Evaluation")
d = 100 > 300 or 400 > 300 or 500 > 600
print(f"100 > 300 or 400 > 300 or 500 > 600 = {d} -->Short Circuit Evaluation")
e = 100 > 300 or 40 > 300 or 500 > 600
print(f"100 > 300 or 40 > 300 or 500 > 600 = {e} -->Full length Evaluation")

