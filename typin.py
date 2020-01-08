import pyautogui

def main(string,delay):
    hard_tab = ['ą','ę','ó','ż','ź','ć','ś','ł','ń','Ą','Ę','Ó','Ż','Ź','Ć','Ź','Ł','Ń']
    easy_tab = ['a','e','o','z','x','c','s','l','n','a','e','o','z','x','c','s','l','n']
      
    def convert(text):
        how_many_chars = len(text)
        tab_char=[]
        for x in range(0,how_many_chars):
            tab_char.append(text[x])
        return tab_char

    def check(a):
        is_hard = 20
        for x in range (0,18):
            if a == hard_tab[x]:
                is_hard = x
        return is_hard

    def hard_key(index):
        if index < 8:
            pyautogui.hotkey('altright',easy_tab[index])
        else:
            pyautogui.hotkey('altright','shift',easy_tab[index])


    def look_for(st,a):
        hard_index=[]
        hard_chars=[]
        l = len(st)
        for x in range (0,l):
            y=0
            while y < 18:
                if st[x] == hard_tab[y]:
                    hard_index.append(x)
                    hard_chars.append(hard_tab[y])
                    break
                y=y+1
        if a == 1:
            return hard_index
        else:
            return hard_chars


    def divide(string,hx):
        str_tab=[]
        l = len(hx)
        for x in range (0,l+1):
            if x == 0:
                str_tab.append(string[0:hx[x]])
            elif x < l:
                str_tab.append(string[hx[x-1]+1:hx[x]])
            else:
                str_tab.append(string[hx[x-1]+1:])
        return str_tab     
                    
    string = convert(string)    # converts string to a array of chars

    hard_index = look_for(string,1) # gets indexes of hard_chars in the array of chars
    hard_chars = look_for(string,2) # gets hard chars in the array of chars 

    tab_str = divide(string,hard_index) #gets array of divided strings

    l = len(hard_index) 
                              # do the typing
    for x in range(0,l+1):
        pyautogui.typewrite(tab_str[x],delay)
        b=hard_chars[x]
        char_index=check(b)
        hard_key(char_index)


