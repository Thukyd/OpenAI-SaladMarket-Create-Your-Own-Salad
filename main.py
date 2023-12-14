# Salad options data structure
salad_options = {
    "ingredients": [
        ("Aceitunas Negras", "Black Olives"), ("Aceitunas Verdes", "Green Olives"),
        ("Aguacate", "Avocado"), ("Almendras Largueta", "Largueta Almonds"),
        ("Arándanos Deshidratados", "Dried Cranberries"), ("Arroz Blanco", "White Rice"),
        ("Arroz Integral", "Brown Rice"), ("Atún", "Tuna"),
        ("Brotes de Soja", "Soy Sprouts"), ("Cebolla Figueres", "Figueres Onion"),
        ("Champiñones Fileteados", "Sliced Mushrooms"), ("Col Kale", "Kale"),
        ("Cus-Cus", "Couscous"), ("Edamame", "Edamame"),
        ("Espinacas Baby", "Baby Spinach"), ("Fresones de Temporada", "Seasonal Strawberries"),
        ("Garbanzos", "Chickpeas"), ("Huevo Duro", "Hard Boiled Egg"),
        ("Hummus", "Hummus"), ("Lechuga Mezclum", "Mixed Lettuce"),
        ("Lechuga Romana", "Romaine Lettuce"), ("Lentejas", "Lentils"),
        ("Maíz Cocido", "Cooked Corn"), ("Manzana", "Apple"),
        ("Mezcla de Frutos Secos", "Mixed Nuts"), ("Nueces", "Walnuts"),
        ("Pasas Sultanas", "Sultana Raisins"), ("Pasta Hélices", "Fusilli Pasta"),
        ("Pasta Pajaritas", "Farfalle Pasta"), ("Pavo", "Turkey"),
        ("Pepino", "Cucumber"), ("Picatostes de Pan", "Croutons"),
        ("Piña", "Pineapple"), ("Pipas de Calabaza", "Pumpkin Seeds"),
        ("Pipas de Girasol", "Sunflower Seeds"), ("Pollo Braseado", "Grilled Chicken"),
        ("Queso Emmental a Dados", "Diced Emmental Cheese"), ("Queso Feta a Dados", "Diced Feta Cheese"),
        ("Queso Mozzarela en Perlas", "Pearl Mozzarella Cheese"), ("Queso Parmesano en Escamas", "Parmesan Flakes"),
        ("Remolacha Cocida", "Cooked Beetroot"), ("Sésamo", "Sesame"),
        ("Surimi", "Surimi"), ("Tomates Cherry", "Cherry Tomatoes"),
        ("Zanahoria", "Carrot")
    ],
    "dressings": [
        ("Sin Aliño", "Without Dressing"),
        ("Aceite y Vinagre", "Oil and Vinegar"),
        ("César", "Caesar (Mayonnaise, Parmesan, Anchovy, Tuna)"),
        ("Crema de Vinagre", "Vinegar Cream"),
        ("Frambuesa", "Raspberry (Raspberry Jam)"),
        ("Limón Exprimido", "Squeezed Lemon"),
        ("Mango", "Mango (Mango Jam and Olive Oil)"),
        ("Miel", "Honey (Honey, Modena Vinegar, and Olive Oil)"),
        ("Mostaza y Miel", "Mustard and Honey (Old Mustard, Honey, a touch of Modena Vinegar, Olive and Sunflower Oil)"),
        ("Pesto", "Pesto (Basil, Parsley, Parmesan, Walnuts, and Olive Oil)"),
        ("Olivada", "Black Olive Spread (Black Olive and Olive Oil)"),
        ("Salad Market", "Salad Market (Old Mustard, Agave Syrup, and Olive Oil)"),
        ("Salsa Picante", "Spicy Sauce (Cayenne, Oregano, Parsley, Onion, and Ketchup)"),
        ("Salsa Rosa", "Pink Sauce (Mayonnaise, Pineapple, Ketchup)"),
        ("Soja", "Soy"),
        ("Yogur", "Yogurt (Natural Yogurt, a touch of Mint and Sugar)"),
        ("Sin Aliño", "Without Dressing")
    ]
}

# Function to validate salad creation
def create_salad(ingredient_selection, dressing_choice):
    # Check if ingredient selection is valid (up to 8 ingredients)
    if len(ingredient_selection) <= 8 and all(item in salad_options["ingredients"] for item in ingredient_selection):
        # Check if dressing choice is valid (exactly one dressing)
        if dressing_choice in salad_options["dressings"]:
            # Proceed with creating the salad
            print("Creating salad with selected ingredients and dressing.")
            # Here, add logic to actually create the salad based on the user's choices
        else:
            print("Invalid dressing selection. Please choose one dressing from the list.")
    else:
        print("Invalid ingredient selection. Please choose up to 8 ingredients from the list.")

# Example user selection
user_ingredient_selection = [("Aguacate", "Avocado"), ("Almendras Largueta", "Largueta Almonds"), ...] # Up to 8 ingredients
user_dressing_choice = ("Pesto", "Pesto (Basil, Parsley, Parmesan, Walnuts, and Olive Oil)")

# Call the function with user's selection
create_salad(user_ingredient_selection, user_dressing_choice)
