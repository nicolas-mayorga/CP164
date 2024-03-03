"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from Food import Food

ORIGIN = ("Canadian", "Chinese", "Indian", "Ethiopian",
          "Mexican", "Greek", "Japanese", "Italian", "American",
          "Scottish", "New Zealand", "English")


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    food_name = input("Name: ")
    food_origin = int(input(f"{Food.origins()}:"))
    vegetarian = input("Vegetarian (Y/N): ")
    if vegetarian == 'Y':
        food_vegetarian = True
    else:
        food_vegetarian = False
    food_calories = int(input("Calories: "))

    food = Food(food_name, food_origin, food_vegetarian, food_calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    food_info = line.split('|')
    if food_info[2] == 'True':
        food_veg = True
    else:
        food_veg = False
    food = Food(food_info[0], int(food_info[1]),
                food_veg, int(food_info[3]))
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    for line in file_variable:
        foods.append(read_food(line))
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for food in foods:
        food_info = [food.name, str(food.origin), str(
            food.is_vegetarian), str(food.calories)]

        string = '|'.join(food_info) + '\n'
        file_variable.write(string)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN)), 'Origin ID invalid'

    origins = []
    for food in foods:
        if food.origin == origin:
            origins.append(food)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total_cals = 0
    num_food = 0
    for food in foods:
        total_cals += food.calories
        num_food += 1

    avg = total_cals // num_food
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    total = 0
    count = 0
    avg = 0
    for food in foods:
        if food.origin == origin:
            total += food.calories
            count += 1
    if count > 0:
        avg = total // count
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print(f"{'Food':35s} {'Origin':12s} {'Vegetarian':>10s} {'Calories': >8s}\n" +
          f"{'-'*35} {'-'*12} {'-'*10} {'-'*8}")
    foods.sort()

    for food in foods:
        name = food.name
        origin = food.ORIGIN[food.origin]
        vegetarian = str(food.is_vegetarian)
        calories = food.calories
        print(f"{name:35s}", end=' ')
        print(f"{origin:12s}", end=' ')
        print(f"{vegetarian:>10s}", end=' ')
        print(f"{calories:>8d}")
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    if origin == -1 and max_cals == 0 and is_veg == False:
        result = foods

    if origin != -1:
        o_check = True
    else:
        o_check = False

    if max_cals > 0:
        c_check = True
    else:
        c_check = False

    for food in foods:
        if o_check and c_check and is_veg:
            if food.origin == origin and food.calories <= max_cals and food.is_vegetarian:
                result.append(food)
        elif o_check and c_check and not is_veg:
            if food.origin == origin and food.calories <= max_cals:
                result.append(food)
        elif o_check and not c_check and not is_veg:
            if food.origin == origin:
                result.append(food)
        elif not o_check and c_check and not is_veg:
            if food.calories <= max_cals:
                result.append(food)
        elif not o_check and not c_check and is_veg:
            if food.is_vegetarian:
                result.append(food)

    return result
