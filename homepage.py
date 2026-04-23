import streamlit as st
import streamlit.components.v1 as components
import textwrap
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
        st.markdown("""
        <div class="glass-card">
            <h1 class="gradient-text" style="font-size: 2.5rem; margin: 0;">Yogeswarachary Modepalli</h1>
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
    <h2 class="gradient-text" style="text-align: center; font-size: 2.2rem;">
    🎯 Proven Business Impact
    </h2>
    """, unsafe_allow_html=True)
    st.write("")
    
    # Define projects
    projects = [
        {
            "icon": "📈",
            "title": "Visalens",
            "desc": "Intelligent visa guidance with compliance-driven extraction from official sources.",
            "metric": "95%",
            "label": "Application Accuracy"
        },
        {
            "icon": "🚩",
            "title": "Fraudmap",
            "desc": "Time-aware fraud scoring and visualization for real-time transaction risk.",
            "metric": "98%",
            "label": "Risk Precision"
        },
        {
            "icon": "💳",
            "title": "JPMorgan Fraud Detection",
            "desc": "Production ML pipeline for transaction fraud classification with imbalanced data handling.",
            "metric": "97%",
            "label": "Detection Precision"
        },
        {
            "icon": "📚",
            "title": "Financial Fraud Research 2024",
            "desc": "Published analysis of emerging fraud patterns and risk signals across India FY24.",
            "metric": "1 Paper",
            "label": "Published Insight"
        },
        {
            "icon": "📦",
            "title": "DHL Supply Chain Analytics",
            "desc": "Inventory and route optimization with KPI monitoring for global logistics.",
            "metric": "25%",
            "label": "Efficiency Gain"
        },
        {
            "icon": "🧪",
            "title": "A/B Testing & Statistics",
            "desc": "Experiment design and retention analysis to drive measurable product lift.",
            "metric": "95%",
            "label": "Confidence Level"
        }
    ]

    slides_html = ""
    dots_html = ""
    for idx, proj in enumerate(projects):
        slides_html += f"""
        <div class="carousel-slide">
            <div class="carousel-card">
                <h3>{proj['icon']} {proj['title']}</h3>
                <p>{proj['desc']}</p>
                <div class="carousel-metric">
                    <div class="value">{proj['metric']}</div>
                    <div class="label">{proj['label']}</div>
                </div>
            </div>
        </div>
        """
        dots_html += f"""
        <div class=\"carousel-dot{' active' if idx == 0 else ''}\" data-index=\"{idx}\"></div>
        """

    carousel_html = textwrap.dedent("""
    <style>
    .carousel-frame {
        width: 60%;
        max-width: 800px;
        margin: 0 auto;
        padding: 0;
    }
    .carousel-inner {
        overflow: hidden;
        border-radius: 20px;
    }
    .carousel-slides {
        display: flex;
        transition: transform 0.6s ease;
        width: calc(100% * {num_projects});
    }
    .carousel-slide {
        min-width: 100%;
        box-sizing: border-box;
        padding: 0;
    }
    .carousel-card {
        width: 100%;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.18);
        backdrop-filter: blur(18px);
        min-height: auto;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .carousel-card h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.6rem;
        color: #00d2ff;
        max-width: 70%;
    }
    .carousel-card p {
        margin: 0 0 1rem 0;
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.5rem;
        max-width: 70%;
    }
    .carousel-metric {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0, 210, 255, 0.08);
        border-radius: 16px;
        padding: 0.75rem 1rem;
        max-width: 70%;
    }
    .carousel-metric .value {
        font-size: 1.75rem;
        font-weight: 700;
        color: #54e5ff;
    }
    .carousel-metric .label {
        color: #94a3b8;
        font-size: 0.85rem;
    }
    .carousel-controls {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 0.75rem;
        gap: 0.75rem;
    }
    .carousel-arrow {
        width: 55px;
        height: 55px;
        border-radius: 50%;
        border: 1px solid rgba(255, 255, 255, 0.18);
        background: rgba(255, 255, 255, 0.05);
        color: #38bdf8;
        font-size: 1.5rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.2s ease, background 0.2s ease;
        cursor: pointer;
    }
    .carousel-arrow:hover {
        transform: scale(1.05);
        background: rgba(0, 210, 255, 0.12);
    }
    .carousel-dots {
        display: flex;
        justify-content: center;
        gap: 0.4rem;
        flex-wrap: wrap;
        margin-top: 0.4rem;
    }
    .carousel-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.18);
        cursor: pointer;
        transition: background 0.2s ease, transform 0.2s ease;
    }
    .carousel-dot.active {
        background: #38bdf8;
        transform: scale(1.2);
    }
    </style>

    <div class="carousel-frame">
        <div class="carousel-inner">
            <div class="carousel-slides" id="carouselSlides">
                {slides_html}
            </div>
        </div>
        <div class="carousel-controls">
            <div class="carousel-arrow" id="prevBtn">◀</div>
            <div class="carousel-dots" id="carouselDots">
                {dots_html}
            </div>
            <div class="carousel-arrow" id="nextBtn">▶</div>
        </div>
    </div>

    <script>
    const slides = document.querySelectorAll('.carousel-slide');
    const slideCount = slides.length;
    const slidesContainer = document.getElementById('carouselSlides');
    const dots = document.querySelectorAll('.carousel-dot');
    const intervalTime = 5000;
    let currentIndex = 0;
    let timer = null;

    function updateCarousel() {
        slidesContainer.style.transform = 'translateX(-' + (currentIndex * 100) + '%)';
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateCarousel();
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        updateCarousel();
    }

    function restartTimer() {
        if (timer) clearInterval(timer);
        timer = setInterval(nextSlide, intervalTime);
    }

    document.getElementById('nextBtn').addEventListener('click', () => {
        nextSlide();
        restartTimer();
    });
    document.getElementById('prevBtn').addEventListener('click', () => {
        prevSlide();
        restartTimer();
    });
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentIndex = index;
            updateCarousel();
            restartTimer();
        });
    });

    restartTimer();
    </script>
    """).replace("{slides_html}", slides_html).replace("{dots_html}", dots_html).replace("{num_projects}", str(len(projects)))

    components.html(carousel_html, height=340)

    st.write("##")

    # The Transition Narrative - CRITICAL FOR CAREER-SHIFTERS
    st.markdown("""
    <h2 class="gradient-text" style="text-align: center; font-size: 2.2rem;">
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
        ("7", "Live Projects"),
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
