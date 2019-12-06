k_val = int(input("Please enter k-value: "))
n_val = int(input("Please enter n-value: "))
private_poly = int(input("Please enter private polynomial: "))
poly_shares = int(input("Please enter polynomial shares from collaborating participants: "))
degree = k_val - 1
deactivation_code = 0

shared_polys = {1: 468, 2: 2784, 4: 20822, 5: 70960, 7: 256422}

collaborators = [1, 2, 4, 5, 7]
x = 0
quotient = 1
for i in collaborators:
    for j in collaborators:
        if j != i:
            quotient *= j / (j - i)
    x += shared_polys.get(i) * quotient
    print(x)
    quotient = 1

print(x)
# print(deactivation_code)