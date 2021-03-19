#Regex email extractor 

import re

string = "pytest@yahooooo.in, NEW DELHIFC-26, SHASTRI PARK, DELHI – 110 053 contact@gmail.ac.in hello@outlook.com http:/www.cmdgitmdelh.ac.in"

email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",string)

print(email)