import csv


def get_banch():
    date = input("Дата в формате yyyy-mm-dd [all]:")
    name = input("Тикер [all]:")
    filname = input("Файл [dump.csv]:")
    if filname == "":
        filname = "dump.csv"
    return get_by_date(date, name, filname)


def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    n = "".join(name)
    dat = "".join(date)
    f_n = "".join(filename)
    f = open("all_stocks_5yr.csv", "r", encoding="utf-8")
    reader = csv.DictReader(f, delimiter=',', quotechar='|')

    if dat == "" or n == "":
        top10 = sorted((d for d in reader if d["Name"] == n or d["date"] == dat), key=lambda x: float(x["high"] or 0),
                       reverse=True)
    else:
        top10 = sorted((d for d in reader if d["Name"] == n and d["date"] == dat), key=lambda x: float(x["high"] or 0),
                       reverse=True)

    for row in top10:
        print(f"{row['date']}|{row['open']}|{row['high']}|{row['low']}|{row['close']}|{row['volume']}|{row['Name']}")

        """Запись в файл"""
    f = open(f_n, "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(f, fieldnames=list(top10[0].keys()), delimiter=",", quoting=csv.QUOTE_NONE)
    writer.writeheader()
    for i in top10:
        writer.writerow(i)

    return top10, f.close()
