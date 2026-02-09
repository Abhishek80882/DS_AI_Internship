#TASK 01
def calc_rectangle(length, width):
    area=length * width
    perimeter = 2*(length + width)
    return print(f'Area : {area}\nPerimeter : {perimeter}')
calc_rectangle(4,8)