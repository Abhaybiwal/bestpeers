# My Awesome Cart

My Awesome Cart is an e-commerce website designed to provide a seamless shopping experience. Users can browse products, add items to their cart, and proceed to checkout with ease. This project is built with Django and aims to offer a robust platform for online shopping.

## Features

- User authentication (signup, login, logout)
- Product listing with categories and search functionality
- Shopping cart with item management
- Checkout process with order summary
- Responsive design for mobile and desktop views
- [List other features specific to your project]

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed:

- Python 3.x
- Django 3.x or above
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Abhaybiwal/bestpeers.git
    cd bestpeers
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**
   Create a `.env` file in the root directory of the project and add the following:
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    DATABASE_URL=your_database_url_here
    ```

5. **Run the initial migrations and create a superuser:**
    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/` to start shopping!

## Usage

Once set up, you can:

- **Browse Products**: View the product listings and categories.
- **Manage Cart**: Add products to your cart and view cart details.
- **Checkout**: Proceed to checkout to complete your purchase.
- **User Account**: Register, log in, and manage your account details.

## Configuration

Configure the application using the `.env` file. Ensure you set the following variables:

- `SECRET_KEY`: The secret key for Django security.
- `DEBUG`: Set to `True` for development and `False` for production.
- `DATABASE_URL`: Connection URL for your database.

## Contributing

We welcome contributions to enhance the project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes and test thoroughly.
4. Submit a pull request with a detailed description of your changes.

