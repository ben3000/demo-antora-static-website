import csv
import uuid

print("Hello, CI/CD")

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["uuid", "name_id", "name1", "name2", "author"])
    writer.writerow([uuid.uuid4(), 1800, "Banksia", "attenuata", "R.Br."])
    writer.writerow([uuid.uuid4(), 21316, "Banksia", None, "L.f."])
    writer.writerow([uuid.uuid4(), 22793, "Proteaceae", None, "Juss."])
