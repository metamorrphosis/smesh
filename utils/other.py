def nc(arg: str) -> str:
    arg = arg[::-1]
    step, new_str = 0, ''

    for i in arg[::-1]:
        if step == 3:
            new_str += ','
            step = 0

        new_str += i
        s += 1
    
    return new_str[::-1]