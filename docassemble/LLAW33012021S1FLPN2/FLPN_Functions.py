def regionToString(regions):
  regionNumberMap = {1:"Adelaide Hills", 2:"Barossa Light and Lower North",3:"Eastern Adelaide",4:"Eyre Western",5:"Far North",6:"Fleurieu and Kangaroo Island",7:"Limestone Coast",8:"Murrary and Mallee",9:"Northern Adelaide",10:"Southern Adelaide",11:"Western Adelaide",12:"Yorke and Mid North"}
  
  
  output = ""
  
  for num, trueFalse in regions.items():
    if trueFalse == True:

        # if number is passed as string for whatever reason, cast to int
        number = int(num)
        
        if output == "":
            output = "{}".format(regionNumberMap[number])
        else:
            output = "{}, {}".format(output, regionNumberMap[number]) 
    
  
  return output

# formats multi-string list into a single-line HTML string (to work around docassemble tables newline issue)
def formatListIntoHTML(list):
  output = ""
  for x in list:
    output = output + "<li>" + x + "</li>"
  return output