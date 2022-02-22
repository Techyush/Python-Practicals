def avg(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks) / len(marks)


mark2 = [55, 56, 58, 52, 50]
print("Average of marks2: ", avg(mark2))

mark1 = []
print("Average of marks1: ", avg(mark1))