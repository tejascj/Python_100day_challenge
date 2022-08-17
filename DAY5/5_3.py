# https://replit.com/@tejascj/day-5-3-exercise#README.md <-- README.md
# ADD EVEN NUMBERS
n=int(input("Ente the from 1 to :"))
total=0
# for i in range(1,n+1):
#     if i%2==0:
#         total+=i
# print(total)

for i in range(2,n+1,2):
    total+=i
print(total)