import pandas as pd

class PandasDataProcess:
    def __init__(self,offset_number=0):
        self.dataframe=None
        self.offset=offset_number
        
    # uploading file into memory
    def upload_file_csv(self,file_path):
        try:
            self.dataframe=pd.read_csv(file_path)
            print(f"Successfully read the file:{file_path}")
        except Exception as e:
            print(f"Failed to read the file :{e}")

    # computing maximum number in each column
    # offest_number: the start index of the columns to read
    def compute_max(self):
        if(self.dataframe is not None):
            column_titles=self.dataframe.columns[self.offset:] # get column name
            result= self.dataframe[column_titles].max() 
            print(f"Successfully found the maximum:{result}")
            return result
        else:
            print("Please use function 'upload_file_csv' to read data first!")
            
    # computing minimum number in each column
    def compute_min(self):
        if(self.dataframe is not None):
            column_titles=self.dataframe.columns[self.offset:] # get column name
            result= self.dataframe[column_titles].min()
            print(f"Successfully found the minimum:{result}")
            return result
        else:
            print("Please use function 'upload_file_csv' to read data first!")

    # computing average number in each column
    def compute_avg(self):
        if(self.dataframe is not None):
            column_titles=self.dataframe.columns[self.offset:] 
            result= self.dataframe[column_titles].mean()
            print(f"Successfully found the average :{result}")
            return result
        else:
            print("Please use function 'upload_file_csv' to read data first!")
    
    # computing absolute number in each column
    def compute_abs(self):
        if(self.dataframe is not None):
            column_titles=self.dataframe.columns[self.offset:]
            result= self.dataframe[column_titles].abs()
            print(f"Successfully found the absolute :{result}")
            return result
        else:
            print("Please use function 'upload_file_csv' to read data first!")
    
    # convert large datasets into Parquet format
    def save_parquet(self):
        if(self.dataframe is not None):
            self.dataframe.to_parquet("output.parquet",engine="pyarrow",index=False)
            print(f"Data successfully saved to Parquet : output.parquet")
        else:
            print("Please use function 'upload_file_csv' to read data first!")

if __name__=="__main__":

    # read CSV (PIR:Passive Infrared Sensor)
    path="database/pirvision_office_dataset1.csv"
    pdp = PandasDataProcess(3)
    pdp.upload_file_csv(path)

    pdp.save_parquet()

    pdmax= pdp.compute_max()
    pdmin= pdp.compute_min()
    pdavg= pdp.compute_avg()
    pdabs=pdp.compute_abs()

    # show value in one dataframe
    stats = pd.DataFrame({
                "max": pdmax,
                "min": pdmin,
                "mean": pdavg,
                "abs_max": pdabs.max(numeric_only=True)
            })
    
    print(stats)