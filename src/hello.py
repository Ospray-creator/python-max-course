def main():
    name = input("Как тебя зовут? ")
    greeting = f"Привет, {name}!"
    print(greeting)

    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write(greeting)


if __name__ == "__main__":
    main()
