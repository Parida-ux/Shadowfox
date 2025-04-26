Task1
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))


for=4
This will throw the syntax error because for is a reserved keyword
in python used for loops.





2
P = 10000  
R = 5   
T = 3      

simple_interest = (P * R * T) / 100
print("Simple Interest:", simple_interest)




2-NUMBERS 
TASK=1

def format_example(number, format_type):
    formatted = "{0:{1}}".format(number, format_type)
    return formatted

result = format_example(145, 'o')
print("Formatted result:", result)


2=import math

radius = 84
pi = 3.14
area = pi * (radius ** 2)
water_per_square_meter = 1.4
total_water = int(area * water_per_square_meter)

print("Area of the pond:", int(area))
print("Total water in the pond (in liters):", total_water)


3=distance = 490  
time = 7        
# First, convert time to seconds (1 minute = 60 seconds)
time_in_seconds = time * 60
speed = distance / time_in_seconds
speed_no_decimal = int(speed)

print(speed_no_decimal)



3=List 
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members
print(f"Step 1: Number of members = {len(justice_league)}")

# 2. Batman recruited Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print(f"Step 2: After adding Batgirl and Nightwing = {justice_league}")

# 3. Wonder Woman becomes the leader (move her to start)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Step 3: After making Wonder Woman leader = {justice_league}")

# 4. Separate Aquaman and Flash by inserting Green Lantern between them

aquaman_index = justice_league.index("Aquaman")
# Remove Green Lantern first to avoid duplication
justice_league.remove("Green Lantern")
# Insert Green Lantern after Aquaman
justice_league.insert(aquaman_index + 1, "Green Lantern")
print(f"Step 4: After separating Aquaman and Flash = {justice_league}")

# 5. Crisis! Replace entire list with new team members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"Step 5: New Justice League after crisis = {justice_league}")

# 6. Sort the list alphabetically
justice_league.sort()
print(f"Step 6: Justice League after sorting alphabetically = {justice_league}")

# Bonus: Predict new leader
print(f"Bonus: The new leader is {justice_league[0]}")




4=if(condition)
city_country = {
    "mumbai": "india",
    "chennai": "india",
    "delhi": "india",
    "sydney": "australia",
    "melbourne": "australia",
    "dubai": "uae",
    "abu dhabi": "uae",
    "new york": "usa",
    "los angeles": "usa",
    "london": "uk",
    "manchester": "uk"
}

# Taking input from user
city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()

# Checking if both cities are in the dictionary
if city1 in city_country and city2 in city_country:
    if city_country[city1] == city_country[city2]:
        print(f"Both cities are in {city_country[city1].title()}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not recognized")
    
    
    
    7=File handling
    # Step 1: Read the CSV file
students = []

with open('student_marks.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Step 2: Update dictionary with total_marks and average_marks
for student in students:
    # Extract only the subject marks and calculate total and average
    marks = [int(student[subject]) for subject in student if subject not in ['Name', 'RollNo']]
    total = sum(marks)
    average = total / len(marks)
    student['Total_Marks'] = total
    student['Average_Marks'] = round(average, 2)

# Step 3: Write the updated information to a new CSV file
fieldnames = list(students[0].keys())

with open('student_marks_updated.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("New file 'student_marks_updated.csv' created successfully!")
