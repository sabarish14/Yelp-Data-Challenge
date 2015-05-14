import csv


def compute_avg():
    business_id=open("business_id.txt","r").readlines()
    predicted=open("predicted_labels","r").readlines()
    actual=open("actual_labels","r").readlines()
    #fpl=open("sentiment_businessid.txt","w")
    for i in range(len(predicted)):
        predicted[i]=predicted[i].replace("\n","")
        business_id[i]=business_id[i].replace("\n","")
        actual[i]=actual[i].replace("\n","")
    business_id_label={}
    for b,p,a in zip(business_id,predicted,actual):
        try:
            temp_list=business_id_label[b]
            temp_list[0]+=float(p)
            temp_list[2]+=float(a)
            temp_list[1]+=1
            temp_list[3]+=1
            business_id_label[b]=temp_list
        except KeyError:
            count_p=1
            count_a=1
            p=float(p)
            a=float(a)
            temp_list=[p,count_p,a,count_a]
            business_id_label[b]=temp_list
            
            
    data=[]
    for key in business_id_label:
        temp_list=business_id_label[key]
        temp_list[0]=temp_list[0]/temp_list[1]
        temp_list[2]=temp_list[2]/temp_list[3]
        data.append([key,temp_list[0],temp_list[2]])
    with open('sentiment_business_id.csv', 'w') as fp:
                a = csv.writer(fp, delimiter=',')
                a.writerows(data)
        
        #fpl.write(key+"\t"+str(temp_list[0])+"\t"+str(temp_list[2])+"\n")
        
    
    