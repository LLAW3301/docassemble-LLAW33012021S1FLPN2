def regionToString(region):
  # if number is passed as string for whatever reason, cast to int
  number = int(region)
    
  regionNumberMap = {1:"Adelaide Hills", 2:"Barossa Light and Lower North",3:"Eastern Adelaide",4:"Eyre Western",5:"Far North",6:"Fleurieu and Kangaroo Island",7:"Limestone Coast",8:"Murrary and Mallee",9:"Northern Adelaide",10:"Southern Adelaide",11:"Western Adelaide",12:"Yorke and Mid North"}
  return regionNumberMap[number]