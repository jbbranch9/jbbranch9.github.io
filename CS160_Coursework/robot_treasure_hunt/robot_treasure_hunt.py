def algorithm_one(energy_position, zb_position, zb_movement, zb_direction):
    total_movement_algorithm_one = 0
    while zb_position != energy_position:
        for i in range (zb_movement):
            zb_position += (zb_direction)
            total_movement_algorithm_one += zb_movement
            if zb_position == energy_position:
                break
        if zb_position == energy_position:
            break
        zb_direction = -(zb_direction)
        zb_movement += 250  
    return total_movement_algorithm_one

def algorithm_two(energy_position, zb_position, zb_movement, zb_direction):
    total_movement_algorithm_two = 0
    while zb_position != energy_position:
        for i in range (zb_movement):
            zb_position += (zb_direction)
            total_movement_algorithm_two += zb_movement
            if zb_position == energy_position:
                break
        if zb_position == energy_position:
            break
        zb_direction = -(zb_direction)
        zb_movement += 500  
    return total_movement_algorithm_two

def main():
    algorith_one_list = []
    algorith_two_list = []
    for i in range(-1000, 1001):
        total_movement_algorithm_one = algorithm_one(i, 0, 250, 1)
        total_movement_algorithm_two = algorithm_two(i, 0, 500, 1)

        print("Energy position:", i, "m", "   Algorithm One:", total_movement_algorithm_one, "m", "   Algorithm Two", total_movement_algorithm_two, "m")
        
        algorith_one_list.append(total_movement_algorithm_one)
        algorith_two_list.append(total_movement_algorithm_two)
    
    print(algorith_one_list)
    print(algorith_two_list)
    
main()
input()