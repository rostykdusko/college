class Person:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def display_info(self):
        print(f"{self.name} належить до групи {self.group}")

if __name__ == "__main__":
    person1 = Person(name="Ігор", group="ТК-42")
    person2 = Person(name="крута", group="ТК-42")
    person3 = Person(name="людина", group="ТК-42")

    person1.display_info()
    person2.display_info()
    person3.display_info()