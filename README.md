<h1>🛒 BrightBuy – Full Stack E-Commerce Web Application</h1>

<p>
  BrightBuy is a <strong>production-ready full-stack e-commerce platform</strong> built using
  <strong>Django</strong>. It supports secure authentication, product management, cart & wishlist,
  online payments, and transactional emails.
</p>

<p>
  This project demonstrates <strong>real-world backend development, API integrations, and deployment
  practices</strong>, making it ideal for <strong>backend / full-stack internship roles</strong>.
</p>

<hr />

<h2>🔗 Quick Links</h2>
<ul>
  <li>
    🌐 <strong>Live Demo:</strong>
    <a href="https://brightbuy-l59r.onrender.com">https://brightbuy-l59r.onrender.com</a>
  </li>
  <li>
    💻 <strong>Source Code:</strong>
    <a href="https://github.com/Heshane-11/BrightBuy-Django">
      https://github.com/Heshane-11/BrightBuy-Django
    </a>
  </li>
</ul>

<p>
  <strong>Note:</strong> Hosted on Render free tier. It may take <strong>30–60 seconds</strong> to
  start if idle.
</p>

<hr />

<h2>🚀 Features</h2>
<ul>
  <li>Secure user authentication</li>
  <li>Product catalog with categories & variations</li>
  <li>Cart and Wishlist systems</li>
  <li>Checkout with order history</li>
  <li>PayPal payment integration</li>
  <li>Transactional emails via SendGrid</li>
  <li>Image hosting using Cloudinary</li>
  <li>Admin dashboard for inventory & orders</li>
</ul>

<hr />

<h2>🛠️ Tech Stack</h2>
<table border="1" cellpadding="6">
  <tr>
    <th>Component</th>
    <th>Technology</th>
  </tr>
  <tr>
    <td>Backend</td>
    <td>Django (Python)</td>
  </tr>
  <tr>
    <td>Database</td>
    <td>PostgreSQL</td>
  </tr>
  <tr>
    <td>Frontend</td>
    <td>HTML5, CSS3, JavaScript</td>
  </tr>
  <tr>
    <td>Payments</td>
    <td>PayPal API</td>
  </tr>
  <tr>
    <td>Email</td>
    <td>SendGrid</td>
  </tr>
  <tr>
    <td>Storage</td>
    <td>Cloudinary</td>
  </tr>
  <tr>
    <td>Deployment</td>
    <td>Render</td>
  </tr>
</table>

<hr />

<h2>💻 Installation & Setup</h2>

<pre>
git clone https://github.com/Heshane-11/BrightBuy-Django.git
cd BrightBuy-Django
</pre>

<pre>
python -m venv venv
source venv/bin/activate  (Windows: venv\Scripts\activate)
</pre>

<pre>
pip install -r requirements.txt
</pre>

<p>Create <code>.env</code> file:</p>

<pre>
SECRET_KEY=your_secret_key
DEBUG=True
SENDGRID_API_KEY=your_sendgrid_api_key
DEFAULT_FROM_EMAIL=your_email@example.com
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
</pre>

<pre>
python manage.py migrate
python manage.py runserver
</pre>

<hr />

<h2>📂 Project Structure</h2>
<pre>
BrightBuy/
 ├── accounts/
 ├── carts/
 ├── category/
 ├── orders/
 ├── products/
 ├── store/
 ├── wishlist/
 ├── templates/
 ├── static/
 ├── BrightBuy/
 ├── manage.py
 └── requirements.txt
</pre>

<hr />

<h2>⚙️ Key Integrations</h2>
<ul>
  <li><strong>PayPal:</strong> Secure payment processing</li>
  <li><strong>SendGrid:</strong> Transactional email service</li>
  <li><strong>Cloudinary:</strong> Cloud-based image storage</li>
</ul>

<hr />

<h2>📌 Learning Outcomes</h2>
<ul>
  <li>Designed and developed scalable Django backend architecture</li>
  <li>Integrated third-party APIs (PayPal, SendGrid, Cloudinary)</li>
  <li>Implemented full e-commerce workflows</li>
  <li>Applied production-grade security practices</li>
  <li>Deployed and maintained live system on Render using PostgreSQL</li>
</ul>

<hr />

<h2>👤 Author</h2>
<p>
  <strong>Heshane Garg</strong><br />
  B.Tech CSE | Backend & Django Developer<br />
  <a href="https://github.com/Heshane-11">GitHub</a> |
  <a href="https://www.linkedin.com/in/heshane-garg-9b638a28b/">LinkedIn</a>
</p>
