import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.mappings = {
            'Education': {1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'},
            'EnvironmentSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
            'JobInvolvement': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
            'JobSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
            'PerformanceRating': {1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'},
            'RelationshipSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
            'WorkLifeBalance': {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'}
        }
        
    def load_and_process_data(self):
        self.data = pd.read_csv(self.file_path)
        
        for column, mapping in self.mappings.items():
            self.data[column] = self.data[column].map(mapping)
            
        return self.data

file_path = '/mnt/data/데이터분석_Expert_HR_data.csv'

data_processor = DataProcessor(file_path)
processed_data = data_processor.load_and_process_data()

processed_data.head()
