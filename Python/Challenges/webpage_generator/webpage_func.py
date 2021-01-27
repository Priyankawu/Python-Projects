import webbrowser

def createHTML_file(text):
    #create a file if it does not exist
    f=open("htmlfile.html","w")
    f.write("\
    <html> \n\
        <body> \n\
            <h1> \n\
            Stay tuned for our amazing summer sale!\n\
            </h1> \n\
        </body> \n\
    </html>"
     )
    f.close()
    #notice the r before the path: w/o it, it doesn't work
    url = r'C:\Users\sanjeev\GitHub\Python Projects\Python\Challenges\htmlfile.html'
    webbrowser.open(url,1)


#get entry text, inject in html file
def printText(self):
   print("method printText") 
