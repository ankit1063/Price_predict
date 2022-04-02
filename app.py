from flask import Flask,render_template,request,url_for,jsonify,redirect
import pandas as pd
import numpy as np
import pickle

import warnings

warnings.filterwarnings("ignore")

# from pydantic import NoneIsAllowedError
#from python_library.test_lib2 import test_func

with open('model_xg.pkl' , 'rb') as f:
  model1 = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods =['GET','POST'])
def home():
    return render_template("index.html")


@app.route("/output", methods =['GET','POST'])

def output():
    features=[]
    year=request.json['user_year']
    year=int(year)
    features.append(year)
    
    mileage=request.json['user_mileage']
    mileage=int(mileage)
    features.append(mileage)
    
    city=request.json['user_city']
    features.append(city)
    
    state=request.json['user_state']
    features.append(state)
    
    make=request.json['user_make']
    features.append(make)
    
    
    model=request.json['user_model']
    features.append(model)
    
    currentyear=2022
    
    year_used=currentyear-year
    features.append(year_used)
    
    condition=(mileage/year_used)
    features.append(condition)
    
    feat = [np.asarray(features,dtype=None,order=None)]
    
    t_2=pd.DataFrame(feat)
    t_2.rename(columns = {0:'Year', 
                   1:'Mileage',
                  2:'City', 
                   3:'State',
                  4:'Make', 
                   5:'Model',
                  6:'Year_used', 
                   7:'Condition',
                             }, 
        inplace = True)
    
    if condition >= 8500:
      con="Bad Condition"  
      
    elif condition >5000 and condition < 8500:
      con="Average Condition You can go for buy"
    else:
      con="Good Working Condition "
   
    prediction = model1.predict(t_2)
    pre=int(prediction)
    sen= ('Expected Price - {} $  , Car Model- {} , Made By- {} Company Car Year-  {} , Total distance travelled- {} Km  Car Condition -  {}'.format(pre,model,make,year,mileage,con)  )      
   
 
    
    return jsonify(sen)
   
    
 

if __name__ == "__main__":
    app.run(debug=False)
    
    
