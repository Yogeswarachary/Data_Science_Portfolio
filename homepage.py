import streamlit as st
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

def show():
    # Hero Section
    col1, col2 = st.columns([1.2, 2.8])
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <div style="
                width: 200px;
                height: 200px;
                margin: 0 auto;
                border-radius: 50%;
                background: linear-gradient(135deg, #00d2ff, #3a7bd5);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 100px;
                color: white;
            ">👨‍💻</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="glass-card">
            <h1 class="gradient-text" style="color: #94a3b8;font-size: 2.5rem; margin: 0;">Yogeswarachary Modepalli</h1>
            <h2 style="margin-top: 0.5rem; color: #00d2ff; font-weight: 400;">Data Scientist | Analytics Engineer | ML Specialist</h2>
            <p style="font-size: 1rem; color: #94a3b8; line-height: 1.6;">
            📊 <b>Career Pivot Success Story</b><br>
            ✅ From <b>3 Years in Regulatory Compliance & Visa Consultancy</b><br>
            ✅ To <b>Data-Driven Problem Solving in Fintech, Supply Chain & AI</b><br><br>
            🚀 Built production-grade ML pipelines for fraud detection, inventory optimization, and A/B testing analysis with proven business impact.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Skill Badges
        st.write("")
        skills = [
            "Python", "Pandas", "Scikit-Learn", "Machine Learning", "Hypothesis Testing", "Streamlit", "MySQL",
            "Azure", "Databricks", "Ollama", "OpenClaw", "Jan.AI", "GROQ"
        ]
        skills_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
        st.markdown(f"<p style='color: #94a3b8; font-size: 0.9rem;'><b>Technical Skills:</b></p>{skills_html}", unsafe_allow_html=True)

    st.write("##")

    # Business Impact Highlights - THE RECRUITER HOOK
    st.markdown("""
    <h2 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #f8fafc !important; text-align: center;">
    🎯 Proven Business Impact
    </h2>
    """, unsafe_allow_html=True)
    st.write("")
    
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="glass-card" style="height: 280px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h3 style="color: #00d2ff; margin-top: 0;">💳 JPMorgan Fraud Detection</h3>
                <p style="color: #94a3b8; margin: 1rem 0;">End-to-end ML pipeline for financial risk detection with imbalanced dataset handling.</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">
                <div style="color: #00d2ff; font-size: 1.5rem; font-weight: bold;">98%</div>
                <div style="color: #94a3b8; font-size: 0.9rem;">Accuracy</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cols[1]:
        st.markdown("""
        <div class="glass-card" style="height: 280px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h3 style="color: #00d2ff; margin-top: 0;">📦 DHL Supply Chain Analytics</h3>
                <p style="color: #94a3b8; margin: 1rem 0;">Real-time KPI dashboards & inventory optimization for global logistics operations.</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">
                <div style="color: #00d2ff; font-size: 1.5rem; font-weight: bold;">25%</div>
                <div style="color: #94a3b8; font-size: 0.9rem;">Efficiency Gain</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cols[2]:
        st.markdown("""
        <div class="glass-card" style="height: 280px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h3 style="color: #00d2ff; margin-top: 0;">🧪 A/B Testing & Statistics</h3>
                <p style="color: #94a3b8; margin: 1rem 0;">Rigorous hypothesis testing for Cookie Cats game user retention optimization.</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.1); padding: 1rem; border-radius: 10px; text-align: center;">
                <div style="color: #00d2ff; font-size: 1.5rem; font-weight: bold;">95%</div>
                <div style="color: #94a3b8; font-size: 0.9rem;">Confidence</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("##")

    # The Transition Narrative - CRITICAL FOR CAREER-SHIFTERS
    st.markdown("""
    <h2 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #f8fafc !important; text-align: center;">
    🚀 Why I'm Ready for Enterprise Roles
    </h2>
    """, unsafe_allow_html=True)
    st.write("")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">🎯 Domain Expertise (3 Years)</h3>
        <ul style="color: #94a3b8;">
            <li><b>Fraud & Risk Detection:</b> Identified anomalies in visa applications with zero-error tolerance.</li>
            <li><b>Regulatory Compliance:</b> Ensured 100% adherence to immigration laws across multiple jurisdictions.</li>
            <li><b>Stakeholder Management:</b> Coordinated with 100+ clients, maintaining professional documentation.</li>
            <li><b>Process Optimization:</b> Designed systems reducing turnaround time by 50%.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
        <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">💡 Technical Excellence</h3>
        <ul style="color: #94a3b8;">
            <li><b>Precision Programming:</b> Production-grade Python, SQL, and ML pipelines.</li>
            <li><b>Risk Models:</b> Good Understanding of Machine Learning in fraud detection and predictive analytics.</li>
            <li><b>Data Engineering:</b> ETL/ELT, Databricks, Azure fundamentals.</li>
            <li><b>Communication:</b> Executive dashboards & findings to non-technical stakeholders.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("##")
    st.divider()
    st.write("##")
    
    # Quick Stats for HR
    st.markdown('<h3 style="text-align: center; color: #94a3b8;">📈 Quick Facts</h3>', unsafe_allow_html=True)
    
    stat_cols = st.columns(5)
    stats = [
        ("5", "Live Projects"),
        ("3", "Years Experience"),
        ("98%", "Avg Accuracy"),
        ("3", "Certifications"),
        ("1", "Independent Research")
    ]
    
    for i, (stat, label) in enumerate(stats):
        with stat_cols[i]:
            st.markdown(f"""
            <div class="glass-card" style="text-align: center;">
                <div style="font-size: 2rem; font-weight: bold; color: #00d2ff;">{stat}</div>
                <div style="color: #94a3b8; font-size: 0.95rem;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("##")
    st.write("##")
    
    # Call to Action
    st.markdown("""
    <div class="glass-card" style="background: rgba(0, 210, 255, 0.05); border: 2px solid #00d2ff; text-align: center;">
        <h3 style="color: #00d2ff; margin-top: 0;">🤝 Let&apos;s Connect</h3>
        <p style="color: #94a3b8; margin: 1rem 0;">
            <b>Open to Data Science, Big DataAnalytics, AI Engineering, Machine Learning Engineering, and Data Engineering roles</b> at forward-thinking organizations. 
            Eager to contribute to impact-driven projects that combine data science with business value.
        </p>
        <div style="margin-top: 1.5rem;">
            <p style="color: #94a3b8; margin: 0.5rem 0;">
                📧 <a href="mailto:myogeswarachary@gmail.com" style="color: #00d2ff; text-decoration: none;"><b>myogeswarachary@gmail.com</b></a><br>
                🔗 <a href="https://www.linkedin.com/in/yogeswarachary-modepalli-4a91571b8/" target="_blank" style="color: #00d2ff; text-decoration: none;"><b>LinkedIn</b></a> | 
                💻 <a href="https://github.com/Yogeswarachary" target="_blank" style="color: #00d2ff; text-decoration: none;"><b>GitHub</b></a> | 
                📱 <a href="https://wa.me/919676106803" target="_blank" style="color: #00d2ff; text-decoration: none;"><b>+91 9676106803</b></a>
            </p>
        </div>
        <div style="margin-top: 1.5rem;">
            <p style="color: #94a3b8; margin: 0.5rem 0; font-size: 0.9rem;">
                📄 <b>Download my resume:</b>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Resume Download Button on Homepage
    with open("ymodepalli-RESUME.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="📥 Download Resume PDF",
            data=pdf_bytes,
            file_name="Yogeswarachary_Modepalli_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
