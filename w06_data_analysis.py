#added options to compare expctancy between years

#open the file
with open("python/life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    
    max_preferred_expectancy = -1
    min_preferred_expectancy = 1000
    min_expectancy = 1000
    max_expectancy = -1
    count_countries = 0
    total_expectancy = 0

    #get user input
    year_of_interest = int(input("Enter the year of interest:"))

    print()

    for line in life_expectancy:
        #split each line into parts
        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        year2= int(parts[2])
        expectancy = float(parts[3])


        # Year of interest
        if year == year_of_interest:
            

            total_expectancy += expectancy
            count_countries += 1
        
            avg_expectancy = total_expectancy / count_countries

            #preferred max expectancy
            if expectancy > max_preferred_expectancy:
                max_preferred_expectancy = expectancy
                max_preferred_country = parts[0]

            #preferred min expectancy
            if expectancy < min_preferred_expectancy:
                min_preferred_expectancy = expectancy
                min_preferred_country = parts[0]
        
        #Max expectancy
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_entity = parts[0]
            max_yr = parts[2]

        #Min expectancy
        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_entity = parts[0]
            min_yr = parts[2]
        
    #Displaying

    #max
    print(f"The overall max life expectancy is: {max_expectancy} from {max_entity} in {max_yr}")

    #min
    print(f"The overall min life expectancy is: {min_expectancy} from {min_entity} in {min_yr}")
    
    print()
    
    #Preferred Year
    print(f"For the year {year_of_interest} :")
    
    #Average expectancy
    print(f"The average life expectancy across all countries was {avg_expectancy:.2f}")
    
    #Max and Min of preferred year
    print(f"The max life expectancy was in {max_preferred_country} with {max_preferred_expectancy}")
    print(f"The min life expectancy was in {min_preferred_country} with {min_preferred_expectancy}")

'''

    #compare 2 years

    compare = input("Do you have 2 years in mind you would like to compare (yes/no) : ")
    if compare.lower() == "yes":
        total_expectancy1 = 0
        total_expectancy2 = 0

        year1 = int(input("Enter the first year : "))
        year2 = int(input("Enter the second year : "))

        for line in life_expectancy:
            #split each line int parts
            parts = line.split(",")

            year = int(parts[2])
            expectancy1 = float(parts[3])
            expectancy2 = float(parts[3])

            #year 1 total expectancy
            if year == year1:
                total_expectancy1 += expectancy1  
            
            #year 2 total expectancy
            if year == year2:
                total_expectancy2 += expectancy2
            
        #compare total expectancy

        #year1 has the highest expectancy
        if total_expectancy1 > total_expectancy2:
            diferrence = total_expectancy1 - total_expectancy2
            print(f"The year {year1} had a higher life expectancy than {year2}")
            print(f"The diferrence is {diferrence}")
        #year2 has the highest expectancy
        elif total_expectancy1 < total_expectancy2:
            diferrence = total_expectancy2 - total_expectancy1
            print(f"The year {year2} had a higher life expectancy than {year1}")
            print(f"The diferrence is {diferrence}")
        else:
            print("Unable to comapre try other years")
    elif compare.lower() == "no":
        print("Assignment complete")
    else:
        print("Invalid input")
        '''