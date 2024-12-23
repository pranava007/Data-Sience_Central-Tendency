class Univariend():
    def Qualquan(dataset):
        quan =[]
        qual =[]
        for columns in dataset:
            # print(columns)
            if(dataset[columns].dtype == 'O'):
                qual.append(columns)
            else:
                quan.append(columns)
        return quan,qual