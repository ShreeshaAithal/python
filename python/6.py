from flask import Flask
app=Flask(__name__)

@app.route("/")

import random
def otp1():
    size=6
    qty=10
  
    for i in range(0,qty,1):
        rand1=random.randint(10**(size-1),10**size-1)
        print(rand1)

if __name__=="__main__":
    app.run()
