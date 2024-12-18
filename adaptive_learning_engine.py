import numpy as np

class AdaptiveLearningEngine:
    def __init__(self):
        """
        Initialize the adaptive learning engine with a baseline model.
        """
        self.student_profiles = {}

    def add_student(self, student_id):
        """
        Add a new student to the system.
        
        Args:
            student_id (str): Unique identifier for the student.
        """
        # Initialize student profile with baseline learning preference weights
        self.student_profiles[student_id] = np.array([1.0, 1.0, 1.0])  # [visual, auditory, kinesthetic]

    def update_learning_path(self, student_id, feedback):
        """
        Update learning preferences based on feedback.
        
        Args:
            student_id (str): Unique identifier for the student.
            feedback (dict): Dictionary with feedback on learning styles, e.g. {'visual': 1, 'auditory': -1, 'kinesthetic': 0}
        """
        profile = self.student_profiles.get(student_id)
        if profile is not None:
            for key, value in feedback.items():
                index = ['visual', 'auditory', 'kinesthetic'].index(key)
                profile[index] += value
            self.student_profiles[student_id] = profile / profile.sum()  # Normalize

    def get_learning_preferences(self, student_id):
        """
        Get current learning preferences for the student.
        
        Args:
            student_id (str): Unique identifier for the student.
            
        Returns:
            np.array: Normalized weights for learning styles.
        """
        return self.student_profiles.get(student_id, np.array([1.0, 1.0, 1.0]))
