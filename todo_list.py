import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] #jika file tidak ada, mulai dengan daftar kosong
    
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas saat ini.")
        return
    print("\nDaftar Tugas:")
    for index, task in enumerate(tasks, start=1):
        status = "OK" if task["completed"] else "NOT"
        print(f"{index}. {task['task']} [{status}]")

def add_task(tasks):
    task_name = input("Masukkan nama tugas: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print(f"Tugas '{task_name}' berhasil ditambahkan!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Pilih nomor tugas yang sudah selesai: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Tugas '{tasks[task_num - 1]['task']}' berhasil ditandai selesai!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Pilih nomor tugas yang akan dihapus: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Tugas '{removed_task['task']} berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def menu():
    print("\n=== Todo List ===")
    print("1. Lihat semua tugas")
    print("2. Tambah tugas baru")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Keluar")
    return input("Pilih menu (1-5): ")

def main():
    tasks = load_tasks()
    while True:
        choice = menu()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tugas berhasil disimpan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()