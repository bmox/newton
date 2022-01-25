import streamlit as st
import numpy as np
import pandas as pd
st.title("Calculate Newton Forward and Backward")

input_range = st.number_input('Enter number of data points',key='input_range')
# st.write(type(input_range))
n=int(input_range)
x = np.zeros((n))
y = np.zeros((n,n))
for i in range(n):
    x[i] = st.number_input('x['+str(i)+']:',key=x[i] )
    y[i][0] = st.number_input('y['+str(i)+']:',key=y[i][0])

a = st.number_input('Base value',key='a')
find = st.number_input('Find value',key='find')
option = st.selectbox('Choose method',('Newton Forward','Newton Backward'))
a=float(a)
find=float(find)

        
def format_float(number):
  new_val = "{:0.2f}".format(number)
  new_val=float(new_val)
  return new_val


def newton_forward(x,y,a,find):
  x_value=x.tolist()
  index=x_value.index(a)
  h=x_value[1]-x_value[0]
  u=(find-a)/h
  table=y.tolist()
  if len(table[0])>=5:
    values=[]
    for i in range(len(table[:5])):
      values.append(table[index][i])
    # print(values)
    f1=values[0]
    f2=(u*values[1])
    f3=(u*(u-1)*values[2])/factorial(2)
    f4=(u*(u-1)*(u-2)*values[3])/factorial(3)
    f5=(u*(u-1)*(u-2)*(u-3)*values[4])/factorial(4)
    result=f1+f2+f3+f4+f5
  if len(table[0])<5:
    values=[]
    for i in range(len(table)):
      values.append(table[index][i])
    # print(values)
    if len(table[0])==4:
      f1=values[0]
      f2=(u*values[1])
      f3=(u*(u-1)*values[2])/factorial(2)
      f4=(u*(u-1)*(u-2)*values[3])/factorial(3)
      result=f1+f2+f3+f4
    if len(table[0])==3:
      f1=values[0]
      f2=(u*values[1])
      f3=(u*(u-1)*values[2])/factorial(2)
      result=f1+f2+f3
      
  return result    


def factorial(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))
    
def newton_backward(x,y,a,find):
  x_value=x.tolist()
  h=float(x_value[1]-x_value[0])
  u=(find-a)/h
  table=y.tolist()
  reverse_table=[]
  for i in range( len(table) - 1, -1, -1) :
    reverse_table.append(table[i])
  reverse_x_value=x_value[::-1]
  index=reverse_x_value.index(a)
  values=[]
  j=0
  for i in reverse_table[index:]:
    values.append(i[j])
    j+=1
  if len(table[0])>=5:
    f1=values[0]
    f2=(u*values[1])
    f3=(u*(u+1)*values[2])/factorial(2)
    f4=(u*(u+1)*(u+2)*values[3])/factorial(3)
    f5=(u*(u+1)*(u+2)*(u+3)*values[4])/factorial(4)
    result=f1+f2+f3+f4+f5
  if len(table[0])==4:
    f1=values[0]
    f2=(u*values[1])
    f3=(u*(u+1)*values[2])/factorial(2)
    f4=(u*(u+1)*(u+2)*values[3])/factorial(3)
    result=f1+f2+f3+f4
  if len(table[0])==3:
    f1=values[0]
    f2=(u*values[1])
    f3=(u*(u+1)*values[2])/factorial(2)
    result=f1+f2+f3
  return result



if st.button('calculate'):
    # Generating forward difference table dataframe using pandas
    for i in range(1,n):
        for j in range(0,n-i):
            y[j][i] = y[j+1][i-1] - y[j][i-1]
    main_list=[]
    for i in range(0,n):
        temp_list=[]
        temp_list.append(format_float(x[i]))
        for j in range(0, n-i):
            temp_list.append(format_float(y[i][j]))
        main_list.append(temp_list)
    name_df=["x","f(x)"]
    for i in range(len(main_list[0])-2):
        name_df.append(f"Δ{i+1}f(x)")
    main_list.insert(0,name_df)
    df = pd.DataFrame(main_list)
    df.columns = df.iloc[0]
    df.drop(df.head(1).index, inplace=True)
    # df.replace(np.NaN, '', inplace=True)

    hide_table_row_index = """
                <style>
                tbody th {display:none}
                .blank {display:none}
                </style>
                """

 
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Display a static table
    st.table(df)
    
    if option=="Newton Forward":
        result=newton_forward(x,y,a,find)
        st.write(f"For {find} Newton Forward ans is  {result}")
    if option=="Newton Backward":
        result=newton_backward(x,y,a,find)
        st.write(f"For {find} Newton Backward ans is  {result}")
    
   
    
        
        

            
