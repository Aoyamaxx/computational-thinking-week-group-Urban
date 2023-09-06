def solution_station_4(input):
    if input > 1:
        for i in range(2, int(input/2)+1):
            if (input % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False