chapters = [
      'chapters/dirac_ch1.md',
      'chapters/dirac_ch2.md',
      'chapters/dirac_ch3.md',
      'chapters/dirac_ch4.md',
      'chapters/dirac_ch5.md',
      'chapters/dirac_ch6.md',
      'chapters/dirac_ch7.md',
      'chapters/dirac_ch8.md',
      'chapters/dirac_ch9.md',
      'chapters/dirac_ch10.md',
      'chapters/dirac_ch11.md',
      'chapters/dirac_ch12.md',
        ]

for c in chapters:
    with open(c,'r') as chapter_file:
        chapter = chapter_file.read().split('\n')
        section_indices = []
        for i in range(len(chapter)):
            if (chapter[i].startswith('#') and chapter[i][1].isdigit()):
                section_indices.append(i)
        section_indices.append(len(chapter))

        for i in range(len(section_indices)-1):
            index1 = section_indices[i]
            index2 = section_indices[i+1]
            section_num = chapter[index1][1:].split(' ')[0][:-1]
            print section_num, chapter[index1]
            with open('sections/dirac'+section_num+'.md','w') as section:
                section.write('\n'.join(chapter[index1:index2]))

