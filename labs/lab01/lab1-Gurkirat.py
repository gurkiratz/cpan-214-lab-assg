x=4
y=2
print(x+y)

car_name="Mercedes"
num_wheels=4
print(f'My {car_name} has {num_wheels} wheels.')

name="Kirat"
num_apples=24
num_friends=7
apples_per_friend = num_apples//num_friends
print(f'I am {name} and I have {num_friends} friends. We have {num_apples} apples. So, each person will get {apples_per_friend} apples.')

bill_total=125
num_people=4
cost_per_person=float(bill_total/num_people)
# cost_per_person=format((bill_total/num_people), '.2f')

print("-------")
print(f"Num of people: {num_people}\nTotal bill: ${bill_total}\nCost per person: ${cost_per_person:.2f}\n")
print(f"Num of people: {num_people}\nTotal bill: ${bill_total}\nCost per person: ${int(round(cost_per_person))}")

print("-------")
dessert_cost=6.55
print(f"Num of people: {num_people}\nDessert cost: ${dessert_cost:0.2f}\nTotal Cost: ${num_people*dessert_cost:.2f}")
