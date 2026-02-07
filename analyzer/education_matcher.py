def edu_matcher(resume):
    edu=["btech","b.tech","b-tech","bachelor","be","bca"]
    b=["ai","ds","data science","machine learning","cse","computer science"]
    for i in edu:
        if i in resume:
            for j in b:
                if i in resume:
                    return "Education requirements met."
    else:
        return "Education requirements not met."
    