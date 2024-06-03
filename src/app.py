import streamlit as st
from prediction_pipeline import Predictor
import numpy as np
from logger import logging
# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    body {
        background-image: url('https://your-image-url.com/background.jpg');
        background-size: cover;
        font-family: 'Poppins', sans-serif;
    }
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 2.5em;
        
    }
    .main-description {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: 1.2em;
    }
    .form-container {
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
    }
    .center-button {
        display: flex;
        justify-content: center;
    }
    .custom-button {
        background-color: #000000;
        color: white;
        padding: 0.5em 2em;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        font-size: 1em;
        margin-top: 1em;
        text-decoration: none;
        font-family: 'Poppins', sans-serif;
    }
    .custom-button:hover {
        background-color: #ff6347;
    }
    .success-message {
    color: #32CD32;
    font-size: 1.5em;
    text-align: center;
    font-family: 'Poppins', sans-serif;
    border: 2px solid #32CD32; /* Green border */
    background-color: #f0fff0; /* Light green background */
    padding: 10px; /* Padding around the text */
    border-radius: 5px; /* Rounded corners */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Shadow for a little depth */
    }
    
    </style>
    """, unsafe_allow_html=True)

# Function to render the main page
def main():
    logging.info("App Started running...")
    st.markdown('<h1 class="main-title">Delivery Time Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-description">Enter your delivery details and receive your estimated delivery time..</p>', unsafe_allow_html=True)

    vehicle_condition_options = {
        "0 - Very Poor Condition": 0,
        "1 - Poor Condition": 1,
        "2 - Fair Condition": 2,
        "3 - Good Condition": 3
    }

    with st.form(key='delivery_form_main', clear_on_submit=True):
        with st.container():
            st.markdown('<div class="form-container">', unsafe_allow_html=True)
            delivery_person_id = st.text_input('Delivery Person ID', '')
            delivery_person_age = st.number_input('Delivery Person Age (Minimum 20)', min_value=20)
            delivery_person_ratings = st.number_input('Delivery Person Ratings', min_value=0.0, step=0.1)
            weather_conditions = st.selectbox('Weather Conditions', ["Fog", "Stormy", "Sandstorms", "Windy", "Cloudy", "Sunny"])
            road_traffic_density = st.selectbox('Road Traffic Density', ["Jam", "High", "Medium", "Low"])
            vehicle_condition_display = st.selectbox('Vehicle Condition', list(vehicle_condition_options.keys()))
            type_of_order = st.selectbox('Type of Order', ["Snack", "Meal", "Drinks", "Buffet"])
            type_of_vehicle = st.selectbox('Type of Vehicle', ["Motorcycle", "Scooter", "Electric Scooter", "Bicycle"])
            multiple_deliveries = st.selectbox('Multiple Deliveries', [0, 1, 2, 3])
            festival = st.selectbox('Festival', ["Yes", "No"])
            city = st.selectbox('City', ["Metropolitan", "Urban", "Semi-Urban"])
            distance_in_kms = st.number_input('Distance in Kms (greater than 2)', min_value=2.0, step=0.1)
            order_day = st.number_input('Order Day (1-31)', min_value=1, max_value=31)
            order_month = st.number_input('Order Month (1-12)', min_value=1, max_value=12)
            order_year = st.number_input('Order Year', min_value=2000)  # Adjust the min_value as necessary
            time_ordered_hour = st.number_input('Time Ordered Hour (Minimum 1, 0-23)', min_value=1, max_value=23)
            time_ordered_mins = st.number_input('Time Ordered Mins (0-59)', min_value=0, max_value=59)
            time_order_picked_hour = st.number_input('Time Order Picked Hour (Minimum 1, 0-23)', min_value=1, max_value=23)
            time_order_picked_mins = st.number_input('Time Order Picked Mins (0-59)', min_value=0, max_value=59)

            submit_button = st.form_submit_button(label='Submit')
            st.markdown('</div>', unsafe_allow_html=True)
            st.text("Note : Double click the submit button to get results")
            logging.info('Submitted result Successfully')

    if submit_button:
        vehicle_condition = vehicle_condition_options[vehicle_condition_display]

        data = [
            delivery_person_id, delivery_person_age, delivery_person_ratings, weather_conditions,
            road_traffic_density, vehicle_condition, type_of_order, type_of_vehicle, multiple_deliveries,
            festival, city, distance_in_kms, order_day, order_month, order_year, time_ordered_hour,
            time_ordered_mins, time_order_picked_hour, time_order_picked_mins
        ]
        predictor = Predictor()
        results = predictor.results(data)

        if results is not None:
            st.experimental_set_query_params(page='result', result=np.round(results[0], 3))
        else:
            st.error("Prediction failed. Please check your input data or try again later.")

# Function to render the results page
def results_page(result):
    st.markdown('<h1 class="main-title">Submitted Delivery Information Successfully</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="success-message">Your order will be delivered in {result} minutes</p>', unsafe_allow_html=True)
    st.markdown('<div class="center-button"><a href="/?page=reasons" class="custom-button">Reasons</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="center-button"><a href="/" class="custom-button">Go Back</a></div>', unsafe_allow_html=True)

# Function to render the reasons page
def reasons_page():
    st.markdown("<h1 class='main-title'>Reasons for the Prediction</h1>", unsafe_allow_html=True)

    reasons_data = {
        "Age": "Statistical analysis shows a correlation of 0.3 between age and delivery time, suggesting that younger people are generally faster at completing deliveries compared to their older peers.",
        "Road Traffic Density": "High or jam traffic leads to an increase in delivery time, with a correlation value of 0.4 between road traffic density and the time taken to deliver an order.",
        "Multiple Deliveries": "More deliveries by a delivery agent will lead to an increase in delivery time, with a correlation value of 0.4 between the number of deliveries and delivery time.",
        "Festival": "When there is a festival, it leads to more time required for delivery, with a correlation value of 0.3 between the occurrence of a festival and delivery time.",
        "Time Ordered and Picked": "An increase in both time ordered and time picked leads to longer delivery times, with a correlation value of 0.2.",
        "City": "City type influences delivery times, with a correlation value of 0.2. Metropolitan cities tend to have longer delivery times compared to semi-urban areas, while urban areas generally experience shorter delivery times.",
        "Delivery Person Ratings": "Delivery times decrease as delivery person ratings increase, with a correlation of -0.3 between rating and delivery time.",
        "Vehicle Condition": "There is an inverse relationship between vehicle condition and delivery time with a correlation value of -0.2, where a better vehicle condition leads to shorter delivery times.",
        "Weather Condition - Sunny": "Sunny weather conditions are associated with shorter delivery times, indicating that delivery times decrease when it is sunny."
    }

    for reason, description in reasons_data.items():
        with st.expander(reason):
            st.write(description)

    st.markdown('<div class="center-button"><a href="/" class="custom-button">Go Back</a></div>', unsafe_allow_html=True)

# Page navigation
query_params = st.experimental_get_query_params()
if 'page' in query_params:
    if query_params['page'][0] == 'reasons':
        reasons_page()
    elif query_params['page'][0] == 'result' and 'result' in query_params:
        results_page(query_params['result'][0])
    else:
        main()
else:
    main()


