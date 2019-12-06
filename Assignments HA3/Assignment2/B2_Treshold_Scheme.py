import numpy


k_val = int(input("Please enter k-value (treshold): "))
n_val = int(input("Please enter n-value (total number of participants): "))
participant_val = int(input("Please enter your participant number: "))
coefficients = [x for x in map(int, input("Please enter your private polynomial coefficients separated by spaces: ").split())]


participant_poly = numpy.polyval(coefficients, participant_val)
master_participant_poly = 0


master_participant_poly += sum([x for x in map(int, input("Please enter the other "
                                                          "participants polynomial value for x = 1 "
                                                          "separated by spaces: ").split())])

master_participant_poly = master_participant_poly + participant_poly
shared_polys = {}
collaborators = [participant_val]
shared_polys[participant_val] = master_participant_poly


for i in range(1, k_val):
    poly_share = int(input(f"Please enter polynomial share {i} from collaborating participants: "))
    collaborator = int(input("Please enter collaborator number: "))
    shared_polys[collaborator] = poly_share
    collaborators.append(collaborator)


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