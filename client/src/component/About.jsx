import React from 'react';

const About = () => {
  return (
    <div id='aboutcompo'>
    <div className="container py-5" >
      <div className="row">
        <div className="col-lg-8 mx-auto" >
          <div id='aboutus'>
            <h2 className="mb-4">About Us</h2>
          <p>Welcome to our e-commerce store!
          We are dedicated to providing high-quality products and excellent services to our customers.
          Our mission is to make your shopping experience enjoyable and hassle-free.
          Feel free to browse through our collection of products and don't hesitate to contact us if you have any questions.
          Thank you for choosing us!</p>
          </div>
          <div>
          <h2 className="mt-5 mb-4">Contact Us</h2>
          <p>If you have any questions or concerns, please don't hesitate to get in touch with us:</p>
          <ul>
            <li>Email: <a href='/#' style={{textDecoration:'none'}}>Ekart@company.com</a></li>
            <li>Phone: <a href='/#'style={{textDecoration:'none'}}>123-456-7890</a></li>
            <li>Address: <a href='/#'style={{textDecoration:'none'}}>123 Main Street, Nairobi, Kenya</a></li>
          </ul>
          </div>
        </div>
      </div>
    </div>
    </div>
  );
};

export default About;
