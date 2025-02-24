# Open and read the HR system file
with open('hr_system.txt', 'r') as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Strip whitespace and split the line into parts
    parts = line.strip().split()
    
    # Extract data
    name = parts[0]
    id_number = parts[1]
    job_title = parts[2]
    salary = float(parts[3])
    
    # Calculate paycheck (paid twice a month)
    paycheck = salary / 24
    
    # Apply bonus if the employee is an Engineer
    if job_title.lower() == "engineer":
        paycheck += 1000
    
    # Display the formatted output
    print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")


input("\nPress Enter to exit...")