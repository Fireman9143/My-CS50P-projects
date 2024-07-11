def main() -> None:
    total = 50
    while 0 < total <= 50:
        try:
            print(f"Amount Due: {total} ")
            amount:int = int(input(f"Insert Coin: "))
            total = total - coin_check(amount)
            if total <= 0:
                print(f"Change due: {total*-1}")
                break
        except ValueError:
            pass

def coin_check(value) -> int:
    match(value):
        case(5):
            return 5
        case(10):
            return 10
        case(25):
            return 25
        case(_):
            return 0

if __name__ == "__main__":
    main()