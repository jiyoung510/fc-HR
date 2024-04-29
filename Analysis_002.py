import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 파일 로드
data_path = 'C:\\Users\\hongj\\venv\\HR_anal\\data\\Expert_HR_data.csv'
hr_data = pd.read_csv(data_path)

# 수치형 데이터에 대한 상관관계 계산
correlation_matrix = hr_data.corr()

# PerformanceRating과의 상관관계를 특별히 보기
performance_corr = correlation_matrix["PerformanceRating"].sort_values(ascending=False)

# 상관관계 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

performance_corr
