# enemies = 1
#
# def increace_enemies():
#     enemies = 2
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
#
# increace_enemies()
# print(f"Enemies outside the function: {enemies}")
#


# when need to access global varialbe:
# enemies = 1
#
# def increace_enemies():
#     # enemies = 2 #this is local varialbe
#     global enemies # this is global variable
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
#
# increace_enemies()
# print(f"Enemies outside the function: {enemies}")


# in festure modify global varible that give some logical error so:

enemies = 1

def increace_enemies(enemy):
    print(f"Enemies inside function: {enemies}")
    return enemy + 1

enemies = increace_enemies(8)
print(f"Enemies outside the function: {enemies}")