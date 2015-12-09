global statusCodes
statusCodes = {200: ('OK', 'Request fulfilled, document follows'), 201: ('Created', 'Document created, URL follows'), 202: ('Accepted', 'Request accepted, processing continues off-line'), 203: ('Non-Authoritative Information', 'Request fulfilled from cache'), 204: ('No Content', 'Request fulfilled, nothing follows'), 205: ('Reset Content', 'Clear input form for further input.'), 206: ('Partial Content', 'Partial content follows.'), 400: ('Bad Request', 'Bad request syntax or unsupported method'), 401: ('Unauthorized', 'No permission -- see authorization schemes'), 402: ('Payment Required', 'No payment -- see charging schemes'), 403: ('Forbidden', 'Request forbidden -- authorization will not help'), 404: ('Not Found', 'Page not found on server'), 405: ('Method Not Allowed', 'Specified method is invalid for this server.'), 406: ('Not Acceptable', 'URI not available in preferred format.'), 407: ('Proxy Authentication Required', 'You must authenticate with this proxy before proceeding.'), 408: ('Connection Failed', 'Request timed out; try again later.'), 409: ('Conflict', 'Connection Reset/Request conflict.'), 410: ('Gone', 'URI no longer exists and has been permanently removed.'), 411: ('Length Required', 'Client must specify "Content-Length".'), 412: ('Precondition Failed', 'Precondition in headers is false.'), 413: ('Request Entity Too Large', 'Entity is too large.'), 414: ('Request-URI Too Long', 'URI is too long.'), 415: ('Unsupported Media Type', 'Entity body in unsupported format.'), 416: ('Requested Range Not Satisfiable', 'Cannot satisfy request range.'), 417: ('Expectation Failed', 'Expect condition could not be satisfied.'), 100: ('Continue', 'Request received, please continue'), 101: ('Switching Protocols', 'Switching to new protocol; obey Upgrade header'), 300: ('Multiple Choices', 'Object has several resources -- see URI list'), 301: ('Moved Permanently', 'Object moved permanently -- see URI list'), 302: ('Found', 'Object moved temporarily -- see URI list'), 303: ('See Other', 'Object moved -- see Method and URL list'), 304: ('Not Modified', 'Document has not changed since given time'), 305: ('Use Proxy', 'You must use proxy specified in Location to access this resource.'), 307: ('Temporary Redirect', 'Object moved temporarily -- see URI list'), 500: ('Internal Server Error', 'An error occurred within the server'), 501: ('Not Implemented', 'Server does not support this operation'), 502: ('Bad Gateway', 'Invalid responses from another server/proxy.'), 503: ('Service Unavailable', 'The server cannot process the request due to a high server load'), 504: ('Gateway Timeout', 'The gateway server did not receive a timely response'), 505: ('HTTP Version Not Supported', 'Cannot fulfill request.')}
global error_codes
error_codes = {111:('Invalid Argument','An internal function raised exception due to invalid argument(s)'), -128: ('Non-Authoritative Information', 'Request fulfilled from cache'), -127: ('Accepted', 'Request accepted, processing continues off-line'), -126: ('Created', 'Document created, URL follows'), -125: ('OK', 'Request fulfilled, document follows'), 146: ('Malformed JSON object', 'JSON Presented is an invalid format'), -429: ('Gateway Timeout', 'The gateway server did not receive a timely response'), -428: ('Service Unavailable', 'The server cannot process the request due to a high server load'), -427: ('Bad Gateway', 'Invalid responses from another server/proxy.'), -426: ('Not Implemented', 'Server does not support this operation'), -425: ('Internal Server Error', 'An error occurred within the server'), -232: ('Temporary Redirect', 'Object moved temporarily -- see URI list'), -230: ('Use Proxy', 'You must use proxy specified in Location to access this resource.'), -229: ('Not Modified', 'Document has not changed since given time'), -228: ('See Other', 'Object moved -- see Method and URL list'), -227: ('Found', 'Object moved temporarily -- see URI list'), -226: ('Moved Permanently', 'Object moved permanently -- see URI list'), -225: ('Multiple Choices', 'Object has several resources -- see URI list'), -430: ('HTTP Version Not Supported', 'Cannot fulfill request.'), -26: ('Switching Protocols', 'Switching to new protocol; obey Upgrade header'), -25: ('Continue', 'Request received, please continue'), -342: ('Expectation Failed', 'Expect condition could not be satisfied.'), -341: ('Requested Range Not Satisfiable', 'Cannot satisfy request range.'), -340: ('Unsupported Media Type', 'Entity body in unsupported format.'), -339: ('Request-URI Too Long', 'URI is too long.'), -338: ('Request Entity Too Large', 'Entity is too large.'), -337: ('Precondition Failed', 'Precondition in headers is false.'), -336: ('Length Required', 'Client must specify "Content-Length".'), -335: ('Gone', 'URI no longer exists and has been permanently removed.'), -334: ('Conflict', 'Connection Reset/Request conflict.'), -333: ('Connection Failed', 'Request timed out; try again later.'), -332: ('Proxy Authentication Required', 'You must authenticate with this proxy before proceeding.'), -331: ('Not Acceptable', 'URI not available in preferred format.'), -330: ('Method Not Allowed', 'Specified method is invalid for this server.'), -329: ('Not Found', 'Page not found on server'), -328: ('Forbidden', 'Request forbidden -- authorization will not help'), -327: ('Payment Required', 'No payment -- see charging schemes'), -326: ('Unauthorized', 'No permission -- see authorization schemes'), -325: ('Bad Request', 'Bad request syntax or unsupported method'), -131: ('Partial Content', 'Partial content follows.'), -130: ('Reset Content', 'Clear input form for further input.'), -129: ('No Content', 'Request fulfilled, nothing follows')}
global blank_zip
blank_zip = b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
global blank_svg
blank_svg = b'<svg version="1.1" width="2" height="2" viewBox="-1 -1 2 2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"></svg>'
global error_code
error_code = None
import subprocess
packages = ['requests']
try:
    import pip
except:
    pass
for x in packages:
    try:
        exec('import ' + x)
    except:
        pip.main(['install',x])
import requests
import os
import traceback
import pprint
import time
import io
import zipfile
import json
import getpass
import tkinter
import webbrowser
import tkinter.filedialog
import tkinter.scrolledtext as sct
import tkinter.simpledialog as sd
import tkinter.messagebox as db
from tkinter import *
from tkinter.ttk import *
def downloadProject(pk): # GUI
    try:
        downUrl = 'http://projects.scratch.mit.edu/internalapi/project/' + str(pk) + '/get/'
        def st(text2):
            lbl.config(text=text2)
            lbl.update()
        def per(num, denom, obj=str):
            try:
                return obj(int(num / denom * 100))
            except:
                return obj(0)
        def getAsset(md5):
            class ret: pass
            try:
                ct = s.get('http://cdn.assets.scratch.mit.edu/internalapi/asset/' + str(md5) + '/get/',headers=headers)
                istr = io.BytesIO(ct.content).read()
            except:
                rt = {'iostream':None,'code':-1}
            else:
                rt = {'iostream':istr,'code':ct.status_code}
            ret.code = rt['code']; ret.iostream = rt['iostream']
            return ret
        def processAsset(fid, md5, path, tp): #j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]
            if path['node'] is not None:
                try:
                    bad_code = 0
                    stream = getAsset(md5)
                    n = int(str(stream.code)[0])
                    if not ((n > 1) and (n < 4)):
                        bad_code = 1
                        raise RuntimeError()
                    ext = os.path.splitext(md5)[1]
                    if tp == 'imageLayer':
                        j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['baseLayerID'] = int(fid)
                    elif tp == 'textLayer':
                        j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['textLayerID'] = int(fid)
                    else:
                        j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['soundID'] = int(fid)
                    zipf.writestr(str(fid) + ext, stream.iostream)
                except:
                    return {'success':False, 'error':bad_code, 'statusCode':stream.code}
                else:
                    return {'success':True, 'error':None, 'statusCode':stream.code}
            else:
                try:
                    bad_code = 0
                    stream = getAsset(md5)
                    n = int(str(stream.code)[0])
                    if not ((n > 1) and (n < 4)):
                        bad_code = 1
                        raise RuntimeError()
                    ext = os.path.splitext(md5)[1]
                    if tp == 'imageLayer':
                        j[path['assetType']][path['assetIndex']]['baseLayerID'] = int(fid)
                    elif tp == 'textLayer':
                        j[path['assetType']][path['assetIndex']]['textLayerID'] = int(fid)
                    else:
                        j[path['assetType']][path['assetIndex']]['soundID'] = int(fid)
                    zipf.writestr(str(fid) + ext, stream.iostream)
                except:
                    traceback.print_exc()
                    return {'success':False, 'error':bad_code, 'statusCode':stream.code}
                else:
                    return {'success':True, 'error':None, 'statusCode':stream.code}
        def processAssetContent(fid, stream, path, tp, ext): #j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]
            if tp == 'imageLayer':
                j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['baseLayerID'] = int(fid)
            elif tp == 'textLayer':
                j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['textLayerID'] = int(fid)
            else:
                j[path['node']][path['spriteIndex']][path['assetType']][path['assetIndex']]['soundID'] = int(fid)
            zipf.writestr(str(fid) + ext, stream)
        global l
        l = Tk()
        l.title('Project Downloader')
        lbl = Label(l, text='0% Getting Project...', font=['Calabri',10])
        lbl.pack(side=TOP)
        sct = ScrolledText(l)
        l.update()
        pjson = s.get(downUrl,headers=headers)
        sct.print('Got JSON. Looking up project in API...')
        info = s.get('https://scratch.mit.edu/api/v1/project/' + str(pk) + '/?format=json',headers=headers)
        sct.print('Done.')
        sct.print('Status Code ' + str(pjson.status_code))
        if not pjson.status_code == 200: # See if status code is 200
            l.destroy()
            return {'status':'error','error':'Scratch Website threw bad status code','code':encodeStatus(pjson.status_code),'stack':False}
        try:
            j = pjson.json() # Try to parse JSON
        except BaseException as e:
            l.destroy()
            return {'status':'error','error':'JSON threw bad JSON exception','stack':True,'code':146}
        sct.print('Reading info...')
        try:
            info = info.json()
        except:
            sct.print('Couldn\'t read info, is it not shared?')
            info = {'title':'Scratch Project'}
        else:
            sct.print('Done.')
        st('100% Getting Project')
        sct.print('Buffering...')
        buf = io.BytesIO(blank_zip)
        zipf = zipfile.ZipFile(buf, mode='w')
        sct.print('Looking for assets')
        st('0% Looking Up Assets')
        assets = []
        imgCount = 0
        sfxCount = 0
        listIndex = -1
        if not ('costumes' in j):
            db.showwarning('Project Downloader', '"costumes" is missing in "' + '__stage__' + '". This is likely a corruption. The project will be fixed, note that the scratch editor will take a while to assign the costume a new md5')
            sct.print('WARN: Costumes missing')
            j['costumes'] = []
            j['costumes'].append({"costumeName": "costume-1", "baseLayerID": -1,"baseLayerMD5": "cd21514d0531fdffb22204e0ec5ed84a.svg","bitmapResolution": 1,"rotationCenterX": 240,"rotationCenterY": 180})
        if len(j['costumes']) == 0:
            db.showwarning('Project Downloader', '"costumes" is empty in "' + '__stage__' + '". This is likely a corruption. The project will be fixed, note that the scratch editor will take a while to assign the costume a new md5')
            sct.print('WARN: Costumes tag empty. Fixing...')
            j['costumes'].append({"costumeName": "costume-1", "baseLayerID": -1,"baseLayerMD5": "cd21514d0531fdffb22204e0ec5ed84a.svg","bitmapResolution": 1,"rotationCenterX": 240,"rotationCenterY": 180})
        for y in j['costumes']:
            listIndex = listIndex + 1
            sct.print('__stage__' + '>' + y['costumeName'])
            assets.append({'id':imgCount,'md5':y['baseLayerMD5'],'route':{'node':None,'spriteIndex':None,'assetType':'costumes','assetIndex':listIndex},'type':'imageLayer','display':'__stage__' + '>☼' + y['costumeName']})
            imgCount = imgCount + 1
            if 'textLayerID' in y:
                assets.append({'id':imgCount,'md5':y['textLayerMD5'],'route':{'node':None,'spriteIndex':None,'assetType':'costumes','assetIndex':listIndex},'type':'textLayer', 'display':'__stage__' + '>☼' + y['costumeName'] + '/Old-1.4textLayer'})
                imgCount = imgCount + 1
        if 'sounds' in j:
            internalListIndex = 0
            for y in j['sounds']:
                sct.print('__stage__' + '>♫' + y['soundName'])
                assets.append({'id':sfxCount,'md5':y['md5'],'route':{'node':None,'spriteIndex':None,'assetType':'sounds','assetIndex':internalListIndex},'type':'sound','display':'__stage__' + '>♫' + y['soundName']})
                internalListIndex = internalListIndex + 1
                sfxCount = sfxCount + 1
        listIndex = -1
        for x in j['children']:
            listIndex = listIndex + 1
            st(str(per(listIndex + 1, len(j['children']))) + '% Looking Up Assets')
            if not ('objName' in x): # True if not a sprite. 'objName' should be in a sprite
                continue
            if not ('costumes' in x):
                db.showwarning('Project Downloader', '"costumes" is missing in "' + x['objName'] + '". This is likely a corruption. The project will be fixed, note that the scratch editor will take a while to assign the costume a new md5')
                sct.print('WARN: Costumes missing')
                j['children'][listIndex]['costumes'] = []
                j['children'][listIndex]['costumes'].append({"costumeName": "costume-1", "baseLayerID": -1,"baseLayerMD5": "cd21514d0531fdffb22204e0ec5ed84a.svg","bitmapResolution": 1,"rotationCenterX": 240,"rotationCenterY": 180})
            if len(x['costumes']) == 0:
                db.showwarning('Project Downloader', '"costumes" is empty in "' + x['objName'] + '". This is likely a corruption. The project will be fixed, note that the scratch editor will take a while to assign the costume a new md5')
                sct.print('WARN: Costumes tag empty. Fixing...')
                j['children'][listIndex]['costumes'].append({"costumeName": "costume-1", "baseLayerID": -1,"baseLayerMD5": "cd21514d0531fdffb22204e0ec5ed84a.svg","bitmapResolution": 1,"rotationCenterX": 240,"rotationCenterY": 180})
            internalListIndex = 0
            for y in x['costumes']:
                sct.print(x['objName'] + '>' + y['costumeName'])
                assets.append({'id':imgCount,'md5':y['baseLayerMD5'],'route':{'node':'children','spriteIndex':listIndex,'assetType':'costumes','assetIndex':internalListIndex},'type':'imageLayer','display':x['objName'] + '>☼' + y['costumeName']})
                imgCount = imgCount + 1
                if 'textLayerID' in y:
                    assets.append({'id':imgCount,'md5':y['textLayerMD5'],'route':{'node':'children','spriteIndex':listIndex,'assetType':'costumes','assetIndex':internalListIndex},'type':'textLayer', 'display':x['objName'] + '>☼' + y['costumeName'] + '/Old-1.4textLayer'})
                    imgCount = imgCount + 1
                internalListIndex = internalListIndex + 1
            if 'sounds' in x:
                internalListIndex = 0
                for y in x['sounds']:
                    sct.print(x['objName'] + '>♫' + y['soundName'])
                    assets.append({'id':sfxCount,'md5':y['md5'],'route':{'node':'children','spriteIndex':listIndex,'assetType':'sounds','assetIndex':internalListIndex},'type':'sound','display':x['objName'] + '>♫' + y['soundName']})
                    internalListIndex = internalListIndex + 1
                    sfxCount = sfxCount + 1
        count = 0
        st('0% Downloading Assets')
        l.update()
        for x in assets:
            st(str(per(count + 1, len(assets))) + '% Downloading Assets')
            status = processAsset(x['id'],x['md5'],x['route'],x['type'])
            if status['success']:
                sct.print('Downloaded ' + x['display'] + ' (id ' + str(x['id']) + ' md5 ' + x['md5'] + ')')
            else:
                if x['type'] == 'imageLayer':
                    sct.print('Failed to download ' + x['display'] + ': ' + str(status['statusCode']) + ' (' + x['md5'] + ') Missing? Replacing with blank svg.')
                    stat = processAssetContent(x['id'],blank_svg,x['route'],x['type'],'.svg')
                elif x['type'] == 'textLayer':
                    sct.print('Failed to download ' + x['display'] + ': ' + str(status['statusCode']) + ' (' + x['md5'] + ') Missing? Replacing with blank png.')
                    stat = processAsset(x['id'],'d36f6603ec293d2c2198d3ea05109fe0.png',x['route'],x['type'])
                else:
                    sct.print('Failed to download ' + x['display'] + ': ' + str(status['statusCode']) + ' (' + x['md5'] + ') Missing? Replacing with blank wav.')
                    stat = processAsset(x['id'],'50dcf96f5dabc3941972f14ae6e3c103.wav',x['route'],x['type'])
                if not stat['success']:
                    return {'status':False, 'error':2, stack:False}
            count = count + 1 
        st('Configuring Assets...')
        
        zipf.writestr('project.json', json.dumps(j, indent=4).encode())
        zipf.close()
        f = tkinter.filedialog.asksaveasfilename(initialfile=info['title'],filetypes=[('Scratch Projects','.sb2')], title='Save Scratch Project', initialdir='C:\\Users\\' + getpass.getuser() + '\\Desktop')
        if f == '':
            l.destroy()
            return {'status':'cancel'}
        if os.path.splitext(f)[1] != '.sb2':
            f = f + '.sb2'
        fn = open(f, 'wb')
        fn.write(buf.getvalue())
        fn.close()
        try:
            l.destroy()
        except:
            pass
    except:
        return {'status':'error','error':'Internal Function raised Exception','stack':True,'code':111}
    else:
        return {'status':'success'}
def encodeStatus(sc):
    return int((100 - sc * 2 + 50) / 2)
def decodeStatus(sc):
    return int(sc - 75) + abs((-425.0 - 75) * 2)
def getpassword(title='Enter Password', prompt=['Enter Username', 'Enter Password'], buttontext=['OK', 'Cancel']): # Show Password Dialog
    global tk
    tk = tkinter.Tk()
    tk.title(title)
    try:
        tk.attributes('-toolwindow', 1)
    except:
        pass
    tk.iconify()
    tk.update_idletasks()
    tk.deiconify()
    tk.wm_attributes('-topmost')
    tk.update_idletasks()
    global st
    st = tkinter.StringVar()
    lb = tkinter.Label(tk, text=prompt[0],font=['Arial',16])
    lb.grid(row=0,column=0)
    en = tkinter.Entry(tk, textvariable=st, width=25, font=['Arial',16])
    en.grid(row=0,column=1)
    sep = Label(tk,text=' ',font=['Arial',4])
    sep.grid(row=1,column=0)
    lb1 = tkinter.Label(tk, text=prompt[1], font=['Arial',16])
    lb1.grid(row=2,column=0)
    global ent
    global pas
    pas = StringVar()
    ent = tkinter.Entry(tk, width=25,font=['Arial',16], textvariable=pas, show="•")
    ent.grid(row=2,column=1)
    global bt
    bt = tkinter.Button(tk, text=buttontext[0], command=_Okay, width=10, state="disabled")
    bt.grid(row=5,column=0,sticky='w')
    bt1 = tkinter.Button(tk, text=buttontext[1], command=_Cancel, width=10)
    bt1.grid(row=5,column=0,sticky='e')
    gtee = Label(tk, text='Your login information is not collected in any way. Your username and\npassword are discarded when the program closes.', font=['Calabri',10], foreground="#848484")
    gtee.grid(row=3,column=0,columnspan=2)
    tk.update()
    tk.bind_all('<KeyPress>', _binding)
    global ret
    ret = 0
    globals()[ret] = 0
    tk.update()
    tk.mainloop()
    if globals()[ret] == 0 or globals()[ret] == 1:
        return None
    if globals()[ret] == 2:
        return [st.get(), pas.get()]
def _binding(event=None): # Helper for GetPassword()
    if (len(pas.get()) > 0) and (len(st.get()) > 0):
        bt.config(state="normal")
    else:
        bt.config(state="disabled")
    if (event.keysym == 'Return') and (len(pas.get()) > 0) and (len(st.get()) > 0):    
        _Okay()
def _Okay(): # Helper for GetPassword()
    if (len(pas.get()) > 0) and (len(st.get()) > 0):
        globals()[ret] = 2
        tk.destroy()
def _Cancel(): # Helper for GetPassword()
    globals()[ret] = 1
    tk.destroy()

class ScrolledText(Frame): # ScrolledText Class
    def __init__(self, parent=None, text='', file=None, edit=False):
        Frame.__init__(self, parent)
        self.edit = edit
        self.pack()
        self.makewidgets()
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN, selectbackground='Green', font=('Lucida Console', 10))
        sbar.config(command=text.yview)               
        text.config(yscrollcommand=sbar.set)
        if not self.edit:
            text.config(state=DISABLED)
        sbar.pack(side=RIGHT,fill=Y)                 
        text.pack()
        self.text = text
    def settext(self, text='', file=None):
        self.text.config(state=NORMAL)
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                 
        self.text.insert('1.0', text)               
        self.text.mark_set(INSERT, END)          
        self.text.see(END)
        if not self.edit:
            self.text.config(state=DISABLED)
    def gettext(self):                             
        return self.text.get('1.0', END+'-1c')      
    def print(self, value):
        self.settext(text=self.gettext() + value + '\n')

def showsplash(sp='Connecting to Scratch...'): # Show Splash Screen
    global splash
    splash = Tk()
    splash.overrideredirect(True)
    width = splash.winfo_screenwidth(); height = splash.winfo_screenheight(); splash.geometry('%dx%d+%d+%d' % (width*0.25, height*0.15, width*0.375, height*0.375))
    canvas = Canvas(splash, height=height*0.3, width=width*0.3, bg="#FAFF6B"); canvas.pack()
    splash.update(); splash.update_idletasks()
    p = [canvas.winfo_width(), canvas.winfo_height()]
    canvas.create_text(p[0]/2,p[1]/2, text=sp,font=['Arial',24], fill='#FF8000')
    splash.update(); splash.update_idletasks()
def load(): # Reusable call load()
    showsplash()
    try:
        requests.get('https://scratch.mit.edu')
    except:
        if db.askretrycancel('Could Not Connect', 'Could not connect to the Scratch website.'):
            splash.destroy()
            load()
            os._exit(1)
        else:
            os._exit(1)
    splash.destroy()
    passinfo = getpassword(title='Login to Scratch account', prompt=['Enter Username', 'Enter Password'])
    if not passinfo:
        os._exit(1)
    auth = (passinfo[0], passinfo[1])
    showsplash()
    global s
    s = requests.session()
    s.get('https://scratch.mit.edu/csrf_token/',headers={"Accept":"*/*","Referer":"https://scratch.mit.edu","X-Requested-With":"XMLHttpRequest"},auth=auth)
    csrf = str(requests.utils.dict_from_cookiejar(s.cookies)['scratchcsrftoken'])
    global headers
    headers = {"Accept":"*/*", "Referer":"https://scratch.mit.edu","Origin":"https://scratch.mit.edu","Content-Type":"application/json","X-CSRFToken":csrf, "X-Requested-With":"XMLHttpRequest"}
    login = str(json.dumps({'csrfmiddlewaretoken':str(csrf),'username':str(passinfo[0]),'password':str(passinfo[1]),'captcha_challenge':'','captcha_response':'','embed_captcha':False,'timezone':'America/New_York'}))
    l = s.post("https://scratch.mit.edu/login/", headers={"Accept":"application/json, text/javascript, */*; q=0.01","Referer":"https://scratch.mit.edu","Origin":"https://scratch.mit.edu","Content-Type":"application/json","X-CSRFToken":csrf,"X-Requested-With":"XMLHttpRequest"}, data=login)
    user_info = s.get('https://scratch.mit.edu/fragment/account-nav.json',headers=headers)
    user_page_info = s.get('https://scratch.mit.edu/api/v1/user/' + passinfo[0] + '/?format=json',headers=headers)
    global proj
    proj = s.get('https://scratch.mit.edu/site-api/projects/all/',headers=headers)
    try:
        proj = proj.json()
        proj[0]["pk"]
        backpack = s.get('https://scratch.mit.edu/internalapi/backpack/Dylan5797/get/',headers=headers).json()
        user_page_info = user_page_info.json()
    except:
        r = s.get('https://scratch.mit.edu/users/' + passinfo[0] + '/')
        if r.status_code == 404:
            db.showerror('Login','Couldn\'t find that user.')
        else:
            db.showerror('Login','Incorrect Password.')
        splash.destroy()
        load()
        os._exit(1)
    def projIcon(e=None):
        class x: pass
        ch = Tk()
        ch.title('Change Project Icon')
        x.lb = Listbox(ch, height=35, width=75); x.lb.grid(row=0,column=0)
        for y in proj:
            x.lb.insert('end', y['fields']['title'])
    def openPage(e=None):
        webbrowser.open('https://scratch.mit.edu/users/' + passinfo[0] + '/')
    def backPack(e=None):
        print(backpack)
    def projDown(e=None, yx=None):
        if not yx:
            yx = sd.askinteger('Enter Project ID', 'Enter the project ID that can be found at the end of the URL of a project.')
        s = downloadProject(yx)
        if s['status'] == 'error':
            try:
                s['stack']
            except:
                stack = True
            else:
                stack = s['stack']
            if stack:
                r = db.askretrycancel('Project Downloader', 'Error: Could not download project: ' + str(s['error']) + '\nStacktrace:\n' + str(traceback.format_exc()) + '\nError Code ' + str(error_code) + ': ' + error_codes[s['code']][0] + '. ' + error_codes[s['code']][1])
            else:
                r = db.askretrycancel('Project Downloader', 'Error: Could not download project: ' + str(s['error']) + '\nError Code ' + str(s['code']) + ': ' + error_codes[s['code']][0] + '. ' + error_codes[s['code']][1])
            if r:
                projDown(yx=yx)
    class w: pass
    splash.destroy()
    wm = tkinter.Tk()
    wm.title(passinfo[0] + '\'s Profile')
    w.t = Label(wm, text=passinfo[0],font=['Calabri',14],cursor="hand2");w.t.grid(row=2,column=0,sticky='w')
    w.cnty = Label(wm, text=user_page_info['userprofile']['country'],font=['Calabri',9]);w.cnty.grid(row=3,column=0,sticky='w')
    w.bio = sct.ScrolledText(wm,height=3,width=70);w.bio.grid(row=4,sticky='w')
    w.bio.insert('1.0', user_page_info['userprofile']['bio'])
    w.bio.config(state='disabled')
    w.sta = sct.ScrolledText(wm,height=3,width=70);w.sta.grid(row=5,sticky='w')
    w.sta.insert('1.0', user_page_info['userprofile']['status'])
    w.sta.config(state='disabled')
    w.m = Button(wm, text='Backpack...',command=backPack); w.m.grid(row=6,sticky='w')
    w.t.bind('<Button-1>', openPage)
    w.ch = Button(wm, text='Change Project Icon', command=projIcon); w.ch.grid(row=7,column=0,sticky='w')
    w.dl = Button(wm, text='Download Project', command=projDown); w.dl.grid(row=8,sticky='w')
    wm.mainloop()
load()
