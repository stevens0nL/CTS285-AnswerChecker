# Framework Decision: Flask vs. Streamlit

## Key Differences Discovered (Based on Actual Documentation 🤓)
- **Ease of Use**: Flask (flask.palletsprojects.com) is a micro-framework requiring manual setup for routing, templates, and forms, making it flexible but with a, uhh, steeper learning curve for beginners. (AI code sweats can do it with little to no prior knowledge or skill in programming.)
- Streamlit (docs.streamlit.io) is designed for data apps with simple decorators (e.g., `@st.text_input`), enabling rapid prototyping without deep web knowledge. (It's the JOption pane of Python, basically. o(^▽^)o)
- **Deployment Simplicity**: Flask supports easy deployment to platforms like Heroku or AWS via WSGI (e.g., Gunicorn), but requires more boilerplate for production. Streamlit has built-in deployment to Streamlit Cloud with one command (`streamlit deploy`), ideal for quick sharing, but less customizable for complex backends.
- **Suitability for Small Tools**: Flask excels for lightweight web tools with custom logic (e.g., integrating Python functions), as seen in its routing examples. Streamlit is better for interactive data tools (e.g., sliders, charts) but can feel restrictive for non-data-focused apps, per its app gallery examples.
- **Performance and Scalability**: Flask is lightweight and scalable for small tools, with minimal overhead. Streamlit reruns the entire script on interactions, which can be inefficient for complex logic.
- **Customization**: Flask allows full HTML/CSS control via Jinja templates. Streamlit uses its own UI components, limiting deep customization.

## Chosen Framework: Flask
I chose Flask because the tool is a simple answer-checker (not data-heavy), and I need flexibility to integrate custom Python logic (e.g., string matching) without Streamlit's script-rerun overhead. It's suitable for small tools per its docs, and deployment is straightforward for my use case (local testing first).

## Anticipated Challenge
One challenge is managing routing and form handling manually, which could lead to more boilerplate code compared to Streamlit's simplicity. I'll mitigate this by starting with basic examples from Flask docs.
