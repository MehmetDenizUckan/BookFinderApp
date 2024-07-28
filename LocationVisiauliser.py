# Author: Uckan
# -*- coding: utf-8 -*-
from PIL import Image



# This code merges two images. The image of a library and a red arrow image to point out the location of the book
def merge_images(ABC_image_path, DEF_image_path ,arrow_image_path, g_image_path, position):
    # Open the ABC image
    ABC_img = Image.open(ABC_image_path)
    
    # Open the DEF image
    DEF_img = Image.open(DEF_image_path)
    
    # Open the arrow image
    arrow_img = Image.open(arrow_image_path)
    
    # Open the g part of the library image
    glib_img = Image.open(g_image_path)

    # Ensure the arrow image has an alpha channel
    if arrow_img.mode != 'RGBA':
        arrow_img = arrow_img.convert('RGBA')

   
    # Unpack coordinates and shelf flag from position tuple
    coordinate_x, coordinate_y, shelf_g_or_not , shelf_abc_or_not = position

    if shelf_g_or_not:
            # Paste the arrow image onto the G shelf image
            glib_img.paste(arrow_img, (coordinate_x, coordinate_y), arrow_img)
            
            # Save the result
            merged_image_path = "merged_image.png"
            glib_img.save(merged_image_path)
            
            
            print(f"Merged image saved as {merged_image_path}")
            
                    
            # Show the merged image
            glib_img.show()
    
            
    elif shelf_abc_or_not :
            # Paste the arrow image onto the library image
            ABC_img.paste(arrow_img, (coordinate_x, coordinate_y), arrow_img) 
                   
            # Save the result
            merged_image_path = "merged_image.png"
            ABC_img.save(merged_image_path)
            
            
            print(f"Merged image saved as {merged_image_path}")
               
            # Show the merged image
            ABC_img.show()
    
    else:
          # Paste the arrow image onto the library image
            DEF_img.paste(arrow_img, (coordinate_x, coordinate_y), arrow_img) 
                   
            # Save the result
            merged_image_path = "merged_image.png"
            DEF_img.save(merged_image_path)

            
            print(f"Merged image saved as {merged_image_path}")
            
               
            # Show the merged image
            DEF_img.show()
        
    
                    

# Paths of the respective images

ABC_image_path = "A-B-C_Lib.jpg"
DEF_image_path = "D-E-F_Lib.jpg"
arrow_image_path = "arrow.png"
g_image_path = "glib.jpg"




# Since there are diffenet images for shelfs the coordinates should be rearranged for every letter group
# Thats Why I added a shelf flags
def position_arranger(x_coor, y_coor , letter):
    g_or_not = False   
    ABC_or_not = False
    abc_list = ['A', 'B', 'C']
    if letter in abc_list:
        ABC_or_not = True
    elif letter == 'G':
        g_or_not = True
    
    position = (x_coor , y_coor , g_or_not, ABC_or_not)
    return position

# Starting points if ABC : 900 , 300 if G 1200 , 600 if DEF 1100 , 400
#her bir raf y ABC için 550 if G 700 if DEF 500
# ABC x için 1100 if DEF 1050


#postion = position_arranger(900, 850 , 'A')
#merge_images(ABC_image_path , DEF_image_path , arrow_image_path , g_image_path ,postion)