def skill(sample,skillsd):
    sample1=sample.lower()
    skills_list=[]
    for skill in skillsd:
        if skill in sample1:
            skills_list.append(skill)
    return skills_list