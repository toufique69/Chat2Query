
# Chat2Query 
Chat2Query is a comprehensive LLM project that leverages Google Palm and Langchain. The goal of this project is to create a system that can interact with a MySQL database. The user can pose questions in a conversational manner, and our system is designed to translate these questions into SQL queries. These queries are then executed on the MySQL database to generate responses.

The data for this system is stored in a MySQL database. For instance, a store manager might ask:
- What is the remaining stock of white Adidas t-shirts?
- What would be the total sales if we sell all extra-small size t-shirts after applying discounts?

Our system is smart enough to formulate precise SQL queries based on these questions and execute them on the MySQL database to provide accurate answers.


## Project Highlights
- We’re dealing with a T-shirt retailer that offers brands like Adidas, Nike, Van Heusen, and Levi’s. 
- The store’s inventory, sales figures, and discount information are all maintained in a MySQL database.
- Our objective is to develop a question-answer system based on Language Model Learning (LLM) that incorporates the following components:
  - Google Palm LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - ChromaDB for vector storage
  - Few-shot learning techniques
- The user interface is designed such that the store manager can pose queries in everyday language, and the system will generate the corresponding responses.


## Installation
1. Clone this repository to your local machine.

2. Install the required dependencies using pip:
```bash
  pip install -r requirements.txt
```

3. Acquire an api key through makersuite.google.com and put it in .env file
```bash
  GOOGLE_API_KEY="your_api_key_here"
```

4. For database setup, run data_t_shirts.sql in your MySQL workbench


## Usage
1. Run the Streamlit app by executing:
```bash
streamlit run main.py
```

2. The web app will open in your browser where you can ask questions


## Sample Questions
  - Total T-Shirt Inventory: How many total t-shirts are currently in stock?
  - Specific T-Shirt Stock: How many Nike t-shirts do we have in stock, specifically in XS size and white color?
  - Total Price of S-Size T-Shirts: What is the total retail price of all S-size t-shirts in our inventory?
  - Discounted Sales for Small Adidas: Considering today's discounts, what would be the total sales amount if we sold all small-size Adidas shirts?
  - Most Popular Size: Based on sales data, what is the most popular size (S, M, L, XL, etc.) for t-shirts?
  - Low Stock Alert: Are there any t-shirt sizes or brands that are currently below a specific stock threshold (e.g., 10 items)?


## Project Structure
- main.py: This is the primary script for the Streamlit application.
- langchain_helper.py: This file contains all the code related to Langchain.
- requirements.txt: This file lists all the Python packages necessary for the project.
- few_shots.py: This script houses the few-shot prompts.
- .env: This is a configuration file where your Google API key is stored.
