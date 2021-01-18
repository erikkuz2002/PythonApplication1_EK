while True:
     av_reg=input("Valik")
     if av_reg=="av":
          print("Avtorizeerimine")
     elif av_reg=="reg":
          print("registreerimine")
          m_avto=input("registeerimise tüüp")
          if m_avto=="m": 
               print("Manual")
          else: 
               print("Auto")   #ptint
     else:
          break
