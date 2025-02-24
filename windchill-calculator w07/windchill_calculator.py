def calculate_wind_chill(temperature_f, wind_speed):
    """Calculates the wind chill based on the temperature in Fahrenheit and wind speed in mph."""
    return 35.74 + (0.6215 * temperature_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature_f * (wind_speed ** 0.16))


def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def get_valid_temperature():
    """Gets a valid temperature input from the user."""
    while True:
        try:
            return float(input("What is the temperature? "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def get_temperature_unit():
    """Gets a valid temperature unit (F or C) from the user."""
    while True:
        unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
        if unit in ["F", "C"]:
            return unit
        print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


def main():
    """Main function to run the wind chill calculator."""
    temperature = get_valid_temperature()
    unit = get_temperature_unit()
    
    if unit == "C":
        temperature = celsius_to_fahrenheit(temperature)
    
    print(f"\nAt temperature {temperature:.2f}°F:")
    for wind_speed in range(5, 65, 5):  # Loop through wind speeds from 5 to 60 mph
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}°F")
    
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
