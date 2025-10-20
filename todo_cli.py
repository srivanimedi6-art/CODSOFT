import json, os, datetime

FNAME = "tasks.json"

def load_tasks():
    if os.path.exists(FNAME):
        try:
            return json.load(open(FNAME, "r", encoding="utf-8"))
        except:
            return []
    return []

def save_tasks(tasks):
    json.dump(tasks, open(FNAME, "w", encoding="utf-8"), indent=2)

def new_id(tasks):
    return max([t["id"] for t in tasks], default=0) + 1

def add_task(tasks):
    title = input("Enter task title: ")
    desc = input("Enter description (optional): ")
    due = input("Enter due date (YYYY-MM-DD, optional): ")
    task = {
        "id": new_id(tasks),
        "title": title,
        "desc": desc,
        "due": due,
        "done": False,
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for t in tasks:
        mark = "✔" if t["done"] else "✖"
        print(f"{t['id']}. [{mark}] {t['title']} (Due: {t['due']})")

def toggle_done(tasks):
    try:
        tid = int(input("Enter task ID to mark done/undone: "))
    except:
        print("Invalid ID"); return
    for t in tasks:
        if t["id"] == tid:
            t["done"] = not t["done"]
            save_tasks(tasks)
            print("Status updated!")
            return
    print("Task not found.")

def delete_task(tasks):
    try:
        tid = int(input("Enter task ID to delete: "))
    except:
        print("Invalid ID"); return
    for t in tasks:
        if t["id"] == tid:
            tasks.remove(t)
            save_tasks(tasks)
            print("Deleted!")
            return
    print("Task not found.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks\n2. Add task\n3. Mark done/undone\n4. Delete task\n5. Exit")
        ch = input("Choose: ")
        if ch == "1": list_tasks(tasks)
        elif ch == "2": add_task(tasks)
        elif ch == "3": toggle_done(tasks)
        elif ch == "4": delete_task(tasks)
        elif ch == "5":
            print("Goodbye!"); break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()