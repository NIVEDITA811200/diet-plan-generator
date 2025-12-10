diet_plan_loss = {
    "Monday": {
        "Breakfast": "Oatmeal with almonds and fruits",
        "Snack": "Cut fruits",
        "Lunch": "Rice with vegetrain curry",
        "Dinner": "Chapati and dal curry"
    },
    "Tuesday": {
        "Breakfast": "Scrambled eggs with bread",
        "Snack": "Mixed nuts",
        "Lunch": "Chapati with chicken",
        "Dinner": "Sweet corn with 1 egg"
    },
    "Wednesday": {
        "Breakfast": "Smoothie with banana,nuts",
        "Snack": "Fruits and nuts bowl",
        "Lunch": "Rice with chicken and veggies ",
        "Dinner": "Oats with soked nuts"
    },
    "Thursday": {
        "Breakfast": "Bread with peanut butter",
        "Snack": "Yogut mixed with veggies",
        "Lunch": "Oats with cut fruits",
        "Dinner": "Chicken  with brown rice"
    },
    "Friday": {
        "Breakfast": "putt with kadala curry",
        "Snack": "Any juiice without suger",
        "Lunch": "Rice with fish curry",
        "Dinner": "Sweet potatos"
    },
    "Saturday": {
        "Breakfast": "Pancakes with honey",
        "Snack": "Nuts bowl with almonds and cashew",
        "Lunch": "Brown rice with grilled fish",
        "Dinner": "Chapathi with chicken curry"
    },
    "Sunday": {
        "Breakfast": "Egg  omelet with bread",
        "Snack": "Nuts and fruit mix",
        "Lunch": "Grilled chicken with garlic nann",
        "Dinner": "Oats and a whole egg"
    }
}

diet_plan_gain = {
    "Monday": {
        "Breakfast": "Oats with peanut butter, banana, and almonds",
        "Snack": "Greek yogurt with fruits",
        "Lunch": "Grilled chicken with brown rice and veg curry",
        "Dinner": "oats shake with peanut butter,oats,banana,and dry fruits"
    },
    "Tuesday": {
        "Breakfast": "Bread with peanut butter and two eggs",
        "Snack": "Bowl of mixed nuts and dried fruits",
        "Lunch": "Brown rice with sambar and fish fry",
        "Dinner": "chapati and egg curry"
    },
    "Wednesday": {
        "Breakfast": "Dosa with sambar and 2 eggs",
        "Snack": "Banana with nuts",
        "Lunch": "Briyani with greek yogut",
        "Dinner": "smoothie with banana,nuts,and protein powder"
    },
    "Thursday": {
        "Breakfast": "Pancakes with peanut butter",
        "Snack": " Egg and fruit bowl",
        "Lunch": "Rice with chicken",
        "Dinner": "Chicken fry with brown rice and curry"
    },
    "Friday": {
        "Breakfast": "Overnight oats with fruits",
        "Snack": "Mixed nuts",
        "Lunch": "Rice with veg curry",
        "Dinner": "chapti with vegetables "
    },
    "Saturday": {
        "Breakfast": "oats with banana,nuts, and fruits",
        "Snack": "Bowl of almonds, walnuts, and dried cranberries",
        "Lunch": "Brown rice with grilled chicken",
        "Dinner": "Chapati with dal curry and 2 eggs"
    },
    "Sunday": {
        "Breakfast": "Bread with omlet",
        "Snack": "dry fritsand nuts bowl",
        "Lunch": "Brown rice with chicken curry ",
        "Dinner": "smoothie with peanut butter,nuts,dry fruits"
    }
}

goal = input("Do you want to lose weight or gain weight? ")

current_weight = float(input("\nWhat is your current weight ? "))
target_change = float(input("\nHow much weight do you want to change ?(Use a positive number for gain and number for loss):"))

if goal == "lose weight":
    print(f"\nYou are aiming to lose {abs(target_change)} kg. Here's a balanced meal plan to help you with that goal.")
elif goal == "gain weight":
    print(f"\nYou are aiming to gain {target_change} kg. Here's a meal plan that will help you build muscle and increase your calorie intake.")
else:
    print("\nInvalid input. Please enter 'lose weight' or 'gain weight'.")

day = input("\nEnter a day:")

if goal == "lose weight" and day in diet_plan_loss:
    print(f"\nMeal Plan for {day}:")
    for meal, food in diet_plan_loss[day].items():
        print(f"{meal}: {food}")
elif goal == "gain weight" and day in diet_plan_gain:
    print(f"\nMeal Plan for {day}:")
    for meal, food in diet_plan_gain[day].items():
        print(f"{meal}: {food}")
else:
    print("Invalid day entered. Please enter a valid day of the week.")