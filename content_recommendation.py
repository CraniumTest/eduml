class ContentRecommendation:
    def __init__(self):
        """
        Initialize the content recommendation system with educational resources.
        """
        self.resources = {
            'visual': ['VisualResource1', 'VisualResource2'],
            'auditory': ['AuditoryResource1', 'AuditoryResource2'],
            'kinesthetic': ['KinestheticResource1', 'KinestheticResource2']
        }

    def recommend_content(self, learning_prefs):
        """
        Recommend content based on learning preferences.
        
        Args:
            learning_prefs (np.array): Normalized learning preference weights.
        
        Returns:
            list: Recommended resources tailored to learning preferences.
        """
        scores = {style: weight for style, weight in zip(['visual', 'auditory', 'kinesthetic'], learning_prefs)}
        recommended = []
        for style in sorted(scores, key=scores.get, reverse=True):
            recommended.extend(self.resources[style][:2])  # Take top 2 resources from each preferred style
        return recommended
