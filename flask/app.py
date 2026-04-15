from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        data = {
            'Product': ['laptop', 'Mouse', 'moniter'],
            'Price': [1200, 25, 300],
            'Quantity': [5, 50, 10]
        }
        df = pd.DataFrame(data)
        df['Total'] = df['Price'] * df['Quantity']
        
        # HTML ટેબલ બનાવવું
        table_html = df.to_html(classes='table table-bordered', index=False)
        
        # એક્સેલ ફાઈલ સેવ કરવી
        df.to_excel('business_data.xlsx', index=False)
        
        return render_template('index.html', table=table_html)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/download')
def download():
    return send_file('business_data.xlsx', as_attachment=True)

if __name__ == '__main__':
    # પોર્ટ બદલીને 8000 કર્યો છે જેથી જૂની એરર ન આવે
    app.run(debug=True, port=8000)