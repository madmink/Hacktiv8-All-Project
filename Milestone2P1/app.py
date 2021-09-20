import flask
from flask.globals import request
import numpy as np
import pandas as pd
import pickle

app = flask.Flask(__name__, template_folder = 'template')

# render template
@app.route('/')
def main():
    return(flask.render_template('main.html'))

# load pickle file
scaler = pickle.load(open('model/scaler_std.pkl', 'rb'))
model = pickle.load(open('model/RF.pkl','rb'))



@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering prediction result.
    '''

    # retrieve data from form
    Age = int(request.form.get('age'))
    BusinessTravel = request.form.get('business-travel')
    DailyRate = int(request.form.get('daily-rate'))
    Department = request.form.get('department')
    DistanceFromHome = int(request.form.get('distance-from-home'))
    Education = request.form.get('education')
    EducationField = request.form.get('education-field')
    EnvironmentSatisfaction = int(request.form.get('environmental-satisfaction'))
    Gender = request.form.get('gender')
    HourlyRate = int(request.form.get('hourly-rate'))
    JobInvolvement = request.form.get('job-involvement')
    JobLevel = request.form.get('job-level')
    JobRole = request.form.get('job-role')
    JobSatisfaction = int(request.form.get('job-satisfaction'))
    MaritalStatus = request.form.get('marital-status')
    MonthlyIncome = int(request.form.get('monthly-income'))
    MonthlyRate = int(request.form.get('monthly-rate'))
    NumCompaniesWorked = int(request.form.get('number-of-companieswork'))
    OverTime = request.form.get('overtime')
    PercentSalaryHike = int(request.form.get('percent-salary-hike'))
    PerformanceRating = int(request.form.get('performance-rating'))
    RelationshipSatisfaction = int(request.form.get('relationship-satisfaction'))
    StockOptionLevel = int(request.form.get('stock-option'))
    TotalWorkingYears = int(request.form.get('total-working-years'))
    TrainingTimesLastYear = int(request.form.get('training-times-lastyear'))
    WorkLifeBalance = int(request.form.get('work-life-balance'))
    YearsAtCompany = int(request.form.get('years-at-company'))
    YearsInCurrentRole = int(request.form.get('years-in-currentrole'))
    YearsSinceLastPromotion = int(request.form.get('years-since-lastpromotion'))
    YearsWithCurrManager = int(request.form.get('years-with-currentmanager'))

    # pre processing one hot encoding that previously used get_dummies
    known_businessTravel = ['BusinessTravel_Travel_Frequently','BusinessTravel_Travel_Rarely','BusinessTravel_Non-Travel']
    known_department = ['Department_Human Resources','Department_Research & Development','Department_Sales']
    known_EducationField = ['EducationField_Life Sciences', 'EducationField_Marketing', 'EducationField_Medical', 'EducationField_Other', 'EducationField_Technical Degree','EducationField_Human Resources']
    known_Gender = ['Gender_Male', 'Gender_Female']
    known_JobRole = ['JobRole_Human Resources', 'JobRole_Laboratory Technician', 'JobRole_Manager','JobRole_Manufacturing Director', 'JobRole_Research Director', 'JobRole_Research Scientist', 'JobRole_Sales Executive','JobRole_Sales Representative', 'JobRole_Healthcare Representative']
    known_maritalStatus = ['MaritalStatus_Married', 'MaritalStatus_Single', 'MaritalStatus_Divorced'] 

    BusinessTravel_type = pd.Series([BusinessTravel])
    BusinessTravel_type = pd.Categorical(BusinessTravel_type, categories=known_businessTravel)
    BusinessTravel_input = pd.get_dummies(BusinessTravel_type, prefix='BusinessTravel', drop_first=True)

    Department_type = pd.Series([Department])
    Department_type = pd.Categorical(Department_type, categories=known_department)
    Department_input = pd.get_dummies(Department_type, prefix='DepartmentType', drop_first=True)

    EducationField_type = pd.Series([EducationField])
    EducationField_type = pd.Categorical(EducationField_type, categories=known_EducationField)
    EducationField_input = pd.get_dummies(EducationField_type, prefix='EducationField', drop_first=True)

    Gender_type = pd.Series([Gender])
    Gender_type = pd.Categorical(Gender_type, categories=known_Gender)
    Gender_input = pd.get_dummies(Gender_type, prefix='Gender', drop_first=True)

    JobRole_type = pd.Series([JobRole])
    JobRole_type = pd.Categorical(JobRole_type, categories=known_JobRole)
    JobRole_input = pd.get_dummies(JobRole_type, prefix='JobRole', drop_first=True)

    MaritalStatus_type = pd.Series([MaritalStatus])
    MaritalStatus_type = pd.Categorical(MaritalStatus_type, categories=known_maritalStatus)
    MaritalStatus_input = pd.get_dummies(MaritalStatus_type, prefix='MaritalStatus', drop_first=True)

    #concat new data
    onehot_result = list(pd.concat([BusinessTravel_input, Department_input, EducationField_input, Gender_input, JobRole_input, MaritalStatus_input], axis=1).iloc[0])
    new_data = [[Age,DailyRate,DistanceFromHome,Education,EnvironmentSatisfaction,HourlyRate,JobInvolvement,JobLevel,JobSatisfaction,MonthlyIncome,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager] + onehot_result]

    scaled_input = scaler.fit_transform(new_data)
    prediction = model.predict(scaled_input)

    output = {0 : 'Attrition Yes', 1 : 'Attrition No'}

    return flask.render_template('results.html', prediction_text = 'The Employee will {} with this condition.'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug = True)



