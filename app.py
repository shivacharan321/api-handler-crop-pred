import pickle
from flask import Flask,request

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def homePage():
    return 'API Server Launched'

@app.route('/predict',methods=['GET'])
def predict():
    n=request.args.get('n')
    p=request.args.get('k')
    k=request.args.get('k')
    t=request.args.get('t')
    h=request.args.get('h')
    ph=request.args.get('ph')
    r=request.args.get('r')
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    return result

if __name__=="_name_":
    app.rin(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

    