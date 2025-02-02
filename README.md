# BharatFD-FAQs

## Overview

BharatFD-FAQs is a Django-based web application for managing frequently asked questions (FAQs). It supports multilingual FAQs and provides an API for creating, retrieving and deleting FAQs.

## Installation

### Prerequisites

- Python 3.13
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/SoumojjalSen/BharatFD-FAQs.git
   cd BharatFD-FAQs
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install pipenv
   pipenv install
   ```

4. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## API Usage

### Endpoints

- **List and Create FAQs:**

  - **URL:** `/api/faqs/`
  - **Description:** Retrieve a list of FAQs or create a new FAQ.
  - **Example Request:**

    ```sh
    curl -X GET http://127.0.0.1:8000/api/faqs/
    ```

- **List and Create FAQs in Hindi:**

  - **URL:** `/api/faqs/?lang=hi`
  - **Description:** Retrieve a list of FAQs or create a new FAQ in Hindi.
  - **Example Request:**
    ```sh
    curl -X GET http://127.0.0.1:8000/api/faqs/?lang=hi
    ```

- **List and Create FAQs in Bengali:**
  - **URL:** `/api/faqs/?lang=bn`
  - **Description:** Retrieve a list of FAQs or create a new FAQ in Bengali.
  - **Example Request:**
    ```sh
    curl -X GET http://127.0.0.1:8000/api/faqs/?lang=bn
    ```

### Example Responses

- **GET /api/faqs/**

  ```json
  [
    {
      "id": 1,
      "question": "What is Django?",
      "answer": "Django is a web framework."
    }
  ]
  ```

- **GET /api/faqs/?lang=hi**

  ```json
  [
    {
      "id": 1,
      "question": "Django क्या है?",
      "answer": "Django एक वेब फ्रेमवर्क है।"
    }
  ]
  ```

- **GET /api/faqs/?lang=bn**

  ```json
  [
    {
      "id": 1,
      "question": "Django কি?",
      "answer": "Django একটি ওয়েব ফ্রেমওয়ার্ক।"
    }
  ]
  ```

## Contact

For any questions or feedback, please contact us at [soumojjalsen@gmail.com](mailto:soumojjalsen@gmail.com).
