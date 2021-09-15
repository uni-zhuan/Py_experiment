from image_extract import *

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')
filename=list('0')

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file(filename)
)
open_button.pack(expand=True)

# run the application
root.mainloop()
# print(filename[0])
pdffile=file_conducter(filename[0])
pdffile.xlssetting()
pdffile.doisearch()
pdffile.extractimages()
for i in range(1,pdffile.num+1,1):
    pdffile.sheet.range('A%s'%(i+2)).value="img%s"%(i)
    fileName = r'E:\study\Experiments\python_calu\indvl_ex\images\图片%s.png'%(i)
    pdffile.add_center("B%s"%(i+2), column_width=50)

pdffile.FIGsearch1()
pdffile.FIGsearch2()  
    
pdffile.xlwbook.save('ExtractImages.xlsx')
pdffile.xlwbook.close()


