# EndToEndML

EndToEndML project (Student Score Prediction) is an open-source, user-friendly web application designed to streamline the entire machine learning pipeline—from data preprocessing to model deployment. It enables users, especially those without programming expertise, to upload datasets, train models using automated, state-of-the-art algorithms, and visualize results through an intuitive graphical interface.

## Features

- **Data Upload and Preprocessing**: Easily upload datasets and let the system handle data cleansing and feature engineering.
- **Automated Model Training**: Utilize automated machine learning algorithms to train models without manual coding.
- **Model Evaluation**: Access built-in evaluation metrics to benchmark model performance on test data.
- **Interactive Visualizations**: Gain insights into model behavior through interactive visualizations.
- **Seamless Deployment**: Deploy trained models directly from the platform.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/anshbadoni30/endtoendml.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd endtoendml
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   python application.py
   ```

2. **Access the Web Interface**:

   Open your web browser and navigate to `http://localhost:5000` to start using EndToEndML.

## Project Structure

```plaintext
endtoendml/
├── artifact/
├── catboost_info/
├── components/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   ├── model_evaluation.py
│   ├── model_pusher.py
├── notebook/
├── src/
├── templates/
├── .gitignore
├── README.md
├── application.py
├── requirements.txt
├── setup.py
```

### Components Folder
- `data_ingestion.py`: Handles data loading and preprocessing.
- `data_transformation.py`: Applies feature engineering and transformations.
- `model_trainer.py`: Trains and validates the machine learning models.
- `model_evaluation.py`: Evaluates the trained model's performance.
- `model_pusher.py`: Deploys the trained model.

### Artifacts Folder
- Stores outputs from various pipeline stages, such as:
  - Processed datasets
  - Trained model files
  - Evaluation reports

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

