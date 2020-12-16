
def calc_dog_age(dog_age):
    """
    @desc Function to calculate dog's age in dog's years
    @param human_years: dog's age in terms of human years
    @return dog age in terms of dog's years
    """
    if dog_age<=2:
        return dog_age * 10.5
    return (2*10.5) + (dog_age - 2) * 4
    