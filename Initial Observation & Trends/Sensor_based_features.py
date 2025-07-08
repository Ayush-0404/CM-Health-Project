import pandas as pd

# Sensor column groups (use train_df only)
acc_cols = [col for col in train_df.columns if col.startswith('acc_')]
rot_cols = [col for col in train_df.columns if col.startswith('rot_')]
thm_cols = [col for col in train_df.columns if col.startswith('thm_')]
tof_cols = [col for col in train_df.columns if col.startswith('tof_')]

# Helper function for summary stats (train only)
def sensor_summary(df, cols, name, dataset_name):
    summary = pd.DataFrame({
        'Feature': cols,
        f'{dataset_name} Missing %': df[cols].isnull().mean().values * 100,
        f'{dataset_name} Min': df[cols].min().values,
        f'{dataset_name} Max': df[cols].max().values,
        f'{dataset_name} Mean': df[cols].mean().values,
        f'{dataset_name} Std': df[cols].std().values
    })
    summary.insert(0, 'Sensor', name)
    return summary

# Compute train summary for each sensor type
def train_sensor_summary(train_df, sensor_cols_dict):
    all_train = []
    for sensor_name, cols in sensor_cols_dict.items():
        all_train.append(sensor_summary(train_df, cols, sensor_name, 'Train'))
    train_summary = pd.concat(all_train, ignore_index=True)
    return train_summary

# Sensor groups to process
sensor_cols_dict = {
    'acc': acc_cols,
    'rot': rot_cols,
    'thm': thm_cols,
    'tof': tof_cols
}

# Run train summary only
sensor_train_summary = train_sensor_summary(train_df, sensor_cols_dict)

# Show sensor-level averages for train
summary_by_group = sensor_train_summary.groupby('Sensor').mean(numeric_only=True)

# Display styled table
summary_by_group.style.background_gradient(cmap='viridis')
