import csv


def file_read(filename,col):
    with open(filename, 'rb') as f:
        
        #row_count = sum(1 for row1 in reader)
        reviews=[]
        
        reader = csv.reader(f)
        for row in reader:
            #print row[3]
            reviews.append( row[col])
        #reviews=reviews[1:100]
            
    return reviews
            
def file_read_text(filename):
    f=open(filename)
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].replace("\n", "")  
    return lines
def write_tuple(lines,filename):
    with open(filename, "w") as the_file:
        csv.register_dialect("custom", delimiter=" ", skipinitialspace=True)
        writer = csv.writer(the_file, dialect="custom")
        for tuples in lines:
            for tup in tuples:
                for str in tup:
                    writer.write(tup)