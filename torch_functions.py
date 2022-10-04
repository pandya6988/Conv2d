import math

def same_padding(in_size:int, kernel_size:int, stride:int):
    return math.ceil( (in_size*(stride-1)-stride+kernel_size)/2 )

def compute_output_shape(in_size:int, kernel_size:int, stride:int, padding:int):
    return int(((in_size+(2*padding)-kernel_size)/stride) + 1) 

def compute_kernel_for_output_size(in_size:int, output_size:int, stride:int, padding:int):
    return in_size + (2*padding) + stride - (stride*output_size)