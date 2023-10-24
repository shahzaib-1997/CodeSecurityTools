from datetime import datetime, timedelta, time

def convert_in_seconds(t):
    t_in_seconds = t.hour * 3600 + t.minute * 60 + t.second
    return t_in_seconds


# Dictionary to store user attendance
attendance = {}

# Function to calculate attendance status based on time_in and time_out
def attendance_on_time_in(time_in):
    try:
        # Convert time_in and time_out to datetime objects
        time_in = datetime.strptime(time_in, "%H:%M")

        # Define time thresholds
        late_threshold = datetime.strptime("12:30", "%H:%M")
        
        if time_in <= late_threshold:
                return "present"
        elif time_in > late_threshold:
            return "late"
        else:
            return "absent"
    except ValueError:
        return "Invalid input format"

def attendance_on_time_out(time_in, time_out):
    try:
        # Convert time_in and time_out to datetime objects
        time_in = datetime.strptime(time_in, "%H:%M")
        time_out = datetime.strptime(time_out, "%H:%M")

        time_out_seconds = convert_in_seconds(time_out)
        time_in_seconds = convert_in_seconds(time_in)
        result_seconds = time_out_seconds - time_in_seconds
        hours, remainder = divmod(result_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_duration = time(hours, minutes, seconds)
        
        # Define time thresholds
        late_threshold = datetime.strptime("12:30", "%H:%M")
        short_threshold = time(hour=6)
        half_day_threshold = time(hour=4)
        print(time_duration)

        if time_duration < half_day_threshold:
            return "absent"
        elif time_duration < short_threshold:
            return "half day"
        elif time_in > late_threshold:
            return "late and short"
        else:
            return "short"

    except ValueError:
        return "Invalid input format"

if __name__ == '__main__':     
    # Main program loop
    while True:
        print("\nOptions:")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            user = input("Enter user name: ")
            time_in = input("Enter time_in (HH:MM): ")
            status = attendance_on_time_in(time_in)
            attendance[user] = [status, time_in]
            print(f"{user}'s attendance status after time in: {status}")
            time_out = input("Enter time_out (HH:MM): ")
            attendance[user].append(time_out)
            new_status = attendance_on_time_out(time_in, time_out)
            if new_status:
                status = new_status
            attendance[user][0]= status
            print(f"{user}'s attendance status after time out: {status}")
        elif choice == '2':
            print("\nUser Attendance:")
            for user, status in attendance.items():
                print(f"{user}: {status}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")