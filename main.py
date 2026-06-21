import csv

record_file = "maintenance.txt"
csv_file_name = "maintenance.csv"

print("=== Van Maintenance Tracker ===")

while True:

    print()
    print("1 - Add maintenance record")
    print("2 - View maintenance records")
    print("3 - Show total maintenance cost")
    print("4 - Search maintenance records")
    print("5 - Next service due")
    print("6 - Export records to CSV")
    print("7 - Quit")

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

        last_service_mileage = input("Last service mileage: ")
        current_mileage = input("Current mileage: ")
        service_interval = input("Service interval miles: ")

        next_service_due = int(last_service_mileage) + int(service_interval)
        miles_remaining = next_service_due - int(current_mileage)

        print()
        print("Next service due:")
        print(f"{next_service_due} miles")
        print()
        print("Miles remaining:")
        print(f"{miles_remaining} miles")

        if miles_remaining <= 0:
            print("Service is due now.")
        elif miles_remaining <= 1000:
            print("Service is coming up soon.")
        else:
            print("Service is not due yet.")

    elif choice == "6":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                content = file.read()

            record_list = [
                record for record in content.split("--------------------")
                if record.strip()
            ]

            with open(csv_file_name, "w", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Date", "Mileage", "Work", "Cost"])

                for record in record_list:
                    date = ""
                    mileage = ""
                    work = ""
                    cost = ""

                    for line in record.strip().split("\n"):
                        if line.startswith("Date:"):
                            date = line.replace("Date:", "").strip()
                        elif line.startswith("Mileage:"):
                            mileage = line.replace("Mileage:", "").strip()
                        elif line.startswith("Work:"):
                            work = line.replace("Work:", "").strip()
                        elif line.startswith("Cost:"):
                            cost = line.replace("Cost:", "").strip()

                    writer.writerow([date, mileage, work, cost])

            print()
            print(f"Export complete: {csv_file_name}")

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "7":

        print("Goodbye.")
        break

    else:

        print("Option not built yet.")