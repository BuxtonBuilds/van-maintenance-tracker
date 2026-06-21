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
    print("7 - Edit record")
    print("8 - Delete record")
    print("9 - Service reminder dashboard")
    print("10 - Quit")

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

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                content = file.read()

            record_list = [
                record for record in content.split("--------------------")
                if record.strip()
            ]

            if not record_list:
                print("No maintenance records found.")
            else:
                print()
                print("Maintenance Records")
                print("-------------------")

                for index, record in enumerate(record_list, start=1):
                    lines = record.strip().split("\n")
                    summary = ", ".join(lines)
                    print(f"{index} - {summary}")

                selected = input("Select record number to edit: ")

                try:
                    selected_index = int(selected) - 1
                    selected_record = record_list[selected_index]
                except (ValueError, IndexError):
                    selected_record = None
                    print("Invalid record number.")

                if selected_record is not None:
                    current_date = ""
                    current_mileage = ""
                    current_work = ""
                    current_cost = ""

                    for line in selected_record.strip().split("\n"):
                        if line.startswith("Date:"):
                            current_date = line.replace("Date:", "").strip()
                        elif line.startswith("Mileage:"):
                            current_mileage = line.replace("Mileage:", "").strip()
                        elif line.startswith("Work:"):
                            current_work = line.replace("Work:", "").strip()
                        elif line.startswith("Cost:"):
                            current_cost = line.replace("Cost:", "").strip()

                    print()
                    print("Leave blank to keep the current value.")

                    new_date = input(f"Date [{current_date}]: ").strip()
                    new_mileage = input(f"Mileage [{current_mileage}]: ").strip()
                    new_work = input(f"Work completed [{current_work}]: ").strip()
                    new_cost = input(f"Cost [{current_cost}]: ").strip()

                    updated_record = (
                        f"Date: {new_date if new_date else current_date}\n"
                        f"Mileage: {new_mileage if new_mileage else current_mileage}\n"
                        f"Work: {new_work if new_work else current_work}\n"
                        f"Cost: {new_cost if new_cost else current_cost}\n"
                    )

                    record_list[selected_index] = updated_record

                    with open(record_file, "w", encoding="utf-8") as file:
                        for record in record_list:
                            file.write(record.strip() + "\n")
                            file.write("--------------------\n")

                    print()
                    print("Record updated.")

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "8":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                content = file.read()

            record_list = [
                record for record in content.split("--------------------")
                if record.strip()
            ]

            if not record_list:
                print("No maintenance records found.")
            else:
                print()
                print("Maintenance Records")
                print("-------------------")

                for index, record in enumerate(record_list, start=1):
                    lines = record.strip().split("\n")
                    summary = ", ".join(lines)
                    print(f"{index} - {summary}")

                selected = input("Select record number to delete: ")

                try:
                    selected_index = int(selected) - 1
                    selected_record = record_list[selected_index]
                except (ValueError, IndexError):
                    selected_record = None
                    print("Invalid record number.")

                if selected_record is not None:
                    print()
                    print(selected_record.strip())
                    confirm = input("Delete this record? (y/n): ").strip().lower()

                    if confirm == "y":
                        del record_list[selected_index]

                        with open(record_file, "w", encoding="utf-8") as file:
                            for record in record_list:
                                file.write(record.strip() + "\n")
                                file.write("--------------------\n")

                        print()
                        print("Record deleted.")
                    else:
                        print("Delete cancelled.")

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "9":

        try:
            with open(record_file, "r", encoding="utf-8") as file:
                content = file.read()

            record_list = [
                record for record in content.split("--------------------")
                if record.strip()
            ]

            service_mileage = None

            for record in record_list:
                work = ""
                mileage = ""

                for line in record.strip().split("\n"):
                    if line.startswith("Work:"):
                        work = line.replace("Work:", "").strip()
                    elif line.startswith("Mileage:"):
                        mileage = line.replace("Mileage:", "").strip()

                if "service" in work.lower() and mileage:
                    mileage_value = int(mileage)

                    if service_mileage is None or mileage_value > service_mileage:
                        service_mileage = mileage_value

            if service_mileage is None:
                print("No service record exists yet.")
            else:
                current_mileage = input("Current mileage: ")
                service_interval = input("Service interval miles: ")

                next_service_due = service_mileage + int(service_interval)
                miles_remaining = next_service_due - int(current_mileage)

                if miles_remaining <= 0:
                    status = "Service is due now."
                elif miles_remaining <= 1000:
                    status = "Service is coming up soon."
                else:
                    status = "Service is not due yet."

                print()
                print("Service Reminder Dashboard")
                print("---------------------------")
                print(f"Last service mileage: {service_mileage} miles")
                print(f"Current mileage: {current_mileage} miles")
                print(f"Service interval: {service_interval} miles")
                print(f"Next service due: {next_service_due} miles")
                print(f"Miles remaining: {miles_remaining} miles")
                print(f"Status: {status}")

        except FileNotFoundError:
            print("No maintenance records found.")

    elif choice == "10":

        print("Goodbye.")
        break

    else:

        print("Option not built yet.")