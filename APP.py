import streamlit as st

# Configuración de página
st.set_page_config(page_title="Clase de Programación", layout="wide")


with st.sidebar:
    st.markdown("Clases")
    st.button("Ejemplo clase guardada 1")
    st.button("Ejemplo clase guardada 2")
    st.button("Ejemplo clase guardada 3")


st.markdown(
    "<h1 style='text-align: center;'>Bienvenido a tu clase de programación</h1>",
    unsafe_allow_html=True
)

# Área del "chat" simulado
st.markdown("## ")
pregunta = st.text_input("Escribe tu pregunta:", placeholder="Quiero saber sobre...")

if pregunta:
    st.success(f"Respuesta simulada a: **{pregunta}**")
