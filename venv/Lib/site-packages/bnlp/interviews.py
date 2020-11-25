import re
#from __init__ import clean

d = {}
d['\u061f'] = "Inverted Question Mark"

def clean(text):
    return text

def getInterviewFromText(text):

    parts = [] 

    interview_group = re.search(ur"((?:<[^>]*>|\n)*(?:[^>\n]*\u061f)(?:<[^>]*>|\n)*([^<\n]*)(?:<[^>]*>|\n)*){2,10}", text)
    interview_text = interview_group.group(0)
    for chunk in re.finditer(ur"(?:(?:<[^>]*>|\n)*(?P<question>[^>\n]*\u061f)(?:<[^>]*>|\n)*(?P<answer>[^<\n]*)(?:<[^>]*>|\n)*){2,20}", text):
        groupdict = chunk.groupdict()
        for key in groupdict:
            part = {}
            part['question'] = clean(groupdict['question'])
            part['answer'] = clean(groupdict['answer'])
            if 'interviewee' in groupdict:
                part['interviewee'] = clean(groupdict['interviewee'])
            else:
                print "interviewee not captured so go get it!"
                print "interview_text.start() is", interview_group.start()

        
from requests import get
text = open("data/interview_example.html").read().decode("utf-8")
interview = getInterviewFromText(text)
#interview = getInterviewFromText(get("""http://www.syriahr.com/2015/07/%D8%B5%D8%A7%D9%84%D8%AD-%D9%85%D8%B3%D9%84%D9%85-%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%85-%D9%81%D9%82%D8%AF-%D8%B4%D8%B1%D8%B9%D9%8A%D8%AA%D9%87-%D9%88%D8%B3%D9%86%D9%82%D8%A7%D9%88%D9%85-%D8%A8%D9%83/""").text)

