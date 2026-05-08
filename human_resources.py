#open file
with open("hr_system.txt") as hr_file:
    next(hr_file)
    #read thru the file
    for line in hr_file:

        #get the various parts and record into variables
        parts = line.split(" ")

        name = parts[0]
        id = int(parts[1])
        job_title = parts[2]
        salary = int(parts[3])

        paycheck_amount = salary / 24

        if job_title.lower() == "engineer":
            paycheck_amount += 1000

        #print out values
        print(f"{name} (ID : {id}), {job_title} - {paycheck_amount:.2f}")
