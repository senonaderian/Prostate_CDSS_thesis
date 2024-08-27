def recommend_treatment(gleason_score, pirads_score):
    """
    Recommend treatment based on Gleason score and PI-RADS score.
    """
    if gleason_score >= 7 and pirads_score in [4, 5]:
        return "Recommend radical prostatectomy"
    elif gleason_score < 7 and pirads_score in [1, 2, 3]:
        return "Monitor and reassess"
    else:
        return "Consult clinical guidelines"

# Example usage
patient_gs = 8
patient_pirads = 5
recommendation = recommend_treatment(patient_gs, patient_pirads)
print(f"Treatment Recommendation: {recommendation}")
