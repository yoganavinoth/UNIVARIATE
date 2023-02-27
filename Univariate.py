class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtypes=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                 quan.append(columnName)
        return quan,qual
