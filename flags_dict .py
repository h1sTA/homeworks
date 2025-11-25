flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue', 'yellow'},
    'de': {'black', 'red', 'yellow'},  
    'fr': {'blue', 'white', 'red'},    
    'it': {'green', 'white', 'red'}    
}

while True:
    user_input = input("Enter the colors of a country flag (or 'exit' to quit): ").lower()
    if user_input == "exit":
        print("Program finished.")
        break
    
    colors = set(user_input.split())
    found = False
    
    for country, flag_colors in flags.items():
        if colors.issubset(flag_colors):
            print(country)
            found = True
    
    if not found:
        print("No country found with these colors.")
