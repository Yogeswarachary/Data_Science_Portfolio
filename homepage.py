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
                <div class="carousel-copy">
                    <div class="carousel-eyebrow">{proj['icon']} Business Impact</div>
                    <h3>{proj['title']}</h3>
                    <p>{proj['desc']}</p>
                </div>
                <div class="carousel-metric">
                    <div class="metric-kicker">Key Outcome</div>
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
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
      :root {
          --accent: #22d3ee;
          --accent-strong: #06b6d4;
          --text-main: #f8fafc;
          --text-muted: #cbd5e1;
          --text-soft: #94a3b8;
          --card-bg: linear-gradient(145deg, rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.78));
          --card-border: rgba(148, 163, 184, 0.18);
      }

      * { box-sizing: border-box; }

      html, body {
          margin: 0;
          padding: 0;
          background: transparent !important;
          color: var(--text-main);
          font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }

      body {
          overflow: hidden;
      }

      .carousel-frame {
          width: min(100%, 860px);
          margin: 0 auto;
          padding: 0 6px;
      }

      .carousel-inner {
          overflow: hidden;
          border-radius: 24px;
      }

      .carousel-slides {
          display: flex;
          transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
          width: calc(100% * {num_projects});
      }

      .carousel-slide {
          min-width: 100%;
          padding: 0;
      }

      .carousel-card {
          display: grid;
          grid-template-columns: minmax(0, 1.7fr) minmax(210px, 0.9fr);
          gap: 1.2rem;
          align-items: stretch;
          width: 100%;
          min-height: 220px;
          padding: 1.4rem;
          border-radius: 24px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          box-shadow: 0 22px 50px rgba(2, 8, 23, 0.32);
          backdrop-filter: blur(14px);
      }

      .carousel-copy {
          display: flex;
          flex-direction: column;
          justify-content: center;
          gap: 0.8rem;
          min-width: 0;
      }

      .carousel-eyebrow {
          display: inline-flex;
          align-items: center;
          gap: 0.45rem;
          width: fit-content;
          padding: 0.4rem 0.75rem;
          border-radius: 999px;
          background: rgba(34, 211, 238, 0.1);
          border: 1px solid rgba(34, 211, 238, 0.18);
          color: #a5f3fc;
          font-size: 0.78rem;
          font-weight: 700;
          letter-spacing: 0.03em;
          text-transform: uppercase;
      }

      .carousel-card h3 {
          margin: 0;
          font-size: clamp(1.45rem, 2.5vw, 2rem);
          line-height: 1.15;
          color: var(--text-main);
      }

      .carousel-card p {
          margin: 0;
          color: var(--text-muted);
          font-size: 1rem;
          line-height: 1.65;
          max-width: 54ch;
      }

      .carousel-metric {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          padding: 1.15rem;
          border-radius: 20px;
          background: linear-gradient(180deg, rgba(34, 211, 238, 0.16), rgba(15, 23, 42, 0.35));
          border: 1px solid rgba(34, 211, 238, 0.22);
          min-height: 100%;
      }

      .metric-kicker {
          color: var(--text-soft);
          font-size: 0.8rem;
          font-weight: 600;
          letter-spacing: 0.08em;
          text-transform: uppercase;
      }

      .carousel-metric .value {
          margin: 0.35rem 0;
          font-size: clamp(2.2rem, 5vw, 3rem);
          line-height: 1;
          font-weight: 800;
          color: #67e8f9;
      }

      .carousel-metric .label {
          color: #e2e8f0;
          font-size: 0.98rem;
          line-height: 1.45;
          font-weight: 600;
      }

      .carousel-controls {
          display: grid;
          grid-template-columns: auto 1fr auto;
          align-items: center;
          gap: 0.9rem;
          margin-top: 0.95rem;
      }

      .carousel-arrow {
          width: 44px;
          height: 44px;
          border-radius: 999px;
          border: 1px solid rgba(148, 163, 184, 0.22);
          background: rgba(15, 23, 42, 0.72);
          color: #67e8f9;
          font-size: 1rem;
          font-weight: 700;
          display: inline-flex;
          align-items: center;
          justify-content: center;
          transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease;
          cursor: pointer;
          user-select: none;
      }

      .carousel-arrow:hover {
          transform: translateY(-1px);
          background: rgba(8, 47, 73, 0.92);
          border-color: rgba(103, 232, 249, 0.45);
      }

      .carousel-dots {
          display: flex;
          justify-content: center;
          gap: 0.5rem;
          flex-wrap: wrap;
      }

      .carousel-dot {
          width: 10px;
          height: 10px;
          border-radius: 999px;
          background: rgba(148, 163, 184, 0.35);
          cursor: pointer;
          transition: all 0.2s ease;
      }

      .carousel-dot.active {
          width: 28px;
          background: linear-gradient(90deg, var(--accent), var(--accent-strong));
      }

      @media (max-width: 700px) {
          .carousel-card {
              grid-template-columns: 1fr;
              min-height: auto;
              padding: 1.1rem;
              gap: 0.9rem;
          }

          .carousel-metric {
              min-height: 132px;
          }

          .carousel-card p {
              font-size: 0.94rem;
              line-height: 1.55;
          }

          .carousel-controls {
              gap: 0.6rem;
          }
      }
      </style>
    </head>
    <body>
    <div class="carousel-frame">
        <div class="carousel-inner">
            <div class="carousel-slides" id="carouselSlides">
                {slides_html}
            </div>
        </div>
        <div class="carousel-controls">
            <div class="carousel-arrow" id="prevBtn" aria-label="Previous slide">&#10094;</div>
            <div class="carousel-dots" id="carouselDots">
                {dots_html}
            </div>
            <div class="carousel-arrow" id="nextBtn" aria-label="Next slide">&#10095;</div>
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