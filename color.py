def is_primary(c): 
    return c[:3].count(256) == 1 and c[:3].count(0) == 2
def is_secondary(c): 
    return c[:3].count(256) == 2 and c[:3].count(0) == 1

def check_value(r: str):
    try:
        c = [int(i) for i in (r.split() + ['256'])[:4]]
        print(f"\rRGB{c} is {'Primary.'*is_primary(c) + 'Secondary.'*is_secondary(c) or 'Neither.'}")
    except ValueError:
        print("\rInvalid input.")
    
    
if __name__ == "__main__":
    while (r := input("Enter RGB: ")) != 'q':
        check_value(r)
    print("\rAborted.")