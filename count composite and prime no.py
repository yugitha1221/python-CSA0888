n = (54, 29, 71, 7, 59, 98, 23)
prime_count = 0
composite_count = 0

for num in n:
    if num > 1:
        d=0
        for i in range(2, num):
            if num % i == 0:
                d=d+1
        if d>2:
            composite_count += 1
        else:
            prime_count += 1

print(f"Composite number: {composite_count}")
print(f"Prime number: {prime_count}")

