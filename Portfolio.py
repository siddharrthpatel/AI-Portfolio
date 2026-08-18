import streamlit as st
import requests
from streamlit_lottie import st_lottie
from urllib.parse import quote
import time
import os
from google import genai

st.set_page_config(page_title="Siddharth Patel AI Portfolio", layout="wide")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

SYSTEM_PROMPT = """
You are an AI assistant for Siddharth Patel's portfolio website. Your primary role is to answer questions about Siddharth Patel, his skills, projects, experience, education, certifications, and background.
Always answer in a professional, friendly, and concise manner. Base your answers STRICTLY on the following details. Do NOT make up or assume any information not present here.

---

**About / Professional Summary**:
I'm Siddharth Patel, a passionate Full Stack Developer focused on building fast, responsive, and user-friendly web applications. I specialize in JavaScript, Node.js, Angular, Python, and MySQL, with hands-on experience gained through internships at HCL GUVI and Coding Cafe.

Over the past year, I've built real-world projects, including portfolio websites, management systems, dashboards, and API-driven web applications. I enjoy solving real-world problems, optimizing application performance, and writing clean, maintainable code while following modern development practices and Agile methodologies.

I'm passionate about learning new technologies and continuously improving my skills to build scalable, high-quality software. Currently pursuing my Master of Computer Applications (MCA), I'm actively seeking opportunities as a Full Stack Developer, Software Developer, or Web Developer, where I can contribute to impactful projects, collaborate with talented teams, and grow as a software engineer.

---

**Technical Skills**:
- Programming Languages: JavaScript, Python, HTML5, CSS3, PHP, Java
- Frontend Technologies: Angular, HTML5, CSS3, JavaScript, Responsive Web Design, UI/UX Design
- Backend Technologies: Spring Boot, RESTful API Development, ASP.NET MVC, Node.js, Express.js
- Databases: MySQL, Database Design and Management
- Development Tools: Git, GitHub, VS Code, XAMPP
- Frameworks & Libraries: Streamlit, Pandas, ASP.NET MVC, Bootstrap
- Other Tools: Payment Gateway Integration (Razorpay, Stripe)
- Methodologies: Agile Development, Software Development Life Cycle (SDLC), Object-Oriented Programming (OOP), Test-Driven Development, Unit Testing

---

**Education**:
1. Master of Computer Applications (MCA) — School of Management Sciences (SMS), Varanasi | 2025 – Present (Currently Pursuing)
2. Bachelor of Computer Applications (BCA) — Microtek College of Management & Technology, Varanasi | 2022 – 2025 (Completed, 71.4%)

---

**Experience**:
1. Full Stack Developer Intern (Virtual) at HCL GUVI (July 2025 – September 2025)
   - Developed and tested full-stack application modules following SDLC and Agile methodologies.
   - Applied OOP principles while building scalable frontend and backend components using JavaScript, Node.js, Express.js, and MySQL.
   - Completed structured coding assignments, performed debugging and unit testing.
   - Practiced collaborative development with Git and GitHub.

2. Python Developer Intern at Coding Cafe, Varanasi (November 2024 – April 2025)
   - Developed and deployed Python-based web applications using Streamlit and Pandas for interactive data visualization and dashboard creation.
   - Optimized backend data processing workflows, achieving performance improvement in application responsiveness.
   - Designed user-centric UI components following modern UX principles.
   - Collaborated with cross-functional teams using Git version control to deliver production-ready applications.

---

**Projects**:
1. Pankaj Sharma Vocalist Portfolio (Mar 2026)
   - Technologies: HTML, CSS, JavaScript
   - Created and launched a live portfolio website featuring a user-friendly interface and responsive design to showcase musical compositions and personal branding.
   - Live: https://pankajsharmavocalist.vercel.app/

2. Travel and Tourism Portal (Sep 2025)
   - Technologies: HTML, CSS, JavaScript
   - Unlocking the world of travel through technology. Modern travel and tourism web application with key features and architecture.

3. Hotel Management System (Aug 2025)
   - Technologies: HTML, CSS, JavaScript
   - Streamlining operations and enhancing guest experience with a hotel management system.

4. Student Result Management System (Jul 2025)
   - Technologies: PHP, MySQL, XAMPP
   - Displaying online results for colleges and schools.

5. Calculator (Jul 2025)
   - Technologies: HTML, CSS, JavaScript, MySQL
   - A web-based calculator with a Java-MySQL backend that saves and shows past calculations.

6. BMI Calculator Application (Feb 2025)
   - Technologies: Python, Streamlit
   - Created an interactive BMI calculator that lets users enter height and weight, calculates BMI, and shows health category in real-time.

7. Portfolio Web App (Dec 2024)
   - Technologies: Python, Streamlit
   - Designed and deployed a responsive portfolio with dark/light mode toggle, project views, and integrated contact section.

---

**Certifications** (All in 2024):
1. Full Stack Development (ASP.NET MVC) — HCL GUVI
2. Full Stack Development (FSD) — Certification of Completion
3. Introduction to Programming Using Python — Microsoft
4. Power BI for Beginners — Data Visualization & Analytics
5. HTML & CSS Bootcamp — Web Development Fundamentals
6. Introduction to Figma — UI/UX Design Tools
7. Introduction to Adobe XD — User Experience Design
8. Introduction to MS Excel — Data Analysis & Management
9. Canva For Beginners

---

**Contact**:
- Email: patelsiddharth264@gmail.com
- Phone: +91 8052082640
- WhatsApp: +91 8052082640
- GitHub: https://github.com/siddharrthpatel
- LinkedIn: https://www.linkedin.com/in/siddharth-patel-108581304/

---

**Additional Information**:
- Open to internships and entry-level developer roles.
- GitHub Profile: Maintained active repository with 6+ projects showcasing full-stack development capabilities.
- Willing to learn new technologies and adapt quickly.
- Strong problem-solving and teamwork skills.

---

Answer naturally and enthusiastically as if you are Siddharth's personal AI agent. When asked about skills, projects, experience, education, or certifications, provide detailed answers from the information above. Do NOT make up information that is not present in this prompt.
"""

MODEL_NAME = "gemini-2.5-flash"

if "chat" not in st.session_state:
    st.session_state.chat = []

def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

lottie_dev = load_lottie("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")

st.title("👨‍💻 Siddharth Patel")
st.subheader("Full Stack Developer | AI Portfolio")

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "⚡ Skills",
    "📂 Projects",
    "💼 Experience",
    "🎓 Education",
    "📜 Certificates",
    "🤖 AI Assistant",
    "📞 Contact"
])

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat = []

st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Connect with Me")
st.sidebar.markdown("📞 [+91 8052082640](tel:+918052082640)")
st.sidebar.markdown("✉️ [patelsiddharth264@gmail.com](mailto:patelsiddharth264@gmail.com)")
st.sidebar.markdown("💬 [WhatsApp](https://wa.me/918052082640)")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/siddharth-patel-108581304/)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/siddharrthpatel)")

if page == "🏠 Home":
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("## 👋 About Me")
        st.markdown("""
        I'm **Siddharth Patel**, a passionate Full Stack Developer focused on building fast, responsive, and user-friendly web applications. I specialize in JavaScript, Node.js, Angular, Python, and MySQL, with hands-on experience gained through internships at **HCL GUVI** and **Coding Cafe**.

        Over the past year, I've built real-world projects, including portfolio websites, management systems, dashboards, and API-driven web applications. I enjoy solving real-world problems, optimizing application performance, and writing clean, maintainable code while following modern development practices and Agile methodologies.

        I'm passionate about learning new technologies and continuously improving my skills to build scalable, high-quality software. Currently pursuing my **Master of Computer Applications (MCA)**, I'm actively seeking opportunities as a Full Stack Developer, Software Developer, or Web Developer, where I can contribute to impactful projects, collaborate with talented teams, and grow as a software engineer.
        """)

    with col2:
        if lottie_dev:
            st_lottie(lottie_dev, height=300)

elif page == "⚡ Skills":
    st.header("⚡ Skills")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### 💻 Programming Languages")
            st.markdown("`JavaScript` `Python` `HTML5` `CSS3` `PHP` `Java`")

        with st.container(border=True):
            st.markdown("#### ⚙️ Backend Technologies")
            st.markdown("`Spring Boot` `RESTful API` `ASP.NET MVC` `Node.js` `Express.js`")

        with st.container(border=True):
            st.markdown("#### 🛠 Development Tools")
            st.markdown("`Git` `GitHub` `VS Code` `XAMPP`")

    with col2:
        with st.container(border=True):
            st.markdown("#### 🎨 Frontend Technologies")
            st.markdown("`Angular` `HTML5` `CSS3` `JavaScript` `Responsive Web Design` `UI/UX Design`")

        with st.container(border=True):
            st.markdown("#### 🗄 Databases")
            st.markdown("`MySQL` `Database Design and Management`")

        with st.container(border=True):
            st.markdown("#### 📦 Frameworks & Libraries")
            st.markdown("`Streamlit` `Pandas` `ASP.NET MVC` `Bootstrap`")

    with st.container(border=True):
        st.markdown("#### 🔄 Methodologies")
        st.markdown("`Agile Development` `SDLC` `OOP` `Test-Driven Development` `Unit Testing`")

elif page == "📂 Projects":
    st.header("📂 Projects")

    with st.container(border=True):
        st.markdown("#### 🎤 Pankaj Sharma Vocalist Portfolio")
        st.markdown("**Technologies:** HTML5, CSS3, JavaScript, Responsive Design")
        st.markdown("Designed and deployed live portfolio website with fully responsive design ensuring optimal viewing experience across desktop, tablet, and mobile devices.")
        st.link_button("🌐 Live Demo", "https://pankajsharmavocalist.vercel.app")

    with st.container(border=True):
        st.markdown("#### ✈️ Travel and Tourism Portal")
        st.markdown("**Technologies:** HTML5, CSS3, JavaScript, RESTful APIs")
        st.markdown("Developed comprehensive travel and tourism web application with modern architecture and scalable design patterns.")

    with st.container(border=True):
        st.markdown("#### 🏨 Hotel Management System")
        st.markdown("**Technologies:** HTML5, CSS3, JavaScript, MySQL")
        st.markdown("Built full-featured hotel management system to automate operations and improve guest experience management.")

    with st.container(border=True):
        st.markdown("#### 📊 Student Result Management System")
        st.markdown("**Technologies:** PHP, MySQL, XAMPP, HTML5, CSS3")
        st.markdown("Developed secure online result management system for educational institutions with role-based access control.")

    with st.container(border=True):
        st.markdown("#### 🧮 BMI Calculator Application")
        st.markdown("**Technologies:** Python, Streamlit")
        st.markdown("Created interactive BMI calculator with real-time BMI calculation and health category classification.")

elif page == "💼 Experience":
    st.header("💼 Experience")

    with st.container(border=True):
        if os.path.exists("guvi_hcl.png"):
            st.image("guvi_hcl.png", width=120)
        st.markdown("#### Full Stack Developer Intern (Virtual)")
        st.caption("July 2025 – September 2025 · **HCL GUVI**")
        st.markdown("""
        - Developed and tested full-stack application modules following SDLC and Agile methodologies.
        - Applied OOP principles while building scalable frontend and backend components using JavaScript, Node.js, Express.js, and MySQL.
        - Completed structured coding assignments, performed debugging and unit testing.
        - Practiced collaborative development with Git and GitHub.
        """)

    with st.container(border=True):
        if os.path.exists("coding_cafe.png"):
            st.image("coding_cafe.png", width=120)
        st.markdown("#### Python Developer Intern")
        st.caption("November 2024 – April 2025 · **Coding Cafe, Varanasi**")
        st.markdown("""
        - Developed and deployed Python-based web applications using Streamlit and Pandas for interactive data visualization and dashboard creation.
        - Optimized backend data processing workflows, achieving performance improvement in application responsiveness.
        - Designed user-centric UI components following modern UX principles.
        - Collaborated with cross-functional teams using Git version control to deliver production-ready applications.
        """)

elif page == "🎓 Education":
    st.header("🎓 Education")

    with st.container(border=True):
        st.markdown("#### 🎓 Master of Computer Applications (MCA)")
        st.caption("2025 – Present")
        st.markdown("**School of Management Sciences (SMS), Varanasi**")
        st.info("📖 Currently Pursuing")

    with st.container(border=True):
        st.markdown("#### 🎓 Bachelor of Computer Applications (BCA)")
        st.caption("2022 – 2025")
        st.markdown("**Microtek College of Management & Technology, Varanasi**")
        st.success("✅ Completed — 71.4%")

elif page == "📜 Certificates":
    st.header("📜 Certificates")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.caption("2026")
            st.markdown("**💻 Full Stack Development (ASP.NET MVC)**")
            st.markdown("HCL GUVI")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**🐍 Introduction to Programming Using Python**")
            st.markdown("Microsoft")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**🌐 HTML & CSS Bootcamp**")
            st.markdown("Web Development Fundamentals")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**🎨 Introduction to Adobe XD**")
            st.markdown("User Experience Design")

    with col2:
        with st.container(border=True):
            st.caption("2025")
            st.markdown("**🛠️ Full Stack Development (FSD)**")
            st.markdown("Certification of Completion")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**📊 Power BI for Beginners**")
            st.markdown("Data Visualization & Analytics")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**✏️ Introduction to Figma**")
            st.markdown("UI/UX Design Tools")

        with st.container(border=True):
            st.caption("2025")
            st.markdown("**📈 Introduction to MS Excel**")
            st.markdown("Data Analysis & Management")

elif page == "🤖 AI Assistant":
    st.header("🤖 AI Assistant")

    if st.button("🗑 Clear Chat", key="clear_chat_main"):
        st.session_state.chat = []
        st.rerun()

    for sender, msg in st.session_state.chat:
        with st.chat_message("user" if sender == "user" else "assistant"):
            st.markdown(msg)

    user_input = st.chat_input("Type your message...")

    if user_input:
        st.session_state.chat.append(("user", user_input))

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=user_input,
                config=genai.types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                )
            )
            reply = response.text
        except Exception as e:
            reply = f"⚠️ Gemini Error: {e}"

        st.session_state.chat.append(("ai", reply))
        st.rerun()

elif page == "📞 Contact":
    st.header("📞 Contact")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("📞 **Phone:** [+91 8052082640](tel:+918052082640)")
        with st.container(border=True):
            st.markdown("💬 **WhatsApp:** [Chat on WhatsApp](https://wa.me/918052082640)")
        with st.container(border=True):
            st.markdown("🐙 **GitHub:** [siddharrthpatel](https://github.com/siddharrthpatel)")
    with col2:
        with st.container(border=True):
            st.markdown("✉️ **Email:** [patelsiddharth264@gmail.com](mailto:patelsiddharth264@gmail.com)")
        with st.container(border=True):
            st.markdown("🔗 **LinkedIn:** [Siddharth Patel](https://www.linkedin.com/in/siddharth-patel-108581304/)")

    st.divider()
    st.subheader("✉️ Send a Message")

    name = st.text_input("Name")
    msg = st.text_area("Message")

    if st.button("Send"):
        if name and msg:
            full_message = f"Portfolio Contact\nName: {name}\nMessage: {msg}"
            wa_url = f"https://api.whatsapp.com/send?phone=918052082640&text={quote(full_message)}"
            mail_url = f"mailto:patelsiddharth264@gmail.com?subject={quote(f'Portfolio Message from {name}')}&body={quote(full_message)}"

            st.html(f"""
                <script>
                    window.open("{wa_url}", "_blank");
                    window.location.href = "{mail_url}";
                </script>
            """)

            st.success("✅ Opening WhatsApp & Email — if blocked, use the links below:")

            col1, col2 = st.columns(2)
            with col1:
                st.link_button("💬 Send on WhatsApp", wa_url)
            with col2:
                st.link_button("✉️ Send via Email", mail_url)
        else:
            st.warning("Please fill all fields.")
