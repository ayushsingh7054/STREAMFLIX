<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>StreamFlix</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar">
  <div class="logo">STREAMFLIX</div>
  <ul class="nav">
    <li onclick="loadSection('home')">Home</li>
    <li onclick="loadSection('movies')">Movies</li>
    <li onclick="loadSection('tv')">TV Shows</li>
    <li onclick="loadSection('new')">New</li>
    <li onclick="loadSection('mylist')">My List</li>
    <li onclick="loadSection('about')">About App</li>
  </ul>
</nav>

<!-- HERO -->
<header class="hero">
  <h1>Unlimited Movies & TV Shows</h1>
  <p>Watch anywhere. Cancel anytime.</p>
</header>

<!-- CONTENT -->
<section class="content" id="content"></section>

<!-- WATCH MODAL -->
<div class="modal" id="watchModal">
  <div class="modal-box">
    <h2>Subscription Required</h2>
    <p>Please buy a plan to watch this content.</p>
    <button onclick="openPlans()">Go To Buy</button>
    <span onclick="closeModal()">✖</span>
  </div>
</div>

<!-- PLAN MODAL -->
<div class="modal" id="planModal">
  <div class="modal-box">
    <h2>Select a Plan</h2>
    <button onclick="openQR(299)">₹299</button>
    <button onclick="openQR(499)">₹499</button>
    <button onclick="openQR(999)">₹999</button>
    <span onclick="closePlans()">✖</span>
  </div>
</div>

<!-- QR MODAL -->
<div class="modal" id="qrModal">
  <div class="modal-box qr-box">
    <h2>Pay Now</h2>

    <img src="qr.png" alt="UPI QR Code" class="qr-image">

    <p class="upi-text">Scan & pay using any UPI app</p>
    <p class="pay-text">
      Pay and send screenshot to <b>7880872482</b>
    </p>

    <span onclick="closeQR()">✖</span>
  </div>
</div>

<script src="script.js"></script>
</body>
</html>
