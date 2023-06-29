# Both Users will need to enter infos

user1_name = input("Enter your name: ")
user1_age = int(input("Enter your age: "))  # Convert age1 to an integer
user1_favorite_food = input("Enter your favorite food: ")
user2_name = input("Enter your name: ")
user2_age = int(input("Enter your age: "))  # Convert age2 to an integer
user2_favorite_food = input("Enter your favorite food: ")
total_age = user1_age + user2_age  # the sum of age1 and age2

message = "Hello " + user1_name + " and " + user2_name + "! You are " + str(total_age) + " years old total " \
         "and your favorite foods are " + user1_favorite_food + " and " + user2_favorite_food + "."

print(message)
