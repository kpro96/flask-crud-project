from datetime import datetime 

def write_diary():
    entry = input("write your diary entry for today:\n")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("my_diary.txt", "a") as file:
        file.write(f"---{current_time}---\n")
        file.write(entry + "\n\n")
    print("Entry saved successfully!")
write_diary()    
   