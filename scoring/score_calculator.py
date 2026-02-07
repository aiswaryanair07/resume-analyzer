def skill_score(s,total):
    score=(s/total)*100
    return round(score,2)

def skill_score_msg(score):
    if score<=100 and score>=80:
        return "Excellent fit!"
    elif score<80 and score>=60:
        return "Good match, minor improvements needed."
    elif score<60 and score>=40:
        return "Partial match, upskilling recommended."
    else:
        return "Significant skill gap!"
