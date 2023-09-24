import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload_paper():
    return render_template('upload.html')
        
@app.route('/question_papers')
def question_papers():
    return render_template('papers.html')

    # temp_array = list()
    # if request.method == 'POST':
    #     batting_team = request.form['batting-team']
    #     if batting_team == 'Chennai Super Kings':
    #         temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0]
    #     elif batting_team == 'Delhi Capitals':
    #         temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0]
    #     elif batting_team == 'Kings XI Punjab':
    #         temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0]
    #     elif batting_team == 'Kolkata Knight Riders':
    #         temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0]
    #     elif batting_team == 'Mumbai Indians':
    #         temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0]
    #     elif batting_team == 'Rajasthan Royals':
    #         temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0]
    #     elif batting_team == 'Royal Challengers Bangalore':
    #         temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0]
    #     elif batting_team == 'Sunrisers Hyderabad':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0]
    #     elif batting_team == 'Gujarat Titans':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0]
    #     elif batting_team == 'Lucknow Super Giants':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1]
            
            
    #     bowling_team = request.form['bowling-team']
    #     if bowling_team == 'Chennai Super Kings':
    #         temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0]
    #     elif bowling_team == 'Delhi Capitals':
    #         temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0]
    #     elif bowling_team == 'Kings XI Punjab':
    #         temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0]
    #     elif bowling_team == 'Kolkata Knight Riders':
    #         temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0]
    #     elif bowling_team == 'Mumbai Indians':
    #         temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0]
    #     elif bowling_team == 'Rajasthan Royals':
    #         temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0]
    #     elif bowling_team == 'Royal Challengers Bangalore':
    #         temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0]
    #     elif bowling_team == 'Sunrisers Hyderabad':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0]
    #     elif bowling_team == 'Gujarat Titans':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0]
    #     elif bowling_team == 'Lucknow Super Giants':
    #         temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1]
            
            
    #     overs = float(request.form['overs'])
    #     runs = int(request.form['runs'])
    #     wickets = int(request.form['wickets'])
    #     runs_in_prev_5 = int(request.form['runs_in_prev_5'])
    #     wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
    #     temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
    #     data = np.array([temp_array])


    #     my_prediction_linear = int(linear_regressor.predict(data)[0])
    #     my_prediction_ridge = int(ridge_regressor.predict(data)[0])
    #     # my_prediction_ann = int(ann.predict(data)[0])
    #     my_prediction_rf = int(rf_regressor.predict(data)[0])

    #     if my_prediction_linear > 250:
    #         my_prediction_linear = my_prediction_linear + 15

        
    #     return render_template('result.html', 
    #                            lower_limit_linear = my_prediction_linear-10, upper_limit_linear = my_prediction_linear+5, 
    #                            lower_limit_ridge = my_prediction_ridge-5, upper_limit_ridge = my_prediction_ridge+2,
    #                            lower_limit_rf = my_prediction_rf-10, upper_limit_rf = my_prediction_rf
    #                         )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)