start = int(input("Enter starting number"))
end = int(input("Enter ending number"))

evenSum = sum(x for x in range(start,end+1 ) if x%2==0)

print(f"Sum of even number between range of {start} and {end} is {evenSum}")