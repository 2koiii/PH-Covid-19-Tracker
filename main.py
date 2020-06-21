from tkinter import *
import requests
import json

root = Tk()
root.title('COVID-19 Tracker')
root.geometry('400x200')
root.resizable(width='False', height='False')
# root.iconbitmap('icons/virus.ico')

def rfrsh():
    global resframe

    resframe.pack_forget()

    resframe = LabelFrame(root, text='Updates')
    resframe.pack(fill=BOTH, padx=5, pady=5, side=TOP)
    
    try:
        api_requests = requests.get("https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true")
        api = json.loads(api_requests.content)
        confirmed = "{:,}".format(api['infected'])
        recovered = "{:,}".format(api['recovered'])
        deaths = "{:,}".format(api['deceased'])
    except Exception as e:
        api = 'Not connected'
    
    confirmed = Label(resframe, text='Confirmed: ' + confirmed, fg='black')
    confirmed.grid(row=1, column=0, sticky='w')

    deaths = Label(resframe, text='Deaths: ' + deaths, fg='red')
    deaths.grid(row=2, column=0, stick='w')

    recovered = Label(resframe, text='Recovered: ' + recovered, fg='green')
    recovered.grid(row=3, column=0, stick='w')

title = Label(root, text='COVID-19 Tracker', bg='black', fg='yellow').pack(fill=X, pady=5)

srchlbl = Label(root, text='PHILIPPINES', font=('Helvetical', 20, 'bold')).pack(padx=5)
rfrshbtn = Button(root, text='Refresh', width=10, command=rfrsh).pack(padx=5, side=TOP, pady=5)
  
resframe = LabelFrame(root, text='Updates')
resframe.pack(fill=X, padx=5, pady=5, side=TOP)
 
try:
    api_requests = requests.get("https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true")
    api = json.loads(api_requests.content)
    confirmed = "{:,}".format(api['infected'])
    recovered = "{:,}".format(api['recovered'])
    deaths = "{:,}".format(api['deceased'])
except Exception as e:
    api = 'Not connected'

confirmed = Label(resframe, text='Confirmed: ' + confirmed, fg='black').grid(row=1, column=0, sticky='w')
deaths = Label(resframe, text='Deaths: ' + deaths, fg='red').grid(row=2, column=0, stick='w')
recovered = Label(resframe, text='Recovered: ' + recovered, fg='green').grid(row=3, column=0, stick='w')

root.mainloop()
