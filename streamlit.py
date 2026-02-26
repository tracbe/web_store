import streamlit as st

st.set_page_config(page_title = "Simple Store" , page_icon = "🛒")

st.title("🛒 My Simple Online Store")

st.text("Welecome! Browse our eclusive products belw:")

st.divider()

products = [
{"name" : "smart watch" , "price": 150, "image":"gs-ultra-8_1.jpg"},
{"name" : "wireless headphone" , "price": 80 , "image":"images (2).jpg"} , 
{"name" : "leather backpack" , "price": 55 , "image":"187_dbd6a372-a23c-4c1b-bc37-bcd7fca2f057.webp"} 
]

if "cart" not in st.session_state :
    st.session_state.cart =[]
# display 
c1 , c2 , c3 = st.columns(3)
with c1 :
    st.image(products[0]["image"])
    st.subheader(products[0]["name"])
    st.info(products[0]["price"])
    if st.button(f'buy {products[0]["name"]}') :
        st.session_state.cart.append({"name":products[0]["name"] ,"price": products[0]["price"]})  #{"name":"smart wetch" ,"price": 150}
        st.success(f'added {products[0]["name"]}')
with c2 :
    st.image(products[1]["image"])
    st.subheader(products[1]["name"])
    st.info(products[1]["price"])
    if st.button(f'buy {products[1]["name"]}') :
        st.session_state.cart.append({"name":products[1]["name"] ,"price": products[1]["price"]})
        st.success(f'added {products[1]["name"]}')
with c3 :
    st.image(products[2]["image"])
    st.subheader(products[2]["name"])
    st.info(products[2]["price"])
    if st.button(f'buy {products[2]["name"]}') :
        st.session_state.cart.append({"name":products[2]["name"] ,"price": products[2]["price"]})
        st.success(f'added {products[2]["name"]}')


st.divider()
st.header("your invoice")

if len(st.session_state.cart) > 0:
    total = 0 
    
    for i in st.session_state.cart :
        total = total + i["price"]
        st.info(f"name:{i['name']} , price {i['price']} ")

    st.success(f"total : {total} $")

        
