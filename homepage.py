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
        
        st.write("")
        skills = [
            "Python", "Pandas", "Scikit-Learn", "Machine Learning", "Hypothesis Testing", "Streamlit", "MySQL",
            "Azure", "Databricks", "Ollama", "OpenClaw", "Jan.AI", "GROQ"
        ]
        skills_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
        st.markdown(
            f"<p style='color: #94a3b8; font-size: 0.9rem;'><b>Technical Skills:</b></p>{skills_html}",
            unsafe_allow_html=True
        )

    st.write("##")

    # Business Impact Highlights
    st.markdown("""
    <h2 class="gradient-text" style="text-align: center; font-size: 2.2rem;">
    🎯 Proven Business Impact
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    projects = [
        {
            "icon": "📈",
            "title": "Visalens",
            "desc": "Intelligent visa guidance with compliance-driven extraction from official sources."
        },
        {
            "icon": "🚩",
            "title": "Fraudmap",
            "desc": "Time-aware fraud scoring and visualization for real-time transaction risk."
        },
        {
            "icon": "💳",
            "title": "JPMorgan Fraud Detection",
            "desc": "Production ML pipeline for transaction fraud classification with imbalanced data handling."
        },
        {
            "icon": "📚",
            "title": "Financial Fraud Research 2024",
            "desc": "Published analysis of emerging fraud patterns and risk signals across India FY24."
        },
        {
            "icon": "📦",
            "title": "DHL Supply Chain Analytics",
            "desc": "Inventory and route optimization with KPI monitoring for global logistics."
        },
        {
            "icon": "🧪",
            "title": "A/B Testing & Statistics",
            "desc": "Experiment design and retention analysis to drive measurable product lift."
        }
    ]

    slides_html = ""
    dots_html = ""

    for idx, proj in enumerate(projects):
        slides_html += f"""
        <div class="carousel-slide">
            <div class="carousel-card">
                <div class="carousel-content">
                    <div class="carousel-eyebrow">{proj['icon']} Business Impact</div>
                    <h3>{proj['title']}</h3>
                    <p>{proj['desc']}</p>
                </div>
            </div>
        </div>
        """
        dots_html += f'<div class="carousel-dot{" active" if idx == 0 else ""}" data-index="{idx}"></div>'

    carousel_html = textwrap.dedent("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        * {
          box-sizing: border-box;
        }

        html, body {
          margin: 0;
          padding: 0;
          width: 100%;
          background: transparent !important;
          overflow: hidden;
          font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        body {
          display: block;
        }

        .carousel-frame {
          width: 100%;
          margin: 0 auto;
          padding: 0;
          background: transparent;
        }

        .carousel-viewport {
          position: relative;
          width: 100%;
          overflow: hidden;
          border-radius: 28px;
          background: transparent;
        }

        .carousel-slides {
          display: flex;
          width: calc(100% * {num_projects});
          transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
        }

        .carousel-slide {
          min-width: 100%;
          padding: 0;
        }

        .carousel-card {
          position: relative;
          width: 100%;
          min-height: 250px;
          padding: 1.6rem 1.8rem 4.4rem 1.8rem;
          border-radius: 28px;
          background: linear-gradient(135deg, rgba(29, 38, 64, 0.98), rgba(38, 49, 78, 0.98));
          border: 1px solid rgba(255, 255, 255, 0.08);
          box-shadow: 0 18px 40px rgba(0, 0, 0, 0.22);
          overflow: hidden;
        }

        .carousel-card::before {
          content: "";
          position: absolute;
          inset: 0;
          background: radial-gradient(circle at top right, rgba(34, 211, 238, 0.08), transparent 35%);
          pointer-events: none;
        }

        .carousel-content {
          position: relative;
          z-index: 2;
          max-width: 78%;
        }

        .carousel-eyebrow {
          display: inline-flex;
          align-items: center;
          gap: 0.45rem;
          padding: 0.45rem 0.95rem;
          border-radius: 999px;
          background: rgba(34, 211, 238, 0.12);
          border: 1px solid rgba(34, 211, 238, 0.18);
          color: #b6f4ff;
          font-size: 0.82rem;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 0.03em;
          margin-bottom: 1.1rem;
        }

        .carousel-card h3 {
          margin: 0 0 0.9rem 0;
          font-size: clamp(1.8rem, 3vw, 2.35rem);
          line-height: 1.15;
          color: #f8fafc;
          font-weight: 700;
        }

        .carousel-card p {
          margin: 0;
          color: #d1d5db;
          font-size: 1rem;
          line-height: 1.75;
          max-width: 680px;
        }

        .carousel-arrow {
          position: absolute;
          bottom: 18px;
          width: 38px;
          height: 38px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          background: rgba(51, 65, 85, 0.88);
          border: 1px solid rgba(255, 255, 255, 0.10);
          color: #4de3ff;
          font-size: 1.2rem;
          font-weight: 700;
          cursor: pointer;
          z-index: 3;
          user-select: none;
          transition: all 0.2s ease;
        }

        .carousel-arrow:hover {
          background: rgba(51, 65, 85, 1);
          transform: scale(1.05);
        }

        .carousel-arrow.left {
          left: 16px;
        }

        .carousel-arrow.right {
          right: 16px;
        }

        .carousel-dots {
          position: absolute;
          bottom: 31px;
          left: 50%;
          transform: translateX(-50%);
          display: flex;
          align-items: center;
          gap: 0.5rem;
          z-index: 3;
        }

        .carousel-dot {
          width: 10px;
          height: 10px;
          border-radius: 999px;
          background: rgba(203, 213, 225, 0.42);
          transition: all 0.25s ease;
          cursor: pointer;
        }

        .carousel-dot.active {
          width: 30px;
          background: linear-gradient(90deg, #22d3ee, #06b6d4);
        }

        @media (max-width: 768px) {
          .carousel-card {
            min-height: 235px;
            padding: 1.2rem 1.1rem 4rem 1.1rem;
          }

          .carousel-content {
            max-width: 100%;
          }

          .carousel-card h3 {
            font-size: 1.45rem;
          }

          .carousel-card p {
            font-size: 0.92rem;
            line-height: 1.6;
          }

          .carousel-arrow {
            width: 34px;
            height: 34px;
            bottom: 16px;
            font-size: 1rem;
          }

          .carousel-dots {
            bottom: 28px;
          }
        }
      </style>
    </head>
    <body>
      <div class="carousel-frame">
        <div class="carousel-viewport">
          <div class="carousel-slides" id="carouselSlides">
            {slides_html}
          </div>

          <div class="carousel-arrow left" id="prevBtn">&#10094;</div>
          <div class="carousel-dots" id="carouselDots">
            {dots_html}
          </div>
          <div class="carousel-arrow right" id="nextBtn">&#10095;</div>
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

        updateCarousel();
        restartTimer();
      </script>
    </body>
    </html>
    """).replace("{slides_html}", slides_html).replace("{dots_html}", dots_html).replace("{num_projects}", str(len(projects)))

    components.html(carousel_html, height=255, scrolling=False)

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