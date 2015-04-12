from file_read import file_read

class restaurant:
    id={}
    reviews=[]
    list_id=[]
    def __init__(self,filename):
        review_col=3
        
        id_col=1
        self.reviews=file_read(filename,review_col)
        self.list_id=file_read(filename,id_col)
        id_count=0
        for l in self.list_id:
            if l not in self.id.keys():
                self.id[l]=id_count
                id_count+=1
    def group_review(self):
        new_reviews=['' for i in range(len(self.id.keys()))]
        for lines,n in zip(self.reviews,self.list_id):
            #print "id:",self.id[n]
            str=new_reviews[self.id[n]]
            str+=lines
            new_reviews[self.id[n]]=str
        self.reviews=new_reviews
    
            
            
            
                
                
        
        