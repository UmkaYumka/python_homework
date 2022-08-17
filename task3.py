with open("task3.txt",  encoding="utf-8") as f:
    emp_dict= {line.split()[0]: float (line.split()[1]) for line in f}
    print(f"Average salary = {round(sum(emp_dict.values())/len(emp_dict), 3)}\n"
          f"Employees with salary less than 20k {[e[0] for e in emp_dict.items() if e[1]<20000]}")
