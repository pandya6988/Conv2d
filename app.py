import streamlit as st 
from torch_functions import *

st.title("PyTorch Conv2d")

info = """
PyTorch is the most popular library among researchers as it provides more control over algorithm. As you have to provide each parameter manually it can slow you down. 

For example: **torch.nn.Conv2d()** API. Here, we have to provide padding, kernel size etc. We have to calculate these parameters to get the desired output shape and gain more control.
    
**Here, I am trying to solve exactly this problem.**
***
"""
st.markdown(info)

st.subheader("Padding size to maintain the input hight and width")

with st.form("my_form1"):
    a1,a2,a3 = st.columns(3)
   
    with a1:
       in_size = int(st.number_input("input size", step=1))
       
    with a2: 
        kernel_size = int(st.slider("kernel size", step=1, min_value=1, max_value=9))

    with a3:
       stride = int(st.slider("stride", step=1, min_value=1, max_value=7))
    
   # Every form must have a submit button.
    submitted = st.form_submit_button("Calculate")
    if submitted:
        pad_value = same_padding(in_size=in_size, kernel_size=kernel_size, stride=stride)
        if pad_value > 0:
            st.write(f"To maintain the input size please set \"padding={pad_value}\"")
            code = f"""
        import torch.nn as nn  
nn.Conv2d(in_channel, out_channel, kernel_size={kernel_size}, stride={stride}, padding={pad_value})
        """
            st.code(code, language='python')
        else: st.warning("Please correct your input.")

st.markdown("***")
#####################################################
#####################################################
st.subheader("Calculate kernel size for desired output")

with st.form("my_form2"):
    b1,b2,b3, b4 = st.columns(4)
   
    with b1:
       in_size = int(st.number_input("input size", step=1))
       
    with b2: 
        out_size = int(st.number_input("output size", step=1))

    with b3:
       stride = int(st.slider("stride", step=1, min_value=1, max_value=7))
       
    with b4:
       padding = int(st.number_input("padding", step=1))
    
   # Every form must have a submit button.
    submitted = st.form_submit_button("Calculate")
    if submitted:
        kernel_size = compute_kernel_for_output_size(in_size=in_size, output_size=out_size, stride=stride, padding=padding)
        if kernel_size > 0:
            st.write(f"To generate the desired output please set \"kernel_size={kernel_size}\"")
            code1 = "import torch.nn as nn"
            code2 = f"\nnn.Conv2d(in_channel, out_channel, kernel_size={kernel_size}, stride={stride}, padding={padding})"
            st.code(code1+code2, language='python')
            
        else: st.warning("Please correct your input.")

st.markdown("***")
#####################################################
#####################################################
st.subheader("Output shape")

with st.form("my_form3"):
    c1,c2,c3, c4 = st.columns(4)
   
    with c1:
       in_size = int(st.number_input("input size", step=1))
       
    with c2: 
        kernel_size = int(st.slider("kernel size", step=1, min_value=1, max_value=9))

    with c3:
       stride = int(st.slider("stride", step=1, min_value=1, max_value=7))
       
    with c4:
       padding = int(st.number_input("padding", step=1))
    
   # Every form must have a submit button.
    submitted = st.form_submit_button("Calculate")
    if submitted:
        output_size = compute_output_shape(in_size=in_size, kernel_size=kernel_size, stride=stride, padding=padding)
        if output_size > 0:
            st.write(f"Output width/hight:  {output_size}")
        else: st.warning("Please correct your input.")

st.markdown("***")