import webbrowser

def createHTML_file(text):
    #create a file if it does not exist
    f=open("htmlfile.html","w")
    
    html_string="\
    <html> \n\
        <body> \n\
            <h1> \n\
            {} \n\
            </h1> \n\
        </body> \n\
    </html>".format(text)

    f.write(html_string)
    f.close()
    #notice the r before the path: w/o it, it doesn't work
    url = r'C:\Users\sanjeev\GitHub\Python Projects\Python\Challenges\htmlfile.html'
    webbrowser.open_new_tab(url) # 0 says to open in same browser, 1 opens new browser

if __name__=="__main__":
    pass
