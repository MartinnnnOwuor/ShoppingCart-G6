import React from 'react';

function Home() {
  return (
    <div id='homecomponent'>
    <div className="container" >
      <h1 id='karttitle'className="text-center">Welcome to e-Kart where quality products speak loud!</h1>
      <div style={{marginLeft:'100px',color:'#0000ff', fontWeight:'bold'}} >
       <h2 className="mt-5 mb-4">Why Shop with us?</h2>
            <ul>
              <li>Secure checkout process</li>
              <li>Fast and reliable shipping</li>
              <li>Easy returns and exchanges</li>
              <li>Customer reviews and ratings</li>
              <li>Responsive customer support</li>
              </ul>
              </div>

            <div style={{marginTop:'-50px', marginLeft:"890px", fontWeight:"bolder", color: "#ffff00"}}>
              <h2 className="mt-5 mb-4"> What makes it different?</h2>
                <ul>
              <li>Usable with phone, tab or computer!!</li>
              <li>Global scope</li>
              <li>Easy navigation</li>
              <li>No redirects</li>
              </ul>
            </div>

            <div style={{marginTop: "90px", color: "green", fontWeight: "bolder"}}>
            <h2 className="mt-5 mb-4">What if its a scam?</h2>
            <ul>
              <li>Secure payment via MPESA, Mastercard, paypall etc</li>
              <li>Receipts after payment to showcase recent transactions</li>
              <li>App under Copyright Protection Law</li>
            </ul>
            </div>
    </div>
    </div>
  );
}

export default Home;