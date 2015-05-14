import xlrd 

from preprocess_new import preprocess


#from preprocess_new import preprocess
def main():
    
    p=preprocess()
    #p=preprocess_new()
    #the name of the excel file
    book = xlrd.open_workbook("price.xlsx")
    words_filename=["price.txt"]
    labels_filename=["labels"]
    for i in range(1,2):
        worksheet = book.sheet_by_index(i)
        end_val=worksheet.nrows
        start_val=2
        
        
        
        #extract data and store it in file featurelist.txt
        p.extractdata(worksheet,start_val,end_val,words_filename[i-1],labels_filename[i-1])
        
main()

