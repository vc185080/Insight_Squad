import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import ast
import os
def recom(fp_growth_rule):
    print("Enter the dragon")
    customer_basket = ['fresh vegetables', 'packaged cheese']
    file_path = 'Output.txt'
   # discount = {'milk':"10 percent off",'packaged cheese':'10 percent off',"fresh vegetables":"20 percent off",'fresh fruits':'20 percent off'}
    items_list =[]
    try:
        with open(file_path,'r') as file:
            content = file.read()
    except FileNotFoundError:
        return
    items_list = content.strip().split(',')
    customer_basket = [item.strip() for item in items_list]
    print(customer_basket)
    # something new
    #customer_basket = sorted(customer_basket)
    fp_growth_rule['antecedents'] = fp_growth_rule['antecedents'].apply(ast.literal_eval)
    fp_growth_rule['consequents'] = fp_growth_rule['consequents'].apply(ast.literal_eval)
    basket_set = set(customer_basket)
    print(len(basket_set))
    print("first loop")
    fp_growth_rule.to_csv('C:\\Users\\vc185080\\Downloads\\Retail_Proj\\consequence111.csv',index=False)
    filtered_rules = fp_growth_rule[fp_growth_rule['antecedents'].apply(lambda x: set(x).issubset(basket_set))]
    #print(filtered_rules.head(10))
    filtered_rules.to_csv('C:\\Users\\vc185080\\Downloads\\Retail_Proj\\consequence222.csv',index=False)
    sorted_reco = filtered_rules.sort_values(by = 'antecedents',key =lambda x:x.apply(len), ascending = False )
    #sorted_reco.to_csv('C:\\Users\\vc185080\\Downloads\\Smart_Reccomendation_Application\\consequence.csv',index=False)
    print(sorted_reco.shape)
    max_length = len(sorted_reco.iloc[0,0])
    print("max length: ",max_length)
    list_names = sorted_reco.iloc[:5,1].tolist()
    set1 = set()
    for i in list_names:
        for j in i:
            if j not in customer_basket:
                set1.add(j.strip())
    print(list_names," --->",set1  )
    recomstring = ""
    recomstring = ", ".join(str(item) for item in set1)
    discount_string="fresh fruits 10% off, packaged cheeses 5% off"
    '''for i in set1:
        if i in discount:
            discount_string= discount_string+i+" "+discount[i]+", "'''

    with open("C:\\Users\\vc185080\\Downloads\\Retail_Proj\\recommendations.txt","w") as file:
        file.write(recomstring)

    with open("C:\\Users\\vc185080\\Downloads\\Retail_Proj\\Discounts.txt","w") as file:
        file.write(discount_string)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        # Replace 'filename.txt' with the name of your file to monitor
        main_data = pd.read_csv("Output.csv")
        df = main_data.copy()
        if event.src_path.endswith('Output.txt'):
            print("File modified! Running your Python code.11")
            # Put your Python code here that you want to invoke when the file is modified
            recom(df)
            if os.path.exists('Output.txt'):
                os.remove('Output.txt')
                print("RIP Output.txt")
            else:
                print("Not found Output.txt")
            print("File modified! Running your Python code.")

if __name__ == "__main__":
    path = '.'  # Replace '.' with the directory path containing the file to monitor
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()