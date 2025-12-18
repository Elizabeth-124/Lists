inventory=["Sword","Potion","Sheild","Map"]
print(f"You start your adventure with: {inventory} ")
#After the battle
inventory[1]="Empty Flask"
inventory[2]="Broken Sheild"
print(f"Hand equipment: {inventory[0:2]}")
print(f"full inventory:{inventory}")