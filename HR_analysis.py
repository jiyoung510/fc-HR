import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        return self.data
    
    def map_columns(self, mappings):
        for column, map_dict in mappings.items():
            self.data[f"{column}_Value"] = self.data[column].replace(map_dict)
        return self.data
    
    def plot_performance_vs_metric(self, metric):
        """
        주어진 메트릭에 대한 박스플롯을 그린다.

        Args:
        metric (str): 데이터셋의 컬럼 이름.
        figsize (tuple): 그래프의 크기를 정의하는 튜플.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='PerformanceRating_Value', y=metric, data=self.data)
        plt.title(f'{metric} by Performance Rating')
        plt.xlabel('Performance Rating')
        plt.ylabel(metric)
        plt.show()

    def plot_bar_with_trend(self, category, metric):
        category_avg = self.data.groupby(category)[metric].mean().reset_index()

        plt.figure(figsize=(10, 6))
        barplot = sns.barplot(x=category, y=metric, data=category_avg, palette='muted')

        plt.plot(category_avg[category], category_avg[metric], marker='o', linestyle='-', color='red')

        plt.xlabel(category)
        plt.ylabel(f'Average {metric}')
        plt.title(f'Average {metric} by {category} with Trend Line')
        plt.tight_layout() 
        plt.show()

    def plot_performance_by_metric(self, metric):
        """주어진 메트릭을 기준으로 PerformanceRating의 분포를 막대 그래프로 나타내고 추이선을 추가한다."""
        # 주어진 메트릭 별로 성과 등급 카운트를 계산
        metric_counts = self.data.groupby([metric, 'PerformanceRating']).size().reset_index(name='Counts')
        
        # 막대 그래프 설정
        plt.figure(figsize=(12, 8))
        sns.barplot(x=metric, y='Counts', hue='PerformanceRating', data=metric_counts)
        
        # 추세선을 위한 데이터 준비
        # 각 메트릭 값별로 성과 등급의 평균을 계산
        metric_means = self.data.groupby(metric)['PerformanceRating'].mean().reset_index()

        # 추세선 추가
        sns.lineplot(x=metric, y='PerformanceRating', data=metric_means, marker='o', color='red', linewidth=2)
        
        # 축 레이블 및 타이틀 설정
        plt.xlabel(metric)
        plt.ylabel(f'Counts of Performance Rating')
        plt.title(f'Counts of Performance Rating by {metric} with Trend Line')
        plt.legend(title='Performance Rating')
        
        # X축에 대해 정수만 표시하도록 설정
        #plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.show()

    def get_stats_by_performance(self, metric):
        print(metric)
        return self.data.groupby('PerformanceRating_Value')[metric].describe()


file_path = 'C:\\Users\\hongj\\venv\\HR_anal\\data\\Expert_HR_data.csv'

analyzer = DataAnalyzer(file_path)
analyzer.load_data()

mappings = {
    'Education': {1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'},
    'EnvironmentSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'JobInvolvement': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'JobSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'PerformanceRating': {1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'},
    'RelationshipSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'WorkLifeBalance': {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'},
    'OverTime': {'Yes': 1, 'No': 0}
}

#analyzer.map_columns(mappings)
mapping_df = analyzer.map_columns(mappings)
mapping_df.to_csv('mapping.csv', index=False)

print('TotalWorkingYears')
stats1 = analyzer.get_stats_by_performance('TotalWorkingYears')
print(stats1)
analyzer.plot_performance_vs_metric('TotalWorkingYears')
analyzer.plot_performance_by_metric('TotalWorkingYears')

stats2 = analyzer.get_stats_by_performance('WorkLifeBalance')
print(stats2)
analyzer.plot_performance_vs_metric('WorkLifeBalance')
analyzer.plot_performance_by_metric('WorkLifeBalance')

stats3 = analyzer.get_stats_by_performance('StockOptionLevel')
print(stats3)
analyzer.plot_performance_vs_metric('StockOptionLevel')
analyzer.plot_performance_by_metric('StockOptionLevel')

stats4 = analyzer.get_stats_by_performance('YearsSinceLastPromotion')
print(stats4)
analyzer.plot_performance_vs_metric('YearsSinceLastPromotion')
analyzer.plot_performance_by_metric('YearsSinceLastPromotion')

stats5 = analyzer.get_stats_by_performance('OverTime_Value')
print(stats5)
analyzer.plot_performance_vs_metric('OverTime')
analyzer.plot_performance_by_metric('OverTime')