from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('ebay_mens_perfume.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    perfume_list = df['title'].unique()
    selected_perfume = None
    perfume_details = None

    if request.method == 'POST':
        selected_perfume = request.form['perfume']
        result = df[df['title'] == selected_perfume]

        if not result.empty:
            perfume_details = result.iloc[0].to_dict()

    return render_template('index.html',
                           perfume_list=perfume_list,
                           selected_perfume=selected_perfume,
                           perfume_details=perfume_details)

if __name__ == '__main__':
    app.run(debug=True)
