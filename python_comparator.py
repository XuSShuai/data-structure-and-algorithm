from operator import attrgetter


class Person:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return "%s %d %d" % (self.name, self.age, self.salary)


if __name__ == "__main__":
    data = [["Rms", 100, 20], ["Adam", 50, 30], ["Moment", 100, 10]]
    person = [Person(x[0], x[1], x[2]) for x in data]

    person.sort(key=lambda obj: obj.age)
    for x in person:
        print(x)

    print()
    person.sort(key=attrgetter("age", "salary"))
    for x in person:
        print(x)
