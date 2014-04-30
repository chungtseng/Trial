import csv
out = []
with open('/home/ycz/Rotation_linkage/passed/Widom Panel 1A Plate 1 2012-10-15.csv', 'rb') as trial_data:
    trial_reader = csv.reader(trial_data, dialect = 'excel')
    for ind,row in enumerate(trial_reader):
        if ind <= 30:
            out.append(row)
out.append('this is the end')
with open('/home/ycz/test_out.csv', 'wb+') as trial_out:
    trial_writer = csv.writer(trial_out, dialect = 'excel')
    trial_writer.writerows(out)
    
