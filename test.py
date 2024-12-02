import mlflow

# Passing empty string
mlflow.set_experiment("")  # Likely switches to the "Default" experiment

# Running an experiment
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.89)

# Check the UI to see where the run was logged (probably under "Default").
