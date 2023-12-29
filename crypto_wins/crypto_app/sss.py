from django.shortcuts import render
from django.http import HttpResponse

def sss(request):
    return HttpResponse("""


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Frequently Asked Questions</title>
    <link rel="stylesheet" href="style.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
      integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");

*{
padding: 0;
margin: 0;
box-sizing: border-box;
font-family: "Roboto", sans-serif;
}

.wrapper {
  max-width: 75%;
  margin: auto;
}

.wrapper > p,
.wrapper > h1 {
  margin: 1.5rem 0;
  text-align: center;
}

.wrapper > h1 {
  letter-spacing: 3px;
}

.accordion {
  background-color: white;
  color: rgba(0, 0, 0, 0.8);
  cursor: pointer;
  font-size: 1.2rem;
  width: 100%;
  padding: 2rem 2.5rem;
  border: none;
  outline: none;
  transition: 0.4s;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.accordion i {
  font-size: 1.6rem;
}

.active,
.accordion:hover {
  background-color: #f1f7f5;
}
.pannel {
  padding: 0 2rem 2.5rem 2rem;
  background-color: white;
  overflow: hidden;
  background-color: #f1f7f5;
  display: none;
}
.pannel p {
  color: rgba(0, 0, 0, 0.7);
  font-size: 1.2rem;
  line-height: 1.4;
}

a.hayalet {
	background-color: #7ad4cc;
    border-color: #FFFFFF;
    border-radius: 110px;
    margin: 120px;
    position: relative;
}

.faq {
  border: 1px solid rgba(0, 0, 0, 0.2);
  margin: 10px 0;
}
.faq.active {
  border: none;
}
.neriman{
width: 54px;
height: 45px;
min-height: 34px;
min-width: 43px;
}
</style>
  
  </head>
  <body>
    <div class="resul" >
    <div class="wrapper">
      <p>Borsaya Dahil Herşey</p>
      <h1>Sıkça Sorulan Sorular</h1>

      <div class="faq">
        <button class="accordion">
          Borsa Nedir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Borsa, yatırımcıların halka açık şirketlerin hisselerini alıp satabildikleri piyasanın adıdır.
             Hisse senetleri şirketlerdeki ortaklık paylarını temsil etmektedir.
          </p>
        </div>
      </div>

      <div class="faq">
        <button class="accordion">
          Kripto Para Borsası Nedir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Kripto para borsaları, kullanıcıların Bitcoin, Ethereum ve Tether gibi birçok kripto parayı alıp satmasına
             olanak tanıyan yatırım yapmanız için olanak sağlayan dijital pazar yerleridir.
          </p>
        </div>
      </div> 
      
      <div class="faq">
        <button class="accordion">
          Yatırım Yapmak İçin Ne Gereklidir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Kendinize uygun yatırım ürününü ve sitesini seçip alım işlemini yapmanız gerekmektedir.
          </p>
        </div>
      </div>

      <div class="faq">
        <button class="accordion">
          Yatırım Yaparken Neye Dikkat Edilmelidir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Risk olasılıklarını ve yatırım yaptığınız ürünün güvenilirliğini araştırmanız gerekmektedir.Unutmayın tüm mesuliyet size aittir!
          </p>
        </div>
      </div>

      <div class="faq">
        <button class="accordion">
          Formasyon Nedir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Birbiri ardına gelen bir veya birkaç fiyat çubuğunun fiyat çizelgelerinde (grafik) oluşturduğu
             ve fiyatın tahmini artışını gösteren oluşumlardır.
          </p>
        </div>
      </div>
     
      <div class="faq">
        <button class="accordion">
          Fear and Greed Index nedir?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Korku ve açgözlülük endeksi, yatırımcıların korku ve açgözlülük (hırs) hislerinin piyasalardaki etkilerini ölçmek için kullanılan bir endekstir. Özellikle yatırımcıların piyasalardaki hareketlilik hakkındaki duygusal tepkilerinin bir grafik göstergesi olarak da düşünülebilir.
          </p>
        </div>
      </div>
      
      <div class="faq">
        <button class="accordion">
          Cyrpto Wins Neyi Amaçlar?
          <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="pannel">
          <p>
            Cyrpto Wins yatırım yapmak isteyen yatırımcılar için gereken bilgileri kolaylıkla ulaşabilmesi
             ve bir arada toplamak amacıyla kurulmuş,hiçbir ücret talep etmeyen internet sitesidir.
          </p>
        </div>
      </div>
    </div>
    <a href="/ " class="hayalet" id="signUp">Ana Sayfaya Dön </a>
  </div>
                    

    <script>
      var acc = document.getElementsByClassName("accordion");
      var i;

      for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function () {
          this.classList.toggle("active");
          this.parentElement.classList.toggle("active");

          var pannel = this.nextElementSibling;

          if (pannel.style.display === "block") {
            pannel.style.display = "none";
          } else {
            pannel.style.display = "block";
          }
        });
      }
    </script>
  </body>
</html>

    """)
