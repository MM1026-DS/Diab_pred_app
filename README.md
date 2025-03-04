# Diabetes Prediction App

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

This project is a web-based application for predicting the likelihood of diabetes in individuals based on input health parameters. It leverages machine learning models to provide an accurate and user-friendly predictive tool.

## Features

- **Machine Learning Model**: Predicts diabetes based on user input features.
- **Interactive Web Interface**: Allows users to enter health parameters and get predictions.
- **Scalable & Lightweight**: Designed to work efficiently on various platforms.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure that Python is installed on your system before running the project.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MM1026-DS/Diab_pred_app.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Diab_pred_app
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the web application**:

   ```bash
   python app.py
   ```

2. **Access the application in your browser**:

   - Open `http://127.0.0.1:5000/` to use the diabetes prediction tool.

3. **Enter the required health parameters** and get a prediction.

## Project Structure

```
Diab_pred_app/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   ├── result.html
├── models/
│   ├── diabetes_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

- **static/**: Contains CSS, JavaScript, and images for UI styling.
- **templates/**: HTML templates for rendering web pages.
- **models/**: Trained machine learning model for diabetes prediction.
- **app.py**: Main application script using Flask.

## Contributing

Contributions are welcome! If you'd like to improve the project, fork the repository and submit a pull request with your updates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
