import os
import re
import imdb
import enchant
import pickle
import shutil
import random
import string


def strip_patterns(movie_name):
    for p in bad_words:
        regex = re.compile(p, re.IGNORECASE)
        movie_name = regex.sub("", movie_name)
    return movie_name


def getTitles(path,newpath):
    
    titles = []
    
    db = False
    if(os.path.exists("titles.p")):
        titles = pickle.load(open("titles.p","rb"))
        db=True
    ia = imdb.IMDb()
    d= enchant.Dict("en_US")
    
    for film in os.listdir(path):

        if(db):
            for name in titles:
                if(name == film):
                    continue  
        
        else:    
            movie_name =  film
            movie_name = strip_patterns(movie_name)
            movie_name = movie_name.strip()
            
            movie_name = movie_name.replace('.', ' ')
            movie_name = movie_name.replace(',', '')
            if(not movie_name.isupper()):
                movie_name = re.sub(r"(\w)([A-Z])", r"\1 \2", movie_name)
            
            
            movie_name = re.sub(r'^https?:\/\/.*[\r\n]*', '', movie_name, flags=re.MULTILINE)
            print("file:", movie_name)
            movie_name = movie_name.split()
            #print("split:", movie_name, "\n")
            pot_name = str()
            #store first possible
            first = str()
            for word in movie_name:
                if(d.check(word)):
                    
                    if(pot_name == ""):
                        pot_name = word
                    else:
                        pot_name = pot_name+" "+word
                #pot_name.join(word)
                    if not ia.search_movie(pot_name):
                        break
                    result = str(ia.search_movie(pot_name)[0])
                    result = result.replace('.', ' ')
                    result = result.replace(',', '')
                    #print("potential:", pot_name)
                    #print("result:" ,result)
                    lw_r = result.lower()
                    lw_p = pot_name.lower()
                    if(first!= "" and lw_r == lw_p):
                        #print("1")
                        first = result
                        #print("new first is", first, "\n")

                    
        ##            elif(first!="" and lw_r.find(lw_p)):
        ##                print("2")
        ##                first = result
        ##                print("name is", first, "\n")
        ##                
                    if(first == "" and lw_r == lw_p):
                        #print("3")
                        first = result
                        #print("first: ", first)
                else:
                    bad_words.append(word)
            if(first==""):
                print("Unsure film title")
                print("Original: " ,film)
                print("new: " ,result)
                choice = input(str("Is this okay? y/n "))
                if(choice == "y"):
                    title = result
                    
                else:
                    title = input(str("Input title: "))
                    
        #print("4")
            else:
                title = first
                print("result", title , "\n")
            
            if(os.path.exists(os.path.join(newpath,title))):
                print("file already exists")
                print("title: ",title)
                print("original file name:", film)
                title = input(str("new name: "))
            if(os.path.isfile(film)):
                os.mkdir(os.path.join(newpath, title))
                shutil.move(film, os.path.join(newpath,title))
                print(film, "has been added to new directory: ", os.path.join(newpath, title))
            else:    
                os.rename(os.path.join(path,film), os.path.join(newpath,title))          
            titles.append(title)

    pickle.dump(titles, open("titles.p","wb"))             
    pickle.dump(bad_words,open("bad_words.p","wb"))      

            
            

bad_words = pickle.load(open("badwords.p", "rb"))
path = "D:/torrents"
newpath= "D:/Films"	
getTitles(path,newpath)

    
        
        #new_name = ''.join(i for i in films if not i in bad_chars) 
    
    
