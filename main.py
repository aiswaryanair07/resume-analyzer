from roles.job_roles import job_roles
from analyzer.skill_matcher import match_skills, extract_skills
from analyzer.education_matcher import edu_matcher
from utils.text_utils import case, read_resume
from scoring.score_calculator import skill_score, skill_score_msg
resume_text = read_resume("resume_data/sample_resume.txt")
resume=case(resume_text)
jobs={1:"ai engineer",2:"data scientist",3:"web developer"}

print("JOB ROLES: ","\n")
print(" 1. AI Engineer","\n","2.Data Scientist","\n","3.Web Developer","\n")
choice=int(input("Enter the job role you want: "))
job=jobs[choice]
print()

print(edu_matcher(resume))
print()

resume_skills=extract_skills(resume,job_roles[job])
missed,matched=match_skills(resume_skills,job_roles[job])
print("Needed Skills: ")
print(", ".join(job_roles[job]))
print()
if matched:
    print("Matched skills:")
    print(", ".join(matched))
else:
    print("😊 No matching skills found for this role yet.","\n","Don’t worry — this just means there’s room to learn and grow. Keep going!")
print()
if missed:
    print("Needs improvement in")
    print(", ".join(missed))
print()
s=len(matched)
score=skill_score(s,len(job_roles[job]))
print(score,'%',"skill matching")
print(skill_score_msg(score))
print()

