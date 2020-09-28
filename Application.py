print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

print("You are starting with", health, "health")
print("Hello, ",name," you are ",age," years old")

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Play")

        leftOrRight = input("First choice... Left or Roght(left/right)? ")
        if leftOrRight == "left":
            ans = input("Good, you are going the right way... You reached a stair in a hall... Do you go up the stairs or walk in the hall (up the stairs/walk the hall)? ")
            if ans == "up the stairs":
                print("You are now upstairs")

            elif ans == "walk the hall":
                print("You were seen by a ghost and you lost 5 health")
                health -= 5

            ans = input("You see a shotgun/cross and a machete/flame bottle. Choose one set(shotgun & cross / machete & flame bottle)?")
            if ans == "machete & flame bottle":
                print("You meet a zombie and ghost. They gang up on you and use you're set.")
                print("This doesn't work and you are now dead.")
                health -= 5

                if health <= 0:
                    print("You lost the game")
                else:
                    print("You have survived")
            elif ans == "shotgun & cross":
                print("You shoot the zombie and use the power of God to send the ghost away.")
                print("You find a health pack")
                health += 5
                print("Your health is now ", health)
        else:
            print("You were killed by a zombie...")

    else:
        print("Alright Cya...")

else:
    print("You are not old enough to play...")









''' 
string "hello", "hi", "89"
int 8,9,-8,1000000
float 6.0,6.7,100.0
bool True, False
'''