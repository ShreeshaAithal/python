import random
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def otp_gen2():
    n1=otp_gen()
    n2=otp_gen()
    return render_template("otp.html",param1=n1,param2=n2)

def otp_gen():
    n=5
    start=10**(n-1)
    stop= (10**n)-1
    otp= random.randint(start,stop)
    return str(otp)
result=otp_gen()
print(result)

if __name__=="__main__":
    app.run()
    
