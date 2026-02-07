def case(r):
    resume=r.lower()
    return resume

def read_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        resume_text = file.read()
    return resume_text
    
