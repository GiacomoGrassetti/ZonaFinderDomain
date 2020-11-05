# codingf: utf-8

def color (string):
    colors = {"default":0, "black":30, "red":31, "green":32, "yellow":33,
          "blue":34,"magenta":35, "cyan":36, "white":37, "black":38,
          "black":39} #33[%colors%m
    
    for color in colors:
        color_string = "\033[%dm\033[1m" % colors[color]
        string = string.replace("<%s>" % color, color_string).replace("</%s>" % color, "\033[0m")
    
    return string
