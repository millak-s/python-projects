from csv import writer


def csv(path, lst):
    with open(path, "w", newline="") as f:
        if len(lst) <= 0:
            return

        the_writer = writer(f)
        the_writer.writerow(lst[0].keys())

        for dic in lst:
            line = [k for k in dic.values()]
            the_writer.writerow(line)
