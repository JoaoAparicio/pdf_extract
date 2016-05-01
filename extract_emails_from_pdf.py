import re, sys

import pdf

if len(sys.argv) != 2:
    print 'Syntax: ' + sys.argv[0] + ' filename'
    exit()

emailregex = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'

pdffilename = sys.argv[1]
m = pdf.convert_pdf_to_txt(pdffilename)
res = m.split()
#for r in res:
#    print r

emails = set()
for line in res:
    m = re.findall(emailregex, line.upper())
    if m:
        for i in m:
            emails.add(i)

for email in emails:
    print email.lower()

