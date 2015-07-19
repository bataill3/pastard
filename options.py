def check(*arguments):
    FILE = 'NONE'
    TITLE = 'NONE'
    args = arguments[0]
    
    for i in range(0, len(args) - 1):
        if args[i] == '-f':
            FILE = args[i + 1]
        elif args[i] == '-t':
            TITLE = args[i + 1]
            
    return FILE, TITLE
