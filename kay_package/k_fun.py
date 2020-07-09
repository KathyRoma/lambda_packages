import math
import re
import pandas

class Kfun:
    def __init__(self, df, colnames):
        ''' Constructor for this class '''
        self.dataframe = df
        self.colnames = colnames


    def convert_all_time(self):
        for col in self.colnames:
            self.convert_time(self.dataframe[col])


    def get_match(self, string, pattern):
        found = None
        if not string != string:
            try: 
                found = pattern.search(str(string))
            except Exception as e: 
                print(f"Unexpected error: {e} for {string}")
            if found != None:
                value = re.compile("\d{1,}").search(found[0])
                return int(value[0])
        return 0 


    def convert_time(self, col):  
        # expects a dataframe column
        for index, row in col.iteritems():
            min_p = re.compile("\d{1,}\sminutes")
            sec_p = re.compile("\d{1,}\sseconds")    
            hr_p = re.compile("\d{1,}\shours")            
            mins = self.get_match(row, min_p)
            secs = self.get_match(row, sec_p)
            hrs = self.get_match(row, hr_p)
            time = mins * 60 + secs + hrs * 60 * 60
            col[index] = time