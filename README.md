# Data Processing and Visualization Tasks

This repository contains Python scripts for various data manipulation, visualization, and WebSocket integration tasks. Each script demonstrates a specific use case, employing efficient data handling techniques and professional coding practices.

---

## **Contents**

### **Task 1: Real-Time Data Collection from WebSocket**
- **Description**: Connects to a WebSocket, receives cryptocurrency price updates, and stores them in a CSV file.
- **Features**:
  - Fetches real-time data for multiple cryptocurrencies.
  - Stores data in batches for performance optimization.
  - Reconnects automatically if the WebSocket connection is lost.
- **Libraries Used**:
  - `asyncio`
  - `websockets`
  - `csv`
  - `json`

### **Task 2: Temperature Data Visualization**
- **Description**: Visualizes daily temperature variations in a city using a line plot.
- **Features**:
  - Reads data from a CSV file.
  - Annotates the highest and lowest temperatures on the plot.
  - Handles date formatting for proper visualization.
- **Libraries Used**:
  - `pandas`
  - `matplotlib`

### **Task 3: Sales Data Manipulation**
- **Description**: Processes a large sales dataset to extract meaningful insights.
- **Features**:
  - Groups data by region and calculates total sales.
  - Adds a new column for average price per unit.
  - Filters rows where total sales exceed a specified threshold.
- **Libraries Used**:
  - `pandas`

---

## **Prerequisites**
Ensure you have the following installed in your environment:
- Python 3.8+
- Required libraries (install using `pip`):
  ```bash
  pip install -r requirements.txt
  ```

---

## **Usage**

1. Clone the repository:
   ```bash
   git clone https://github.com/AyushMayekar/Miles
   cd Miles/Codes
   ```

2. **Task 1**:
   - Run the WebSocket integration script:
     ```bash
     python websocket.py
     ```
   - Ensure you have an active internet connection for real-time updates.

3. **Task 2**:
   - Place the temperature data CSV in the same directory as the script.
   - Run the script to generate a temperature line plot:
     ```bash
     python data_mat.py
     ```
   - View the plot output in the window or save it as an image.

4. **Task 3**:
   - Run the script to process and filter data:
     ```bash
     python data_mani.py
     ```
   - Outputs will be printed and saved as needed.

---

## **Contact**
For any queries or suggestions, feel free to reach out:
- **Email**: ayush.224947101@vcet.edu.in
- **LinkedIn**: [Ayush Mayekar](https://www.linkedin.com/in/ayush-mayekar-b9b883284/)

---

This repository is designed to showcase Python's power in solving real-world data processing and visualization challenges. Happy coding! 😊