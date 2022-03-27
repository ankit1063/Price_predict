from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle




app = Flask(__name__)

with open('model_xg.pkl' , 'rb') as f:
    model1 = pickle.load(f)




@app.route("/")

def index():
    return render_template("index.html")


@app.route("/model", methods =['POST'])

def model():
    if request.method =="POST":
        features=[]
        year = request.form['year']
        year_in=int(year)
        features.append(year_in)
        
        mileage = request.form['mileage']
        mileage_in=int(mileage)
        features.append(mileage_in)
        

        
        city = request.form['city']
        features.append(city)
        
        state= request.form['state']
        features.append(state)
        
        make= request.form['make']
        features.append(make)
        
        model= request.form['model']
        features.append(model)
        
        currentyear=2022
        
        year_used=currentyear-year_in
        features.append(year_used)
        
        condition=(mileage_in/year_used)
        features.append(condition)
        
        feat = [np.array(features)]
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
        
        if condition >= 10000:
          con="Bad Condition"  
          
        elif condition >5000 and condition < 10000:
          con="Average Condition You can go for buy"
        else:
          con="Good Working Condition "
       
        prediction = model1.predict(t_2)
        pre=int(prediction)
        
    
    return render_template("predict_model.html", prediction_price='Expected Price - {} $  , Car Model- {} , Made By- {} Company '.format(pre,model,make),
               prediction_data='Car Year-  {} , Total distance travelled- {} Km '.format(year_in,mileage_in), cond_car= 'Car Condition -  {}  '.format(con)           )


if __name__ == "__main__":
    app.run(debug=True)
    
    