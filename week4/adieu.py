import inflect
p=inflect.engine()
names=[]   

def main():
    while True:
        try:
            name=input("Name: ")
            names.append(name)
        except EOFError:
            mylist=p.join(names)
            print(f" Adieu, adieu to {mylist}")
            break


if __name__ == "__main__":
    main()
    """Run your program with python adieu.py. Type Liesl and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl 
Run your program with python adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl and Friedrich
Run your program with python adieu.py. Type Liesl and press Enter, then type Friedrich and press Enter. Now type Louisa and press Enter, followed by control-d. Your program should output:
Adieu, adieu, to Liesl, Friedrich, and Louisa"""