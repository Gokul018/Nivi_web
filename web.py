import streamlit as st
from PIL import Image

# Configure page settings
st.set_page_config(
    page_title="Nivetha - Personalized Nutrition",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Hero section */
        .hero-container {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 4rem 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        /* Typography */
        h1 { color: #2C3E50; font-size: 2.5rem !important; font-weight: 700 !important; }
        h2 { color: #34495E; font-size: 2rem !important; margin-bottom: 1rem !important; }
        
        /* Cards */
        .service-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            transition: transform 0.3s ease;
        }
        
        .service-card:hover { transform: translateY(-5px); }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Services", "Resources", "Testimonials", "Contact"])

# **Page Definitions**
def home_page():
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Hi, I'm Nivetha 👋")
        st.subheader("Your Partner in Achieving Health and Wellness Through Personalized Nutrition")
        st.write("""
        Transform your health with nutrition tailored just for you -- whether you're managing 
        a condition or aiming for overall wellness, I'm here to support you.
        """)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("Book Free Consultation")
        with btn_col2:
            st.button("Learn More")
    
    with col2:
        st.image("e:/nivi/image/1.jfif", caption="")

    st.markdown('</div>', unsafe_allow_html=True)

    # **Services Preview**
    st.header("What I Offer")
    service_cols = st.columns(3)
    
    services = [
        {"title": "Personalized Diet Plans", "description": "Custom nutrition plans tailored to your unique needs and goals"},
        {"title": "1-on-1 Counseling", "description": "Personal nutrition guidance and ongoing support"},
        {"title": "Health Monitoring", "description": "Regular follow-ups and adjustments to ensure success"}
    ]
    
    for idx, service in enumerate(services):
        with service_cols[idx]:
            st.markdown(f"""
            <div class="service-card">
                <h3>{service['title']}</h3>
                <p>{service['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def about_page():
    st.title("About Me")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        Welcome! I'm Nivetha, a dedicated nutritionist passionate about helping 
        people achieve their health and wellness goals through personalized nutrition. 
        
        With a Postgraduate Diploma in Dietetics and hands-on experience at Christian Medical 
        College, Vellore, I specialize in crafting diet plans that are tailored to everyone's unique needs.
        """)
        
        st.subheader("My Mission")
        st.write("""
        My mission is to empower individuals to take control of their health and well-being 
        through personalized nutrition and education.
        """)
    
    with col2:
        st.image("e:/nivi/image/4.jfif", caption="")

    # Expertise
    st.subheader("Why Choose Me")
    expertise_cols = st.columns(4)
    
    expertise = [
        "Medical Nutrition Experience",
        "Evidence-Based Approach",
        "Personalized Solutions",
        "Regular Follow-ups"
    ]
    
    for idx, exp in enumerate(expertise):
        with expertise_cols[idx]:
            st.markdown(f"""
            <div class="service-card" style="text-align: center;">
                <h4>{exp}</h4>
            </div>
            """, unsafe_allow_html=True)

import streamlit as st

def services_page():
    st.title("Services")
    
    services = [
        {"title": "Nutritional Assessment", "description": "A detailed analysis of your current diet and health status", "image": "e:/nivi/image/13.jpg"},
        {"title": "Custom Meal Plans", "description": "Personalized nutrition plans designed for your lifestyle", "image": "e:/nivi/image/14.jfif"},
        {"title": "Condition Management", "description": "Specialized plans for diabetes, heart health, PCOS, and more", "image": "e:/nivi/image/15.jfif"},
        {"title": "Weight Management", "description": "Sustainable strategies for weight loss or gain", "image": "e:/nivi/image/16.jfif"}
    ]

    for service in services:
        col1, col2 = st.columns([1, 2])  # Adjust column widths

        with col1:
            st.image(service["image"], width=200)  # Reduce image size

        with col2:
            st.markdown(f"""
            <div class="service-card">
                <h3>{service['title']}</h3>
                <p>{service['description']}</p>
            </div>
            """, unsafe_allow_html=True)


def resources_page():
    st.title("Resources")
    
    articles = [
        "10 Superfoods to Boost Your Energy",
        "Managing PCOS with Diet",
        "Understanding Macronutrients",
        "Blood Sugar Control Tips",
        "Weight Management Guide"
    ]
    
    for article in articles:
        with st.expander(article):
            st.write("Full article coming soon...")
            st.button("Read More", key=article)

def testimonials_page():
    st.title("Success Stories")
    
    testimonials = [
        {"name": "Hemavathy", "text": "Nivetha's personalized approach helped me transform my eating habits and achieve my weight loss goals."},
        {"name": "Shruti", "text": "Her meal plans are practical and easy to follow. I feel healthier and more energized than ever!"}
    ]
    
    for testimonial in testimonials:
        st.markdown(f"""
        <div class="service-card">
            <p>"{testimonial['text']}"</p>
            <p><em>- {testimonial['name']}</em></p>
        </div>
        """, unsafe_allow_html=True)

def contact_page():
    st.title("Get in Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Contact Information")
        st.write("📧 Email: your-email@example.com")
        st.write("📞 Phone: +91 XXXXXXXXXX")
        st.write("📍 Address: Your Address Here")
    
    with col2:
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            st.form_submit_button("Send Message")

# **Display the Selected Page**
if page == "Home":
    home_page()
elif page == "About":
    about_page()
elif page == "Services":
    services_page()
elif page == "Resources":
    resources_page()
elif page == "Testimonials":
    testimonials_page()
elif page == "Contact":
    contact_page()
