"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false."""

def validate_pin(pin):
    chars = list(pin)
    digits = 0
    if len(chars) == 4 or len(chars) == 6:
        for char in chars:
            if char.isdigit():
                if int(char) >= 0:
                    digits += 1
    else:
        return False
    return digits == 4 or digits == 6
