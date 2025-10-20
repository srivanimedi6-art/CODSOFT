# calculator.py
def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            # allow floats and ints
            return float(s) if ('.' in s or 'e' in s.lower()) else int(s)
        except:
            print("Invalid number. Try again.")

def menu():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (a^b)")
    print("6. Modulo (a % b)")
    print("7. Exit")

def add(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
    if b == 0:
        return None
    return a / b
def power(a,b): return a ** b
def mod(a,b):
    if b == 0:
        return None
    return a % b

def main():
    while True:
        menu()
        choice = input("Choose option (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        if choice not in {"1","2","3","4","5","6"}:
            print("Invalid choice.")
            continue
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        if choice == "1":
            print("Result:", add(a,b))
        elif choice == "2":
            print("Result:", sub(a,b))
        elif choice == "3":
            print("Result:", mul(a,b))
        elif choice == "4":
            r = div(a,b)
            print("Cannot divide by zero." if r is None else f"Result: {r}")
        elif choice == "5":
            print("Result:", power(a,b))
        elif choice == "6":
            r = mod(a,b)
            print("Cannot modulo by zero." if r is None else f"Result: {r}")

if __name__ == "__main__":
    main()