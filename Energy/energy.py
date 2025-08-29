# device, machine,customer, user role,feature
# insert,update, get
from flask import Flask,request
import apisupport
app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
    return 'Hi'

@app.route('/machines',methods=['GET'])
def helloworld1():
    name = request.args.get('id')
    machines = [{
        'id':1,'machine_name':'Machine1'
    },{
        'id':2,'machine_name':'Machine2'
    }
    ]
    for i in range(len(machines)):
        print(machines[i],machines[i]['id'])
        if machines[i]['id'] == int(name):
            return machines[i].get('machine_name')
    print(name)
    return 'No Machine'

if __name__ == '__main__':
    app.run(debug=True)


