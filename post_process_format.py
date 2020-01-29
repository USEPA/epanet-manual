import re

filename = 'C:\\Users\\tbaranow\\epanet-manual\\_build\\latex\\EPANET.tex'
file = open(filename, 'r', encoding='utf8')

outfile = 'C:\\Users\\tbaranow\\epanet-manual\\_build\\latex\\EPANET_postprocess.tex'
outtex = open(outfile, 'w', encoding='utf8')

for tex in file.readlines():
    print(tex)
    
    tex = re.sub(r'\\documentclass\[letterpaper,10pt,english\]\{sphinxhowto\}', 
                 r'\\documentclass[10pt,english]{article}', tex)
    tex = re.sub(r'\\usepackage{geometry}', 
                 r'\\usepackage[a4paper,bindingoffset=0.2in,left=0.85in,right=0.85in,top=0.9in,bottom=0.9in,\nfootskip=.25in]{geometry}', tex)
    
    # Reformat title page
    tex = re.sub(r'\\title\{EPANET 2.2 Documentation\}', r'\\title{\\begin{footnotesize}\\begin{flushright}EPA/600/R-20/XXX\\\\February 2020\\end{flushright}\\end{footnotesize}\\vspace{20 mm}EPANET 2.2 User Manual}', tex)
    tex = re.sub(r'\\author\{\}', r'\\author{\\\\\\\\\\\\by\\\\\\\\Lewis Rossman\\\\Retired U.S. Environmental Protection Agency\\\\Office of Research and Development\\\\\\\\Hyoungmin Woo\\\\ORISE\\\\U.S. Environmental Protection Agency\\\\Office of Research and Development\\\\\\\\Michael Tryby, Feng Shang, and Terranna Haxton\\\\U.S. Environmental Protection Agency\\\\Office of Research and Development}', tex)
    tex = re.sub(r'\\date\{\w* \w*, \w*\}', r'\\date{}', tex)
    tex = re.sub(r'\\release\{2.2 \(DRAFT Documentation\)\}', r'\\release{}', tex)
    tex = re.sub(r'\\renewcommand\{\\releasename*\}\{Release\}', r'\\renewcommand{\\releasename}{}', tex)
    
    tex = re.sub(r'\\maketitle', r'\\maketitle\n\\clearpage', tex)
    tex = re.sub(r'\\begin\{document\}', r'\\begin{document}\n\\pagenumbering{roman}\n\\setcounter{page}{1}', tex)

    # remove section numbers
    tex = re.sub(r'\\section\{Disclaimer\}', r'\\section*{Disclaimer}', tex)
    tex = re.sub(r'\\section\{Acknowledgments\}', r'\\section*{Acknowledgments}', tex)
    tex = re.sub(r'\\section\{Abbreviations\}', r'\\section*{Abbreviations}', tex)
    # tex = re.sub(r'\\section\{Executive summary\}', r'\\section*{Executive summary}', tex)
        
    # replace link to API docs
    # tex = re.sub(r'See \\DUrole\{xref,std,std-ref\}\{api\\_documentation\}', 
                 # r'See the online API documentation at \url{https://epanet.readthedocs.io}', tex)
    
    # Reformat tables
    tex = re.sub(r'\{\|L\|L\|L\|\}', r'{|p{2in}|p{2in}|p{2in}|}', tex)
    tex = re.sub(r'\{\|L\|L\|\}', r'{|l|L|}', tex)
    
    tex = re.sub(r'\{\|T\|T\|T\|\}', r'{|p{2in}|p{2in}|p{2in}|}', tex)
    tex = re.sub(r'\{\|T\|T\|\}', r'{|l|L|}', tex)
    
    # remove header from reference section
    tex = re.sub(r'\\begin\{sphinxthebibliography\}\{USEPA14\}', r'\\renewcommand{\\refname}{}\n\\begin{sphinxthebibliography}{USEPA14}', tex)
    tex = re.sub(r'sphinxthebibliography', r'thebibliography', tex)
    
    # Reformat citations
    tex = re.sub(r'\\phantomsection\\label\{\\detokenize\{\w*:\w*\}\}\{\\hyperref\[\\detokenize\{reference:\w*\}\]\{\\sphinxcrossref\{\{\[\}(?P<name>\w*)\{\]\}\}\}\}', 
                 r'\\cite{\g<name>}', tex)
    tex = re.sub(r'\\bibitem\[(?P<name>\w*)\]\{\\detokenize\{\w*\}\}\{\\phantomsection\\label\{\\detokenize\{reference:\w*\}\}', 
                 r'\\bibitem{\g<name>}', tex) 
    
    #tex = re.sub(r'Due to limitations with cross referenced citations in reStructuredText \w* \end{footnote}.', r'', tex)
    
    outtex.write(tex)
    
file.close()
outtex.close()
