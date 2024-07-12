def count_potions(inventory):
    count = 0
    for item in inventory:
        if item == "Healing potion":
            count += 1
    return count


def last_item(inventory):
    if len(inventory) <= 0:
        return None
    return inventory[len(inventory) - 1]


def attack_action():
    call(shoot_arrow())
    call(calc_new_health())


def shoot_arrow():
    call(calc_damage())


def calc_damage():
    call(apply_damage())


# don't touch below this line


def calc_new_health():
    pass


def apply_damage():
    pass


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


stack = Stack()


def call(func):
    stack.push(func.__name__)
    print("Pushing " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")
    func()
    stack.pop()
    print("Popping " + func.__name__)
    print("Stack: " + str(stack.items))
    print("=================================")


call(attack_action)


class PotionStack(Stack):
    def push(self, item):
        length = len(self.items)
        if length > 0 and self.items[length - 1] is item:
            return None
        else:
            self.items.append(item)
