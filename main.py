import sys
from flask import Flask,request

param=int(sys.argv[1])
if param==1:
    print(f'Am rulat main.py cu urmatoarele argumente: {sys.argv}')
    path=sys.argv[2]
    print(path)
elif (param==2):
    app= Flask(__name__)
    @app.route('/utilizator',methods=['POST'])
    def signup():
        # print(request.form)
        # print(request.get_json())
        # print("request primit!")
        return 'Cerere inregistrata',200
    
    @app.route('/acces',methods=['POST'])
    def acces():
        # print(request.form)
        # print(request.get_json())
        # print("request primit!")
        return 'Cerere inregistrata',200
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
else:
    print("Nicio optiune nu a fost potrivita!")