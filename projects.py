import streamlit as st

def show():
    st.markdown("""
    <h1 class="gradient-text">
    Project Portfolio
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1rem; color: #94a3b8; margin-bottom: 2rem;">
    5 production-ready projects featuring fraud detection, supply chain analytics, hypothesis testing, ML trading, and AI automation.
    Includes an independent research publication in financial fraud. Each project is deployed with live demos.
    </p>
    """, unsafe_allow_html=True)
    st.write("##")

    # Project Data - 5 Live Projects + Research
    projects = [
        {
            "title": "📈 VisaLens - AI Powered smart visa assistant",
            "desc": "AI-Powered Visa Application Assistant which can provide accurate information from the offical government sources for the different kinds of visa types.",
            "tech": ["TypeScript", "Next.js", "Groq-Compound"],
            "github": "https://github.com/Yogeswarachary/visalens",
            "app": "https://visalens-dq5bjy4sw-yogeswaracharys-projects.vercel.app/",
            "highlight": "90% Accurate Information about visa types and document requirements"
        },
        {
            "title": "🚩 FraudMap - Real-Time Fraud Risk Mapping",
            "desc": "Based on the time of transaction, this project provides a real-time fraud risk score mapping to identify high-risk areas and time periods for financial transactions.",
            "tech": ["TypeScript", "Next.js"],
            "github": "https://github.com/Yogeswarachary/fraudmap",
            "app": "https://fraudmap-jrks-g5gfe95qp-yogeswaracharys-projects.vercel.app/",
            "highlight": "Real-Time Fraud Risk Score Mapping"
        },
        {
            "title": "🏦 JPMorgan Fraud Detection",
            "desc": "End-to-end ML pipeline for financial fraud detection with imbalanced dataset handling. Capstone project with high accuracy and production deployment.",
            "tech": ["Python", "Scikit-Learn", "XGBoost", "Imbalanced Learning", "SQL"],
            "github": "https://github.com/Yogeswarachary/JPMorgan_Fraud_Detection_Project",
            "deployment": "https://github.com/Yogeswarachary/JP_Morgan_and_Chase_Fraud_Detection_Deployment",
            "app": "https://jpmorganandchasefrauddetectiondeployment-dfv8woyv2k4ssr3hqeisl.streamlit.app/",
            "highlight": "98% Accuracy"
        },
        {
            "title": "📊 Financial Fraud India 2024 Research",
            "desc": "Independent research paper analyzing financial fraud trends in India for FY 2024-2025 with statistical rigor and data-driven insights.",
            "tech": ["Statistical Analysis", "Data Science", "Research", "Pandas", "Visualization"],
            "github": "https://github.com/Yogeswarachary/Financial-Fraud-India-2024-Research",
            "paper": "https://yogeswarachary.github.io/Financial-Fraud-India-2024-Research/Financial_Fraud_India_FY_2024_2025.pdf",
            "highlight": "Published Research"
        },
        {
            "title": "🧪 Cookie Cats Game A/B Testing",
            "desc": "Rigorous hypothesis testing to analyze player retention and game level optimization. Applied statistical methods to drive business decisions.",
            "tech": ["SciPy", "Statistics", "Hypothesis Testing", "Python", "Data Analysis"],
            "github": "https://github.com/Yogeswarachary/Cookie_Cats_Game_Hypothesis_Testing",
            "app": "https://cookiecatsgamehypothesistesting-kiljbluetyfzljxv9vawq4.streamlit.app/",
            "highlight": "95% Confidence"
        },
        {
            "title": "📦 DHL Inventory Optimization",
            "desc": "Real-time KPI dashboards for supply chain monitoring and inventory optimization for global logistics operations.",
            "tech": ["Pandas", "Streamlit", "Plotly", "Dashboard Design", "Real-time Analytics"],
            "github": "https://github.com/Yogeswarachary/DHL_Inventory_Project",
            "app": "https://yogeswarachary-dhl-inventory-project-deployementapp-hko4qy.streamlit.app/",
            "highlight": "25% Efficiency Gain"
        },
        {
            "title": "💹 ML Trading Project",
            "desc": "Regression models and feature engineering for trading signal prediction with advanced ML techniques and market analysis.",
            "tech": ["Machine Learning", "Regression", "Feature Engineering", "Visualization", "Python"],
            "github": "https://github.com/Yogeswarachary/ML_Trading_Project",
            "app": "https://mltradingproject-igu369irozxgbdsxzn77ht.streamlit.app/",
            "highlight": "Predictive Models"
        },
        {
            "title": "🤖 AutoDoc - GitHub README Generator",
            "desc": "AI-powered tool for automatic GitHub README file generation. Streamlines documentation creation for data science projects.",
            "tech": ["Streamlit", "Python", "NLP", "Automation", "GitHub API"],
            "github": "https://github.com/Yogeswarachary/AutoDoc",
            "app": "https://autodoc-ek9qbgugv6jfuihzfdjplk.streamlit.app/",
            "highlight": "AI Automation"
        }
    ]

    # Grid Layout - 2 per row for better readability
    cols = st.columns(2)
    for i, p in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 1rem; height: 100%;">
                <h3 style="margin-top: 0; color: #00d2ff;">{p['title']}</h3>
                <p style="color: #94a3b8; margin: 1rem 0;">{p['desc']}</p>
                <div style="margin-bottom: 1rem;">
                    {" ".join([f'<span class="skill-badge">{t}</span>' for t in p['tech']])}
                </div>
                <div style="background: rgba(0, 210, 255, 0.1); padding: 0.75rem; border-radius: 8px; margin-bottom: 1rem;">
                    <span style="color: #00d2ff; font-weight: bold;">✨ {p.get('highlight', 'Feature')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action Buttons
            btn_cols = st.columns([1, 1, 1])
            with btn_cols[0]:
                st.link_button("💻 GitHub", p['github'], use_container_width=True)
            
            if "app" in p and p["app"]:
                with btn_cols[1]:
                    st.link_button("🚀 Live Demo", p["app"], type="primary", use_container_width=True)
            
            if "paper" in p and p["paper"]:
                with btn_cols[2]:
                    st.link_button("📄 Paper", p["paper"], use_container_width=True)
            elif "deployment" in p and p["deployment"]:
                with btn_cols[2]:
                    st.link_button("🔧 Deploy", p["deployment"], use_container_width=True)

            st.write("")

    st.write("##")
    st.divider()
    st.write("##")
    
    # Key Metrics
    st.markdown('<h3 style="text-align: center; color: #94a3b8;">📈 Project Statistics</h3>', unsafe_allow_html=True)
    
    metric_cols = st.columns(3)
    metrics = [
        ("5", "Live Projects", "All deployed to production"),
        ("98%", "Best Accuracy", "JPMorgan fraud model"),
        ("1", "Independent Research Publication", "Research papers & case studies")
    ]
    
    for col, (value, label, detail) in zip(metric_cols, metrics):
        with col:
            st.markdown(f"""
            <div class="glass-card" style="text-align: center; padding: 1.5rem 1rem;">
                <div style="font-size: 1.8rem; font-weight: bold; color: #00d2ff;">{value}</div>
                <div style="color: #94a3b8; font-size: 0.95rem; font-weight: 500;">{label}</div>
                <div style="color: #64748b; font-size: 0.85rem; margin-top: 0.5rem;">{detail}</div>
            </div>
            """, unsafe_allow_html=True)
