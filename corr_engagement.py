# calculate the Pearson's correlation between two variables
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

timestamps = np.arange(1, 25, 1)
timestamps_cleaned = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

engagement = np.array([70, 70, 78, 78, 76, 78, 79, 76, 72, 77, 82, 82, 80, 73, 68, 72, 77, 80, 81, 79, 78, 79, 78, 71])
engagement_cleaned = np.array([70, 70, 78, 78, 76, 78, 79, 76, 72, 68, 72, 77, 80, 81, 79, 78, 79, 78, 71])
communication = np.array([20, 45, 38, 18, 24, 20, 11, 20, 20, 16, 4, 1, 8, 41, 20, 32, 19, 20, 20, 19, 20, 21, 2, 18])
communication_cleaned = np.array([20, 45, 38, 18, 24, 20, 11, 20, 20, 20, 32, 19, 20, 20, 19, 20, 21, 2, 18])

print(len(engagement_cleaned))
print(len(timestamps_cleaned))
# All data
avg_engagement = np.average(engagement)
print("Average engagement: " + str(avg_engagement))
avg_communication = np.average(communication)
print("Average communication: " + str(avg_communication))
residuals_engagement = engagement - avg_engagement
print(residuals_engagement)
residuals_communication = communication - avg_communication
print(residuals_communication)
plt.scatter(timestamps, engagement, color ='blue')
plt.show()

# Minus summer sprints
avg_engagement_cleaned = np.average(engagement_cleaned)
print("Average engagement minus summer: " + str(avg_engagement_cleaned))
avg_communication_cleaned = np.average(communication_cleaned)
print("Average communication minus summer: " + str(avg_communication_cleaned))
residuals_engagement_cleaned = engagement_cleaned - avg_engagement_cleaned
print(residuals_engagement_cleaned)
residuals_communication_cleaned = communication_cleaned - avg_communication_cleaned
print(residuals_communication_cleaned)
plt.scatter(timestamps_cleaned, engagement_cleaned, color ='red')
plt.show()

plt.hist(residuals_engagement, color = 'blue')
plt.show()
plt.hist(residuals_communication, color = 'blue')
plt.show()

plt.hist(residuals_engagement_cleaned, color = 'red')
plt.show()
plt.hist(residuals_communication_cleaned, color = 'red')
plt.show()

# calculate Pearson's correlation
plt.scatter(communication, engagement, color ='blue')
plt.show()
plt.scatter(communication_cleaned, engagement_cleaned, color ='red')
plt.show()
corr, _ = pearsonr(engagement, communication)
print('Pearsons correlation: %.3f' % corr)
corr2, _ = pearsonr(engagement_cleaned, communication_cleaned)
print('Pearsons correlation minus five summer sprints: %.3f' % corr2)