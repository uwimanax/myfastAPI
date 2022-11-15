from fastapi import FastAPI, Request
from datetime import datetime
storage = FastAPI(title ='MY FASTAPI')

@storage.get('/')
def index():
    return "this is the index/first page of my API"
#if __name__== '__main__':
   # app.run()    

@storage.get('/today')
def today():
    return str(datetime.now())
@storage.get('/mynames')
def names(first_name:bool=False, last_name:bool=False, Full_name:bool=False):
    full_names = ""
    if first_name:
        full_names += 'Xaverine'
    if last_name:
        full_names += ' UWIMANA' 
    if Full_name:
        full_names += "my name is xaverine UWIMANA"  
    return full_names     
if __name__ == "__main__":
    storage.run()