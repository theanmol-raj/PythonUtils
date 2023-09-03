# This script has all the image preprocessing functions for the tensorflow v 2.12.0+
# Made by Anmol Raj 
# Github : https://github.com/theanmol-raj
# LinkedIn : https://www.linkedin.com/in/anmolraj5/


import tensorflow as tf

def fullPreprocessing(image : any  ,label : str ,scale : bool = True ,image_shape : float | int = 224 ):
    """
    This function does complete preprocessing from the flow 
    Current Flow :
    > Resize : function resizeImage(image , image_shape = 224)
    > Scaling : function scaleImage(image)
    > Cast to 'float32' : function castFloat(image)
    """
    image = resizeImage(image , image_shape)
    print('pass 1')
    if(image.dtype != tf.float32) :
        image = castFloat(image)
    print('pass 2')
    if(scale) :
        image = scaleImage(image)
    print('pass 3')
    return image ,label






def castFloat(image):
    """
    Cast tensor from any dtype to 'float32' 
    """
    return tf.cast(image , tf.float32)



    

def scaleImage(image):
    """
    Scales (Normalize) image tensor  to a value between 0 & 1 
    """
    return tf.cast(image , tf.float32) / 255.

def resizeImage(image , image_shape : float | int = 224):
    """
    Converts image size from default shape to image_shape (default 224)
    """
    return tf.image.resize(image ,[image_shape ,image_shape])

