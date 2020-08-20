from com.ponder.reptiles.book import *

base = 'http://www.xuanshu.com/'
names = grab_name('http://www.xuanshu.com/sort/1.html')
for name in names:
    print(name.text)
    with open('E:\\ts\\'+name.text+'.txt', 'w', encoding='utf-8') as file:
        print(name['href'])
        chapterUrl = base+name['href']
        chapterList = get_chapter_list(chapterUrl)
        for chapter in chapterList:
            print(chapter)
            chapterContent = get_content(chapterUrl+chapter['href'])
            file.write("[["+chapter.text+"]]")
            file.write(chapterContent)
