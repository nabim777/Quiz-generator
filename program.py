#Image package to create Background
#IMage package to write in that background

from PIL import Image, ImageDraw, ImageFont
import textwrap
#Copy_to_path="/home/nabin/Documents/Dart practice/image generator/images"


class Question:
  def __init__(self, title, a, b, c, d, ans):
    self.title = title
    self.a = a
    self.b = b
    self.c = c
    self.d = d

question_list = [
Question("Most keyboards use an arrangement of keys given the name:","Dvork","QWERTY","Unicode","CISC","2"),
Question("A full-sized rigid, rectangular keyboard that includes function, navigational and numeric keys is this type:","PDA keyboard","Wireless keyboard","Traditional keyboard","Flexible keyboard","3"),
Question("This type of keyboard is designed specifically to alleviate wrist strain associated with the repetitive movements of typing.","Ergonomic keyboard","Wireless keyboard","Traditional keyboard","Flexible keyboard","1"),
Question("A key that turns a function on or off is called a ................ key.","Power","Toggle","Function","Control","2"),
Question("A full-sized rigid, rectangular keyboard that includes function, navigational and numeric keys is this type:","PDA keyboard","Wireless keyboard","Traditional keyboard","Flexible keyboard","3"),
]

count = 0;
for i in question_list:
    count+=1
    question = i.title
    question = textwrap.fill(text=question, width=40)
    answer1 = i.a
    answer2 = i.b
    answer3 = i.c
    answer4 = i.d
    new = Image.open('nalem7.png')
    d= ImageDraw.Draw(new)
    myFont = ImageFont.truetype('/home/nabin/Documents/Thulo Technology/image generator/generator/ffont.ttf', 50)
    myFont2 = ImageFont.truetype('/home/nabin/Documents/Thulo Technology/image generator/generator/GothamMedium.ttf', 34)
    d.text((722,488),question,fill=(255,255,255),font=myFont)
    d.text((818,780),answer1,fill=(255,255,255),font=myFont2)
    d.text((814,908),answer2,fill=(255,255,255),font=myFont2)
    d.text((820,1040),answer3,fill=(255,255,255),font=myFont2)
    d.text((818,1159),answer4,fill=(255,255,255),font=myFont2)
    new.save(f"image{count}.png")
    


