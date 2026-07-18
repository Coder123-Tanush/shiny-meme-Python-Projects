def short_form(*names):
    short=""
    
    try:
        for name in names:
           short=short+name[0]
    except Exception as e:
        print( "something went wrong",e)
    return short.upper()

