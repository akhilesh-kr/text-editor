import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title('TextPad')
#...................main menu...........................
main_menu=tk.Menu()
#........................file................................
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

file=tk.Menu(main_menu,tearoff=0)

#---------------------------------edit--------------------------------
cut_icon=tk.PhotoImage(file='icons2/cut.png')
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')

edit=tk.Menu(main_menu,tearoff=0)

#---------------------------------view---------------------------
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')

view=tk.Menu(main_menu,tearoff=0)

#--------------------------colortheme-----------------------------
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')

color_theme=tk.Menu(main_menu,tearoff=0)
theme_choice=tk.StringVar()
color_icons=(light_default_icon,dark_icon)

#--------------------help----------------------
Help=tk.Menu(main_menu,tearoff=0)
Help.add_command(label='About TextPad',compound=tk.LEFT,accelerator='ctrl+H')

#-------------------cascade-----------------------
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='ColorTheme',menu=color_theme)
main_menu.add_cascade(label='Help',menu=Help)
#---------------------toolbar-------------------
#----------------------font_box-------------------
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuples
font_box.current=(font_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
#--------------------size_box------------------------------
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(0,85))
font_size.current=(14)
font_size.grid(row=0,column=1,padx=5)
#-----------------boldbutton-- ------------------
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#-----------------italic_btn----------------
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#-----------------underline_btn-------------------
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#-----------------font_color_btn-----------------
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
#-----------------left_align-------------
left_align_icon=tk.PhotoImage(file='icons2/align_left.png')
left_align_btn=ttk.Button(tool_bar,image=left_align_icon)
left_align_btn.grid(row=0,column=6,padx=5)
#------------------center_align--------------
center_align_icon=tk.PhotoImage(file='icons2/align_center.png')
center_align_btn=ttk.Button(tool_bar,image=center_align_icon)
center_align_btn.grid(row=0,column=7,padx=5)
#-------------------right_align--------------------------
right_align_icon=tk.PhotoImage(file='icons2/align_right.png')
right_align_btn=ttk.Button(tool_bar,image=right_align_icon)
right_align_btn.grid(row=0,column=8,padx=5)
#------------------rext_editor------------------------------
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
#--------------scroll-bar---------------
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
current_font_family='Arial'
current_font_size='12'
#---------------------function-------------------------
def change_font(event=None):
	global current_font_family
	current_font_family=font_family.get()
	text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
	global current_font_size
	current_font_size=size_var.get()
	text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)

def change_bold():
	text_property=tk.font.Font(font=text_editor['font'])
	if text_property.actual()['weight']=='normal':
		text_editor.configure(font=(current_font_family,current_font_size,'bold'))
	if text_property.actual()['weight']=='bold':
		text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

def change_italic():
        text_property=tk.font.Font(font=text_editor['font'])
        if text_property.actual()['slant']=='roman':
                text_editor.configure(font=(current_font_family,current_font_size,'italic'))
        if text_property.actual()['slant']=='italic':
                text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)

def change_underline():
        text_property=tk.font.Font(font=text_editor['font'])
        if text_property.actual()['underline']==0:
                text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        if text_property.actual()['underline']==1:
                text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

def change_font_color():
        color_var=tk.colorchooser.askcolor()
        text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

def align_left():
        text_content=text_editor.get(1.0,'end')
        text_editor.tag_config('left',justify=tk.LEFT)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_content,'left')
left_align_btn.configure(command=align_left)

def align_center():
        text_content=text_editor.get(1.0,'end')
        text_editor.tag_config('center',justify=tk.CENTER)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_content,'center')
center_align_btn.configure(command=align_center)

def align_right():
        text_content=text_editor.get(1.0,'end')
        text_editor.tag_config('right',justify=tk.RIGHT)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_content,'right')
right_align_btn.configure(command=align_right)

                


text_editor.configure(font=('Arial',12))
#---------------------status_bar----------------------
status_bar=tk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_changed=False

def changed(event=None):
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters:{characters} Words:{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)

url =''
def new_file(event=None):
	global url 
	url=''
	text_editor.delete(1.0,tk.END)


def open_file(event=None):
	global url
	url =filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
	try:
		with open(url,'r') as fr:
			text_editor.delete(1.0,tk.END)
			text_editor.insert(1.0,fr.read())
	except FileNotFoundError:
		return
	except:
		return
	main_application.title(os.path.basename(url))

def save_file(event=None):
	global url
	try:
		if url:
			content=str(text_editor.get(1.0,tk.END))
			with open(url,'w',encoding='utf-8')as fw:
				fw.write(content)
		else:
			url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All files','*.*')))
			content2=text_editor.get(1.0,tk.END)
			url.write(content2)
			url.close()
	except:
		return

def save_as_file(event=None):
	global url
	try:
		content=text_editor.get(1.0,tk.END)
		url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All files','*.*')))
		url.write(content)
		url.close()
	except:
		return


#-----------------------menucommands-----------------------
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)
file.add_command(label='save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
file.add_command(label='save As',image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+shift+S',command=save_as_file)
file.add_command(label='exit',image=exit_icon,compound=tk.LEFT,accelerator='alt+F4')
#---------------------------------edit commands-------------
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+C')
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+X')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+V')
#---------------------------------view commands-------------------------
view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)
#-------------------------------color theme command----------------------------
color_dict={
'light Default':('#000000','#ffffff'),
'Dark':('#c4c4c4','2d2d2d')
}
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count=count+1
#-----------------------------help command---------------------
    


















main_application.config(menu=main_menu)
main_application.mainloop()
