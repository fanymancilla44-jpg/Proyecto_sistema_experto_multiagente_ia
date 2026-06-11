import streamlit as st

st.set_page_config(
    page_title="AnimeFull",
    layout="wide"
)

st.title("AnimeFull")
st.subheader("Sistema experto multiagente para una tienda de anime")

st.write("Este sistema ayudara a gestionar productos, inventario, clientes, pedidos y recomendaciones.")

st.sidebar.title("Menu principal")

opcion = st.sidebar.radio(
    "Selecciona una seccion:",
    [
        "Inicio",
        "Inventario",
        "Clientes",
        "Pedidos",
        "Recomendaciones",
        "Alertas",
        "Agentes"
    ]
)

if opcion == "Inicio":
    st.header("Panel principal")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Productos registrados", "0")

    with col2:
        st.metric("Pedidos generados", "0")

    with col3:
        st.metric("Alertas de stock", "0")

    st.write("Esta es la primera pantalla base del sistema.")

elif opcion == "Inventario":
    st.header("Inventario")
    st.write("Aqui se mostraran los productos registrados de la tienda.")

elif opcion == "Clientes":
    st.header("Clientes")
    st.write("Aqui se podran registrar y consultar clientes.")

elif opcion == "Pedidos":
    st.header("Pedidos")
    st.write("Aqui se podran generar pedidos o ventas.")

elif opcion == "Recomendaciones":
    st.header("Recomendaciones")
    st.write("Aqui el sistema recomendara productos segun lo que busque el cliente.")

elif opcion == "Alertas":
    st.header("Alertas de inventario")
    st.write("Aqui apareceran los productos con bajo stock o agotados.")

elif opcion == "Agentes":
    st.header("Agentes del sistema")

    st.write("En esta parte se mostraran las areas inteligentes que ayudaran al sistema a tomar decisiones.")

    st.write("Cliente: entiende lo que busca el usuario.")
    st.write("Inventario: revisa productos, precios y stock.")
    st.write("Recomendador: busca productos que coincidan con lo que quiere el cliente.")
    st.write("Pedidos: registra pedidos o ventas.")
    st.write("Reabastecimiento: detecta productos con bajo stock.")
    st.write("Explicador: muestra por que el sistema tomo una decision.")