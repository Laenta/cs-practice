def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = []
        for p in line.split(","):
            parts.append(p.strip())

        if header is None:
            header = parts
        elif len(parts) == len(header):
            row = {}
            for i in range(len(header)):
                row[header[i]] = parts[i]
            rows.append(row)

    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1
    return counts


def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            value = row["минуты"].replace(",", ".")
            try:
                total += float(value)
            except ValueError:
                pass
    return round(total, 1)


def to_csv(counts):
    text = "тип,количество\n"
    for kind in sorted(counts):
        text += kind + "," + str(counts[kind]) + "\n"
    return text