import PIL.Image
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter import messagebox

root = Tk(className="Images to Pdf Converter") 
root.geometry('500x300') 
root.configure(bg='violet')
text=Text(root,bg='black',fg='white',height=10)
text.insert(INSERT,"\t\t*** Images Selected ***\n")
l=[]
def open_file(): 
	file = askopenfile(mode ='r', filetypes =[('Image Files', '*.png')]) 
	path=file.name
	l.append(path)
	text.insert(INSERT,'Image '+str(l[-1])+' is selected .\n')
	text.config()
	text.pack()
	
img_list=[]
def completion():
   messagebox.showinfo( "pdfCOnverter", "PDF created \n Go and Check your Desktop")
def create_pdf():
	for i in range(1,len(l)):
		image= PIL.Image.open(l[i])
		im=image.convert("RGB")
		img_list.append(im)
	image = PIL.Image.open(l[0])
	im=image.convert("RGB")
	im.save(r'/home/noor/Desktop/pdf/PDFCREATED.pdf',save_all=True,append_images=img_list)
	
def clear():
	text.delete("1.0","end")
	text.insert(INSERT,"\t\t    *** Images Selected ***\n")
		
btn = Button(root, text ='Select Files',command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 
btn1 = Button(root, text ='Create PDF',command = lambda:[create_pdf(),completion(),clear()])

btn2 = Button(root, text ='Quit',command = root.destroy)
btn2.pack(side = BOTTOM, pady =5)
btn1.pack(side = BOTTOM,pady = 2)
mainloop() 

