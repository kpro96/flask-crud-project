from flask import Flask
render_template, send_file
import pandas as pd 
import os
app =Flask(__name__)

@app.route('/') 
def home():
   data = { 
            'Product':  ['laptop','Mouse','moniter',],
            'Price': [1200, 25 ,300],
            'Quantity': [5, 50, 10]
          }
df = pd.DataFrame(data)
df['Total'] = df['Price'] * df['Quantity'] 
file_name = 'business_data.xlsx'
df.to.excel('business_data.xlsx',index=False) 
table_html = df.to_html(classes = 'table table-border')
   
@app.route('/download')
def download():
         return render_template('index.html',table=table_html)
         return send_file('business_data.xlsx',as_attachment= true)
if __name__=='__main__' : app.run(debug=True)
    
    
    
