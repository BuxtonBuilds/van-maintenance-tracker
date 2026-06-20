record_file = "maintenance.txt"

print("=== Van Maintenance Tracker ===")

while True:

    print()
    print("1 - Add maintenance record")
    print("2 - View maintenance records")
    print("3 - Show total maintenance cost")
    print("4 - Search maintenance records")
    print("5 - Quit")

    choice = input("> ")

    if choice == "1":

        date = input("Date: ")
        mileage = input("Mileage: ")
        work = input("Work completed: ")
        cost = input("Cost: ")

        with open(record_file, "a", encoding="utf-8") as file:
            file.write(f"Date: {date}\n")
            file.write(f"Mileage: {mileage}\n")
            file.write(f"Work: {work}\n")
            file.write(f"Cost: {cost}\n")
            file.write("--------------------\n")

        print("Record saved.")

    elif choice == "2":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                records = file.read()

            print()
            print("Maintenance Records")
            print("-------------------")
            print(records)

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "3":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                lines = file.readlines()

            total = 0.0

            for line in lines:
                if line.startswith("Cost:"):
                    cost_text = line.replace("Cost:", "").strip()
                    total += float(cost_text)

            print()
            print("Total maintenance cost:")
            print(f"£{total:.2f}")

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "4":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                records = file.read()

            keyword = input("Search keyword: ").lower()
            record_list = records.split("--------------------")

            matches = []

            for record in record_list:
                if keyword in record.lower() and record.strip():
                    matches.append(record.strip())

            print()
            print("Matches found:", len(matches))

            for match in matches:
                print()
                print("--------------------")
                print(match)

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "5":

        print("Goodbye.")
        break

    else:

        print("Option not built yet.")