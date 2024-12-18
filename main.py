from adaptive_learning_engine import AdaptiveLearningEngine
from content_recommendation import ContentRecommendation
from progress_tracker import ProgressTracker

def main():
    # Initialize components
    ale = AdaptiveLearningEngine()
    cr = ContentRecommendation()
    pt = ProgressTracker()

    # Sample student and interaction
    student_id = "student_01"
    ale.add_student(student_id)

    # Update learning based on feedback
    ale.update_learning_path(student_id, {'visual': 1, 'auditory': -1, 'kinesthetic': 0})

    # Get current learning preferences
    learning_prefs = ale.get_learning_preferences(student_id)

    # Recommend content
    recommended_content = cr.recommend_content(learning_prefs)
    print(f"Recommended content for {student_id}: {recommended_content}")

    # Track progress
    pt.track_progress(student_id, "Math", 85.0)
    progress = pt.get_student_progress(student_id)
    print(f"Progress for {student_id}: {progress}")

if __name__ == "__main__":
    main()
