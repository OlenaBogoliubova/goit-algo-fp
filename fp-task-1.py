class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None

        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("Зв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("Шукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Реверсуємо зв'язний список
llist.reverse()

print("Зв'язний список після реверсу:")
llist.print_list()

# Вставляємо вузли в довільному порядку
llist.insert_at_end(20)
llist.insert_at_beginning(5)
llist.insert_at_end(25)
llist.insert_at_beginning(10)
llist.insert_at_end(15)

print("Зв'язний список до сортування:")
llist.print_list()

# Сортуємо зв'язний список за допомогою алгоритму сортування вставками
llist.insertion_sort()

print("Зв'язний список після сортування:")
llist.print_list()

# Приклад використання:
list1 = LinkedList()
list1.insert_at_end(5)
list1.insert_at_end(5)
list1.insert_at_end(10)
list1.insert_at_end(15)
list1.insert_at_end(15)
list1.insert_at_end(20)
list1.insert_at_end(20)
list1.insert_at_end(25)
list1.insert_at_end(25)

list2 = LinkedList()
list2.insert_at_end(7)
list2.insert_at_end(12)
list2.insert_at_end(20)

print("Перший відсортований список:")
list1.print_list()

print("Другий відсортований список:")
list2.print_list()

# Об'єднуємо два відсортовані списки
merged_list = list1.merge_sorted_lists(list2)

print("Відсортований список після об'єднання:")
merged_list.print_list()
