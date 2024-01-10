import streamlit as st

#st.header("Yo I'm on the web :surfer:")
st.title("Suma tres Números")

st.write("## Usando `st.number_input`")
n1 = st.number_input("Primer sumando",step=1)
n2 = st.number_input("Segundo sumando",step=1)
n3 = st.number_input("Tercer sumando",step=1)

if n1 and n2 and n3:
    st.write(f"La suma de los tres números es {n1+n2+n3}")

st.write("## Usando `st.slider`")

p1 = st.slider("Primer sumando")
p2 = st.slider("Segundo sumando")
p3 = st.slider("Tercer sumando")

if p1 and p2 and p3:
    st.write(f"La suma de los tres números es {p1+p2+p3}")