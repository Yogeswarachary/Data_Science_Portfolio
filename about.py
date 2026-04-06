import streamlit as st

def show():
    st.markdown("""
    <h1 class="gradient-text">
    About Me
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">📍 The Journey: From Compliance to Code</h3>
        <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.8;">
            My path to Data Science isn't traditional—and that's my strength. With almost <b>3 years as a Visa Consultant 
            and Process Analyst</b>, I developed obsessive attention to detail, regulatory rigor, and the ability 
            to identify anomalies under pressure. I processed 100+ visa applications with <b>zero compliance errors</b> 
            and optimized workflows that improved turnaround time by <b>50%</b>.
        </p>
        <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.8;">
            But I realized my passion wasn't in regulatory documents—it was in <b>solving problems with data</b>. 
            So I self-invested in learning Python, machine learning, and statistics. Today, I leverage my unique 
            blend of domain expertise and technical skills to build models that don't just predict—they 
            <b>add measurable business value</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("##")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">🎯 Why I Stand Out</h3>
            <ul style="color: #94a3b8; line-height: 1.8;">
                <li><b>Rare Hybrid Skill Set:</b> No burnout from previous tech roles. Fresh energy, rapid learning.</li>
                <li><b>Risk Mentality:</b> 3 years identifying anomalies in visa fraud = natural fit for ML fraud detection.</li>
                <li><b>Business Acumen:</b> Understand stakeholder needs, compliance constraints, and ROI impact.</li>
                <li><b>Production Mindset:</b> Built tools that were used daily by my colleagues—quality matters. Achieved 50% improvement in efficiency and Reduced Turn around time of Visa application processes.</li>
                <li><b>Proven Technical Skills:</b> 6 deployed Streamlit apps, research papers, ML models reaching 98% accuracy.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00d2ff; margin-top: 0;">💡 My Philosophy</h3>
            <blockquote style="color: #94a3b8; border-left: 4px solid #00d2ff; padding-left: 1rem; margin: 1rem 0; font-style: italic;">
                <p style="margin: 0; line-height: 1.8;">
                "Data Science is most powerful when applied with deep domain understanding. 
                I don't just build models—I ensure they solve real business problems and stay in production."
                </p>
            </blockquote>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 1.5rem 0;">
            <p style="color: #94a3b8;"><b>Current Focus:</b></p>
            <ul style="color: #94a3b8; padding-left: 20px;">
                <li>Fintech & fraud detection in regulated industries</li>
                <li>Supply chain optimization with real-time dashboards</li>
                <li>Statistical rigor in A/B testing and experimentation</li>
                <li>Production ML systems and MLOps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("##")
    
    # Values Section
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">🚀 Core Values</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
            <div>
                <h4 style="color: #94a3b8; margin-top: 0;">💼 Professionalism</h4>
                <p style="color: #94a3b8; margin: 0;">Deliver production-grade work. Every model is documented, tested, and deployable. No shortcuts.</p>
            </div>
            <div>
                <h4 style="color: #94a3b8; margin-top: 0;">📊 Data-Driven</h4>
                <p style="color: #94a3b8; margin: 0;">Decisions backed by evidence. Use statistical rigor to validate assumptions before implementing solutions.</p>
            </div>
            <div>
                <h4 style="color: #94a3b8; margin-top: 0;">🤝 Collaboration</h4>
                <p style="color: #94a3b8; margin: 0;">Communicate findings to non-technical stakeholders. Bridge the gap between data and business impact.</p>
            </div>
            <div>
                <h4 style="color: #94a3b8; margin-top: 0;">🎯 Impact-Focused</h4>
                <p style="color: #94a3b8; margin: 0;">Build tools that solve real problems. If it doesn't add value, it doesn't get shipped.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("##")
    
    # Fun Facts
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #00d2ff; margin-top: 0;">⚡ Quick Facts</h3>
        <p style="color: #94a3b8; margin: 0;">
            📚 Self-taught in data science | 🎓 B.Tech CSE from JNTU Hyderabad | 
            🌍 Working with international teams | 💻 Open-source contributor | 
            🎤 Learning technical writing | ☕ Coffee-fueled late-night coding sessions
        </p>
    </div>
    """, unsafe_allow_html=True)
