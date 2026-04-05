import streamlit as st

def show():
    st.markdown("""
    <h1 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem; line-height: 1.2; margin-bottom: 1rem;">
    Get In Touch
    </h1>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">🤝 Let's Build Something Impactful</h3>
            <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.8;">
                I'm actively seeking roles in <b>Data Science, AI Engineer, Data Engineering, and Analytics</b> 
                where I can apply my unique blend of domain expertise and technical skills.
            </p>
            <p style="color: #94a3b8;">
                Whether you have a specific opportunity, want to discuss my experience, or just want to connect—
                <b>let's talk!</b> I'm available for interviews and project collaborations.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("##")
        
        # Direct Gmail Link
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">✉️ Email Me Directly</h3>
            <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.8;">
                Use the button below to open Gmail or your default email client and send me a direct message.
            </p>
            <a href="mailto:myogeswarachary@gmail.com?subject=Hello%20Yogeswarachary&body=Hi%20Yogeswarachary%2C%0A%0AI%20would%20like%20to%20connect%20about%20a%20role%20or%20project.%0A%0A" 
               style="display: inline-block; margin-top: 1rem; padding: 0.95rem 1.4rem; background: #00d2ff; color: #0f172a; border-radius: 999px; text-decoration: none; font-weight: 700;">
                📧 Email via Gmail
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.write("##")
        
        # Resume Download Section
        st.markdown("""
        <div class="glass-card" style="background: rgba(0, 210, 255, 0.05); border: 2px solid #00d2ff; text-align: center;">
            <h3 style="color: #00d2ff; margin-top: 0;">📄 Download Resume</h3>
            <p style="color: #94a3b8; margin: 1rem 0;">
                Get my complete resume with detailed experience, projects, and certifications
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with open("ymodepalli-RESUME.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(
                label="📥 Download Full Resume PDF",
                data=pdf_bytes,
                file_name="Yogeswarachary_Modepalli_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary"
            )

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">📬 Direct Contact</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            """
            **📧 Email**  
            [myogeswarachary@gmail.com](mailto:myogeswarachary@gmail.com)  

            **📱 WhatsApp / Mobile**  
            [ +91 9676 106 803 ](https://wa.me/919676106803)  

            **📍 Location**  
            Hyderabad, India (Open to Remote)
            """
        )

    st.write("##")
    st.divider()
    st.write("##")
    
    # Response Time & Availability
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">⚡ Availability & Response Times</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0; font-weight: bold;">Email</p>
                <p style="color: #00d2ff; margin: 0.5rem 0; font-size: 0.95rem;">24 hourss</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0; font-weight: bold;">WhatsApp</p>
                <p style="color: #00d2ff; margin: 0.5rem 0; font-size: 0.95rem;">2-4 hours</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0; font-weight: bold;">LinkedIn</p>
                <p style="color: #00d2ff; margin: 0.5rem 0; font-size: 0.95rem;">24 hours</p>
            </div>
        </div>
        <p style="color: #94a3b8; margin-top: 1.5rem; margin-bottom: 0;">
            <b>👔 Actively looking for Data Science & Analytics roles</b> | <b>⏰ Available for interviews on weekdays & weekends</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
