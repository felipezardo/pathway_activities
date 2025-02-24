# Data Analysis Project - Life Expectancy
# This program reads and analyzes a CSV dataset to determine the lowest and highest life expectancies,
# allows the user to query statistics for a specific year, search for a country, and identify the largest decline.

# Open and read the CSV file
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # Skip header line
    return lines

# Find the overall lowest and highest life expectancy values
def find_min_max_life_expectancy(data):
    min_life = float('inf')
    max_life = float('-inf')
    min_country, min_year = '', ''
    max_country, max_year = '', ''
    
    for line in data:
        parts = line.strip().split(',')
        country, year, life_expectancy = parts[0], parts[2], float(parts[3])
        
        if life_expectancy < min_life:
            min_life, min_country, min_year = life_expectancy, country, year
        
        if life_expectancy > max_life:
            max_life, max_country, max_year = life_expectancy, country, year
    
    return min_life, min_country, min_year, max_life, max_country, max_year

# Process data for a given year
def analyze_year(data, year_of_interest):
    total_life_expectancy = 0
    count = 0
    min_life = float('inf')
    max_life = float('-inf')
    min_country, max_country = '', ''
    
    for line in data:
        parts = line.strip().split(',')
        country, year, life_expectancy = parts[0], int(parts[2]), float(parts[3])
        
        if year == year_of_interest:
            total_life_expectancy += life_expectancy
            count += 1
            
            if life_expectancy < min_life:
                min_life, min_country = life_expectancy, country
            
            if life_expectancy > max_life:
                max_life, max_country = life_expectancy, country
    
    avg_life = total_life_expectancy / count if count > 0 else None
    return avg_life, min_life, min_country, max_life, max_country

# Find country-specific life expectancy stats
def analyze_country(data, country_of_interest):
    country_of_interest = country_of_interest.capitalize()
    min_life = float('inf')
    max_life = float('-inf')
    total_life = 0
    count = 0
    
    for line in data:
        parts = line.strip().split(',')
        country, life_expectancy = parts[0], float(parts[3])
        
        if country == country_of_interest:
            total_life += life_expectancy
            count += 1
            
            if life_expectancy < min_life:
                min_life = life_expectancy
            
            if life_expectancy > max_life:
                max_life = life_expectancy
    
    avg_life = total_life / count if count > 0 else None
    return avg_life, min_life, max_life

# Find the largest drop in life expectancy
def find_largest_drop(data):
    drops = {}
    
    for line in data:
        parts = line.strip().split(',')
        country, year, life_expectancy = parts[0], int(parts[2]), float(parts[3])
        
        if country not in drops:
            drops[country] = (year, life_expectancy)
        else:
            prev_year, prev_life = drops[country]
            drop = prev_life - life_expectancy
            if drop > drops.get('max_drop', (0, 0, 0))[2]:
                drops['max_drop'] = (country, prev_year, year, drop)
            drops[country] = (year, life_expectancy)
    
    return drops.get('max_drop', (None, None, None, None))

# Main function
def main():
    filename = 'life-expectancy.csv'
    data = load_data(filename)
    
    min_life, min_country, min_year, max_life, max_country, max_year = find_min_max_life_expectancy(data)
    print(f'The overall min life expectancy is: {min_life} from {min_country} in {min_year}')
    print(f'The overall max life expectancy is: {max_life} from {max_country} in {max_year}')
    
    year_of_interest = int(input('\nEnter the year of interest: '))
    avg_life, min_life, min_country, max_life, max_country = analyze_year(data, year_of_interest)
    
    if avg_life is not None:
        print(f'\nFor the year {year_of_interest}:')
        print(f'The average life expectancy across all countries was {avg_life:.2f}')
        print(f'The min life expectancy was in {min_country} with {min_life}')
        print(f'The max life expectancy was in {max_country} with {max_life}')
    else:
        print(f'No data available for the year {year_of_interest}.')
    
    while True:
        country_of_interest = input('\nEnter a country of interest: ').capitalize()
        avg_life, min_life, max_life = analyze_country(data, country_of_interest)
        
        if avg_life is not None:
            print(f'\nFor {country_of_interest}:')
            print(f'The average life expectancy was {avg_life:.2f}')
            print(f'The min life expectancy was {min_life}')
            print(f'The max life expectancy was {max_life}')
            break
        else:
            print(f'No data available for {country_of_interest}. Please try again.')
    
    country, prev_year, year, drop = find_largest_drop(data)
    print(f'\nThe largest decline in life expectancy was in {country}, dropping {drop:.2f} years from {prev_year} to {year}.')

  

# Run the program
if __name__ == '__main__':
    main()


input('\nPress Enter to exit...')
