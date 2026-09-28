import streamlit as st

# some fuctions of streamlit
st.title("My Dashboard")
st.write("Hello! Let's learn Streamlit.")
st.title("Sales Dashboard")
st.header("defb")
st.subheader("thank you")
st.text("thank you")
st.caption("tank you")
st.markdown("**markdown**")
st.write("hHI")

# dashboard its interactive table isnt
import pandas as pd
import streamlit as st

data = {
    "Name": ["Aisha", "Rahul", "Priya"],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)

print(st.dataframe(df))

#for symbols nice looking
print(st.metric(
    label="Revenue",
    value="₹50,000",
    delta="10%"
))

# checkbox for to do list
show_data = st.checkbox("Show data")
print(show_data)
if show_data:
    st.write("Here is the data!")

# slider 
age = st.slider(
    "Select your age",
    1,
    100
)

st.write("Your age is:", age)

ag = st.slider(
    "Select age",
    0,
    100,
    step=5
)

marks = st.slider(
    "Marks",
    0,
    100,
    50
)
age_range = st.slider(
    "Select age range",
    0,
    100,
    (18, 30)
)

st.write("Selected range:", age_range)

price = st.slider(
    "Select price",
    0.0,
    100.0,
    25.5,
    step=0.5
)
# the option thing u cant choose more then one here
choice = st.radio(
    "Choose a language",
    ["Python", "Java", "C++"]
)

st.write("You selected:", choice)


# slect from the options aviable
city = st.selectbox(
    "Choose a city",
    ["Bangalore", "Mumbai", "Delhi"]
)


#multiple metric
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Revenue", "₹50K")

with col2:
    st.metric("Profit", "₹10K")

with col3:
    st.metric("Customers", "1200")


#if thing

name = st.text_input("Enter your name")


marks = st.slider("Select your marks", 1, 100)

if name:
    st.write("Hello", name)
    st.write("You have", marks, "marka")

#multiselect 
languages = st.multiselect(
    "Choose languages",
    ["Python", "Java", "C++"]
)
# markdown
print(st.markdown("# Main Heading"))
print(st.markdown("## Main Heading"))
print(st.markdown("### Main Heading"))
st.markdown("*This is italic*")
st.markdown("***Hello***")
st.markdown("""
1.Python
- Pandas
- Streamlit
- Matplotlib
""")


# button thing
st.markdown("""
<style>
.stButton > button {
    background-color: yellow;
    color: green;
}
</style>
""", unsafe_allow_html=True)

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Click me"):
    st.session_state.count += 1
    
    
if st.session_state.count >= 1:
    print("yeah i say click me but not this many times")
    st.write("yo budd wats the hurry")
    st.image("chapter8/download.jpe", width=200)
if st.session_state.count >= 5:
    st.write("how many times will you press me have you lost it")
    st.markdown("""
<style>
.stButton > button {
    background-color: green;
    color: red;
}
</style>
""", unsafe_allow_html=True)
    if st.session_state.count >= 10:
        st.markdown("""
<style>
.stButton > button {
    background-color: red;
    color: white;
}
</style>
""", unsafe_allow_html=True)
        st.write("how can u do this to me u little!")
        if st.session_state.count >= 15:
            st.write("I SAY STOP IT NOW")
            if st.session_state.count >= 20:
                st.write("NOW YOU R ASKING FOR A FIGHT!")
                
st.write("Button pressed:", st.session_state.count, "times")

# code
st.code("print('Hello')")
st.code("""
x = 10
y = 20
if x>y :
   print(x + y)
""", language="python")# syntax 

st.latex(r"\frac{a}{b}")
st.latex(r"\sqrt{x}")
import os

# image audio video
st.write(os.getcwd())
st.write(os.path.exists("image.png"))



st.image("chapter8/image.png", width=200)
st.audio("chapter8/MusicSample.mp3")
st.video("chapter8/jester final.mp4",width=300)
st.table(df)