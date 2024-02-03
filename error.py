def perform_integer_division(a, b):
    try:
        result = a // b
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        try:
            a, b = map(int, input().split())
            result = a // b
            print(result)
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code:", e)
