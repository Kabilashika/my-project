def main():
    print("Welcome to the Main Program!")
    print("This program demonstrates basic print commands and function calls.")

    # Call functions from other modules
    from car import car_info
    from animals import animal_info
    from programs import program_info

    car_info()
    animal_info()
    program_info()

if __name__ == "__main__":
    main()