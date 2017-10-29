
#a simple text-based adventure(boken) game. :)
print("*************************")
print('*    Welcome to Boken!   *')
print("*************************")
name = input("Enter a user name:")
sex = input("sex?-M/F-")
print("------------------")
print("-   Start game!  -")
print("------------------")
print("User: " + name + "(" + sex + ")")
space = input("Click enter to continue: ")
print(name + " is an ordinary high school student.")
print("On an usual rainy evening, you arrive home from school.\nThe sky was getting grey and the rain kept being incessantly heavy.")
print("However, not eveything was the same as before; you \nsee an unusual pattern drawn on your wall: like a magic circle!")
print("A sudden lightening! A weird bright light seems to sip through \nthe crack on the wall circle which made you blind.\n")
input("Press enter to continue.")
print("--------------------")
print("////////////////////")
print("/ / / / / / / / / /")
print("/  /  /  /  /  /  /")
print("/   /   /   /   /  ")
input("Press enter to continue.")
print("\n--Everthing's hazy: it's turning pitch black as you are slowly losing your senses.--")
print("===================")
print("     unconcious    ")
print("===================")
print("\n--You wake up from an almost deep slumber to find yourself in an unknown world.--")
#apple, jewel, potion numbers
amount = [0, 0, 0]
apple = 0
jewel = 0
potion = 0

#bag function prints the number of
#apple, food and jewel you have
def bag():
    print("apple, jewel, potion: ")
    print(amount)
    return

#to update apple in the array amount
def changeapple(n):
    amount[0] = apple + n
    bag()
    return

#to update jewel in the array amount
def changejewel(n):
    amount[1] = jewel + n
    bag()
    return

#to update potions in the array amount
def changepotion(n):
    amount[2] = potion + n
    bag()
    return

print("--After you are fully awake, you find yourself lost and alone with just an empty bag, which was never yours to begin with.--")
bag()

print("\n===================")
print("     Level 1      ")
print("===================")
print("\n+++++++++++++++++++++++")
print("+ + + + + + + + + + + +")
print("| /|/ \| | | | / | | /")
print("|/ |/ \| |/ \|/ |/ \|/")
print("|  ||  | ||  |  ||  ||")
print("----------------------")
print("--While you did not know what to do inside this forest, a villager caught you in sight as he was passing by.--")
print("Villager: A human!.....How on earth have you come here?!")
ans = input("You: ")
print("--You are shocked by the villager's appearance: pointy ears and a tail--")
print("Villager: It is dangerous for a human to stay here. Would you like to come with me to my home.")
print("\nChoose: 1(Would you like to go with the villager?) or 2(Would you like to continue on your own?)")
val = input("enter number: ")

#When option 1 is chosen
if val == '1':
    print("--You follow the villager to his home. You ask about this place and how you can go back to your home.--")
    print("Villager: This is the demon world and you probably have been transported by a summoning circle.")
    input("Press enter to continue!")
    print("+ + + + + + + + + + + + + + + + + + + + + + + + ")
    print("_______________-----------------------=======----------)")
    print("|        $$            ****      $$      |____|       |____")
    print("(east              ||  ||||         |+| |+|                 |__}")
    print("{village ============||===========||===========  $$$ Capital   |________)")
    print("(                  ||           -+-+-+-+-       *****\/++++           __}_")
    print("(  ++++     $$     ||           -=-=-=-   ____|||||_|_||||__________}")
    print("(  ||||        ||      ***++          )___|")
    print("----------------_______||||___$$______|")
    print("+ + + + + + + + + + + + + + + + + + + + + + + + \n")

    print("Villager: Now you are in a small rural and in the furthest east village. Only farmers live here.")
    print("Anyone from another world can only return using the magic circle in the capital centre.")
    print("You: So, how can i get there, the capital center?")
    print("Villager: You have follow the main route to the west, but you can't walk there as it's too far.Therefore, you need food and jewel to travel from our village to the capital.")
    input("Press enter to continue!")
    print("--------------------")
    print("          \_/    ")
    print("          _||__")
    print("         (_*_*_)")
    print("--------------------")
    print("Also, take this potion, drink it when you decide to travel so you can hide yor presence from evil demons.")
    print("You: Thank you. I will take the potion\n")
    changepotion(1)
    print("\nYou: What are jewel used for? Can you tell me where i can get food supply?")
    print("Villager: We exchange jewel as our currency. You will need to find a job to earn some jewel.")
    print("We have apples that you can eat and also you can find apple trees everywhere.")
    print("You: How can i find a work in this world?")
    print("Villager: You see there is a giant water serpent in the river. It is the only source of our water supply.")
    print("Many were killed while trying to get water from that river. Our preserved water is also limited.O human!\n Will you be kind enough to slaughter the serpent for us? We villagers will offer you 30 jewels.")
    print("You: Thank you, kind villager! I will take on your offer.\n")
    print("--You followed the villager to the river where the water serpent is.--")
    print("--On your way you find 10 apples on the ground.--")
    input("To collect the 10 apples press enter: ")

    changeapple(10)

    print("\n///////////////////////")
    print("//___//          ")
    print(" / + \           ")
    print(" \=   \_    ")
    print("   |  * \_             |")
    print("    \   * \           / |")
    print("     \   * \         /  /")
    print("/////////////////////////\n")
    print("+++++++++++++++++")
    print("     Battle      ")
    print("+++++++++++++++++")
    print("--You take the sword given by the villagers and approach it slowly.--")
    print("--As the slightest sound reached the serpent, it moves towards you to attack with its scales.--")
    print("--You use your sword to deflect it's attack and it forces you back.--")
    print("--You run forward to pierce it and the serpent creeps with its mouth open to swallow you whole.--")
    print("________________")
    print("     SLASH      ")
    print("________________")
    print("--Your sword cut the inside of the serpents mouth, while you are gobbled.--")
    print("--You are stuck inside the serpents belly with almost no energy to spare.--")
    print("To regain all your stamina, you can eat 3 apples.")
    input("To eat 3 apple write (3 apples): \n" )

    changeapple(7)

    print("\n++++++++++++++++++++")
    print("    Full recovery   ")
    print("+++++++++++++++++++++")
    print("--Now, you use all force to cut open the serpent to escape.--")
    print("--You hear screams as all the blood splatters with the serpent cut in half.--")
    print("*After slaughtering serpent*")
    print("(Villagers screaming with excitement)")
    print("Villager 1: You are our hero! You saved us from the giant water serpent!")
    print("Village chief: You have done so much for us kind stranger. Please accept a small reward from us:here is your 30 jewels.")
    input("Type 'accept' to accept the jewels: \n")

    changejewel(30)

    print("\nYou: Thank you all, i shall take off now.")
    print("Before you leave the village, you have to drink the potion.")
    input("To drink potion press enter: \n")

    changepotion(0)

    print("\n--You pack your bag and head toward the capital. On your way you find the potion shop.--")
    ans = input("Would you like to buy some potion? y/n: ")
    if ans == 'y':
        print("--You go to the potion shop and ask about the potions.--")
        print("Potion Master: Hello, there! What kind of potions would you like to buy?")
        print("You: I am not sure. What kind of potions do you have?")
        print("Potion Master: I sell 1:(healing potions-10 jewels each) and 2:(invisible potions--5 jewels each).")
        buy = input("Select the type of potion you want to buy, if you want to buy both, then type both: ")
        if buy == '1':
            print("Potion Master: How many of the healing potions would you like to buy?")
            num = input("Enter the number potions you want: ")
            money = 10*int(num)
            print("Potion Master: For " + str(num) + " healing potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)

            print("\n And take you potions.\n")
            changepotion(int(num))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
        elif buy == '2':
            print("Potion Master: How many of the invisible potions would you like to buy?")
            num = input("Enter the number potions you want: ")
            money = 5*int(num)
            print("Potion Master: For " + str(num) + " invisible potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)

            print("\n And take you potions.\n")
            changepotion(int(num))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
        elif buy == 'both':
            print("Potion Master: How many of the healing potions would you like to buy?")
            num1 = input("Enter the number potions you want: ")
            print("Potion Master: How many of the invisible potions would you like to buy?")
            num2 = input("Enter the number potions you want: ")
            money = (10*int(num1)) + (5*int(num2))
            print("Potion Master: For" + str(num1) + "healing potions and " + str(num2) + "invisible potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)
            print("\n And take you potions.\n")

            changepotion(int(num1) + int(num2))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
    else:
        print("--You continue to head to the capital.--");


#when option 2 is chosen
elif val == '2':
    print("You: Thank you for you kindness but I think I will be able to travel on my own now.")
    print("Villager: Alright, then take this potion. Drink it, this will hide your presence from evil demons.")
    print("You: Thank you, i will accept the potion.\n")

    changepotion(1)

    input("\nPress enter to continue!")
    print("--You part with the villager and start to wonder around this big forest.--")
    print("--You search for a way out of this forest and for food supply.--")
    print("--Suddenly, you see apples lying on the ground; you look above and see a lot of big apple trees.--")
    print("--You eat some apples to ease your hunger and pick 10 apples for your journey.--")
    input("To pick 10 apples type 'pick apples': ")

    changeapple(10)

    print("\n--After you secured the food, you continue to move forward. An abrupt howling sound!--")
    print("--The frightening roar of a beast made you cautious. You have to run or kill it, if you want to live.--")
    print("--The ground started to shake and a huge boar like creature is running toward you.--\n")

    print("+++++++++++++++++++++")
    print("     |\______/| ")
    print("    ({+}    {+})")
    print("   ( \   |-|  / ")
    print("  /   (=======) ")
    print(" (     VVVVVVV  ")
    print(" |     ^^^^^^^  ")
    print("+++++++++++++++++++++")

    print("\n--The beast is closing in, almost hitting you.--")
    print("--You dodge the hit, move back and start running.--")
    print("--The beast chases you at the end of the forest and tries to attack you again.--")
    print("--You grab the stones from the ground and hit the beast before it attacks you.--")
    print("--You constantly keep hitting it hard and after a while the beast fell down.--")
    print("--As you are relieved, the beast's body shattered into a spear.--")
    print("--You are shocked by this transformation and slowly approach the shattered body.--")
    print("--You check if it is safe, take the spear with you and move out of the forest.--\n")

    input("Press enter to continue: ")
    print("--You walk to nearby village across a river and a giant serpent attacks you from behind.--")
    print("--You see some of the villagers screaming with fear and you look back to see the vicious serpent.--\n")

    print("\n///////////////////////")
    print("//___//          ")
    print(" / + \           ")
    print(" \=   \_    ")
    print("   |  * \_             |")
    print("    \   * \           / |")
    print("     \   * \         /  /")
    print("/////////////////////////\n")

    print("\n--You are hit by the serpent and lose all you energy.--")
    print("To regain all your stamina, you can eat 3 apples.")
    input("To eat 3 apple write (3 apples): \n" )

    changeapple(7)

    print("\n++++++++++++++++++++")
    print("    Full recovery   ")
    print("+++++++++++++++++++++")
    print("--You run forward to pierce the serpent with your spear. The spear kills off the serpent in one hit.--")
    print("________________")
    print("     Pierce     ")
    print("________________")
    print("--You hear screams as the blood is spilling out of the serpent.--")
    print("*After slaughtering serpent*")
    print("(Villagers screaming with excitement)")
    print("Villager 1: you are the human from before! Thank you very much.")
    print("Villager 2: You are our hero! You saved us from the giant water serpent!")
    print("Village chief: You have done so much for us kind stranger. Please accept a small reward from us:here is your 30 jewels.")
    input("Type 'accept' to accept the jewels: \n")

    changejewel(30)

    print("\nVillager: If you want to go back where you came from, then you should go to the capital centre.")
    print("You: Where is the capital? How can i go there?")
    print("Villager: Now you are in the East village. If you head to the West from here, you will reach the capital.")
    print("You: Thank you all, i shall take off now.")
    print("Before you leave the village, you have to drink the potion.")
    input("To drink potion press enter: \n")

    changepotion(0)

    print("\n--You pack your bag and head toward the capital. On your way you find the potion shop.--")
    ans = input("Would you like to buy some potion? y/n: ")
    if ans == 'y':
        print("--You go to the potion shop and ask about the potions.--")
        print("Potion Master: Hello, there! What kind of potions would you like to buy?")
        print("You: I am not sure. What kind of potions do you have?")
        print("Potion Master: I sell 1:(healing potions-10 jewels each) and 2:(invisible potions--5 jewels each).")
        buy = input("Select the type of potion you want to buy, if you want to buy both, then type both: ")
        if buy == '1':
            print("Potion Master: How many of the healing potions would you like to buy?")
            num = input("Enter the number potions you want: ")
            money = 10*int(num)
            print("Potion Master: For " + str(num) + " healing potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)

            print("\n And take you potions.\n")
            changepotion(int(num))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
        elif buy == '2':
            print("Potion Master: How many of the invisible potions would you like to buy?")
            num = input("Enter the number potions you want: ")
            money = 5*int(num)
            print("Potion Master: For " + str(num) + " invisible potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)

            print("\n And take you potions.\n")
            changepotion(int(num))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
        elif buy == 'both':
            print("Potion Master: How many of the healing potions would you like to buy?")
            num1 = input("Enter the number potions you want: ")
            print("Potion Master: How many of the invisible potions would you like to buy?")
            num2 = input("Enter the number potions you want: ")
            money = (10*int(num1)) + (5*int(num2))
            print("Potion Master: For" + str(num1) + "healing potions and " + str(num2) + "invisible potions, your total is " + str(money) + " jewels.")
            print("You pay the potion master.\n")

            changejewel(30-money)
            print("\n And take you potions.\n")

            changepotion(int(num1) + int(num2))

            print("\nPotion Master: Thank you for coming. Come again if you need any potions.")
            print("You: Thank you.")
    else:
        print("--You continue to head to the capital.--");



#level 2
print("\n===================")
print("     Level 2      ")
print("===================")
print("--While you are walking through this stangely different environment, you realized that you are far away from home.--")
print("--The trees, plants and the landscape, all are very different. You are heading to the West to the Capital by foot.--")
print("--As you walk, you see a sign board that says: 'Bubun village'--")
print("+ + + + + + + + + + + + + + + + + + + + + + + + ")
print("_______________-----------------------=======----------)")
print("|        $$            ****      $$      |____|       |____")
print("(east              ||  |||| Bubun  |+| |+|                 |__}")
print("{village ============||====Village===||===========  $$$ Capital   |________)")
print("(                  ||           -+-+-+-+-       *****\/++++           __}_")
print("(  ++++     $$     ||           -=-=-=-   ____|||||_|_||||__________}")
print("(  ||||        ||      ***++          )___|")
print("----------------_______||||___$$______|")
print("+ + + + + + + + + + + + + + + + + + + + + + + + \n")
print("--Now you have entered the Bubun village, it seems full of beautiful greenery and flowers.--")
print("--As you continue to move inside the village, all you see are dead withered plants and lifeless grounds.--")
print("--You see two demons having a conversation. You approach them and overhear...--")
print("Worker 1: This is just impossible! We try so hard to grow plants for making potion but they all wither! Damn that cursed demon!")
print("Worker 2: If this continues the demon world is soon to end. Aren't the capital aware of that cursed demon. They should be sending someone who can bring that red lotus...")

print("\nYou: Sorry to interrupt. Could you tell me why the surrounding here seems withered?")
print("Worker 1: Don't you know! It's the cursed demon's rampage! everything she touches, dies!")
print("Worker 2: She was actually a worker here who unknowingly drunk her own experimented potion that went wrong. We need someone who can go to the pixis' den to get the red lotus. it's the only way to save her and this world.")
print("You: What is the red lotus for?")
print("-----------------------")
print("        (\/\/)       ")
print("      (\/\/\/\/)       ")
print("     (\/\/\/\/\/)       ")
print("    (\/\/\/\/\/\/)      ")
print("   (\/\/\/\/\/\/\/)      ")
print("    (  ********   )   ")
print("     (___________)   ")
print("-----------------------")
print("Worker 1: We finally found that the smell of that flower can reverse the curse.")
print("--You feel sorry for these demons.--")
print("You: I'll go! I will help you. Where is the pixis' den?")
print("Worker 1: Really! You can do it!")
print("Worker 2: You walk straight on this path and it will lead you to the Wind forest. As you walk inside, there on the left side you will see the pixis' den.")
print("You: I'll try my best.")
print("Worker 2: The pixis are vicious creatures, but we have no choice. Here are 5 sleeping potions. Make sure the vapour of the potions spreads thoroughly without you inhaling it. Good luck!")
input("To accept 5 sleeping potions type 'take': \n")

changepotion(amount[2]+5)

input("\nPress enter to continue: ")
print("--You started to walk straight ahead on this path. After minutes of walk you see the forest.--")
print("--You feel tired and hungry after all this walk. So you take a break and eat 3 apples.--")
input("To eat 3 apples type 'eat': \n")

changeapple(4)

print("\n--You walk inside the forest and keep walking, while looking on your left to find the pixis' den.--")
print("--After walking for several minutes, you find the pixis' den.--")
print("++++++=++++++++++++++========+++++++++++++++=========+++++++++++")
print("                                     ++++++++++++++++++++++++")
print("     +++++++                             {^^^^^^^^^^^^^^^^^}  ")
print("  ****************                    __(                   )")
print("   | | | | | | | =========           (     pixis' den        )")
print("   | | | | | | |  | | | |         __(                        )")
print("   | | | | | | |  | | | |     ^^^(                 *******    )___")
print("   | | | | | | |  | | | |  /\/\/\(               */\/\/\/\/\/\/\/\)")
print("++++++=++++++++++++++========+++++++++++++++=========+++++++++++")
print("--Finally, you found it. You slowly cover your nose and take out one of the sleeping potions.--")
input("To use one sleeping potion write 'use': \n")

changepotion(amount[2]-1)

print("\n--You use the sleeping potion on the pixis at the entrance and they fall asleep.--")
print("--You carefully walk across the entrance and look for the red lotus, but few pixis comes out from the inside.--")
print("--Pixis fiercely attack you with their stink. You have to hurry and make a decision.--")
fight = ['attack', 'dodge']
print(fight)
choice = input("Enter 'attack' to kill or 'dodge' to avoid: ")
if choice == 'attack':
    print("--You attack the pixis with your weapon and deflect their attack. The next attack hits them all.--")
    print("--You killed the attacking pixis.--")
    print("--Now, You decide to go far inside the den to search for the red lotus.--")
elif choice == 'dodge':
    print("--You dodge the attacking pixis and use another sleeping potion.--")
    input("To use another sleeping potion write 'use': \n")

    changepotion(amount[2]-1)
    print("\n--The pixis fell on the ground and started to sleep.--")
    print("--Now, You decide to go far inside the den to search for the red lotus.--")

print("--As you walk inside in stealth motion, you see a large number of pixis surrounding a corner.--")
print("--Therefore, you decide to use another sleeping potion.--")
input("To use another sleeping potion write 'use': \n")

changepotion(amount[2]-1)

print("\n--All the pixis have fallen asleep and you see the red lotus in a corner.--")
input("To pluck the red lotus write 'pluck': ")
print("--You carefully plucked the red lotus and quickly get out of the pixis' den.--")
print("--You walk out of the forest to meet the workers from before.--\n")

print("--You went back and saw one of the workers standing there.--")
print("You: Hello Sir, i have come back with the red lotus from the pixis' den.")
print("Worker 2: You have finally come back. At long last this curse will be broken.")
print("--You give the red lotus to the worker. The workers made a potion for you to use on the cursed demon.--")
print("Worker 1: Please take this red lotus potion and splash it on the cursed demon, who resides on the barren ground.")
print("--You take the potion and follow the workers to the barren ground.--")
changepotion(amount[2]+1)
print("--You all see the cursed demon sitting on the barren ground withering all around her.--")
print("--You approach the demon slowly and take out the red lotus potion.--")
input("To pour the lotus potion on the cursed demon write 'splash': \n")

changepotion(amount[2]-1)

print("\n--After you splashed the potion, the cursed demon screeched and fainted.--")
print("--Few seconds later, the curse is lifted, the demon is back to normal and the lands are turning green.--")
print("++++++++++++++++++++++++++")
print("  *   *  *   *   *   *  * ")
print(" ++  ++ ++ ++ ++ ++ ++ ++ ")
print(" ||  || || || || || || ||")
print("++++++++++++++++++++++++++")
input("Press enter to continue: ")
print("*The workers shouts with joy*")
print("--The workers are happy and they want to offer 10 jewels and 5 sleeping potions for saving their friend.--")
input("To accept 15 jewels and 1 sleeping potions write 'accept': \n")

changejewel(amount[1]+15)
changepotion(amount[2]+1)

print("Cured demon: Thank you for helping me. I want you to take this magic stone. it will help you in your journey.")
print("You: Thank you. I will accept.")
print("Workers: Thank you very much. Have a safe journey.")
print("--You thanked everyone and head out of the Bubun village to the Capital.--")
input("Press enter to continue: ")

#level 3
print("\n===================")
print("     Level 3      ")
print("===================")
print("+ + + + + + + + + + + + + + + + + + + + + + + + ")
print("_______________-----------------------=======----------)")
print("|        $$            ****      $$      |____|       |____")
print("(east              ||  |||| Bubun  |+| |+|                 |__}")
print("{village ============||====Village===||===========  $$$ Capital   |________)")
print("(                  ||           -+-+-+-+-       *****\/++++           __}_")
print("(  ++++     $$     ||           -=-=-=-   ____|||||_|_||||__________}")
print("(  ||||        ||      ***++          )___|")
print("----------------_______||||___$$______|")
print("+ + + + + + + + + + + + + + + + + + + + + + + + \n")
print("--You continue on your journey to the Capital, so you can go back home.--")
print("--After a little walk, you pass by a cart on your way.--")
print("--The cart driver approach you.--")
print("Cart driver: Would like a ride in my cart? I am going to the capital. 15 jewels each.")
print("You: Sure, Thank you.")
input("To pay for your ride write '15 jewels': ")

changejewel(amount[1]-15)

print("\n--You get inside the cart and have a seat. You also notice that there are a few other passenger.--")
print("--The cart starts to move and head to the capital.--")
print("--Many hours gone by, you feel confused about why this is taking a long time?--")
print("--A sudden halt, the cart stopped moving. You thought you have reached the Capital.--")
print("--But to your surprise, you look outside to see that it has stopped in an unfamiliar shady forest.--")
print("--All on a sudden, a group of bandits rush toward the cart and shouting.--")
print("--Before you can speak, they use sleeping potions.--")
print("--Immediately you fall in deep slumber!--")

print("\n===================")
print("     unconcious    ")
print("===================")

input("\Press enter to continue:")
print("--Chaotic sound wakes you up. The bright daylight clears your vision. You realise that you have been kidnapped.--")
print("--You look around to see that other passenger are also tight like you: with price tags on all your foreheads.--")
print("--A day seem to have passed. You have been brought here by the bandits to be sold in the black-market.--")
print("--You sit there helplessly on that slave sale auction.--")
print("--You could not understand what to do, you are scared to be sold out like some other demons.--")
print("--Anxious hours pass by and fortunately you are safe for a brief moment.--")
print("--Night falls.--")
print("--The auction ended for today and you are taken to the store chamber with some other demons.--")
print("--Everyone seems to have fallen asleep.--")
print("--You struggle to untie yourself and check your bag.--")
changejewel(0)

print("\n--You find no jewel in your bag; all the jewels are stolen.--")
print("You can plan to escape this place or go to sleep hoping you will be saved soon.")
decide = input("Enter 1:(to try to escape) or 2:(to sleep here for the night): ")
if decide == '1':
    print("\n--You wonder around to look for the keys of this chamber.--")
    print("--You look here and there, but still can't find it. Your sight gets caught on a small hole on the wall.--")
    print("--You put your hand inside and you can feel a breeze. You look inside and see something shiny.--")
    print("--You take out the shiny object and it turns out to be a key.--")
    print("--You use this key to open the door and it opens.--")
    print("--Misfortune does not seem to leave you. the guards see you open the door.--")
    print("--Before you can escape they hit you and you pass out.--")
elif decide == '2':
    print("\n--You hold onto your bag and look for a blanket.--")
    print("--You find a warm blanket and cover yourself to sleep.--")

input("\nPress enter to continue: ")
print("--You wake up the next morning and hear loud noises.--")
print("--There seem to be some security officials who found out about this black-market sale.--")
print("--Now, they are here to take everything in their custody.--")
print("--You along with other demons are chained up and taken to another official cart, which head to the capital.--")
input("Press enter to continue: ")

print("\n--The cart stops after few hours and you are brought inside the king's palace.--")
print("Adviser: Sire! I can’t believe this! A human!")
print("King: What! Such hindrance! How dear you trespass our world!")
print("--You are frozen with fear thinking what would happen to you now. Will you ever be able to go back?--")
print("You: But I… I don’t know anything….")
print("King: I hereby declare this imposter’s execution! Take this creature away!")
print("--The guards try to take you away.--")
print("You: Wait no!")
print("Do you want to try to escape or convince the King of your innocence?")
go = input("Choose 1:(try to escape) or 2:(try to convince): ")

if go == '1':
    print("\nYou need to regain your energy in order to escape.")
    input("Write 'eat' to eat 3 apples to regain your energy: ")
    changeapple(amount[0]-3)
    print("--You regain your energy and push the guards to escape.--")
    print("--You run toward the exit and stumble upon a demon knight.--")
    print("--The magic stone falls out of the bag and touches you.--")
    print("--A projection of all your doings are emitted by the stone.--")
elif go == '2':
    print("\nYou need to regain your energy in order to convince.")
    input("Write 'eat' to eat 3 apples to regain your energy: ")
    changeapple(amount[0]-3)
    print("You: I didn’t do anything to harm anybody! Do you have any proof of me being guilty! Just because I’m a different being doesn’t mean I’m a culprit! What kind of law is this!")
    print("Demon knight: Sire, we found this magic stone in it’s attire. This can give us a true answer.")
    print("--The stone touches you and a projection of all your doings are emitted by the stone.--")

input("\nPress enter to continue: ")
print("Adviser: The human doesn’t seem to be harmful.")
print("Demon knight: Sire! This human completed the tasks that we couldn’t fulfill. The water serpent and that cursed demon!")
print("King: We humbly apologise to you human. What would you like to receive as you reward?")
print("You: I want to go back to my world.")
print("--The king gladly agrees to grant your wish and escorts you to the Magic Council.--")
print("Magic magistrate: We ask for your forgiveness, humble human.")
print("--You accept their apology and they happily prepare for your journey home.--")
print("--Everyone gathers around as the teleportation circle opens.--")
print("King: I ask you, human. Do you wish to erase your memory of this world?")
ques = input("Enter 1:(no) or 2:(yes):- ")

if ques == '1':
    print("\n--You show your gratitude for all their help, say goodbye to everyone and enter the magic circle.--")
    print("--------------------")
    print(" /  /  /  /  /  /  /")
    print(" \  \  \  \  \  \  \/")
    print(" /  /  /  /  /  /  /")
    print("--------------------")
    print("--You wake up remembering your great adventure and with some knowledge you gained you start your ordinary life.--")
elif ques == '2':
    print("\n--You show your gratitude for all their help, say goodbye to everyone and enter the magic circle.--")
    print("--------------------")
    print(" /  /  /  /  /  /  /")
    print(" \  \  \  \  \  \  \/")
    print(" /  /  /  /  /  /  /")
    print("--------------------")
    print("--You wake up from your strange adventurous dream yet you feel like you have learned something and with some knowledge you gained you start your ordinary life.--\n")

print("\n------------------")
print("-    End game!    -")
print("------------------\n")

play = input ("Press any key to exit! :)")
