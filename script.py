import os

ext_img=['jpg','jpeg','png']
ext_vid=['mp4','mkv','avi']
ext_doc=['pdf','docx','ppt']
ext_comp=['zip','tar']
ext_inst=['dmg','iso','exe']

dir_item=['movie','image',"module",'Compression','installation']
downloads_path = os.path.expanduser('~/Downloads')+'/'
print(downloads_path)
files=os.listdir()
for dir in dir_item:
    if not os.path.exists(downloads_path+dir):
        os.mkdir(downloads_path+dir)
