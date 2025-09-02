score1 = 85
score2 = 92.5
score3 = 78

# Calculate averange of three score
averange = (score1 + score2 + score3) / 3
calculation = score1 ** 2  / score2 + score3 % 7
averange1 = int(averange)

print(f"({averange} (type: {type(averange)})")
print(f"{int(averange)} (type: {type(int(averange))})")
print(f"{calculation}(type: {type(calculation)})")
print(f"{float(score1)}")
print(f"{int(score2)}")
print(f"{averange}")