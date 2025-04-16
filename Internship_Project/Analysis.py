import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('bmh')

# Load and clean data
data = pd.read_csv('Internship_Project/Dataset/Machine_Downtime.csv')
data = data.dropna()

#                   FIRST MOVEMENT BUSINESS DECISION
Average = data.iloc[:, 3:15].mean()
Median = data.iloc[:, 3:15].median()
Mode = data.iloc[:, [0, 1, 2, 15]].mode()

#                  SECOND MOVEMENT BUSINESS DECISION
Std = data.iloc[:, 3:15].std()
Variance = data.iloc[:, 3:15].var()
Range = data.iloc[:, 3:15].max() - data.iloc[:, 3:15].min()

#            THIRD MOVEMENT BUSINESS DECISION: Distribution of each column
plt.figure(figsize=(12, 10))
columns = data.iloc[:, 3:15].columns
for i in range(len(columns)):
    plt.subplot(4, 3, i + 1)
    plt.hist(data[columns[i]], bins=20, color='skyblue', edgecolor='black')
    plt.title(columns[i], fontsize=10)
plt.suptitle('📊 Distribution of Equipment Parameters', fontsize=16, fontweight='bold')
plt.tight_layout(pad=2.0)
plt.show()

#             FOURTH MOVEMENT BUSINESS DECISION
all_equipment_kurt = data.iloc[:, 3:15].kurt()

#                    EDA
new_data = data.drop(columns=['Spindle_Speed_RPM'])

#                        MEAN ANALYSIS
Machine_good_condition = new_data[new_data['Downtime'] == 'No_Machine_Failure'].iloc[:, 3:13].mean()
Machine_bad_condition = new_data[new_data['Downtime'] == 'Machine_Failure'].iloc[:, 3:13].mean()
Decreased_difference = Machine_bad_condition[Machine_bad_condition.values < Machine_good_condition.values]
Increased_difference = Machine_bad_condition[Machine_bad_condition.values > Machine_good_condition.values]

plt.figure(figsize=(12, 8))
plt.suptitle('📊 Machine Performance Comparison (MEAN)', fontsize=16, fontweight='bold')

# GOOD condition
plt.subplot(2, 2, 1)
plt.bar(Machine_good_condition.index.tolist(), Machine_good_condition.values.tolist(), color='green')
plt.title('✅ Mean - No Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_good_condition.index):
    plt.text(label, Machine_good_condition.values[i], f'{Machine_good_condition.values[i]:.2f}', ha='center')

# BAD condition
plt.subplot(2, 2, 2)
plt.bar(Machine_bad_condition.index.tolist(), Machine_bad_condition.values.tolist(), color='red')
plt.title('❌ Mean - Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_bad_condition.index):
    plt.text(label, Machine_bad_condition.values[i], f'{Machine_bad_condition.values[i]:.2f}', ha='center')

# Decrease
plt.subplot(2, 2, 3)
plt.bar(Decreased_difference.index.tolist(), Decreased_difference.values.tolist(), color='orange')
plt.title('⬇️ Mean Decrease During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Decreased_difference.index):
    plt.text(label, Decreased_difference.values[i], f'{Decreased_difference.values[i]:.2f}', ha='center')

# Increase
plt.subplot(2, 2, 4)
plt.bar(Increased_difference.index.tolist(), Increased_difference.values.tolist(), color='skyblue')
plt.title('⬆️ Mean Increase During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Increased_difference.index):
    plt.text(label, Increased_difference.values[i], f'{Increased_difference.values[i]:.2f}', ha='center')

plt.tight_layout(pad=2.0)
plt.show()

#                           MEDIAN ANALYSIS
Machine_good_condition_median = new_data[new_data['Downtime'] == 'No_Machine_Failure'].iloc[:, 3:13].median()
Machine_bad_condition_median = new_data[new_data['Downtime'] == 'Machine_Failure'].iloc[:, 3:13].median()
Decreased_difference_median = Machine_bad_condition_median[Machine_bad_condition_median.values < Machine_good_condition_median.values]
Increased_difference_median = Machine_bad_condition_median[Machine_bad_condition_median.values > Machine_good_condition_median.values]

plt.figure(figsize=(12, 8))
plt.suptitle('📊 Machine Performance Comparison (MEDIAN)', fontsize=16, fontweight='bold')

plt.subplot(2, 2, 1)
plt.bar(Machine_good_condition_median.index.tolist(), Machine_good_condition_median.values.tolist(), color='green')
plt.title('✅ Median - No Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_good_condition_median.index):
    plt.text(label, Machine_good_condition_median.values[i], f'{Machine_good_condition_median.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 2)
plt.bar(Machine_bad_condition_median.index.tolist(), Machine_bad_condition_median.values.tolist(), color='red')
plt.title('❌ Median - Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_bad_condition_median.index):
    plt.text(label, Machine_bad_condition_median.values[i], f'{Machine_bad_condition_median.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 3)
plt.bar(Decreased_difference_median.index.tolist(), Decreased_difference_median.values.tolist(), color='orange')
plt.title('⬇️ Median Decrease During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Decreased_difference_median.index):
    plt.text(label, Decreased_difference_median.values[i], f'{Decreased_difference_median.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 4)
plt.bar(Increased_difference_median.index.tolist(), Increased_difference_median.values.tolist(), color='skyblue')
plt.title('⬆️ Median Increase During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Increased_difference_median.index):
    plt.text(label, Increased_difference_median.values[i], f'{Increased_difference_median.values[i]:.2f}', ha='center')

plt.tight_layout(pad=2.0)
plt.show()

#                                 MAX ANALYSIS
Machine_good_condition_max = new_data[new_data['Downtime'] == 'No_Machine_Failure'].iloc[:, 3:13].max()
Machine_bad_condition_max = new_data[new_data['Downtime'] == 'Machine_Failure'].iloc[:, 3:13].max()
Decreased_difference_max = Machine_bad_condition_max[Machine_bad_condition_max.values < Machine_good_condition_max.values]
Increased_difference_max = Machine_bad_condition_max[Machine_bad_condition_max.values > Machine_good_condition_max.values]

plt.figure(figsize=(12, 8))
plt.suptitle('📊 Machine Performance Comparison (MAX)', fontsize=16, fontweight='bold')

plt.subplot(2, 2, 1)
plt.bar(Machine_good_condition_max.index.tolist(), Machine_good_condition_max.values.tolist(), color='green')
plt.title('✅ Max - No Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_good_condition_max.index):
    plt.text(label, Machine_good_condition_max.values[i], f'{Machine_good_condition_max.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 2)
plt.bar(Machine_bad_condition_max.index.tolist(), Machine_bad_condition_max.values.tolist(), color='red')
plt.title('❌ Max - Machine Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Machine_bad_condition_max.index):
    plt.text(label, Machine_bad_condition_max.values[i], f'{Machine_bad_condition_max.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 3)
plt.bar(Decreased_difference_max.index.tolist(), Decreased_difference_max.values.tolist(), color='orange')
plt.title('⬇️ Max Decrease During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Decreased_difference_max.index):
    plt.text(label, Decreased_difference_max.values[i], f'{Decreased_difference_max.values[i]:.2f}', ha='center')

plt.subplot(2, 2, 4)
plt.bar(Increased_difference_max.index.tolist(), Increased_difference_max.values.tolist(), color='skyblue')
plt.title('⬆️ Max Increase During Failure')
plt.xticks(rotation=45, ha='right')
for i, label in enumerate(Increased_difference_max.index):
    plt.text(label, Increased_difference_max.values[i], f'{Increased_difference_max.values[i]:.2f}', ha='center')

plt.tight_layout(pad=2.0)
plt.show()

# COMMON INCREASE AND DECREASE SUMMARY
mean_increase_labels = set(Increased_difference.index.to_list())
median_increase_labels = set(Increased_difference_median.index.to_list())
max_increase_labels = set(Increased_difference_max.index.to_list())
common_increased_labels = mean_increase_labels & median_increase_labels & max_increase_labels

mean_decrease_labels = set(Decreased_difference.index.to_list())
median_decrease_labels = set(Decreased_difference_median.index.to_list())
max_decrease_labels = set(Decreased_difference_max.index.to_list())
common_decrease_labels = mean_decrease_labels & median_decrease_labels & max_decrease_labels

# Final summary print
print("=" * 60)
print("🔍 Summary: Common Attribute Changes During Machine Downtime")
print("=" * 60)
print(f"✅ Attributes that consistently INCREASED during downtime:\n{sorted(common_increased_labels)}")
print(f"❌ Attributes that consistently DECREASED during downtime:\n{sorted(common_decrease_labels)}")
print("=" * 60)
print(data.columns)