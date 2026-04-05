import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import homepage
import projects
import about
import resume
import contact

ROOT_DIR = Path(__file__).resolve().parent

# Page Config
st.set_page_config(
    page_title="Yogeswarachary Modepalli | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# Load CSS
css_path = ROOT_DIR / "assets" / "style.css"
with open(css_path, "r", encoding="utf-8") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;">
            Yogeswarachary Modepalli
        </h2>
        <p style="color: #94a3b8; margin-top: 0.5rem;">Data Scientist & Engineer</p>
        <p style="color: #94a3b8; font-size: 0.9rem;">Career Shift | Fraud Detection | Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Projects", "Experience", "Education & Certs", "About", "Resume", "Contact"],
        icons=["house", "briefcase", "suitcase-fill", "award", "person", "file-text", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#020617"},
            "icon": {"color": "#00d2ff", "font-size": "20px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "10px 0",
                "border-radius": "5px",
                "color": "#94a3b8",
            },
            "nav-link-selected": {
                "background-color": "rgba(0, 210, 255, 0.1)",
                "color": "#00d2ff",
                "border": "2px solid #00d2ff",
            },
        }
    )
    
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
        <p><b>Quick Links</b></p>
        <p>
            <a href="https://github.com/Yogeswarachary" target="_blank" style="color: #00d2ff; text-decoration: none;">💻 GitHub</a><br>
            <a href="https://www.linkedin.com/in/yogeswarachary-modepalli-4a91571b8/" target="_blank" style="color: #00d2ff; text-decoration: none;">🔗 LinkedIn</a><br>
            <a href="https://yogeswarachary.github.io/Financial-Fraud-India-2024-Research/Financial_Fraud_India_FY_2024_2025.pdf" target="_blank" style="color: #00d2ff; text-decoration: none;">📄 Research Paper</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Page Routing
if selected == "Home":
    homepage.show()
elif selected == "Projects":
    projects.show()
elif selected == "Experience":
    st.markdown("""
    <h1 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem; line-height: 1.2; margin-bottom: 1rem;">
    Professional Experience
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1rem; color: #94a3b8; margin-bottom: 2rem;">
    3 years of progressive experience in regulatory compliance and visa consultancy, 
    with successful transition to <b>Data Science & Analytics</b>. 
    Proven ability to learn complex technical skills while delivering business value.
    </p>
    """, unsafe_allow_html=True)
    
    # Experience Timeline
    experiences = [
        {
            "title": "Student Visa Process Executive",
            "company": "Gateway Visas & Immigration Consultancy",
            "location": "Hyderabad",
            "duration": "Aug 2024 - Sep 2025",
            "highlights": [
                "Managed visa processing for 300+ international student, tourist visa, and work visa(H1B) applicants",
                "Maintained 100% compliance with immigration regulations",
                "Improved and Automated document verification process efficiency by 50%",
                "Handled stakeholder communication across 6+ countries"
            ]
        },
        {
            "title": "Process Analyst - Student Visa",
            "company": "LaGlobal Overseas Edu",
            "location": "Hyderabad",
            "duration": "May 2023 - Jul 2024",
            "highlights": [
                "Analyzed 200+ student visa application patterns to identify bottlenecks",
                "Implemented process improvements reducing turnaround time by 50%",
                "Trained 3+ new team members on compliance procedures",
                "Created automated documentation frameworks for regulatory requirements, and Handled multiple stack holders",
                "Developed checklist systems to reduce rejection rates"
            ]
        },
        {
            "title": "Admissions Expert - Student Visa",
            "company": "Flywise Overseas Edu",
            "location": "Hyderabad",
            "duration": "Jan 2023 - Apr 2023",
            "highlights": [
                "Consulted with 30+ students on visa pathways",
                "Maintained detailed case tracking, follow-up systems via Zoho CRM",
                "Achieved 70% visa approval rate",
                "Coordinated with 10+ universities for application processing"
            ]
        },
        {
            "title": "Java Intern",
            "company": "Pratian Technologies",
            "location": "Benguluru",
            "duration": "Jun 2022 - Sep 2022",
            "highlights": [
                "Worked on Java-based application called Job-Check",
                "Collaborated with Frontend developers on code reviews",
                "Learned OOP principles and design patterns",
                "First exposure to professional software development"
            ]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <h3 style="margin: 0; color: #00d2ff;">{exp['title']}</h3>
                    <p style="margin: 5px 0; color: #94a3b8;"><b>{exp['company']}</b> | {exp['location']}</p>
                    <p style="margin: 0; color: #64748b; font-size: 0.9rem;">{exp['duration']}</p>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 1rem 0;">
            <ul style="color: #94a3b8; margin: 0; padding-left: 20px;">
                {''.join([f'<li>{h}</li>' for h in exp['highlights']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
    
elif selected == "Education & Certs":
    st.markdown("""
    <h1 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem; line-height: 1.2; margin-bottom: 1rem;">
    Education & Certifications
    </h1>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎓 Education")
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d2ff; margin-top: 0;">Bachelor of Technology (B.Tech)</h4>
            <p><b>Computer Science & Engineering (CSE)</b></p>
            <p><b>Jawaharlal Nehru Technological University</b><br>Hyderabad</p>
            <p style="color: #64748b; margin-bottom: 0;">
                <b>Duration:</b> June 2017 - November 2020
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🏆 Certifications & Achievements")
        
        certs = [
            {
                "title": "Accelerator: Business Analytics & Data Science Program",
                "issuer": "Hero Vired",
                "link": "https://herovired.verification.givemycertificate.com/v/b9a251ff-696c-4324-be64-57232fea5053"
            },
            {
                "title": "Introduction to Data Science with Python",
                "issuer": "HarvardX (via edX)",
                "link": "https://courses.edx.org/certificates/8d34efd900dd4aaeb82ec62fd4c3aee2"
            },
            {
                "title": "Generative AI for Data, Tech & Finance",
                "issuer": "Hero Vired",
                "link": "https://verification.givemycertificate.com/v/e1e14eb7-f016-484c-a393-e58058a05226"
            }
        ]
        
        for cert in certs:
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 1rem;">
                <h4 style="color: #00d2ff; margin: 0;">{cert['title']}</h4>
                <p style="color: #94a3b8; margin: 5px 0;"><b>{cert['issuer']}</b></p>
                <a href="{cert['link']}" target="_blank" style="color: #00d2ff; text-decoration: none; font-size: 0.9rem;">📎 View Certificate →</a>
            </div>
            """, unsafe_allow_html=True)

elif selected == "About":
    about.show()
elif selected == "Resume":
    resume.show()
elif selected == "Contact":
    contact.show()
