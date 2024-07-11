def main() -> None:
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and 2<=len(s)<=6 and s.isalnum() and check_nums(s):
        return True
    else:
        return False
    
def bug(s):
    if s[:2].isalpha() and s.isalnum() and check_nums(s):
        return True
    else:
        return False
    

def check_nums(chars):
    nums = []
    for num in chars[2:]:
        if num.isnumeric():
            nums.append(num)
        elif num.isalpha() and len(nums)>=1:
            return False
    if len(nums)>0 and nums[0] == "0":
        return False
    else:
        return True


if __name__ == "__main__":
    main()

"""
“Numbers cannot be used in the middle of a plate; they must come at the end. 
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""