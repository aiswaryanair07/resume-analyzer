def extract_skills(resume_text, job_skills):
    skill_list=[]
    for skill in job_skills:
        if skill in resume_text:
            skill_list.append(skill)
    return skill_list

def match_skills(skill_list,job_skills):
    missed=[]
    matched=[]
    for skill in job_skills:
        if skill not in skill_list:
            missed.append(skill)
        else:
            matched.append(skill)
    return missed, matched

    
