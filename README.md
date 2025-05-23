# 🧠 End-to-End Data Science Pipeline Project

This repository showcases the complete lifecycle of a machine learning project — from raw data acquisition to model deployment. Built with modular and scalable design principles, this project integrates essential MLOps practices like experiment tracking (MLflow) and version control (DagsHub).

---

## 🔄 ML Pipeline Workflow

The core machine learning pipeline includes the following stages:

1. **Data Ingestion** – Load raw data from source
2. **Data Validation** – Ensure schema integrity and quality
3. **Data Transformation** – Feature engineering and preprocessing
4. **Model Training** – Train models on processed data
5. **Model Evaluation** – Evaluate using metrics and track via MLflow/DagsHub

---

## 🛠️ Development Workflow

To customize or extend the pipeline, follow these steps:

1. Update `config/config.yaml` – define data source paths and settings
2. Update `schema.yaml` – define data schema for validation
3. Update `params.yaml` – adjust model hyperparameters
4. Update entity classes in `src/datascience/entity/`
5. Update the Configuration Manager in `src/datascience/configuration/`
6. Add or revise pipeline components in `src/datascience/components/`
7. Update or create new pipeline scripts under `src/datascience/pipeline/`
8. Run or modify the pipeline entry script: `main.py`


---

## 🔍 Pipeline Components

### ✅ 1. Data Ingestion
- **Script**: `src/datascience/components/data_ingestion.py`
- **Function**: Load data from source into the system
- **Config**: Controlled via `config/config.yaml`

### 🔍 2. Data Validation
- **Script**: `src/datascience/components/data_validation.py`
- **Function**: Validate data structure, nulls, and formats
- **Schema**: Defined in `schema.yaml`

### 🧹 3. Data Transformation
- **Script**: `src/datascience/components/data_transformation.py`
- **Function**: Feature engineering, encoding, scaling

### 🧠 4. Model Training
- **Script**: `src/datascience/components/model_trainer.py`
- **Function**: Train machine learning models
- **Models**: Logistic Regression, Random Forest, etc.
- **Parameters**: Set in `params.yaml`

### 📊 5. Model Evaluation
- **Script**: `src/datascience/components/model_evaluation.py`
- **Function**: Evaluate model with performance metrics
- **Tracking**: Uses MLflow and DagsHub for logging

---

## 🖥️ How to Run the Pipeline

```bash
# 1. Clone the repository
git clone https://github.com/Nahidzeinali-web/End_to_End_Pipeline-Project1.git
cd End_to_End_Pipeline-Project1

# 2. Create and activate a virtual environment
Conda create -p ./venv python==13.3 -y
conda activate ./venv            # On Windows

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the complete pipeline
python main.py




## 🛠️ Technologies & Tools Used

- **Programming Language**: Python 3.x  
- **Frameworks & Libraries**:  
  - Scikit-learn, Pandas, NumPy, PyYAML  
  - Matplotlib / Seaborn (for visualization if applicable)  
- **MLOps & Experiment Tracking**:  
  - MLflow  
  - DagsHub  
- **Web Framework**:  
  - Flask (for serving the model)  
- **Containerization**:  
  - Docker  
- **Version Control & CI/CD**:  
  - Git & GitHub  
  - GitHub Actions (CI/CD automation)
