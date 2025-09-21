import streamlit as st
import requests


restaurants = {
    "vizag": {
        "Domino": ["Margherita Pizza", "Pepperoni Pizza", "Veggie Supreme"],
        "Pizza Hut": ["Cheese Pizza", "Chicken Supreme", "Paneer Tikka Pizza"],
        "Ciro's Pizzeria": ["Neapolitan Pizza", "Buffalo Mozzarella", "Garlic Bread"],
        "Aqua-The park":["lobster tail","roast peppers","Prawns","basil","salmon","Pizza Indiana","4 cheese","Mushroom pizza" ],
        "Flying Spaghetti Monster":["Marghertia","gamberetti","E Sugo Rosa" ],
        "Oven Story Pizza":[ "Death By Cheese","Roasted Chickhen","Chicken maximus"],
       "TFC tasty Food Court":["Death By Cheese"," Roasted Chicken", "BBQ Chicken"," Chicken Maximus", "Chicken Tikka"],
       "The project by oven Story":[" Double Cheese Corn Veggie Delight"," Tandoori Paneer Tikka", "Garden Fresh Veggie", "Dragonfire Paneer"],
       "Pappas Pizza":["Signature Korean Paneer Pizza", " buldak sauce", "spicy paneer chunks"," onion", "capsicum","tomato"],
       "Pizza stories":[ "chicken golden delight","non veg supreme","chicken dominator","pepper barbecue"],
       "lasya pizza":[ "pepper barbecue chicken","chicken sausage","chicken fiesta","Indi chicken tikka","chicken pepperoni"],
       "Bunny's Pizza":[ "Creamy tomato Pasta pizza","keema Do pyaza","moroccan spice pasta pizza"],
       "Bentoz Pizza":[ "Corn N cheese","Paneer paratha","chicken keema paratha pizza"],
       "Mr Pizza":[ "veg loaded","cheesy","paneer&onion","capsicum","onion","golden corn"],
       "Gaga Pizza":["double cheese margherita","Farm House","peppy paneer","mexican green wave","deluxe veggie" ],
      "Blazed pizza":["fresh veggie","veggie paradise","paneer makhani","indi tandoori paneer","achari do pyaza" ],
   },
    "gajuwaka": {
        "Mom's Mazic": ["Buffalo Mozzarella Special", "Classic Veg", "Spicy Chicken"],
        "Aqua-The park": ["Seafood Pizza", "Veg Delight", "BBQ Chicken Pizza"],
       "Pinoz Pizza":["Death By Cheese"," Roasted Chicken", "BBQ Chicken"," Chicken Maximus", "Chicken Tikka" ],
       "Pizza Hut": ["Double Cheese Corn Veggie Delight"," Tandoori Paneer Tikka", "Garden Fresh Veggie", "Dragonfire Paneer" ],
      "Chicago Pizza":[ "pepper barbecue chicken","chicken sausage","chicken fiesta","Indi chicken tikka","chicken pepperoni"],
      "Pizza Capital":["lobster tail","roast peppers","Prawns","basil","salmon","Pizza Indiana","4 cheese","Mushroom pizza" ],
      "The Fusion Point":[ "double cheese margherita","Farm House","peppy paneer","mexican green wave","deluxe veggie" ],
      "Eaters Stop":[ "pepper barbecue chicken","chicken sausage","chicken fiesta","Indi chicken tikka","chicken pepperoni"],
      "Domino's":["fresh veggie","veggie paradise","paneer makhani","indi tandoori paneer","achari do pyaza" ],
      "7th Heaven Bakery":[  "pepper barbecue chicken","chicken sausage","chicken fiesta","Indi chicken tikka","chicken pepperoni"],
      "Bae's food":[  "chicken golden delight","non veg supreme","chicken dominator","pepper barbecue"],
    }
}
restaurant_images = {
    "Domino": [
        "images/domino1.jpeg",
        "images/domino2.jpeg"
    ],
    "Pizza Hut": [
        "images/pizzahut1.jpeg",
        "images/pizzahut2.jpeg"
    ],
    "Ciro's Pizzeria": [
        "images/ciros1.jpeg",
        "images/ciros2.jpeg"
    ],
    "Aqua-The park": [
        "images/aqua1.jpeg",
        "images/aqua2.jpeg"
    ],
    "Flying Spaghetti Monster": [
        "images/fsm1.jpeg",
        "images/fsm2.jpeg"
    ],
    "Oven Story Pizza": [
        "images/ovenstory1.jpeg",
        "images/ovenstory2.jpeg"
    ],
    "TFC tasty Food Court": [
        "images/tfc1.jpeg",
        "images/tfc2.jpeg"
    ],
    "The project by oven Story": [
        "images/project1.jpeg",
        "images/project2.jpeg"
    ],
    "Pappas Pizza": [
        "images/pappas1.jpeg",
        "images/pappas2.jpeg"
    ],
    "Pizza stories": [
        "images/pizzastories1.jpeg",
        "images/pizzastories2.jpeg"
    ],
    "lasya pizza": [
        "images/lasya1.jpeg",
        "images/lasya2.jpeg"
    ],
    "Bunny's Pizza": [
        "images/bunnys1.jpeg",
        "images/bunnys2.jpeg"
    ],
    "Bentoz Pizza": [
        "images/bentoz1.jpeg",
        "images/bentoz2.jpeg"
    ],
    "Mr Pizza": [
        "images/mrpizza1.jpeg",
        "images/mrpizza2.jpeg"
    ],
    "Gaga Pizza": [
        "images/gaga1.jpeg",
        "images/gaga2.jpeg"
    ],
    "Blazed pizza": [
        "images/blazed1.jpeg",
        "images/blazed2.jpeg"
    ],
    "Mom's Mazic": [
        "images/moms1.jpeg",
        "images/moms2.jpeg"
    ],
    "Pinoz Pizza": [
        "images/pinoz1.jpeg",
        "images/pinoz2.jpeg"
    ],
    "Chicago Pizza": [
        "images/chicago1.jpeg",
        "images/chicago2.jpeg"
    ],
    "Pizza Capital": [
        "images/pizzacapital1.jpeg",
        "images/pizzacapital2.jpeg"
    ],
    "The Fusion Point": [
        "images/fusion1.jpeg",
        "images/fusion2.jpeg"
    ],
    "Eaters Stop": [
        "images/eaters1.jpeg",
        "images/eaters2.jpeg"
    ],
    "Domino's": [
        "images/dominos1.jpeg",
        "images/dominos2.jpeg"
    ],
    "7th Heaven Bakery": [
        "images/7thheaven1.jpeg",
        "images/7thheaven2.jpeg"
    ],
    "Bae's food": [
        "images/baes1.jpeg",
        "images/baes2.jpeg"
    ],
}
st.markdown(
    """
    <div style="
        text-align: center;
        background-color:#FAFAFA;
        padding:25px;
        border-radius:12px;
        border:1px solid #E0E0E0;
        ">
        <img src="images/logo2.png" width="20">
        <h1 style="color:#B22222; margin-bottom:5px;">We Love Pizza</h1>
        <h4 style="color:#2E7D32; font-weight:400; margin-top:0;">Your trusted restaurant guide</h4>
    </div>
    """,
    unsafe_allow_html=True
)



st.title("Welcome!")

# 1. Location selection
location = st.selectbox("📍Select Location", options=["vizag", "gajuwaka"])

# 2. Restaurant selection (only if location is selected)
if location:
    rest_names = list(restaurants[location].keys())
    restaurant = st.selectbox("📜 Select Restaurant", options=rest_names)
    
    # 3. Display menu (only if restaurant is selected)
    if restaurant:
        images=restaurant_images.get(restaurant,[])
        if images:
            cols=st.columns(len(images))
            for i,img_path in enumerate(images):
                with cols[i]:
                    st.image(img_path,width="stretch")                
        st.subheader(f"Menu for {restaurant}:")
        menu_items=restaurants[location][restaurant]
        for item in menu_items:
            st.markdown(
                   
                f"""
                <div style="background-color:#FFFFFF;
                            border:1px solid #E0E0E0;
                            padding:8px 12px;
                            margin:4px 0;
                            border-radius:8px;
                            color:#212121;">
                    {item}
                </div>
                """,
                unsafe_allow_html=True
           )                

    # Show images side by side
    

st.markdown("---")

# Q&A Section
question = st.text_input("💬 Ask a question about pizza restaurants:")

if st.button("Ask") and question:
    response = requests.get("http://localhost:8000/ask", params={"question": question})
    if response.ok:
        data = response.json()
        st.subheader("📖 Relevant Reviews:")
        for review in data["reviews"]:
            st.markdown(
                f"""
                <div style="background-color:#FFFFFF; border:1px solid #E0E0E0;
                            border-radius:10px; padding:12px; margin-bottom:10px;">
                    <strong style="color:#B22222;">{review['restaurant']} ({review['city']})</strong><br>
                    <span style="color:#757575;">{review['date']} | Rating: ⭐ {review['rating']}</span>
                    <p style="margin-top:8px; color:#212121;">{review['content']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.error("Failed to get response from API.")