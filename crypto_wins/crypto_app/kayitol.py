from django.shortcuts import render
from django.http import HttpResponse

def kayitol(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,800');

* {
	box-sizing: border-box;
}

body {
	background: #f6f5f7;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	font-family: 'Montserrat', sans-serif;
	height: 100vh;
	margin: -20px 0 50px;
}

h1 {
	font-weight: bold;
	margin: 0;
}

h2 {
	text-align: center;
}

p {
	font-size: 14px;
	font-weight: 100;
	line-height: 20px;
	letter-spacing: 0.5px;
	margin: 20px 0 30px;
}

span {
	font-size: 12px;
}

a {
	color: #333;
	font-size: 14px;
	text-decoration: none;
	margin: 15px 0;
}

button {
	border-radius: 20px;
	border: 0px solid #FF4B2B;
	background-color: #7ad4cc;
	color: #FFFFFF;
	font-size: 12px;
	font-weight: bold;
	padding: 12px 45px;
	letter-spacing: 1px;
	text-transform: uppercase;
	transition: transform 80ms ease-in;
}

button:active {
	transform: scale(0.95);
}

button:focus {
	outline: none;
}

a.hayalet {
	background-color: #7ad4cc;  
	border-color: #FFFFFF;
                        padding: 9px;
                        border-radius: 110px;
}
                        

form {
	background-color: #FFFFFF;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 50px;
	height: 100%;
	text-align: center;
}

input {
	background-color: #eee;
	border: none;
	padding: 12px 15px;
	margin: 8px 0;
	width: 100%;
}

.container {
	background-color: #fff;
	border-radius: 10px;
  	box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
			0 10px 10px rgba(0,0,0,0.22);
	position: relative;
	overflow: hidden;
	width: 768px;
	max-width: 100%;
	min-height: 480px;
}

.form-container {
	position: absolute;
	top: 0;
	height: 100%;
	transition: all 0.6s ease-in-out;
}

.sign-in-container {
	left: 0;
	width: 50%;
	z-index: 2;
}

.container.right-panel-active .sign-in-container {
	transform: translateX(100%);
}

.sign-up-container {
	left: 0;
	width: 50%;
	opacity: 0;
	z-index: 1;
}

.container.right-panel-active .sign-up-container {
	transform: translateX(100%);
	opacity: 1;
	z-index: 5;
	animation: show 0.6s;
}

@keyframes show {
	0%, 49.99% {
		opacity: 0;
		z-index: 1;
	}
	
	50%, 100% {
		opacity: 1;
		z-index: 5;
	}
}

.dışkısım1 {
	position: absolute;
	top: 0;
	left: 50%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: transform 0.6s ease-in-out;
	z-index: 100;
}

.container.right-panel-active .dışkısım1{
	transform: translateX(-100%);
}

.dışkısım2 {
	background: #7AD4CC;
	background: -webkit-linear-gradient(to right, #7AD4CC, #483fec);
	background: linear-gradient(to right, #7AD4CC, #483fec );
	background-repeat: no-repeat;
	background-size: cover;
	background-position: 0 0;
	color: #FFFFFF;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
  	transform: translateX(0);
	transition: transform 0.1s ease-in-out;
}

.container.right-panel-active .dışkısım2 {
  	transform: translateX(50%);
}
.dışkısım2-panel {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	text-align: center;
	top: 0;
	height: 100%;
	width: 50%;
	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.dışkısım2-left {
	transform: translateX(-20%);
}

.container.right-panel-active .dışkısım2-left {
	transform: translateX(0);
}

.dışkısım2-right {
	right: 0;
	transform: translateX(0);
}

.container.right-panel-active .dışkısım2-right {
	transform: translateX(20%);
}

.sosyal-bar {
	margin: 20px 0;
}

.sosyal-bar a {
	border: 1px solid #DDDDDD;
	border-radius: 50%;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	margin: 0 5px;
	height: 40px;
	width: 40px;
}

.main_kemal{
    margin: 0px;
    padding: 5px;
    padding-left: 55px;
    padding-right: 55px;
}

footer {
    background-color: #222;
    color: #fff;
    font-size: 14px;
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}

footer p {
    margin: 10px 0;
}

footer i {
    color: red;
}

.futır1{
	margin-top: 23px;
	max-width: 1200px;

}

    </style>
</head>
<body> 
    <div class="main_kemal">
    <h2>CryptoWins'e Hoşgeldiniz!</h2> <br> 
<div class="container" id="container">
	<div class="giris-kayit-ol-main">
		<form action="#">
			<div class="sosyal-bar">
				<a href="#" class="sosyallink"><i class="fab fa-facebook-f"></i></a>
				<a href="#" class="sosyallink"><i class="fab fa-google-plus-g"></i></a>
				<a href="#" class="sosyallink"><i class="fab fa-linkedin-in"></i></a>
			</div>
			<span>or use your email for registration</span>
			<input type="text" placeholder="Name" />
			<input type="email" placeholder="Email" />
			<input type="password" placeholder="Password" />
			<button>Giriş Yap</button>
		</form>
	</div>
	<div class="form-container sign-in-container">
		<form action="#">
			<h1>Giriş Yap</h1>
            <br><br>
			<input type="email" placeholder="E-posta" />
			<input type="password" placeholder="Şifre" />
			<a href="#">Şifrenizi mi unuttunz?</a>
			<button>Giriş Yap</button>
		</form>
	</div>
	<div class="dışkısım1">
		<div class="dışkısım2">
			<div class="dışkısım2-panel dışkısım2-left">
				<button class="hayalet" id="signIn">Kayıt Ol</button>
			</div>
			<div class="dışkısım2-panel dışkısım2-right">
				<h1>Hoşgeldiniz!</h1>
				<p>Güncel kripto bilgisi almak ister misiniz? Üstelik yeni kayıt olan kullanıcılarımıza python yazılım dili öğrenim paketi hediye! Kişisel e-postanızı girerek bize katılın!</p>
				<a href="/ " class="hayalet" id="signUp">Ana Sayfaya Dön </a>
			</div>
		</div>
	</div>
</div>
</div>

</body>
</html>
	
    """)
