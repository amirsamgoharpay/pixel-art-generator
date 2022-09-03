import cairo
import random
def creator(name:str , amount):
    colors = [[43, 110, 217], [204, 156, 35] , [35, 204, 131] , [204, 35, 159]]
    with cairo.SVGSurface(f"{name}.svg", 1000, 1000) as surface:
        context = cairo.Context(surface)
        color = random.randint(0 , len(colors)-1)
        rgb = colors[color]
        context.set_source_rgb(rgb[0]/255 , rgb[1]/255,rgb[2]/255)
        for i in range(amount):
            x = random.randint(0 , 3)*100
            y = random.randint(0 , 4)*200
            context.rectangle(x, y, 200, 200)
            x2 = 800-x
            context.rectangle(x2, y, 200, 200)
            context.fill()
    
if __name__ == "__main__" :
    na = str(input("please type your file name : "))
    creator(na , 3)
    print(f"{na}.svg saved")


