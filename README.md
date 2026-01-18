# AI SQL Agent: Text-to-Database Querying

A Streamlit-based application that empowers non-technical users to interact with SQL databases using natural language. Built with Python, LangChain, and OpenAI, this agent translates English questions into executable SQL queries, retrieves the data, and summarizes the results.

### Overview
In traditional enterprise environments, accessing data requires SQL knowledge or reliance on data analysts. This project bridges that gap by using a Large Language Model (LLM) as a reasoning engine to:
1.  **Understand** the user's intent.
2.  **Inspect** the database schema (tables and columns).
3.  **Generate** and **Execute** valid SQL queries.
4.  **Explain** the results in plain English.

### Key features
* **Natural Language Interface:** Ask questions like *"What is the total revenue for December?"* instead of writing complex joins.
* **Transparent Logic:** Utilizes `StreamlitCallbackHandler` to display the agent's "thought process" and the actual SQL queries generated in real-time.
* **Dynamic Schema Awareness:** The agent automatically detects table structures, meaning it can adapt to different database schemas without hard-coded rules.
* **Safety & Determinism:** Configured with `temperature=0` to ensure consistent, accurate SQL generation.

### Tech stack
* **Frontend:** Streamlit
* **Orchestration:** LangChain (SQL Database Toolkit)
* **Model:** OpenAI GPT-3.5 Turbo
* **Database:** SQLite (Local)
* **Language:** Python 3.x

### How to run locally
1.  Clone the repository:
    ```bash
    git clone [https://github.com/NivNeuvirth/ai_agent_text_to_sql.git](https://github.com/NivNeuvirth/ai_agent_text_to_sql.git)
    cd ai_agent_text_to_sql
    ```
2. Create a virtual environment:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```

### Project structure
* **app.py:** The main application logic and UI.
* **init_db.py:** Script to generate the SQLite database with dummy data.
* **sales.db:** The local SQLite database file.
* **requirements.txt:** Python dependencies.

### Future improvements
* Add visualization support (generating charts from the data).
* Implement read-only permissions for enhanced security.
* Support for connecting to external databases (PostgreSQL, MySQL).
