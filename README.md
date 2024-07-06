# Delivery Time Prediction Web Application

### Introduction:
This repository contains a Streamlit-based web application for predicting delivery times based on various factors. The application allows users to input delivery details and receive an estimated delivery time. Additionally, users can explore the reasons behind the predictions based on statistical correlations and model insights.

### Technology stack 
<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/4a1d188d-a4bc-4d25-881d-80e6db331914" alt="Vscode" width="200"/>

<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/4f0730f0-0f7f-4536-af72-ca89802f8b77" alt="Python Logo" width="200"/>

<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/b5ab334c-4f77-4e07-9556-99c6874022e1" alt="Jupyter notebook" width="200"/>

<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/df040526-5e3f-4309-92a2-b092e0bfea9f" alt="Pandas" width="200"/>

<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/708ee0a7-f846-494b-b1ec-a22fa1bf572e" alt="Numpy" width="200"/>

<img src="https://github.com/MDS53/Adultcensusincome-_/assets/82602774/9ff1d913-4cd5-4411-a6b4-0cd66eaf6acb" alt="Sklearn icon" width="200"/>

<img src="https://github.com/MDS53/Youtube-Content-Scrapper/assets/82602774/18062093-e3bf-4dc6-b3c4-9e060d29b144" alt="Streamlit" width="200"/>


######

### Working

- **User Input Form**: Collects data such as delivery person ID, age, ratings, weather conditions, road traffic density, vehicle condition, type of order, type of vehicle, multiple deliveries, festival occurrence, city, distance, and order time details.
- **Prediction Results**: Displays the predicted delivery time based on the input data.
- **Reasons for Prediction**: Provides detailed insights into the factors affecting the delivery time prediction.

### Technical Details

- **Data Collection and Cleaning**: Ensures the input data is clean and in the correct format.
- **Feature Engineering**: Constructs new features from the input data to improve model accuracy.
- **Model Training**: Utilizes various machine learning models such as Linear Regression, Ridge, Lasso, SVR, RandomForest, XGBoost, CatBoost, and LightGBM.
- **Hyperparameter Tuning**: Uses Hyperopt for optimizing model parameters.
- **Evaluation Metrics**: Reports model performance using metrics like R² score, MSE, RMSE, MAE, and MAPE.


## How to Use

You can use the Delivery Time Prediction Web Application in two ways: by running the code locally or by accessing it through a deployed link.

### 1. Running the Code Locally

1. **Install Requirements**: 
   - Ensure you have Python installed.
   - Clone the repository to your local machine.
   - Navigate to the repository directory and install the required libraries using:
     ```bash
     pip install -r requirements.txt
     ```
2. **Run the App**:
   - Start the Streamlit app using the command:
     ```bash
     streamlit run app.py
     ```
3. **Enter Details**:
   - Open the local URL provided by Streamlit (usually `http://localhost:8501`).
   - Fill out the delivery details form and submit to get the predicted delivery time.
4. **Explore Reasons**:
   - Click on the "Reasons" button to understand the factors affecting the prediction.

### 2. Using the Deployed Link

1. **Access the App**:
   - Open your web browser and navigate to the deployed link :
     https://r7hamyvjr8yzemeszctquh.streamlit.app/
2. **Enter Details**:
   - Fill out the delivery details form on the webpage and submit to get the predicted delivery time.
3. **Explore Reasons**:
   - Click on the "Reasons" button to understand the factors affecting the prediction.

## Data Cleaning and Model Training Workflow

The attached image illustrates the comprehensive workflow for data cleaning and model training, encompassing steps such as:

- **Data Cleaning**: Correcting formats and handling missing values.
- **Feature Transformation**: Encoding categorical features.
- **Feature Selection**: Dropping unnecessary features.
- **Feature Construction**: Creating new features based on time data and calculating distances.
- **Model Training**: Implementing various regression and ensemble models.
- **Hyperparameter Tuning**: Optimizing model parameters.
- **Model Evaluation**: Assessing model performance using multiple metrics.

![Data Cleaning and Model Training Workflow (2)](https://github.com/MDS53/zomato_delivery_time_prediction_using-Streamlit/assets/82602774/792045d4-3574-4420-a9b2-bcbcd222681f)

This workflow ensures a robust pipeline for accurate delivery time predictions.


## Benefits:

 -  Improve delivery efficiency
 -  Enhance customer satisfaction
 -  Gain insights into delivery operations



## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or new features.

---

Feel free to reach out if you have any questions or need further assistance with the application. Happy predicting!

Demo : 

https://github.com/MDS53/zomato_delivery_time_prediction_using-Streamlit/assets/82602774/4b50910d-c974-4f83-8b3a-9f0817ef08a4

Try out the app!! 
### Deployed app: https://r7hamyvjr8yzemeszctquh.streamlit.app/


In case, if you would like to connect with me:
#### Linkedin : https://www.linkedin.com/in/mohammad-salman-a633b9238/
