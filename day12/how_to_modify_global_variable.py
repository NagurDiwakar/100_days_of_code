# modifying the global scope varibles

# usually dont do this by changing global varibles , leads to bugs and error prone

enemies = 1

def increase_enemies():
    # global scope
    global enemies
    enemies += 2
    print(f"enemies inside function : {enemies}")

increase_enemies()