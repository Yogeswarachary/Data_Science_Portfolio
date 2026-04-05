import streamlit as st
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

def show():
    st.markdown("""
    <h1 style="background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #f8fafc !important; font-size: 3.5rem; line-height: 1.2; margin-bottom: 1rem;">
    Technical Skills & Resume
    </h1>
    """, unsafe_allow_html=True)
    
    # Resume Download Section - PROMINENT PLACEMENT
    st.markdown("""
    <div class="glass-card" style="background: rgba(0, 210, 255, 0.05); border: 2px solid #00d2ff; text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #00d2ff; margin-top: 0;">📄 Download My Resume</h2>
        <p style="color: #94a3b8; margin: 1rem 0;">
            Get the complete version with detailed experience, projects, and certifications
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Download Button
    col_download = st.columns([1, 2, 1])
    with col_download[1]:
        resume_path = ROOT_DIR / "ymodepalli-RESUME.pdf"
        with open(resume_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(
                label="📥 Download Resume PDF",
                data=pdf_bytes,
                file_name="Yogeswarachary_Modepalli_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary"
            )
    
    st.write("##")
    
    col1, col2 = st.columns([2.5, 1.5])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">Professional Profile</h3>
            <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.8;">
                <b>Data Scientist & Engineer</b> with a unique background in regulatory compliance and 
                fraud detection. Proven track record of building production-ready data pipelines and ML 
                models that solve real-world financial and operational challenges.
            </p>
            <p style="color: #94a3b8;">
                <b>Career Path:</b> 3 years visa consultancy → Self-taught data science →
                5 deployed ML projects → 1 research publication
            </p>
            <p style="color: #94a3b8;">
                <b>Targeting Roles:</b> 1-3 Years Experience - Data Scientist, ML Engineer, AI Engineer, Data Engineer, and Analytics Engineer
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("##")
        
        # Technical Skills - Organized by Category
        st.markdown('<h3 style="color: #00d2ff;">🛠️ Technical Arsenal</h3>', unsafe_allow_html=True)
        
        skill_columns = st.columns(2)
        
        with skill_columns[0]:
            st.markdown("""
            <div class="glass-card">
                <h4 style="color: #00d2ff; margin-top: 0;">Programming & Data</h4>
                <ul style="color: #94a3b8; line-height: 1.8;">
                    <li><b>Languages:</b> Python (Advanced), SQL (Advanced)</li>
                    <li><b>Libraries:</b> Pandas, NumPy, SciPy, Scikit-Learn</li>
                    <li><b>ML:</b> XGBoost, Random Forest, CatBoost, LightGBM</li>
                    <li><b>Statistical Methods:</b> Hypothesis Testing, A/B Testing, Regression, and Classification</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with skill_columns[1]:
            st.markdown("""
            <div class="glass-card">
                <h4 style="color: #00d2ff; margin-top: 0;">Data Engineering & Cloud</h4>
                <ul style="color: #94a3b8; line-height: 1.8;">
                    <li><b>Platforms:</b> Azure, Databricks, Streamlit</li>
                    <li><b>ETL/ELT:</b> Data pipelines, workflow orchestration</li>
                    <li><b>Visualization:</b> Matplotlib, Seaborn</li>
                    <li><b>DevOps Basics:</b> Docker, GitHub</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.write("##")
        
        # Competencies
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">Core Competencies</h3>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                <span class="skill-badge">Fraud Detection</span>
                <span class="skill-badge">ML Pipeline Design</span>
                <span class="skill-badge">Data Engineering</span>
                <span class="skill-badge">Business Analytics</span>
                <span class="skill-badge">Azure Services</span>
                <span class="skill-badge">Risk Assessment</span>
                <span class="skill-badge">Stakeholder Communication</span>
                <span class="skill-badge">Production Systems</span>
                <span class="skill-badge">Regulatory Compliance</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h3 style="color: #00d2ff; margin-top: 0;">Resume & Downloads</h3>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p style="color: #94a3b8; margin: 1rem 0;">
                <span style="font-size: 2rem;">📄</span><br>
                <b>Full Resume</b>, CV, and project documentation available.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d2ff; margin-top: 0;">📊 Key Numbers</h4>
            <ul style="color: #94a3b8; line-height: 1.9;">
                <li><b>5</b> live projects deployed</li>
                <li><b>98%</b> top model accuracy</li>
                <li><b>Achieved</b> near Zero False Negatives</li>
                <li><b>3</b> years domain experience</li>
                <li><b>3</b> certifications</li>
                <li><b>Advanced</b> SQL skills</li>
                <li><b>Published</b> 1 research paper</li>
                <li><b>0</b> production incidents</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("##")
    st.divider()
    st.write("##")
    
    # Advanced Skills
    st.markdown('<h3 style="text-align: center; color: #94a3b8;">🎓 Advanced Skills & Specializations</h3>', unsafe_allow_html=True)
    st.write("")
    
    advanced_cols = st.columns(3)
    
    with advanced_cols[0]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d2ff; margin: 0;">Fraud & Risk Detection</h4>
            <ul style="color: #94a3b8; font-size: 0.95rem; padding-left: 20px; margin: 1rem 0;">
                <li>Anomaly detection steps</li>
                <li>Imbalanced learning techniques</li>
                <li>Feature engineering</li>
                <li>SMOTE, class weighting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with advanced_cols[1]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d2ff; margin: 0;">Statistical & A/B Testing</h4>
            <ul style="color: #94a3b8; font-size: 0.95rem; padding-left: 20px; margin: 1rem 0;">
                <li>Hypothesis testing (t-tests, Chi-square)</li>
                <li>A/B testing design & analysis</li>
                <li>Power analysis, effect sizes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with advanced_cols[2]:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d2ff; margin: 0;">Production & Deployment</h4>
            <ul style="color: #94a3b8; font-size: 0.95rem; padding-left: 20px; margin: 1rem 0;">
                <li>Streamlit app development</li>
                <li>Azure & Databricks deployment</li>
                <li>ML Model monitoring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("##")
    
    # Certifications Section
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">🏆 Professional Certifications</h3>
        <p style="color: #94a3b8; margin-bottom: 1rem;">Continuous learning from industry-leading platforms:</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div style="background: rgba(0, 210, 255, 0.05); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0;"><b>HeroVired</b></p>
                <p style="color: #64748b; margin: 0.5rem 0; font-size: 0.95rem;">Accelerator: Business Analytics & Data Science</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.05); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0;"><b>HarvardX</b></p>
                <p style="color: #64748b; margin: 0.5rem 0; font-size: 0.95rem;">Introduction to Data Science with Python</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.05); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0;"><b>Hero Vired</b></p>
                <p style="color: #64748b; margin: 0.5rem 0; font-size: 0.95rem;">Generative AI for Data, Tech & Finance</p>
            </div>
            <div style="background: rgba(0, 210, 255, 0.05); padding: 1rem; border-radius: 8px; border-left: 4px solid #00d2ff;">
                <p style="color: #94a3b8; margin: 0;"><b>JNTU</b></p>
                <p style="color: #64748b; margin: 0.5rem 0; font-size: 0.95rem;">B.Tech Computer Science & Engineering</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Resume Download Button
    resume_path = ROOT_DIR / "ymodepalli-RESUME.pdf"
    with open(resume_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="📥 Download Resume PDF",
            data=pdf_bytes,
            file_name="Yogeswarachary_Modepalli_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    st.write("##")
