import random

def main():
    level=get_level()
    score=0
    for i in range(0,10):
        x,y,z=generate_integer(level)
        attempts = 2
        while attempts >=0:
            try:
                answer=int(input(f"{x} + {y} = "))
                if answer == z:
                    score+=1
                    break
                elif answer!= z and attempts>0:
                    attempts-=1
                    raise ValueError
                elif answer != z and attempts==0:
                    print(f"{x} + {y} = {z}")
                    break
            except ValueError:
                print("EEE")
    print(f"Score: {score}")

def get_level()->int:
    while True:
        try:
            level=int(input("Level: "))
            if level in range(1,4):
                return level
                break
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level)->list:
    if level == 1:
        x=random.randrange(0,9)
        y=random.randrange(0,9)
    elif level == 2:
        x=random.randrange(10,99)
        y=random.randrange(10, 99)
    elif level == 3:
        x=random.randrange(100,999)
        y=random.randrange(100,999)
    z=x+y
    return x,y,z
        


if __name__ == "__main__":
    main()