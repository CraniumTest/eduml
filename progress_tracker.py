class ProgressTracker:
    def __init__(self):
        """
        Initializes the progress tracker.
        """
        self.progress_data = {}

    def track_progress(self, student_id, topic, score):
        """
        Track progress of a student in a specific topic.
        
        Args:
            student_id (str): Unique identifier for the student.
            topic (str): Name of the topic.
            score (float): Score achieved by the student.
        """
        if student_id not in self.progress_data:
            self.progress_data[student_id] = {}
        self.progress_data[student_id][topic] = score

    def get_student_progress(self, student_id):
        """
        Retrieve the progress data for a given student.
        
        Args:
            student_id (str): Unique identifier for the student.
            
        Returns:
            dict: Progress scores by topic.
        """
        return self.progress_data.get(student_id, {})
