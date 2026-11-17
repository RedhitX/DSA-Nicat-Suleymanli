from random import Random
from time import perf_counter_ns

from CustomDataStructures.CustomArray import Array, DynamicArray
from CustomDataStructures.CustomBST import BST
from CustomDataStructures.CustomHashTable import HashTable
from CustomDataStructures.CustomLinkedList import DoublyLinkedList, SinglyLinkedList
from CustomDataStructures.SQDQ import Deque, Queue, Stack


SIZES = (100, 1000, 10000)


def measure(operation, repeat=30):
    start = perf_counter_ns()
    for _ in range(repeat):
        operation()
    return (perf_counter_ns() - start) / repeat / 1000


def compare_sequences():
    print("\nMassivlər və əlaqəli siyahılar — orta vaxt (µs)")
    print(f"{'n':>6}  {'Struktur':<24} {'Əlavə + silmə':>15} {'Axtarış':>12}")
    for size in SIZES:
        array = Array(size + 1)
        dynamic = DynamicArray()
        singly = SinglyLinkedList()
        doubly = DoublyLinkedList()
        for index in range(size):
            array.append(index)
            dynamic.append(index)
            doubly.append(index)
            singly.prepend(size - index - 1)

        for name, items in (("Massiv", array), ("Dinamik massiv", dynamic)):
            def change_start():
                items.insert(0, -1)
                items.delete_at(0)

            print(f"{size:>6}  {name:<24} {measure(change_start):>15.2f}"
                  f" {measure(lambda: items.search(-1)):>12.2f}")

        for name, items in (("Tək əlaqəli siyahı", singly), ("İki əlaqəli siyahı", doubly)):
            def change_start():
                items.prepend(-1)
                items.delete_first()

            print(f"{size:>6}  {name:<24} {measure(change_start):>15.2f}"
                  f" {measure(lambda: items.search(-1)):>12.2f}")


def compare_queues():
    print("\nStack, Queue və Deque — bir əlavə və bir silmənin orta vaxtı (µs)")
    print(f"{'n':>6}  {'Stack':>12} {'Queue':>12} {'Deque':>12}")
    for size in SIZES:
        stack, queue, deque = Stack(), Queue(), Deque()
        for index in range(size):
            stack.push(index)
            queue.enqueue(index)
            deque.add_back(index)

        def stack_pair():
            stack.push(-1)
            stack.pop()

        def queue_pair():
            queue.enqueue(-1)
            queue.dequeue()

        def deque_pair():
            deque.add_back(-1)
            deque.remove_front()

        print(f"{size:>6}  {measure(stack_pair):>12.2f} {measure(queue_pair):>12.2f}"
              f" {measure(deque_pair):>12.2f}")


def undo_redo():
    undo, redo = Stack(), Stack()
    text = ""
    while True:
        print(f"\nMətn: {text!r}")
        choice = input("1. Yaz  2. Geri al  3. Bərpa et  0. Menyu\nSeçim: ").strip()
        if choice == "0":
            return
        if choice == "1":
            addition = input("Əlavə olunacaq mətn: ")
            undo.push(text)
            text += addition
            redo = Stack()
        elif choice == "2" and not undo.is_empty():
            redo.push(text)
            text = undo.pop()
        elif choice == "3" and not redo.is_empty():
            undo.push(text)
            text = redo.pop()
        elif choice in ("2", "3"):
            print("Bu əməliyyat üçün tarixçə boşdur.")
        else:
            print("Yanlış seçim.")


def print_jobs():
    queue = Queue()
    while True:
        print(f"\nÇap növbəsi: {queue.to_list()}")
        choice = input("1. Sənəd əlavə et  2. Növbətini çap et  0. Menyu\nSeçim: ").strip()
        if choice == "0":
            return
        if choice == "1":
            name = input("Sənədin adı: ").strip()
            if name:
                queue.enqueue(name)
            else:
                print("Sənədin adını daxil edin.")
        elif choice == "2":
            if queue.is_empty():
                print("Növbə boşdur.")
            else:
                print("Çap olundu:", queue.dequeue())
        else:
            print("Yanlış seçim.")


def recent_pages():
    history = Deque()
    while True:
        print(f"\nSon səhifələr (köhnədən yeniyə): {history.to_list()}")
        page = input("Səhifənin adı (menyuya qayıtmaq üçün 0): ").strip()
        if page == "0":
            return
        if page:
            if len(history) == 5:
                history.remove_front()
            history.add_back(page)


def hash_table_demo():
    print("\nHash Table — 1 və 4 eyni xanaya düşür")
    table = HashTable(capacity=3, max_load=1)
    table.put(1, "Alma")
    table.put(4, "Armud")
    table.show()
    print("Açar 4:", table.get(4))
    table.put(4, "Heyva")
    print("Yeniləndikdən sonra açar 4:", table.get(4))
    table.delete(1)
    print("Açar 1 cədvəldədir:", 1 in table)

    print("\nMövcud olmayan açarın axtarışı — orta vaxt (µs)")
    print(f"{'n':>6}  {'Hash Table':>12} {'Massiv':>12}")
    for size in SIZES:
        table = HashTable()
        items = Array(size)
        for index in range(size):
            table.put(index, index)
            items.append(index)
        print(f"{size:>6}  {measure(lambda: table.get(-1)):>12.2f}"
              f" {measure(lambda: items.search(-1)):>12.2f}")


def bst_demo():
    print("\nİkili axtarış ağacı")
    tree = BST()
    for key in (50, 30, 70, 20, 40, 60, 80):
        tree.insert(key)
    print("Sıralı keçid:", tree.inorder())
    print("60 tapıldı:", tree.search(60))
    tree.delete(50)
    print("50 silindikdən sonra:", tree.inorder())

    print("\nAğacın qurulma vaxtı (ms) və hündürlüyü")
    print(f"{'n':>6}  {'Əlavə etmə sırası':<18} {'Vaxt (ms)':>12} {'Hündürlük':>12}")
    random = Random(42)
    for size in SIZES:
        keys = list(range(size))
        random.shuffle(keys)
        for order, values in (("Qarışıq", keys), ("Artan", range(size))):
            tree = BST()
            start = perf_counter_ns()
            for key in values:
                tree.insert(key)
            elapsed_ms = (perf_counter_ns() - start) / 1_000_000
            print(f"{size:>6}  {order:<18} {elapsed_ms:>12.2f} {tree.height():>12}")


def main():
    options = {
        "1": ("Massivlər və əlaqəli siyahılar", compare_sequences),
        "2": ("Stack, Queue və Deque müqayisəsi", compare_queues),
        "3": ("Mətni geri al və bərpa et", undo_redo),
        "4": ("Çap növbəsi", print_jobs),
        "5": ("Son 5 səhifə", recent_pages),
        "6": ("Hash Table", hash_table_demo),
        "7": ("İkili axtarış ağacı", bst_demo),
    }
    while True:
        print("\nMəlumat strukturları | Nicat Süleymanlı")
        for key, (label, _) in options.items():
            print(f"{key}. {label}")
        print("0. Çıxış")
        choice = input("Seçim: ").strip()
        if choice == "0":
            return
        if choice in options:
            options[choice][1]()
        else:
            print("Yanlış seçim.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProqram bağlandı.")
