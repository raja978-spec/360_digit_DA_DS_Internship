import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Internship_Project/Dataset/Machine_Downtime.csv')
data = data.dropna()

#print(data.info())
# print(data.shape)

# FIRST MOVEMENT BUSINESS DECISION
Average = data.iloc[:,3:15].mean()
Median = data.iloc[:,3:15].median()
Mode = data.iloc[:,[0,1,2,15]].mode()

# print(Average.iloc[0])
# print(Median.iloc[0])
# print(Mode.iloc[0])

#   SECOND MOVEMENT BUSINESS DECISION
Std = data.iloc[:,3:15].std()
Variance = data.iloc[:,3:15].var()
Range = data.iloc[:,3:15].max() - data.iloc[:,3:15].min()

#print(Std)
#print(Variance)
#print(Range)

#  THIRD MOVEMENT BUSINESS DECISION
plt.figure(figsize=(12, 10)) 
columns = data.iloc[:, 3:15].columns

for i in range(len(columns)):
    plt.subplot(4, 3, i + 1)
    plt.hist(data[columns[i]], bins=20)
    plt.title(columns[i], fontsize=10)  
plt.suptitle('Third movement business decision')
plt.tight_layout(pad=2.0) 
plt.show()

#             FOURTH MOVEMENT BUSINESS DECISION
all_equipment_kurt = data.iloc[:, 3:15].kurt()
#print(all_equipment_kurt)


#                       EDA
new_data=data.drop(columns=['Spindle_Speed(RPM)'])
Machine_good_condition = new_data[new_data['Downtime']=='No_Machine_Failure'].iloc[:,3:13].mean()
Machine_bad_condition = new_data[new_data['Downtime']=='Machine_Failure'].iloc[:,3:13].mean()

plt.figure(figsize=(10,6))

plt.subplot(1,2,1).bar(Machine_good_condition.index.tolist(),
         Machine_good_condition.values.tolist(),
         color='green')
plt.title('Machine condition good')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_good_condition.index.tolist())):
    x=Machine_good_condition.index.tolist()
    y=Machine_good_condition.values.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='center')

plt.subplot(1,2,2).bar(Machine_bad_condition.index.tolist(),
         Machine_bad_condition.values.tolist(),
         color='red')
plt.title('Machine condition bad')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_bad_condition.index.tolist())):
    x=Machine_bad_condition.index.tolist()
    y=Machine_bad_condition.values.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='center')
plt.suptitle('Machine good and bad condition analysis')
plt.tight_layout(pad=2.0)
plt.show()

###############################################################################################
variance1 = Machine_good_condition.values - Machine_bad_condition.values
plt.figure(figsize=(10,6))
plt.subplot(2,2,1).plot(Machine_bad_condition.index.tolist(),
         variance1.tolist(),
         color='gold',
         marker='*',
         ms=10,
         mfc='red',
         mec='black')
plt.title('Mean analysis')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_bad_condition.index.tolist())):
    x=Machine_bad_condition.index.tolist()
    y=variance1.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='right', va='bottom')


#              MEDIAN
Machine_good_condition_median = new_data[new_data['Downtime']=='No_Machine_Failure'].iloc[:,3:13].median()
Machine_bad_condition_median = new_data[new_data['Downtime']=='Machine_Failure'].iloc[:,3:13].median()

variance2 = Machine_good_condition_median.values - Machine_bad_condition_median.values
plt.subplot(2,2,2).plot(Machine_bad_condition_median.index.tolist(),
         variance2.tolist(),
         color='gold',
         marker='*',
         ms=10,
         mfc='red',
         mec='black')
plt.title('Median Analysis')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_bad_condition_median.index.tolist())):
    x=Machine_bad_condition_median.index.tolist()
    y=variance2.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='right', va='bottom')


#              MAX
Machine_good_condition_max = new_data[new_data['Downtime']=='No_Machine_Failure'].iloc[:,3:13].max()
Machine_bad_condition_max = new_data[new_data['Downtime']=='Machine_Failure'].iloc[:,3:13].max()

variance3 = Machine_good_condition_max.values - Machine_bad_condition_max.values
plt.subplot(2,2,3).plot(Machine_bad_condition_max.index.tolist(),
         variance3.tolist(),
         color='gold',
         marker='*',
         ms=10,
         mfc='red',
         mec='black')
plt.title('Max Value Analysis')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_bad_condition_max.index.tolist())):
    x=Machine_bad_condition_max.index.tolist()
    y=variance3.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='right', va='bottom')


#              Standard
Machine_good_condition_var = new_data[new_data['Downtime']=='No_Machine_Failure'].iloc[:,3:13].var()
Machine_bad_condition_var = new_data[new_data['Downtime']=='Machine_Failure'].iloc[:,3:13].var()

variance4 = Machine_good_condition_max.values - Machine_bad_condition_max.values
plt.subplot(2,2,4).plot(Machine_bad_condition_var.index.tolist(),
         variance4.tolist(),
         color='gold',
         marker='*',
         ms=10,
         mfc='red',
         mec='black')
plt.title('Variance Value Analysis')
plt.xticks(rotation=45, ha='right')
for i in range(len(Machine_bad_condition_var.index.tolist())):
    x=Machine_bad_condition_var.index.tolist()
    y=variance4.tolist()
    data_point='{:.2f}'.format(y[i])
    plt.text(x[i],y[i],data_point, ha='right', va='bottom')

plt.tight_layout(pad=1.1)
plt.show()


