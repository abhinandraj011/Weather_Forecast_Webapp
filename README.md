# Weather Forecast Web Application

This is a simple web application built with Streamlit that provides weather forecast information for the next few days. It utilizes data retrieved from a backend API.

## Setup Instructions

1. **Clone this repository:**
    ```
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**
    ```
    cd your-repository
    ```

3. **Install the required dependencies:**
    ```
    pip install streamlit plotly pandas requests
    ```

4. **Run the Streamlit application:**
    ```
    streamlit run app.py
    ```

## Usage

Once the application is running, you can interact with it via the Streamlit interface in your browser. Here are the features available:

- **Title:** "Weather Forecast for the Next Days"
- **Text Input:** Enter the place for which you want to get the weather forecast.
- **Slider:** Choose the number of days for the forecast (between 1 and 5).
- **Selectbox:** Choose whether to view temperature or sky conditions.
- **Subheader:** Displays the selected option and location.
- **Visualization:** Depending on the selected option (temperature or sky), the app will display either a line chart of temperatures or images representing sky conditions.

## Features

- **Input Validation:** The app checks if the entered place exists.
- **Interactive Interface:** Users can dynamically select the location, forecast days, and data type (temperature or sky conditions).
- **Visualization:** Utilizes Plotly Express for interactive data visualization.

## Dependencies

- Streamlit
- Plotly Express
- Pandas
- Requests
