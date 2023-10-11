from flask import Flask,render_template
import random

app=Flask(__name__)

@app.route("/")
def otp1():
    size=6
    qty=10
    list1=[]
  
    for i in range(0,qty,1):
        list1.append(random.randint(10**(size-1),10**size-1))
    print(list1)
    return render_template("otp1.html",param1=list1)
        
        
if __name__=="__main__":
    app.run()
