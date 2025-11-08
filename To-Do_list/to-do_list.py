#Created a to do list using python. 

def main():
    tasks=[]
    while True:
        print("\n\t===To-Do List===")
        print("""
        1. Add Task
        2. Show Tasks
        3. Mark task as done
        4. Exit """)

        choice= int(input("Enter your choice: "))
        if choice == 1:
            print()
            n_tasks = int(input("How may task you want to add: "))
            for i in range(n_tasks):
                task= input("Enter the task: ")
                tasks.append({'task': task, 'done': False})
                print("Task Done")
        
        elif choice ==2:
            print("\n TASKS:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
        
        elif choice == 3:
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice ==4:
            print("Exiting to-do list. Thank You!")
            break
        else:
            print("Inalid Choice, Please Try Again..")
            








if __name__ == "__main__":
    main()
