#coding: utf-8 

sumador = 0
restador =0
sumador1 = 0
restador1 =0
R_i=[]
D_u = {}
def pregunta1_1 ():
            print ("Que es HTML?: a).Compilador de Programas, b)Lector de Hojas con extension .HTML, c)Explorador, d)Lenguaje de programacion, e)puede crear paginas web")
            p1 = ["a","b","c","d","e"] 
            r1 = raw_input ("Ingrese la respuesta:")
            r1 = raw_input ("Ingrese la respuesta:")   
            if (r1 == "b" in p1):
                global sumador,restador  
                print "1 punto"                 
                sumador += 1
            elif (r1 == "d" in p1): 
                print "1 punto"                
                sumador += 1           
            else: 
                print "0 punto"                         
                restador += 1
                R_i.append("Que es HTML?")
           
def pregunta1 ():
            print ("Que es HTML?: a).Compilador de Programas, b)Lector de Hojas con extension .HTML, c)Explorador, d)Lenguaje de programacion, e)puede crear paginas web")
            p1 = ["a","b","c","d","e"] 
            r1 = raw_input ("Ingrese la respuesta:")
            r1 = raw_input ("Ingrese la respuesta:")    
            if (r1 == "b" in p1):
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1
            elif (r1 == "d" in p1): 
                print "1 punto"                
                sumador1 += 1           
            else: 
                print "0 punto"                         
                restador1 += 1
                R_i.append("Que es HTML?")
                
def pregunta1_2 (): 
            print ("Que extension tienen los documentos electronicos?: a)HTTPs, b)HTTP, c)HTML, d)LINK, e)wwa")
            p2 = ["a","b","c","d","e"]  
            r2 = raw_input ("Ingrese la respuesta:")
            r2 = raw_input ("Ingrese la respuesta:")      
            if (r2 == "b" in p2):
                global sumador,restador  
                print "1 punto"                 
                sumador += 1 
            elif (r2 == "a" in p2): 
                print "1 punto"               
                sumador += 1
            else: 
                print "0 punto"                 
                restador += 1 
                R_i.append("Que extension tienen los documentos electronicos?")
def pregunta2(): 
            print ("Que extension tienen los documentos electronicos?: a)HTTPs, b)HTTP, c)HTML, d)LINK, e)wwa")
            p2 = ["a","b","c","d","e"]  
            r2 = raw_input ("Ingrese la respuesta:") 
            r2 = raw_input ("Ingrese la respuesta:")   
            if (r2 == "b" in p2):
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1 
            elif (r2 == "a" in p2): 
                print "1 punto"               
                sumador1 += 1
            else: 
                print "0 punto"                 
                restador1 += 1 
                R_i.append("Que extension tienen los documentos electronicos?")      
                  
def pregunta1_3 (): 
            print ("Que etiqueta se utiliza para declarar un documento HTML?: a)BODY>, b)TITLE>, c)HTML>, d)FONT>, e)la opcion d es la correcta")
            p3 = ["a","b","c","d","e"]  
            r3 = raw_input ("Ingrese la respuesta:")
            r3 = raw_input ("Ingrese la respuesta:")    
            if (r3 == "d" in p3):
                global sumador,restador  
                print "1 punto"                 
                sumador += 1 
            elif (r3 == "a" in p3): 
                print "1 punto"                
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que etiqueta se utiliza para declarar un documento HTML?")
def pregunta3 (): 
            print ("Que etiqueta se utiliza para declarar un documento HTML?: a)BODY>, b)TITLE>, c)HTML>, d)FONT>, e)la opcion d es la correcta")
            p3 = ["a","b","c","d","e"]  
            r3 = raw_input ("Ingrese la respuesta:")
            r3 = raw_input ("Ingrese la respuesta:")     
            if (r3 == "d" in p3):
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1 
            elif (r3 == "a" in p3): 
                print "1 punto"                
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que etiqueta se utiliza para declarar un documento HTML?")
                        
def pregunta1_4 (): 
            print ("Con que etiqueta podemos insertar una imagen?: a)FONT>, b)BACKGROUND>, c)IMS SRC>, d)la b es correcta, e)wwe>")
            p4 = ["a","b","c","d","e"]  
            r4 = raw_input ("Ingrese la respuesta:")
            r4 = raw_input ("Ingrese la respuesta:")    
            if (r4 == "b" in p4):
                global sumador,restador  
                print "1 punto"                  
                sumador += 1 
            elif (r4 == "d" in p4): 
                print "1 punto"                  
                sumador += 1
            else: 
                print "0 punto"                 
                restador += 1 
                R_i.append("Con que etiqueta podemos insertar una imagen?")
def pregunta4 (): 
            print ("Con que etiqueta podemos insertar una imagen?: a)FONT>, b)BACKGROUND>, c)IMS SRC>, d)la b es correcta, e)wwe>")
            p4 = ["a","b","c","d","e"]  
            r4 = raw_input ("Ingrese la respuesta:")
            r4 = raw_input ("Ingrese la respuesta:")    
            if (r4 == "b" in p4):
                global sumador1,restador1  
                print "1 punto"                  
                sumador1 += 1 
            elif (r4 == "d" in p4): 
                print "1 punto"                  
                sumador1 += 1
            else: 
                print "0 punto"                 
                restador1 += 1 
                R_i.append("Con que etiqueta podemos insertar una imagen?")            
def pregunta1_5 (): 
            print ("Que utilizamos para declarar un parrafo?: a)P>, b)SOUND>, c)FONT>, d)Nada, solo se escribe, e)la c es correcta")
            p5 = ["a","b","c","d","e"]  
            r5 = raw_input ("Ingrese la respuesta:")
            r5 = raw_input ("Ingrese la respuesta:")    
            if (r5 == "c" in p5): 
                global sumador,restador  
                print "1 punto"                 
                sumador += 1 
            elif (r5 == "e" in p5): 
                print "1 punto"                
                sumador += 1
            else: 
                print "0 punto"                 
                restador += 1 
                R_i.append("Que utilizamos para declarar un parrafo?")
def pregunta5 (): 
            print ("Que utilizamos para declarar un parrafo?: a)P>, b)SOUND>, c)FONT>, d)Nada, solo se escribe, e)la c es correcta")
            p5 = ["a","b","c","d","e"]  
            r5 = raw_input ("Ingrese la respuesta:")
            r5 = raw_input ("Ingrese la respuesta:")
            if (r5 == "c" in p5): 
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1 
            elif (r5 == "e" in p5): 
                print "1 punto"                
                sumador1 += 1
            else: 
                print "0 punto"                 
                restador1 += 1 
                R_i.append("Que utilizamos para declarar un parrafo?")            
def pregunta1_6 (): 
            print ("Con que simbolo cerramos casi todas las etiquetas?: a)A>, b)<()>, c)<=>, d)/>, e)a")
            p6 = ["a","b","c","d","e"]  
            r6 = raw_input ("Ingrese la respuesta:")
            r6 = raw_input ("Ingrese la respuesta:")    
            if (r6 == "a" in p6):
                global sumador,restador  
                print "1 punto"                 
                sumador += 1
            elif (r6 == "e" in p6): 
                print "1 punto"                
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Con que simbolo cerramos casi todas las etiquetas?")
def pregunta6 (): 
            print ("Con que simbolo cerramos casi todas las etiquetas?: a)A>, b)<()>, c)<=>, d)/>, e)a")
            p6 = ["a","b","c","d","e"]  
            r6 = raw_input ("Ingrese la respuesta:")
            r6 = raw_input ("Ingrese la respuesta:")    
            if (r6 == "a" in p6):
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1
            elif (r6 == "e" in p6): 
                print "1 punto"                
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Con que simbolo cerramos casi todas las etiquetas?")           
def pregunta1_7 (): 
            print ("Cual es la etiqueta que se utiliza para iniciar el cuerpo del programa?: a)CUERPO, b)BODY, c)TITLE, d)HEAD, e)cabeza")
            p7 = ["a","b","c","d","e"]  
            r7 = raw_input ("Ingrese la respuesta:") 
            r7 = raw_input ("Ingrese la respuesta:")   
            if (r7 == "b" in p7):
                global sumador,restador  
                print "1 punto"                  
                sumador += 1 
            elif (r7 == "a" in p7): 
                print "1 punto"                
                sumador += 1
            else: 
                print "0 punto"                 
                restador += 1 
                R_i.append("Cual es la etiqueta que se utiliza para iniciar el cuerpo del programa?")
def pregunta7 (): 
            print ("Cual es la etiqueta que se utiliza para iniciar el cuerpo del programa?: a)CUERPO, b)BODY, c)TITLE, d)HEAD, e)cabeza")
            p7 = ["a","b","c","d","e"]  
            r7 = raw_input ("Ingrese la respuesta:") 
            r7 = raw_input ("Ingrese la respuesta:")   
            if (r7 == "b" in p7):
                global sumador1,restador1  
                print "1 punto"                  
                sumador1 += 1 
            elif (r7 == "a" in p7): 
                print "1 punto"                
                sumador1 += 1
            else: 
                print "0 punto"                 
                restador1 += 1 
                R_i.append("Cual es la etiqueta que se utiliza para iniciar el cuerpo del programa?")            
def pregunta1_8 (): 
            print ("Que etiqueta se utiliza para insertar una linea?: a)B, b)M, c)L, d)HR, e)l")
            p8 = ["a","b","c","d","e"]  
            r8 = raw_input ("Ingrese la respuesta:")
            r8= raw_input ("Ingrese la respuesta:")        
            if (r8 == "c" in p8):
                global sumador,restador  
                print "1 punto"                 
                sumador += 1 
            elif (r8 == "e" in p8): 
                print "1 punto"                  
                sumador += 1
            else: 
                print "0 punto"                  
                restador += 1 
                R_i.append("Que etiqueta se utiliza para insertar una linea?")
def pregunta8 (): 
            print ("Que etiqueta se utiliza para insertar una linea?: a)B, b)M, c)L, d)HR, e)l")
            p8 = ["a","b","c","d","e"]  
            r8 = raw_input ("Ingrese la respuesta:")
            r8 = raw_input ("Ingrese la respuesta:")    
            if (r8 == "c" in p8):
                global sumador1,restador1  
                print "1 punto"                 
                sumador1 += 1 
            elif (r8 == "e" in p8): 
                print "1 punto"                  
                sumador1 += 1
            else: 
                print "0 punto"                  
                restador1 += 1 
                R_i.append("Que etiqueta se utiliza para insertar una linea?")           
def pregunta1_9 (): 
            print ("Que otro lenguaje es similar a HTML y se puede relacionar entre si?: a)C, b)JavaScript, c)internet exploret, d)Java, e)PYTHON")
            p9 = ["a","b","c","d","e"]  
            r9 = raw_input ("Ingrese la respuesta:")
            r9 = raw_input ("Ingrese la respuesta:")    
            if (r9 == "e" in p9):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r9 == "a" in p9): 
                print "1 punto"                
                sumador += 1
            else: 
                print "0 punto"                  
                restador += 1 
                R_i.append("Que otro lenguaje es similar a HTML y se puede relacionar entre si?")
def pregunta9 (): 
            print ("Que otro lenguaje es similar a HTML y se puede relacionar entre si?: a)C, b)JavaScript, c)internet exploret, d)Java, e)PYTHON")
            p9 = ["a","b","c","d","e"]  
            r9 = raw_input ("Ingrese la respuesta:")
            r9 = raw_input ("Ingrese la respuesta:")    
            if (r9 == "e" in p9):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r9 == "a" in p9): 
                print "1 punto"                
                sumador1 += 1
            else: 
                print "0 punto"                  
                restador1 += 1 
                R_i.append("Que otro lenguaje es similar a HTML y se puede relacionar entre si?")            
def pregunta1_10 (): 
            print ("Cual de estas etiquetas no existe en HTML?: a)BODI, b)FONT, c)HR, d)TABLE, e)x1x")
            p10 = ["a","b","c","d","e"]  
            r10 = raw_input ("Ingrese la respuesta:")
            r10 = raw_input ("Ingrese la respuesta:")    
            if (r10 == "a" in p10):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r10 == "e" in p10): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cual de estas etiquetas no existe en HTML?")
def pregunta10 (): 
            print ("Cual de estas etiquetas no existe en HTML?: a)BODI, b)FONT, c)HR, d)TABLE, e)x1x")
            p10 = ["a","b","c","d","e"]  
            r10 = raw_input ("Ingrese la respuesta:")
            r10 = raw_input ("Ingrese la respuesta:")    
            if (r10 == "a" in p10):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r10 == "e" in p10): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cual de estas etiquetas no existe en HTML?")            
def pregunta1_11 (): 
            print ("Cual etiqueta utilizamos para declarar un salto de linea?: a)FRAMES, b)BR, c)A, d)c, e)C")
            p11 = ["a","b","c","d","e"]  
            r11 = raw_input ("Ingrese la respuesta:")
            r11 = raw_input ("Ingrese la respuesta:")    
            if (r11 == "c" in p11):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r11 == "d" in p11): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cual etiqueta utilizamos para declarar un salto de linea?")
def pregunta11 (): 
            print ("Cual etiqueta utilizamos para declarar un salto de linea?: a)FRAMES, b)BR, c)A, d)c, e)C")
            p11 = ["a","b","c","d","e"]  
            r11 = raw_input ("Ingrese la respuesta:")
            r11 = raw_input ("Ingrese la respuesta:")    
            if (r11 == "c" in p11):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r11 == "d" in p11): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cual etiqueta utilizamos para declarar un salto de linea?")            
def pregunta1_12 (): 
            print ("Que etiqueta se usa para encabezamientos?: a)H, b)FONT, c)SIZE, d)HG, e)h")
            p12 = ["a","b","c","d","e"]  
            r12 = raw_input ("Ingrese la respuesta:")
            r12 = raw_input ("Ingrese la respuesta:")     
            if (r12 == "a" in p12):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r12 == "e" in p12): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que etiqueta se usa para encabezamientos?")
def pregunta12 (): 
            print ("Que etiqueta se usa para encabezamientos?: a)H, b)FONT, c)SIZE, d)HG, e)h")
            p12 = ["a","b","c","d","e"]  
            r12 = raw_input ("Ingrese la respuesta:")
            r12 = raw_input ("Ingrese la respuesta:")     
            if (r12 == "a" in p12):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r12 == "e" in p12): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que etiqueta se usa para encabezamientos?")
                        
def pregunta1_13 (): 
            print ("Que etiqueta utilizamos para insertar un video?: a)IMG, b)MOVIE, c)HREF, d)EMBED=SRC, e)img")
            p13 = ["a","b","c","d","e"]  
            r13 = raw_input ("Ingrese la respuesta:")
            r13 = raw_input ("Ingrese la respuesta:")   
            if (r13 == "a" in p13):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r13 == "e" in p13): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que etiqueta utilizamos para insertar un video?")
def pregunta13 (): 
            print ("Que etiqueta utilizamos para insertar un video?: a)IMG, b)MOVIE, c)HREF, d)EMBED=SRC, e)img")
            p13 = ["a","b","c","d","e"]  
            r13 = raw_input ("Ingrese la respuesta:")
            r13 = raw_input ("Ingrese la respuesta:")    
            if (r13 == "a" in p13):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r13 == "e" in p13): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que etiqueta utilizamos para insertar un video?")
                        
def pregunta1_14 (): 
            print ("Cual etiqueta puede centrar practicamente todo?: a)C, b)/CENTER, c)CENTER, d)RIGHT, e)/center")
            p14 = ["a","b","c","d","e"]  
            r14 = raw_input ("Ingrese la respuesta:")
            r14 = raw_input ("Ingrese la respuesta:")   
            if (r14 == "b" in p14):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r14 == "e" in p14): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cual etiqueta puede centrar practicamente todo?")
def pregunta14 (): 
            print ("Cual etiqueta puede centrar practicamente todo?: a)C, b)/CENTER, c)CENTER, d)RIGHT, e)/center")
            p14 = ["a","b","c","d","e"]  
            r14 = raw_input ("Ingrese la respuesta:")
            r14 = raw_input ("Ingrese la respuesta:")     
            if (r14 == "b" in p14):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r14 == "e" in p14): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cual etiqueta puede centrar practicamente todo?")
                        
def pregunta1_15 (): 
            print ("Que es un caracter especial?: a)@, b)´, c)Ninguno, d)/")
            p15 = ["a","b","c","d"]  
            r15 = raw_input ("Ingrese la respuesta:")
            r15 = raw_input ("Ingrese la respuesta:")    
            if (r15 == "c" in p15):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r15 == "c" in p15): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que es un caracter especial?")
def pregunta15 (): 
            print ("Que es un caracter especial?: a)@, b)´, c)Ninguno, d)/")
            p15 = ["a","b","c","d"]  
            r15 = raw_input ("Ingrese la respuesta:")
            r15 = raw_input ("Ingrese la respuesta:")    
            if (r15 == "c" in p15):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r15 == "c" in p15): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que es un caracter especial?")

def pregunta1_16 (): 
            print ("Que etiqueta utilizamos para declarar listas de definicion?: a)DT, b)OL TYPE, c)DD, d)/dl, e)/DL")
            p16 = ["a","b","c","d","e"]  
            r16 = raw_input ("Ingrese la respuesta:")
            r16 = raw_input ("Ingrese la respuesta:")    
            if (r16 == "e" in p16):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r16 == "d" in p16): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que etiqueta utilizamos para declarar listas de definicion?")                                                                                                                                                                                                                                                                                                                                                                                                                          
def pregunta16 (): 
            print ("Que etiqueta utilizamos para declarar listas de definicion?: a)DT, b)OL TYPE, c)DD, d)/dl, e)/DL")
            p16 = ["a","b","c","d","e"]  
            r16 = raw_input ("Ingrese la respuesta:")
            r16 = raw_input ("Ingrese la respuesta:")    
            if (r16 == "e" in p16):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r16 == "d" in p16): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que etiqueta utilizamos para declarar listas de definicion?")                                                                                                                                                                                                                                                                                                                                                                                                                          
  
def pregunta1_17 (): 
            print ("CUAL DE ESTOS ENUNCIADOS NO PUEDE LEER ARCHIVOS CON EXTENSION HTML: a)Gogle Chroome, b)INTERNET EXPLORER, c)Block de Notas, d)Opera, e)reproductor de musica")
            p17 = ["a","b","c","d","e"]  
            r17 = raw_input ("Ingrese la respuesta:")
            r17 = raw_input ("Ingrese la respuesta:")    
            if (r17 == "d" in p17):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r17 == "e" in p17): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("CUAL DE ESTOS ENUNCIADOS NO PUEDE LEER ARCHIVOS CON EXTENSION HTML")
def pregunta17 (): 
            print ("CUAL DE ESTOS ENUNCIADOS NO PUEDE LEER ARCHIVOS CON EXTENSION HTML: a)Gogle Chroome, b)INTERNET EXPLORER, c)Block de Notas, d)Opera, e)reproductor de musica")
            p17 = ["a","b","c","d","e"]  
            r17 = raw_input ("Ingrese la respuesta:")
            r17 = raw_input ("Ingrese la respuesta:")    
            if (r17 == "d" in p17):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r17 == "e" in p17): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("CUAL DE ESTOS ENUNCIADOS NO PUEDE LEER ARCHIVOS CON EXTENSION HTML")
                        
def pregunta1_18 (): 
            print ("Que etiqueta se utiliza para alinear un parrafo a la izquierda?: a)P ALIGN=left, b)LEFT, c)T, d)L, e)P ALIGN=LEFT")
            p18 = ["a","b","c","d","e"]  
            r18 = raw_input ("Ingrese la respuesta:")
            r18 = raw_input ("Ingrese la respuesta:")    
            if (r18 == "a" in p18):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r18 == "e" in p18): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que etiqueta se utiliza para alinear un parrafo a la izquierda?")
def pregunta18 (): 
            print ("Que etiqueta se utiliza para alinear un parrafo a la izquierda?: a)P ALIGN=left, b)LEFT, c)T, d)L, e)P ALIGN=LEFT")
            p18 = ["a","b","c","d","e"]  
            r18 = raw_input ("Ingrese la respuesta:")
            r18 = raw_input ("Ingrese la respuesta:")    
            if (r18 == "a" in p18):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r18 == "e" in p18): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que etiqueta se utiliza para alinear un parrafo a la izquierda?")

def pregunta1_19 (): 
            print ("Cual es el editor mas comun de documentos HTML?: a)BLOCK DE NOTAS, b)WORD, c)INTERNET EXPLORER, d)GOGLE CHROOME, e)sublime")
            p19 = ["a","b","c","d","e"]  
            r19 = raw_input ("Ingrese la respuesta:")
            r19 = raw_input ("Ingrese la respuesta:")    
            if (r19 == "a" in p19):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r19 == "e" in p19): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cual es el editor mas comun de documentos HTML?")
def pregunta19 (): 
            print ("Cual es el editor mas comun de documentos HTML?: a)BLOCK DE NOTAS, b)WORD, c)INTERNET EXPLORER, d)GOGLE CHROOME, e)sublime")
            p19 = ["a","b","c","d","e"]  
            r19 = raw_input ("Ingrese la respuesta:")
            r19 = raw_input ("Ingrese la respuesta:")    
            if (r19 == "a" in p19):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r19 == "e" in p19): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cual es el editor mas comun de documentos HTML?")
      
def pregunta1_20 (): 
            print ("Cual atributo define el tamano de letra: a)TAMANO, b)ALINEAR, c)SIZE, d)tamano=, e)TAMANO=")
            p20 = ["a","b","c","d","e"]  
            r20 = raw_input ("Ingrese la respuesta:")
            r20 = raw_input ("Ingrese la respuesta:")    
            if (r20 == "a" in p20):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r20 == "e" in p20): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cual atributo define el tamano de letra")
def pregunta20 (): 
            print ("Cual atributo define el tamano de letra: a)TAMANO, b)ALINEAR, c)SIZE, d)tamano=, e)TAMANO=")
            p20 = ["a","b","c","d","e"]  
            r20 = raw_input ("Ingrese la respuesta:")
            r20 = raw_input ("Ingrese la respuesta:")    
            if (r20 == "a" in p20):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r20 == "e" in p20): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cual atributo define el tamano de letra")            
def pregunta1_21 (): 
            print ("Que es un browser?: a)un programa, b)visualizar paginas de internet, c)internet, d)texto, e)no se")
            p21 = ["a","b","c","d","e"]  
            r21 = raw_input ("Ingrese la respuesta:")
            r21 = raw_input ("Ingrese la respuesta:")    
            if (r21 == "a" in p21):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r21 == "b" in p21): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que es un browser?")
def pregunta21 (): 
            print ("Que es un browser?: a)un programa, b)visualizar paginas de internet, c)internet, d)texto, e)no se")
            p21 = ["a","b","c","d","e"]  
            r21 = raw_input ("Ingrese la respuesta:")
            r21 = raw_input ("Ingrese la respuesta:")    
            if (r21 == "a" in p21):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r21 == "b" in p21): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que es un browser?")
                        
def pregunta1_22 (): 
            print ("Cuales son las etiquetas basicas de un documento html?: a)HTML, b)HEAD, c)xd, d)hd, e)no se")
            p22 = ["a","b","c","d","e"]  
            r22 = raw_input ("Ingrese la respuesta:")
            r22 = raw_input ("Ingrese la respuesta:")    
            if (r22 == "a" in p22):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r22 == "b" in p22): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Cuales son las etiquetas basicas de un documento html?")               
def pregunta22 (): 
            print ("Cuales son las etiquetas basicas de un documento html?: a)HTML, b)HEAD, c)xd, d)hd, e)no se")
            p22 = ["a","b","c","d","e"]  
            r22 = raw_input ("Ingrese la respuesta:")
            r22 = raw_input ("Ingrese la respuesta:")    
            if (r22 == "a" in p22):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r22 == "b" in p22): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Cuales son las etiquetas basicas de un documento html?")               

def pregunta1_23 (): 
            print ("Que accion realiza la etiqueta Font color?: a)camnbia el colorde la letra, b)cambia el color de los strig, c)nada, d)cambia el color de los enteros, e)no se")
            p23 = ["a","b","c","d","e"]  
            r23 = raw_input ("Ingrese la respuesta:")
            r23 = raw_input ("Ingrese la respuesta:")    
            if (r23 == "a" in p23):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r23 == "b" in p23): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta Font color?")
def pregunta23 (): 
            print ("Que accion realiza la etiqueta Font color?: a)camnbia el colorde la letra, b)cambia el color de los strig, c)nada, d)cambia el color de los enteros, e)no se")
            p23 = ["a","b","c","d","e"]  
            r23 = raw_input ("Ingrese la respuesta:")
            r23 = raw_input ("Ingrese la respuesta:")    
            if (r23 == "a" in p23):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r23 == "b" in p23): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que accion realiza la etiqueta Font color?")
                          
def pregunta1_24 (): 
            print ("Que accion realiza la etiqueta Font size?: a)camnbia el tamano la letra, b)cambia el tamano de los strig, c)nada, d)cambia el tamano de los enteros, e)no se")
            p24 = ["a","b","c","d","e"]  
            r24 = raw_input ("Ingrese la respuesta:")
            r24 = raw_input ("Ingrese la respuesta:")    
            if (r24 == "a" in p24):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r24 == "b" in p24): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta Font size?")
def pregunta24 (): 
            print ("Que accion realiza la etiqueta Font size?: a)camnbia el tamano la letra, b)cambia el tamano de los strig, c)nada, d)cambia el tamano de los enteros, e)no se")
            p24 = ["a","b","c","d","e"]  
            r24 = raw_input ("Ingrese la respuesta:")
            r24 = raw_input ("Ingrese la respuesta:")     
            if (r24 == "a" in p24):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r24 == "b" in p24): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que accion realiza la etiqueta Font size?")
                        
def pregunta1_25 (): 
            print ("Que accion realiza la etiqueta Font face?: a)camnbia el tipo la letra, b)cambia el tipo de los strig, c)nada, d)cambia el tipo de los enteros, e)no se")
            p25 = ["a","b","c","d","e"]  
            r25 = raw_input ("Ingrese la respuesta:")
            r25 = raw_input ("Ingrese la respuesta:")        
            if (r25 == "a" in p25):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r25 == "b" in p25): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta Font face?")
def pregunta25 (): 
            print ("Que accion realiza la etiqueta Font face?: a)camnbia el tipo la letra, b)cambia el tipo de los strig, c)nada, d)cambia el tipo de los enteros, e)no se")
            p25 = ["a","b","c","d","e"]  
            r25 = raw_input ("Ingrese la respuesta:")
            r25 = raw_input ("Ingrese la respuesta:")        
            if (r25 == "a" in p25):
                global sumador1,restador1  
                print "1 punto"                
                sumador1 += 1 
            elif (r25 == "b" in p25): 
                print "1 punto"                 
                sumador1 += 1
            else: 
                print "0 punto"                
                restador1 += 1 
                R_i.append("Que accion realiza la etiqueta Font face?")
                                              
def pregunta1_26 (): 
            print ("Que accion realiza la etiqueta H1?: a)Aplica formato predeterminado a los títulos de las páginas web, b)cambia el formato web, c)nada, d)ninguna de las anteriores, e)no se")
            p26 = ["a","b","c","d","e"]  
            r26 = raw_input ("Ingrese la respuesta:")
            r26 = raw_input ("Ingrese la respuesta:")        
            if (r26 == "a" in p26):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r26 == "b" in p26): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta H1?")
  
def pregunta1_27 (): 
            print ("Que accion realiza la etiqueta b?: a)Aplica negrita, b)cambia el cambia el formato de la letra a un tono oscuro, c)salto de linea, d)ninguna de las anteriores, e)no se")
            p27 = ["a","b","c","d","e"]  
            r27 = raw_input ("Ingrese la respuesta:")
            r27 = raw_input ("Ingrese la respuesta:")        
            if (r27 == "a" in p27):
                global sumador,restador 
                print "1 punto"                
                sumador += 1 
            elif (r27 == "b" in p27): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta b?")
            
def pregunta1_28 (): 
            print ("Que accion realiza la etiqueta i?: a)Aplica cursiva, b)cambia el cambia el formato de la letra a curva, c)salto de pagina, d)ninguna de las anteriores, e)no se")
            p28 = ["a","b","c","d","e"]  
            r28 = raw_input ("Ingrese la respuesta:")
            r28 = raw_input ("Ingrese la respuesta:")        
            if (r28 == "a" in p28):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r28 == "b" in p28): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta i?")
            
def pregunta1_29 (): 
            print ("Que accion realiza la etiqueta u?: a)Aplica subrayado, b)cambia el unapalabra y subrayado, c)salto de linea, d)todas de las anteriores, e)no se")
            p29 = ["a","b","c","d","e"]  
            r29 = raw_input ("Ingrese la respuesta:")
            r29 = raw_input ("Ingrese la respuesta:")        
            if (r29 == "a" in p29):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r29 == "b" in p29): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta u?")
             
def pregunta1_30 (): 
            print ("Que accion realiza la etiqueta s?: a)Aplica tachado, b)cambia todas las palabras, c)tacha palabras, d)todas de las anteriores, e)no se")
            p30 = ["a","b","c","d","e"]  
            r30 = raw_input ("Ingrese la respuesta:")
            r30 = raw_input ("Ingrese la respuesta:")        
            if (r30 == "a" in p30):
                global sumador,restador  
                print "1 punto"                
                sumador += 1 
            elif (r30 == "d" in p30): 
                print "1 punto"                 
                sumador += 1
            else: 
                print "0 punto"                
                restador += 1 
                R_i.append("Que accion realiza la etiqueta s?")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            
def resultado():            
            if(sumador>= 15 and sumador <= 20):
                print "Aprobo por obtener:" ,sumador,"respuestas correctas"
            elif (sumador >= 20 and sumador <= 25):
                print "Aprobo por obtener:" ,sumador,"respuestas correctas y certificado como experto en informatica"
            elif (sumador >= 25 and sumador <= 30):
                print "Aprobo por obtener:" ,sumador,"aprueba el cuestionario con honores "
            else:
                print "Obtuvo menos 15 respuesta correctas que eso equivala a un 60%, tiene la oportunidad de hacerlo de nuevo, pero con penalizacion del 20% sobre nota final"
def resultado1():            
            if(sumador1>= 15 and sumador1 <= 20):
                print "Aprobo por obtener:" ,sumador1,"respuestas correctas"
            elif (sumador1 >= 20 and sumador1 <= 25):
                print "Aprobo por obtener:" ,sumador1,"respuestas correctas y certificado como experto en informatica"
            else:
                print "Obtuvo menos 15 respuesta correctas que eso equivalale a dejar el curso"

def Datos_del_usuario(): 
    D_u['Nombres'] = Nombres
    D_u['Apellidos'] = Apellidos
    D_u['Direccion'] = Direccion
    D_u['Departamento'] = Departamento
    D_u['Telefono'] = Telefono
        
while True:
    print "QUE TANTO SABES DE HTML"
    print "1 - Registrar nuevo usuario"
    print "2 - Iniciar cuestionario"
    print "3 - Interrumpir cuestionario"
    print "4 - Mostrar resultados"
    print "5 - Salir"
    
    opcion = int(raw_input("Seleccione opcion: "))
    
    if opcion == 1:
        while True:
            try:
                

                Nombres = str(raw_input("Nombres: "))
                Apellidos = str(raw_input("Apellidos: "))
                Direccion = str(raw_input("Direccion: "))
                Departamento = str(raw_input("Departamento: "))
                Telefono = int(input("Telefono: "))
                if (Telefono == D_u.get('Telefono')):
                    print "ya existe"
   
                Datos_del_usuario()
                break
            except:
                print "el tipo de dato ingresado es invalido"
   
   
   
   
    elif opcion == 2:
       while True:
            try:
                N = raw_input("Nombre: ")
                if (N == D_u.get('Nombres')):
                    print "valido"
                    Datos_del_usuario()
                    break             
            except:
                print "no valido"
                
       import random  
       print "al momento de contestar coleque el literal corespondiente" 
       preguntas = [pregunta1_1(), pregunta1_2(), pregunta1_3(), pregunta1_4(), pregunta1_5(), pregunta1_6(), pregunta1_7(), pregunta1_8(), pregunta1_9(), pregunta1_10(), pregunta1_11(), pregunta1_12(), pregunta1_13(), pregunta1_14(), pregunta1_15(), pregunta1_16(), pregunta1_17(), pregunta1_18(), pregunta1_19(), pregunta1_20(), pregunta1_21(), pregunta1_22(), pregunta1_23(), pregunta1_24(), pregunta1_25(), pregunta1_26(), pregunta1_27(), pregunta1_28(), pregunta1_29(), pregunta1_30()]
       random.choice(preguntas)
       print 'Tu puntaje es de: ', sumador, ' puntos'

    elif opcion == 3:
        print "al volver hacer el cuestionario se le restara 20% de su nota final"
        
        preguntas = [pregunta1(), pregunta2(), pregunta3(), pregunta4(), pregunta5(), pregunta6(), pregunta7(), pregunta8(), pregunta9(), pregunta10(), pregunta11(), pregunta12(), pregunta13(), pregunta14(), pregunta15(), pregunta16(), pregunta17(), pregunta18(), pregunta19(), pregunta20(), pregunta21(), pregunta22(), pregunta23(), pregunta24(), pregunta25()]
        
        print 'Tu puntaje es de: ', sumador1, ' puntos'
        resultado1()
    elif opcion == 4:
            print ""
            print 'Nombre:',D_u['Nombres']
            print ""
            print 'Preguntas acertadas: ', sumador
            print ""
            print 'Preguntas no acertadas: ', restador
            print ""
            print resultado()
            print ""
            print "preguntas en la que se equivoco"
            print R_i
            print ""
    elif opcion == 5:
        break    
        
    
    else:
        print "incorrecto"