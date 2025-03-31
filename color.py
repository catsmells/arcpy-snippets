def is_primary(c): return c[:3].count(256) == 1 and c[:3].count(0) == 2
def is_secondary(c): return c[:3].count(256) == 2 and c[:3].count(0) == 1
def main():
    while (r := input("Enter RGB: ")) != 'q':
        try:
            c = tuple(map(int, (r.split() + ['256'])[:4]))
            print(f"\rRGB{c} is " + ("Primary." if is_primary(c) else "Secondary." if is_secondary(c) else "Neither."))
        except ValueError: print("\rInvalid input.")
    print("\rAborted.")
if __name__ == "__main__": main()
