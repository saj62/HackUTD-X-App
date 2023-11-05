// src/Welcome.js
import React from 'react';

function WelcomePage() {
  return (
    <div className="WelcomePage" style={{width: 1512, height: 982, position: 'relative', background: 'white'}}>
        <div className="Bg" style={{width: 1512, height: 840, left: 0, top: 142, position: 'absolute', background: '#92140C'}} />
        <div className="Getquote" style={{width: 402, height: 89, left: 974, top: 487, position: 'absolute', background: 'white', borderRadius: 15, border: '2px #92140C solid'}}></div>
        <div className="GetAQuote" style={{width: 382, height: 62, left: 984, top: 500, position: 'absolute', textAlign: 'center', color: 'black', fontSize: 50, fontFamily: 'Radio Canada', fontWeight: '500', wordWrap: 'break-word'}}>Get a quote</div>
        <div className="HelpingSmallBusinessesGrow" style={{width: 674, height: 568, left: 103, top: 278, position: 'absolute', textAlign: 'center', color: 'white', fontSize: 100, fontFamily: 'Rozha One', fontWeight: '400', wordWrap: 'break-word'}}>Helping Small Businesses Grow</div>
        <div className="Loginrectangle" style={{width: 252, height: 53, left: 1124, top: 49, position: 'absolute', background: 'rgba(146, 20, 12, 0.20)', borderRadius: 15, border: '2px #92140C solid'}}></div>
        <div className="LogIn" style={{width: 246, height: 40, left: 1124, top: 55, position: 'absolute', textAlign: 'center', color: '#92140C', fontSize: 40, fontFamily: 'Radio Canada', fontWeight: '500', wordWrap: 'break-word'}}>Log In</div>
        <img className="InsureaseLogo" style={{width: 287, height: 74, left: 35, top: 38, position: 'absolute'}} src="https://via.placeholder.com/287x74" />
    </div>
  );
}

export default WelcomePage;
