from flask import Flask,redirect, url_for, jsonify, request
import subprocess
import CallTest

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

def handle_request():
    # The GET endpoint
    if request.method == "GET":
        return "This is the GET Endpoint of flask API."
    
    # The POST endpoint
    if request.method == "POST":
    
        response=request.get_json()
        fin_output = response.get('encoded_image', '')
        
        with open("servertag", "wb") as file:
            file.write(fin_output)

        def arxeioGrapsimo(filedata,filename):
            with open(filename, "wb") as file:
                file.write(filedata)

        file1= response.get('parameters', 'param_list[0]')
        file2= response.get('parameters', 'param_list[1]')
        file3= response.get('parameters', 'param_list[2]')
        file4=response.get('parameters', 'param_list[3]')
        file5=response.get('parameters', 'param_list[4]')

        arxeioGrapsimo(file1,"arithmos3")
        arxeioGrapsimo(file2,"noumero3")
        arxeioGrapsimo(file3,"diafora3")
        arxeioGrapsimo(file4,"pososta3")
        arxeioGrapsimo(file5,"xarakthres3")

        
        arg1="servertag"
        arg2="arithmos3"
        arg3="noumero3"
        arg4="diafora3"
        arg5="pososta3"
        arg6="xarakthres3"

        subprocess.call(['python', 'sumpiesh\map_wdecode.py', arg1 , arg2, arg3, arg4, arg5, arg6])

        #with open("output.bmp","wb") as file:
            #file.write(bytes.fromhex(fin_output))

        subprocess.call(['python', 'CallTest.py'])
   

        # return the response as JSON
        return jsonify(response)
    
    
if __name__=="__main__":
    app.run(host="192.168.2.8", port="5000")

