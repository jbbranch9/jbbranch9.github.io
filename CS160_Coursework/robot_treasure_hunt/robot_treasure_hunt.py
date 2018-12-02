import random

def algorithm_one(energy_position, zb_position, zb_movement):
    zb_direction = 1
    total_movement_algorithm_one = 0
    while zb_position != energy_position:
        zb_position += (zb_movement * zb_direction)
        total_movement_algorithm_one += zb_movement
        zb_direction = -(zb_direction)
        zb_movement += 1  
    return total_movement_algorithm_one
        
def algorithm_two_positive_first(energy_position, zb_position, zb_movement):
    zb_direction = 1
    total_movement_algorithm_two = 0
    while zb_position != energy_position:
        zb_position += zb_direction
        total_movement_algorithm_two += zb_movement
        if zb_position == -1000 or zb_position == 1000:
            zb_direction = -(zb_direction)      
    return total_movement_algorithm_two

def algorithm_two_negative_first(energy_position, zb_position, zb_movement):
    zb_direction = -1
    total_movement_algorithm_two = 0
    while zb_position != energy_position:
        zb_position += zb_direction
        total_movement_algorithm_two += zb_movement
        if zb_position == -1000 or zb_position == 1000:
            zb_direction = -(zb_direction)      
    return total_movement_algorithm_two

def main():
    algorith_one_list = []
    algorith_two_list = []
    for i in range(-1000, 1001):
        #initial values, units in meters
        energy_position = i
        zb_movement = 1
        zb_position = 0
        
        total_movement_algorithm_one = algorithm_one(energy_position, zb_position, zb_movement)
        
        total_movement_algorithm_two_positive_first = algorithm_two_positive_first(energy_position, zb_position, zb_movement)
        total_movement_algorithm_two_negative_first = algorithm_two_negative_first(energy_position, zb_position, zb_movement)
        
        total_movement_algorithm_two = int(.5 * (total_movement_algorithm_two_positive_first + total_movement_algorithm_two_negative_first))
        
        print("Energy position:", energy_position, "m", "   Algorithm One:", total_movement_algorithm_one, "m", "   Algorithm Two*", total_movement_algorithm_two, "m", "   *average rounded to nearest meter")
        
        algorith_one_list.append(total_movement_algorithm_one)
        algorith_two_list.append(total_movement_algorithm_two)
    
    print(algorith_one_list)
    print(algorith_two_list)
    
main()
