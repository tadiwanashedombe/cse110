#Added a while loop 

origin_story = input("Your are a park ranger and your hear that the baboons broke out of their cages. Do you call for SUPPORT  or handle it ALONE ? ")

if origin_story.lower() == "support":
    origin_story = input("The calvary has arrived  but one baboon seem to have wandered into the wild. Are you going into the WILD to find it or let the baboon get LOOSE ? ")
    if origin_story.lower() == "wild":
        print("You followed the baboon into the wilderness and brought it back and you became the hero , now you are up for promotion")
    elif origin_story.lower() == "loose": 
        print("You are in big trouble for letting the baboon get lost into the wild and now the manager is in the talks about finding your replacement")   
    else:
        print("Invalid Response")    
elif origin_story.lower() == "alone":
    origin_story = input("You manage to get the baboons back into their places except for one and it starts to get violent. Do you RUN or TASER it ? ")
    if origin_story.lower() == "run":
        print("You tried to manage the situation but things got out of hand quickly so you run for your dear life.")
    elif origin_story.lower() == "taser":
        taser_count = 3
        
        while taser_count > 0:
            shooting = input(f"You take out you taser and realise you have  {taser_count} shot(s). Do you SHOOT or RUN ? ")

            if shooting.lower() == "run":
                taser_count = 0
                print("You doubt the taser will be of any help. You run for your dear life")
            elif taser_count == 1:
                 print("The third time is a charm, the baboon gets knocked out and and help finally arrrives and every thing is in order, they just admire your bravery.")
            elif shooting.lower() != "shoot":
                print("Invalid Response")
                taser_count = 0
            taser_count  = taser_count - 1
            
    else:
        print("Invalid Response")

else:
    print("Invalid Response")
 