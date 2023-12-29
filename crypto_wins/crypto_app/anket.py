from django.shortcuts import render
from django.http import HttpResponse

def anket(request):
    return HttpResponse("""
	<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
	<title>Eğitimlerimiz</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" />
	            <link rel="stylesheet" href="{% static 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css' %}">

	<style>

 */:root{--blue:#007bff;--indigo:#6610f2;--purple:#6f42c1;--pink:#e83e8c;--red:#dc3545;--orange:#fd7e14;--yellow:#ffc107;--green:#28a745;--teal:#20c997;--cyan:#17a2b8;--white:#fff;--gray:#6c757d;--gray-dark:#343a40;--primary:#007bff;--secondary:#6c757d;--success:#28a745;--info:#17a2b8;--warning:#ffc107;--danger:#dc3545;--light:#f8f9fa;--dark:#343a40;--breakpoint-xs:0;--breakpoint-sm:576px;--breakpoint-md:768px;--breakpoint-lg:992px;--breakpoint-xl:1200px;--font-family-sans-serif:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";--font-family-monospace:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace}*,::after,::before{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;-ms-overflow-style:scrollbar;-webkit-tap-highlight-color:transparent}@-ms-viewport{width:device-width}article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";font-size:1rem;font-weight:400;line-height:1.5;color:#212529;text-align:left;background-color:#fff}[tabindex="-1"]:focus{outline:0!important}hr{box-sizing:content-box;height:0;overflow:visible}h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:.5rem}p{margin-top:0;margin-bottom:1rem}abbr[data-original-title],abbr[title]{text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted;cursor:help;border-bottom:0}address{margin-bottom:1rem;font-style:normal;line-height:inherit}dl,ol,ul{margin-top:0;margin-bottom:1rem}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}dt{font-weight:700}dd{margin-bottom:.5rem;margin-left:0}blockquote{margin:0 0 1rem}dfn{font-style:italic}b,strong{font-weight:bolder}small{font-size:80%}sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}a{color:#007bff;text-decoration:none;background-color:transparent;-webkit-text-decoration-skip:objects}a:hover{color:#0056b3;text-decoration:underline}a:not([href]):not([tabindex]){color:inherit;text-decoration:none}a:not([href]):not([tabindex]):focus,a:not([href]):not([tabindex]):hover{color:inherit;text-decoration:none}a:not([href]):not([tabindex]):focus{outline:0}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}pre{margin-top:0;margin-bottom:1rem;overflow:auto;-ms-overflow-style:scrollbar}figure{margin:0 0 1rem}img{vertical-align:middle;border-style:none}svg:not(:root){overflow:hidden}table{border-collapse:collapse}caption{padding-top:.75rem;padding-bottom:.75rem;color:#6c757d;text-align:left;caption-side:bottom}th{text-align:inherit}label{display:inline-block;margin-bottom:.5rem}button{border-radius:0}button:focus{outline:1px dotted;outline:5px auto -webkit-focus-ring-color}button,input,optgroup,select,textarea{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{padding:0;border-style:none}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=date],input[type=datetime-local],input[type=month],input[type=time]{-webkit-appearance:listbox}textarea{overflow:auto;resize:vertical}fieldset{min-width:0;padding:0;margin:0;border:0}legend{display:block;width:100%;max-width:100%;padding:0;margin-bottom:.5rem;font-size:1.5rem;line-height:inherit;color:inherit;white-space:normal}progress{vertical-align:baseline}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{outline-offset:-2px;-webkit-appearance:none}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}output{display:inline-block}summary{display:list-item;cursor:pointer}template{display:none}[hidden]{display:none!important}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{margin-bottom:.5rem;font-family:inherit;font-weight:500;line-height:1.2;color:inherit}.h1,h1{font-size:2.5rem}.h2,h2{font-size:2rem}.h3,h3{font-size:1.75rem}.h4,h4{font-size:1.5rem}.h5,h5{font-size:1.25rem}.h6,h6{font-size:1rem}.lead{font-size:1.25rem;font-weight:300}.display-1{font-size:6rem;font-weight:300;line-height:1.2}.display-2{font-size:5.5rem;font-weight:300;line-height:1.2}.display-3{font-size:4.5rem;font-weight:300;line-height:1.2}.display-4{font-size:3.5rem;font-weight:300;line-height:1.2}hr{margin-top:1rem;margin-bottom:1rem;border:0;border-top:1px solid rgba(0,0,0,.1)}.small,small{font-size:80%;font-weight:400}.mark,mark{padding:.2em;background-color:#fcf8e3}.list-unstyled{padding-left:0;list-style:none}.list-inline{padding-left:0;list-style:none}.list-inline-item{display:inline-block}.list-inline-item:not(:last-child){margin-right:.5rem}.initialism{font-size:90%;text-transform:uppercase}.blockquote{margin-bottom:1rem;font-size:1.25rem}.blockquote-footer{display:block;font-size:80%;color:#6c757d}.blockquote-footer::before{content:"\2014 \00A0"}.img-fluid{max-width:100%;height:auto}.img-thumbnail{padding:.25rem;background-color:#fff;border:1px solid #dee2e6;border-radius:.25rem;max-width:100%;height:auto}.figure{display:inline-block}.figure-img{margin-bottom:.5rem;line-height:1}.figure-caption{font-size:90%;color:#6c757d}code,kbd,pre,samp{font-family:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace}code{font-size:87.5%;color:#e83e8c;word-break:break-word}a>code{color:inherit}kbd{padding:.2rem .4rem;font-size:87.5%;color:#fff;background-color:#212529;border-radius:.2rem}kbd kbd{padding:0;font-size:100%;font-weight:700}pre{display:block;font-size:87.5%;color:#212529}pre code{font-size:inherit;color:inherit;word-break:normal}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:576px){.container{max-width:540px}}@media (min-width:768px){.container{max-width:720px}}@media (min-width:992px){.container{max-width:960px}}@media (min-width:1200px){.container{max-width:1140px}}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.row{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.no-gutters{margin-right:0;margin-left:0}.no-gutters>.col,.no-gutters>[class*=col-]{padding-right:0;padding-left:0}.col,.col-1,.col-10,.col-11,.col-12,.col-2,.col-3,.col-4,.col-5,.col-6,.col-7,.col-8,.col-9,.col-auto,.col-lg,.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-lg-auto,.col-md,.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-md-auto,.col-sm,.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-sm-auto,.col-xl,.col-xl-1,.col-xl-10,.col-xl-11,.col-xl-12,.col-xl-2,.col-xl-3,.col-xl-4,.col-xl-5,.col-xl-6,.col-xl-7,.col-xl-8,.col-xl-9,.col-xl-auto{position:relative;width:100%;min-height:1px;padding-right:15px;padding-left:15px}.col{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-1{-webkit-box-flex:0;-ms-flex:0 0 8.333333%;flex:0 0 8.333333%;max-width:8.333333%}.col-2{-webkit-box-flex:0;-ms-flex:0 0 16.666667%;flex:0 0 16.666667%;max-width:16.666667%}.col-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-4{-webkit-box-flex:0;-ms-flex:0 0 33.333333%;flex:0 0 33.333333%;max-width:33.333333%}.col-5{-webkit-box-flex:0;-ms-flex:0 0 41.666667%;flex:0 0 41.666667%;max-width:41.666667%}.col-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-7{-webkit-box-flex:0;-ms-flex:0 0 58.333333%;flex:0 0 58.333333%;max-width:58.333333%}.col-8{-webkit-box-flex:0;-ms-flex:0 0 66.666667%;flex:0 0 66.666667%;max-width:66.666667%}.col-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-10{-webkit-box-flex:0;-ms-flex:0 0 83.333333%;flex:0 0 83.333333%;max-width:83.333333%}.col-11{-webkit-box-flex:0;-ms-flex:0 0 91.666667%;flex:0 0 91.666667%;max-width:91.666667%}.col-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-1{margin-left:8.333333%}.offset-2{margin-left:16.666667%}.offset-3{margin-left:25%}.offset-4{margin-left:33.333333%}.offset-5{margin-left:41.666667%}.offset-6{margin-left:50%}.offset-7{margin-left:58.333333%}.offset-8{margin-left:66.666667%}.offset-9{margin-left:75%}.offset-10{margin-left:83.333333%}.offset-11{margin-left:91.666667%}@media (min-width:576px){.col-sm{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-sm-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-sm-1{-webkit-box-flex:0;-ms-flex:0 0 8.333333%;flex:0 0 8.333333%;max-width:8.333333%}.col-sm-2{-webkit-box-flex:0;-ms-flex:0 0 16.666667%;flex:0 0 16.666667%;max-width:16.666667%}.col-sm-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-sm-4{-webkit-box-flex:0;-ms-flex:0 0 33.333333%;flex:0 0 33.333333%;max-width:33.333333%}.col-sm-5{-webkit-box-flex:0;-ms-flex:0 0 41.666667%;flex:0 0 41.666667%;max-width:41.666667%}.col-sm-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-sm-7{-webkit-box-flex:0;-ms-flex:0 0 58.333333%;flex:0 0 58.333333%;max-width:58.333333%}.col-sm-8{-webkit-box-flex:0;-ms-flex:0 0 66.666667%;flex:0 0 66.666667%;max-width:66.666667%}.col-sm-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-sm-10{-webkit-box-flex:0;-ms-flex:0 0 83.333333%;flex:0 0 83.333333%;max-width:83.333333%}.col-sm-11{-webkit-box-flex:0;-ms-flex:0 0 91.666667%;flex:0 0 91.666667%;max-width:91.666667%}.col-sm-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-sm-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-sm-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-sm-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-sm-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-sm-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-sm-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-sm-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-sm-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-sm-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-sm-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-sm-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-sm-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-sm-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-sm-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-sm-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-sm-0{margin-left:0}.offset-sm-1{margin-left:8.333333%}.offset-sm-2{margin-left:16.666667%}.offset-sm-3{margin-left:25%}.offset-sm-4{margin-left:33.333333%}.offset-sm-5{margin-left:41.666667%}.offset-sm-6{margin-left:50%}.offset-sm-7{margin-left:58.333333%}.offset-sm-8{margin-left:66.666667%}.offset-sm-9{margin-left:75%}.offset-sm-10{margin-left:83.333333%}.offset-sm-11{margin-left:91.666667%}}@media (min-width:768px){.col-md{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-md-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-md-1{-webkit-box-flex:0;-ms-flex:0 0 8.333333%;flex:0 0 8.333333%;max-width:8.333333%}.col-md-2{-webkit-box-flex:0;-ms-flex:0 0 16.666667%;flex:0 0 16.666667%;max-width:16.666667%}.col-md-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-md-4{-webkit-box-flex:0;-ms-flex:0 0 33.333333%;flex:0 0 33.333333%;max-width:33.333333%}.col-md-5{-webkit-box-flex:0;-ms-flex:0 0 41.666667%;flex:0 0 41.666667%;max-width:41.666667%}.col-md-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-md-7{-webkit-box-flex:0;-ms-flex:0 0 58.333333%;flex:0 0 58.333333%;max-width:58.333333%}.col-md-8{-webkit-box-flex:0;-ms-flex:0 0 66.666667%;flex:0 0 66.666667%;max-width:66.666667%}.col-md-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-md-10{-webkit-box-flex:0;-ms-flex:0 0 83.333333%;flex:0 0 83.333333%;max-width:83.333333%}.col-md-11{-webkit-box-flex:0;-ms-flex:0 0 91.666667%;flex:0 0 91.666667%;max-width:91.666667%}.col-md-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-md-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-md-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-md-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-md-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-md-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-md-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-md-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-md-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-md-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-md-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-md-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-md-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-md-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-md-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-md-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-md-0{margin-left:0}.offset-md-1{margin-left:8.333333%}.offset-md-2{margin-left:16.666667%}.offset-md-3{margin-left:25%}.offset-md-4{margin-left:33.333333%}.offset-md-5{margin-left:41.666667%}.offset-md-6{margin-left:50%}.offset-md-7{margin-left:58.333333%}.offset-md-8{margin-left:66.666667%}.offset-md-9{margin-left:75%}.offset-md-10{margin-left:83.333333%}.offset-md-11{margin-left:91.666667%}}@media (min-width:992px){.col-lg{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-lg-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-lg-1{-webkit-box-flex:0;-ms-flex:0 0 8.333333%;flex:0 0 8.333333%;max-width:8.333333%}.col-lg-2{-webkit-box-flex:0;-ms-flex:0 0 16.666667%;flex:0 0 16.666667%;max-width:16.666667%}.col-lg-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-lg-4{-webkit-box-flex:0;-ms-flex:0 0 33.333333%;flex:0 0 33.333333%;max-width:33.333333%}.col-lg-5{-webkit-box-flex:0;-ms-flex:0 0 41.666667%;flex:0 0 41.666667%;max-width:41.666667%}.col-lg-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-lg-7{-webkit-box-flex:0;-ms-flex:0 0 58.333333%;flex:0 0 58.333333%;max-width:58.333333%}.col-lg-8{-webkit-box-flex:0;-ms-flex:0 0 66.666667%;flex:0 0 66.666667%;max-width:66.666667%}.col-lg-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-lg-10{-webkit-box-flex:0;-ms-flex:0 0 83.333333%;flex:0 0 83.333333%;max-width:83.333333%}.col-lg-11{-webkit-box-flex:0;-ms-flex:0 0 91.666667%;flex:0 0 91.666667%;max-width:91.666667%}.col-lg-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-lg-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-lg-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-lg-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-lg-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-lg-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-lg-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-lg-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-lg-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-lg-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-lg-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-lg-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-lg-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-lg-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-lg-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-lg-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-lg-0{margin-left:0}.offset-lg-1{margin-left:8.333333%}.offset-lg-2{margin-left:16.666667%}.offset-lg-3{margin-left:25%}.offset-lg-4{margin-left:33.333333%}.offset-lg-5{margin-left:41.666667%}.offset-lg-6{margin-left:50%}.offset-lg-7{margin-left:58.333333%}.offset-lg-8{margin-left:66.666667%}.offset-lg-9{margin-left:75%}.offset-lg-10{margin-left:83.333333%}.offset-lg-11{margin-left:91.666667%}}@media (min-width:1200px){.col-xl{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-xl-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-xl-1{-webkit-box-flex:0;-ms-flex:0 0 8.333333%;flex:0 0 8.333333%;max-width:8.333333%}.col-xl-2{-webkit-box-flex:0;-ms-flex:0 0 16.666667%;flex:0 0 16.666667%;max-width:16.666667%}.col-xl-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-xl-4{-webkit-box-flex:0;-ms-flex:0 0 33.333333%;flex:0 0 33.333333%;max-width:33.333333%}.col-xl-5{-webkit-box-flex:0;-ms-flex:0 0 41.666667%;flex:0 0 41.666667%;max-width:41.666667%}.col-xl-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-xl-7{-webkit-box-flex:0;-ms-flex:0 0 58.333333%;flex:0 0 58.333333%;max-width:58.333333%}.col-xl-8{-webkit-box-flex:0;-ms-flex:0 0 66.666667%;flex:0 0 66.666667%;max-width:66.666667%}.col-xl-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-xl-10{-webkit-box-flex:0;-ms-flex:0 0 83.333333%;flex:0 0 83.333333%;max-width:83.333333%}.col-xl-11{-webkit-box-flex:0;-ms-flex:0 0 91.666667%;flex:0 0 91.666667%;max-width:91.666667%}.col-xl-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-xl-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-xl-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-xl-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-xl-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-xl-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-xl-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-xl-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-xl-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-xl-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-xl-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-xl-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-xl-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-xl-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-xl-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-xl-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-xl-0{margin-left:0}.offset-xl-1{margin-left:8.333333%}.offset-xl-2{margin-left:16.666667%}.offset-xl-3{margin-left:25%}.offset-xl-4{margin-left:33.333333%}.offset-xl-5{margin-left:41.666667%}.offset-xl-6{margin-left:50%}.offset-xl-7{margin-left:58.333333%}.offset-xl-8{margin-left:66.666667%}.offset-xl-9{margin-left:75%}.offset-xl-10{margin-left:83.333333%}.offset-xl-11{margin-left:91.666667%}}.table{width:100%;max-width:100%;margin-bottom:1rem;background-color:transparent}.table td,.table th{padding:.75rem;vertical-align:top;border-top:1px solid #dee2e6}.table thead th{vertical-align:bottom;border-bottom:2px solid #dee2e6}.table tbody+tbody{border-top:2px solid #dee2e6}.table .table{background-color:#fff}.table-sm td,.table-sm th{padding:.3rem}.table-bordered{border:1px solid #dee2e6}.table-bordered td,.table-bordered th{border:1px solid #dee2e6}.table-bordered thead td,.table-bordered thead th{border-bottom-width:2px}.table-striped tbody tr:nth-of-type(odd){background-color:rgba(0,0,0,.05)}.table-hover tbody tr:hover{background-color:rgba(0,0,0,.075)}.table-primary,.table-primary>td,.table-primary>th{background-color:#b8daff}.table-hover .table-primary:hover{background-color:#9fcdff}.table-hover .table-primary:hover>td,.table-hover .table-primary:hover>th{background-color:#9fcdff}.table-secondary,.table-secondary>td,.table-secondary>th{background-color:#d6d8db}.table-hover .table-secondary:hover{background-color:#c8cbcf}.table-hover .table-secondary:hover>td,.table-hover .table-secondary:hover>th{background-color:#c8cbcf}.table-success,.table-success>td,.table-success>th{background-color:#c3e6cb}.table-hover .table-success:hover{background-color:#b1dfbb}.table-hover .table-success:hover>td,.table-hover .table-success:hover>th{background-color:#b1dfbb}.table-info,.table-info>td,.table-info>th{background-color:#bee5eb}.table-hover .table-info:hover{background-color:#abdde5}.table-hover .table-info:hover>td,.table-hover .table-info:hover>th{background-color:#abdde5}.table-warning,.table-warning>td,.table-warning>th{background-color:#ffeeba}.table-hover .table-warning:hover{background-color:#ffe8a1}.table-hover .table-warning:hover>td,.table-hover .table-warning:hover>th{background-color:#ffe8a1}.table-danger,.table-danger>td,.table-danger>th{background-color:#f5c6cb}.table-hover .table-danger:hover{background-color:#f1b0b7}.table-hover .table-danger:hover>td,.table-hover .table-danger:hover>th{background-color:#f1b0b7}.table-light,.table-light>td,.table-light>th{background-color:#fdfdfe}.table-hover .table-light:hover{background-color:#ececf6}.table-hover .table-light:hover>td,.table-hover .table-light:hover>th{background-color:#ececf6}.table-dark,.table-dark>td,.table-dark>th{background-color:#c6c8ca}.table-hover .table-dark:hover{background-color:#b9bbbe}.table-hover .table-dark:hover>td,.table-hover .table-dark:hover>th{background-color:#b9bbbe}.table-active,.table-active>td,.table-active>th{background-color:rgba(0,0,0,.075)}.table-hover .table-active:hover{background-color:rgba(0,0,0,.075)}.table-hover .table-active:hover>td,.table-hover .table-active:hover>th{background-color:rgba(0,0,0,.075)}.table .thead-dark th{color:#fff;background-color:#212529;border-color:#32383e}.table .thead-light th{color:#495057;background-color:#e9ecef;border-color:#dee2e6}.table-dark{color:#fff;background-color:#212529}.table-dark td,.table-dark th,.table-dark thead th{border-color:#32383e}.table-dark.table-bordered{border:0}.table-dark.table-striped tbody tr:nth-of-type(odd){background-color:rgba(255,255,255,.05)}.table-dark.table-hover tbody tr:hover{background-color:rgba(255,255,255,.075)}@media (max-width:575.98px){.table-responsive-sm{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-sm>.table-bordered{border:0}}@media (max-width:767.98px){.table-responsive-md{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-md>.table-bordered{border:0}}@media (max-width:991.98px){.table-responsive-lg{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-lg>.table-bordered{border:0}}@media (max-width:1199.98px){.table-responsive-xl{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-xl>.table-bordered{border:0}}.table-responsive{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive>.table-bordered{border:0}.form-control{display:block;width:100%;padding:.375rem .75rem;font-size:1rem;line-height:1.5;color:#495057;background-color:#fff;background-clip:padding-box;border:1px solid #ced4da;border-radius:.25rem;transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out}.form-control::-ms-expand{background-color:transparent;border:0}.form-control:focus{color:#495057;background-color:#fff;border-color:#80bdff;outline:0;box-shadow:0 0 0 .2rem rgba(0,123,255,.25)}.form-control::-webkit-input-placeholder{color:#6c757d;opacity:1}.form-control::-moz-placeholder{color:#6c757d;opacity:1}.form-control:-ms-input-placeholder{color:#6c757d;opacity:1}.form-control::-ms-input-placeholder{color:#6c757d;opacity:1}.form-control::placeholder{color:#6c757d;opacity:1}.form-control:disabled,.form-control[readonly]{background-color:#e9ecef;opacity:1}select.form-control:not([size]):not([multiple]){height:calc(2.25rem + 2px)}select.form-control:focus::-ms-value{color:#495057;background-color:#fff}.form-control-file,.form-control-range{display:block;width:100%}.col-form-label{padding-top:calc(.375rem + 1px);padding-bottom:calc(.375rem + 1px);margin-bottom:0;font-size:inherit;line-height:1.5}.col-form-label-lg{padding-top:calc(.5rem + 1px);padding-bottom:calc(.5rem + 1px);font-size:1.25rem;line-height:1.5}.col-form-label-sm{padding-top:calc(.25rem + 1px);padding-bottom:calc(.25rem + 1px);font-size:.875rem;line-height:1.5}.form-control-plaintext{display:block;width:100%;padding-top:.375rem;padding-bottom:.375rem;margin-bottom:0;line-height:1.5;background-color:transparent;border:solid transparent;border-width:1px 0}.form-control-plaintext.form-control-lg,.form-control-plaintext.form-control-sm,.input-group-lg>.form-control-plaintext.form-control,.input-group-lg>.input-group-append>.form-control-plaintext.btn,.input-group-lg>.input-group-append>.form-control-plaintext.input-group-text,.input-group-lg>.input-group-prepend>.form-control-plaintext.btn,.input-group-lg>.input-group-prepend>.form-control-plaintext.input-group-text,.input-group-sm>.form-control-plaintext.form-control,.input-group-sm>.input-group-append>.form-control-plaintext.btn,.input-group-sm>.input-group-append>.form-control-plaintext.input-group-text,.input-group-sm>.input-group-prepend>.form-control-plaintext.btn,.input-group-sm>.input-group-prepend>.form-control-plaintext.input-group-text{padding-right:0;padding-left:0}.form-control-sm,.input-group-sm>.form-control,.input-group-sm>.input-group-append>.btn,.input-group-sm>.input-group-append>.input-group-text,.input-group-sm>.input-group-prepend>.btn,.input-group-sm>.input-group-prepend>.input-group-text{padding:.25rem .5rem;font-size:.875rem;line-height:1.5;border-radius:.2rem}.input-group-sm>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-sm>select.form-control:not([size]):not([multiple]),select.form-control-sm:not([size]):not([multiple]){height:calc(1.8125rem + 2px)}.form-control-lg,.input-group-lg>.form-control,.input-group-lg>.input-group-append>.btn,.input-group-lg>.input-group-append>.input-group-text,.input-group-lg>.input-group-prepend>.btn,.input-group-lg>.input-group-prepend>.input-group-text{padding:.5rem 1rem;font-size:1.25rem;line-height:1.5;border-radius:.3rem}.input-group-lg>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-lg>select.form-control:not([size]):not([multiple]),select.form-control-lg:not([size]):not([multiple]){height:calc(2.875rem + 2px)}.form-group{margin-bottom:1rem}.form-text{display:block;margin-top:.25rem}.form-row{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-5px;margin-left:-5px}.form-row>.col,.form-row>[class*=col-]{padding-right:5px;padding-left:5px}.form-check{position:relative;display:block;padding-left:1.25rem}.form-check-input{position:absolute;margin-top:.3rem;margin-left:-1.25rem}.form-check-input:disabled~.form-check-label{color:#6c757d}.form-check-label{margin-bottom:0}.form-check-inline{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-left:0;margin-right:.75rem}.form-check-inline .form-check-input{position:static;margin-top:0;margin-right:.3125rem;margin-left:0}.valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#28a745}.valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(40,167,69,.8);border-radius:.2rem}.custom-select.is-valid,.form-control.is-valid,.was-validated .custom-select:valid,.was-validated .form-control:valid{border-color:#28a745}.custom-select.is-valid:focus,.form-control.is-valid:focus,.was-validated .custom-select:valid:focus,.was-validated .form-control:valid:focus{border-color:#28a745;box-shadow:0 0 0 .2rem rgba(40,167,69,.25)}.custom-select.is-valid~.valid-feedback,.custom-select.is-valid~.valid-tooltip,.form-control.is-valid~.valid-feedback,.form-control.is-valid~.valid-tooltip,.was-validated .custom-select:valid~.valid-feedback,.was-validated .custom-select:valid~.valid-tooltip,.was-validated .form-control:valid~.valid-feedback,.was-validated .form-control:valid~.valid-tooltip{display:block}.form-check-input.is-valid~.form-check-label,.was-validated .form-check-input:valid~.form-check-label{color:#28a745}.form-check-input.is-valid~.valid-feedback,.form-check-input.is-valid~.valid-tooltip,.was-validated .form-check-input:valid~.valid-feedback,.was-validated .form-check-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid~.custom-control-label,.was-validated .custom-control-input:valid~.custom-control-label{color:#28a745}.custom-control-input.is-valid~.custom-control-label::before,.was-validated .custom-control-input:valid~.custom-control-label::before{background-color:#71dd8a}.custom-control-input.is-valid~.valid-feedback,.custom-control-input.is-valid~.valid-tooltip,.was-validated .custom-control-input:valid~.valid-feedback,.was-validated .custom-control-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid:checked~.custom-control-label::before,.was-validated .custom-control-input:valid:checked~.custom-control-label::before{background-color:#34ce57}.custom-control-input.is-valid:focus~.custom-control-label::before,.was-validated .custom-control-input:valid:focus~.custom-control-label::before{box-shadow:0 0 0 1px #fff,0 0 0 .2rem rgba(40,167,69,.25)}.custom-file-input.is-valid~.custom-file-label,.was-validated .custom-file-input:valid~.custom-file-label{border-color:#28a745}.custom-file-input.is-valid~.custom-file-label::before,.was-validated .custom-file-input:valid~.custom-file-label::before{border-color:inherit}.custom-file-input.is-valid~.valid-feedback,.custom-file-input.is-valid~.valid-tooltip,.was-validated .custom-file-input:valid~.valid-feedback,.was-validated .custom-file-input:valid~.valid-tooltip{display:block}.custom-file-input.is-valid:focus~.custom-file-label,.was-validated .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(40,167,69,.25)}.invalid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#dc3545}.invalid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(220,53,69,.8);border-radius:.2rem}.custom-select.is-invalid,.form-control.is-invalid,.was-validated .custom-select:invalid,.was-validated .form-control:invalid{border-color:#dc3545}.custom-select.is-invalid:focus,.form-control.is-invalid:focus,.was-validated .custom-select:invalid:focus,.was-validated .form-control:invalid:focus{border-color:#dc3545;box-shadow:0 0 0 .2rem rgba(220,53,69,.25)}.custom-select.is-invalid~.invalid-feedback,.custom-select.is-invalid~.invalid-tooltip,.form-control.is-invalid~.invalid-feedback,.form-control.is-invalid~.invalid-tooltip,.was-validated .custom-select:invalid~.invalid-feedback,.was-validated .custom-select:invalid~.invalid-tooltip,.was-validated .form-control:invalid~.invalid-feedback,.was-validated .form-control:invalid~.invalid-tooltip{display:block}.form-check-input.is-invalid~.form-check-label,.was-validated .form-check-input:invalid~.form-check-label{color:#dc3545}.form-check-input.is-invalid~.invalid-feedback,.form-check-input.is-invalid~.invalid-tooltip,.was-validated .form-check-input:invalid~.invalid-feedback,.was-validated .form-check-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid~.custom-control-label,.was-validated .custom-control-input:invalid~.custom-control-label{color:#dc3545}.custom-control-input.is-invalid~.custom-control-label::before,.was-validated .custom-control-input:invalid~.custom-control-label::before{background-color:#efa2a9}.custom-control-input.is-invalid~.invalid-feedback,.custom-control-input.is-invalid~.invalid-tooltip,.was-validated .custom-control-input:invalid~.invalid-feedback,.was-validated .custom-control-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid:checked~.custom-control-label::before,.was-validated .custom-control-input:invalid:checked~.custom-control-label::before{background-color:#e4606d}.custom-control-input.is-invalid:focus~.custom-control-label::before,.was-validated .custom-control-input:invalid:focus~.custom-control-label::before{box-shadow:0 0 0 1px #fff,0 0 0 .2rem rgba(220,53,69,.25)}.custom-file-input.is-invalid~.custom-file-label,.was-validated .custom-file-input:invalid~.custom-file-label{border-color:#dc3545}.custom-file-input.is-invalid~.custom-file-label::before,.was-validated .custom-file-input:invalid~.custom-file-label::before{border-color:inherit}.custom-file-input.is-invalid~.invalid-feedback,.custom-file-input.is-invalid~.invalid-tooltip,.was-validated .custom-file-input:invalid~.invalid-feedback,.was-validated .custom-file-input:invalid~.invalid-tooltip{display:block}.custom-file-input.is-invalid:focus~.custom-file-label,.was-validated .custom-file-input:invalid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(220,53,69,.25)}.form-inline{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.form-inline .form-check{width:100%}@media (min-width:576px){.form-inline label{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;margin-bottom:0}.form-inline .form-group{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center;margin-bottom:0}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-plaintext{display:inline-block}.form-inline .input-group{width:auto}.form-inline .form-check{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:auto;padding-left:0}.form-inline .form-check-input{position:relative;margin-top:0;margin-right:.25rem;margin-left:0}.form-inline .custom-control{-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.form-inline .custom-control-label{margin-bottom:0}}.btn{display:inline-block;font-weight:400;text-align:center;white-space:nowrap;vertical-align:middle;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;border:1px solid transparent;padding:.375rem .75rem;font-size:1rem;line-height:1.5;border-radius:.25rem;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}.btn:focus,.btn:hover{text-decoration:none}.btn.focus,.btn:focus{outline:0;box-shadow:0 0 0 .2rem rgba(0,123,255,.25)}.btn.disabled,.btn:disabled{opacity:.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.btn:not(:disabled):not(.disabled).active,.btn:not(:disabled):not(.disabled):active{background-image:none}a.btn.disabled,fieldset:disabled a.btn{pointer-events:none}.btn-primary{color:#fff;background-color:#007bff;border-color:#007bff}.btn-primary:hover{color:#fff;background-color:#0069d9;border-color:#0062cc}.btn-primary.focus,.btn-primary:focus{box-shadow:0 0 0 .2rem rgba(0,123,255,.5)}.btn-primary.disabled,.btn-primary:disabled{color:#fff;background-color:#007bff;border-color:#007bff}.btn-primary:not(:disabled):not(.disabled).active,.btn-primary:not(:disabled):not(.disabled):active,.show>.btn-primary.dropdown-toggle{color:#fff;background-color:#0062cc;border-color:#005cbf}.btn-primary:not(:disabled):not(.disabled).active:focus,.btn-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-primary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(0,123,255,.5)}.btn-secondary{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-secondary:hover{color:#fff;background-color:#5a6268;border-color:#545b62}.btn-secondary.focus,.btn-secondary:focus{box-shadow:0 0 0 .2rem rgba(108,117,125,.5)}.btn-secondary.disabled,.btn-secondary:disabled{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-secondary:not(:disabled):not(.disabled).active,.btn-secondary:not(:disabled):not(.disabled):active,.show>.btn-secondary.dropdown-toggle{color:#fff;background-color:#545b62;border-color:#4e555b}.btn-secondary:not(:disabled):not(.disabled).active:focus,.btn-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-secondary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(108,117,125,.5)}.btn-success{color:#fff;background-color:#28a745;border-color:#28a745}.btn-success:hover{color:#fff;background-color:#218838;border-color:#1e7e34}.btn-success.focus,.btn-success:focus{box-shadow:0 0 0 .2rem rgba(40,167,69,.5)}.btn-success.disabled,.btn-success:disabled{color:#fff;background-color:#28a745;border-color:#28a745}.btn-success:not(:disabled):not(.disabled).active,.btn-success:not(:disabled):not(.disabled):active,.show>.btn-success.dropdown-toggle{color:#fff;background-color:#1e7e34;border-color:#1c7430}.btn-success:not(:disabled):not(.disabled).active:focus,.btn-success:not(:disabled):not(.disabled):active:focus,.show>.btn-success.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(40,167,69,.5)}.btn-info{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-info:hover{color:#fff;background-color:#138496;border-color:#117a8b}.btn-info.focus,.btn-info:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-info.disabled,.btn-info:disabled{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-info:not(:disabled):not(.disabled).active,.btn-info:not(:disabled):not(.disabled):active,.show>.btn-info.dropdown-toggle{color:#fff;background-color:#117a8b;border-color:#10707f}.btn-info:not(:disabled):not(.disabled).active:focus,.btn-info:not(:disabled):not(.disabled):active:focus,.show>.btn-info.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-warning{color:#212529;background-color:#ffc107;border-color:#ffc107}.btn-warning:hover{color:#212529;background-color:#e0a800;border-color:#d39e00}.btn-warning.focus,.btn-warning:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-warning.disabled,.btn-warning:disabled{color:#212529;background-color:#ffc107;border-color:#ffc107}.btn-warning:not(:disabled):not(.disabled).active,.btn-warning:not(:disabled):not(.disabled):active,.show>.btn-warning.dropdown-toggle{color:#212529;background-color:#d39e00;border-color:#c69500}.btn-warning:not(:disabled):not(.disabled).active:focus,.btn-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-warning.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-danger{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-danger:hover{color:#fff;background-color:#c82333;border-color:#bd2130}.btn-danger.focus,.btn-danger:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-danger.disabled,.btn-danger:disabled{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-danger:not(:disabled):not(.disabled).active,.btn-danger:not(:disabled):not(.disabled):active,.show>.btn-danger.dropdown-toggle{color:#fff;background-color:#bd2130;border-color:#b21f2d}.btn-danger:not(:disabled):not(.disabled).active:focus,.btn-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-danger.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-light{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:hover{color:#212529;background-color:#e2e6ea;border-color:#dae0e5}.btn-light.focus,.btn-light:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-light.disabled,.btn-light:disabled{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:not(:disabled):not(.disabled).active,.btn-light:not(:disabled):not(.disabled):active,.show>.btn-light.dropdown-toggle{color:#212529;background-color:#dae0e5;border-color:#d3d9df}.btn-light:not(:disabled):not(.disabled).active:focus,.btn-light:not(:disabled):not(.disabled):active:focus,.show>.btn-light.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-dark{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:hover{color:#fff;background-color:#23272b;border-color:#1d2124}.btn-dark.focus,.btn-dark:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-dark.disabled,.btn-dark:disabled{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:not(:disabled):not(.disabled).active,.btn-dark:not(:disabled):not(.disabled):active,.show>.btn-dark.dropdown-toggle{color:#fff;background-color:#1d2124;border-color:#171a1d}.btn-dark:not(:disabled):not(.disabled).active:focus,.btn-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-dark.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-primary{color:#007bff;background-color:transparent;background-image:none;border-color:#007bff}.btn-outline-primary:hover{color:#fff;background-color:#007bff;border-color:#007bff}.btn-outline-primary.focus,.btn-outline-primary:focus{box-shadow:0 0 0 .2rem rgba(0,123,255,.5)}.btn-outline-primary.disabled,.btn-outline-primary:disabled{color:#007bff;background-color:transparent}.btn-outline-primary:not(:disabled):not(.disabled).active,.btn-outline-primary:not(:disabled):not(.disabled):active,.show>.btn-outline-primary.dropdown-toggle{color:#fff;background-color:#007bff;border-color:#007bff}.btn-outline-primary:not(:disabled):not(.disabled).active:focus,.btn-outline-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-primary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(0,123,255,.5)}.btn-outline-secondary{color:#6c757d;background-color:transparent;background-image:none;border-color:#6c757d}.btn-outline-secondary:hover{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary.focus,.btn-outline-secondary:focus{box-shadow:0 0 0 .2rem rgba(108,117,125,.5)}.btn-outline-secondary.disabled,.btn-outline-secondary:disabled{color:#6c757d;background-color:transparent}.btn-outline-secondary:not(:disabled):not(.disabled).active,.btn-outline-secondary:not(:disabled):not(.disabled):active,.show>.btn-outline-secondary.dropdown-toggle{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary:not(:disabled):not(.disabled).active:focus,.btn-outline-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-secondary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(108,117,125,.5)}.btn-outline-success{color:#28a745;background-color:transparent;background-image:none;border-color:#28a745}.btn-outline-success:hover{color:#fff;background-color:#28a745;border-color:#28a745}.btn-outline-success.focus,.btn-outline-success:focus{box-shadow:0 0 0 .2rem rgba(40,167,69,.5)}.btn-outline-success.disabled,.btn-outline-success:disabled{color:#28a745;background-color:transparent}.btn-outline-success:not(:disabled):not(.disabled).active,.btn-outline-success:not(:disabled):not(.disabled):active,.show>.btn-outline-success.dropdown-toggle{color:#fff;background-color:#28a745;border-color:#28a745}.btn-outline-success:not(:disabled):not(.disabled).active:focus,.btn-outline-success:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-success.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(40,167,69,.5)}.btn-outline-info{color:#17a2b8;background-color:transparent;background-image:none;border-color:#17a2b8}.btn-outline-info:hover{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-outline-info.focus,.btn-outline-info:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-outline-info.disabled,.btn-outline-info:disabled{color:#17a2b8;background-color:transparent}.btn-outline-info:not(:disabled):not(.disabled).active,.btn-outline-info:not(:disabled):not(.disabled):active,.show>.btn-outline-info.dropdown-toggle{color:#fff;background-color:#17a2b8;border-color:#17a2b8}.btn-outline-info:not(:disabled):not(.disabled).active:focus,.btn-outline-info:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-info.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(23,162,184,.5)}.btn-outline-warning{color:#ffc107;background-color:transparent;background-image:none;border-color:#ffc107}.btn-outline-warning:hover{color:#212529;background-color:#ffc107;border-color:#ffc107}.btn-outline-warning.focus,.btn-outline-warning:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-outline-warning.disabled,.btn-outline-warning:disabled{color:#ffc107;background-color:transparent}.btn-outline-warning:not(:disabled):not(.disabled).active,.btn-outline-warning:not(:disabled):not(.disabled):active,.show>.btn-outline-warning.dropdown-toggle{color:#212529;background-color:#ffc107;border-color:#ffc107}.btn-outline-warning:not(:disabled):not(.disabled).active:focus,.btn-outline-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-warning.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(255,193,7,.5)}.btn-outline-danger{color:#dc3545;background-color:transparent;background-image:none;border-color:#dc3545}.btn-outline-danger:hover{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-outline-danger.focus,.btn-outline-danger:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-outline-danger.disabled,.btn-outline-danger:disabled{color:#dc3545;background-color:transparent}.btn-outline-danger:not(:disabled):not(.disabled).active,.btn-outline-danger:not(:disabled):not(.disabled):active,.show>.btn-outline-danger.dropdown-toggle{color:#fff;background-color:#dc3545;border-color:#dc3545}.btn-outline-danger:not(:disabled):not(.disabled).active:focus,.btn-outline-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-danger.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(220,53,69,.5)}.btn-outline-light{color:#f8f9fa;background-color:transparent;background-image:none;border-color:#f8f9fa}.btn-outline-light:hover{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light.focus,.btn-outline-light:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-light.disabled,.btn-outline-light:disabled{color:#f8f9fa;background-color:transparent}.btn-outline-light:not(:disabled):not(.disabled).active,.btn-outline-light:not(:disabled):not(.disabled):active,.show>.btn-outline-light.dropdown-toggle{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light:not(:disabled):not(.disabled).active:focus,.btn-outline-light:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-light.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-dark{color:#343a40;background-color:transparent;background-image:none;border-color:#343a40}.btn-outline-dark:hover{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark.focus,.btn-outline-dark:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-dark.disabled,.btn-outline-dark:disabled{color:#343a40;background-color:transparent}.btn-outline-dark:not(:disabled):not(.disabled).active,.btn-outline-dark:not(:disabled):not(.disabled):active,.show>.btn-outline-dark.dropdown-toggle{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark:not(:disabled):not(.disabled).active:focus,.btn-outline-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-dark.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-link{font-weight:400;color:#007bff;background-color:transparent}.btn-link:hover{color:#0056b3;text-decoration:underline;background-color:transparent;border-color:transparent}.btn-link.focus,.btn-link:focus{text-decoration:underline;border-color:transparent;box-shadow:none}.btn-link.disabled,.btn-link:disabled{color:#6c757d}.btn-group-lg>.btn,.btn-lg{padding:.5rem 1rem;font-size:1.25rem;line-height:1.5;border-radius:.3rem}.btn-group-sm>.btn,.btn-sm{padding:.25rem .5rem;font-size:.875rem;line-height:1.5;border-radius:.2rem}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:.5rem}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}.fade{opacity:0;transition:opacity .15s linear}.fade.show{opacity:1}.collapse{display:none}.collapse.show{display:block}tr.collapse.show{display:table-row}tbody.collapse.show{display:table-row-group}.collapsing{position:relative;height:0;overflow:hidden;transition:height .35s ease}.dropdown,.dropup{position:relative}.dropdown-toggle::after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid;border-right:.3em solid transparent;border-bottom:0;border-left:.3em solid transparent}.dropdown-toggle:empty::after{margin-left:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:.5rem 0;margin:.125rem 0 0;font-size:1rem;color:#212529;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.15);border-radius:.25rem}.dropup .dropdown-menu{margin-top:0;margin-bottom:.125rem}.dropup .dropdown-toggle::after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:0;border-right:.3em solid transparent;border-bottom:.3em solid;border-left:.3em solid transparent}.dropup .dropdown-toggle:empty::after{margin-left:0}.dropright .dropdown-menu{margin-top:0;margin-left:.125rem}.dropright .dropdown-toggle::after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-bottom:.3em solid transparent;border-left:.3em solid}.dropright .dropdown-toggle:empty::after{margin-left:0}.dropright .dropdown-toggle::after{vertical-align:0}.dropleft .dropdown-menu{margin-top:0;margin-right:.125rem}.dropleft .dropdown-toggle::after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:""}.dropleft .dropdown-toggle::after{display:none}.dropleft .dropdown-toggle::before{display:inline-block;width:0;height:0;margin-right:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:.3em solid;border-bottom:.3em solid transparent}.dropleft .dropdown-toggle:empty::after{margin-left:0}.dropleft .dropdown-toggle::before{vertical-align:0}.dropdown-divider{height:0;margin:.5rem 0;overflow:hidden;border-top:1px solid #e9ecef}.dropdown-item{display:block;width:100%;padding:.25rem 1.5rem;clear:both;font-weight:400;color:#212529;text-align:inherit;white-space:nowrap;background-color:transparent;border:0}.dropdown-item:focus,.dropdown-item:hover{color:#16181b;text-decoration:none;background-color:#f8f9fa}.dropdown-item.active,.dropdown-item:active{color:#fff;text-decoration:none;background-color:#007bff}.dropdown-item.disabled,.dropdown-item:disabled{color:#6c757d;background-color:transparent}.dropdown-menu.show{display:block}.dropdown-header{display:block;padding:.5rem 1.5rem;margin-bottom:0;font-size:.875rem;color:#6c757d;white-space:nowrap}.btn-group,.btn-group-vertical{position:relative;display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto}.btn-group-vertical>.btn:hover,.btn-group>.btn:hover{z-index:1}.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus{z-index:1}.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group,.btn-group-vertical .btn+.btn,.btn-group-vertical .btn+.btn-group,.btn-group-vertical .btn-group+.btn,.btn-group-vertical .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.btn-toolbar .input-group{width:auto}.btn-group>.btn:first-child{margin-left:0}.btn-group>.btn-group:not(:last-child)>.btn,.btn-group>.btn:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn-group:not(:first-child)>.btn,.btn-group>.btn:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.dropdown-toggle-split{padding-right:.5625rem;padding-left:.5625rem}.dropdown-toggle-split::after{margin-left:0}.btn-group-sm>.btn+.dropdown-toggle-split,.btn-sm+.dropdown-toggle-split{padding-right:.375rem;padding-left:.375rem}.btn-group-lg>.btn+.dropdown-toggle-split,.btn-lg+.dropdown-toggle-split{padding-right:.75rem;padding-left:.75rem}.btn-group-vertical{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.btn-group-vertical .btn,.btn-group-vertical .btn-group{width:100%}.btn-group-vertical>.btn+.btn,.btn-group-vertical>.btn+.btn-group,.btn-group-vertical>.btn-group+.btn,.btn-group-vertical>.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical>.btn-group:not(:last-child)>.btn,.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:not(:first-child)>.btn,.btn-group-vertical>.btn:not(:first-child){border-top-left-radius:0;border-top-right-radius:0}.btn-group-toggle>.btn,.btn-group-toggle>.btn-group>.btn{margin-bottom:0}.btn-group-toggle>.btn input[type=checkbox],.btn-group-toggle>.btn input[type=radio],.btn-group-toggle>.btn-group>.btn input[type=checkbox],.btn-group-toggle>.btn-group>.btn input[type=radio]{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.input-group{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;width:100%}.input-group>.custom-file,.input-group>.custom-select,.input-group>.form-control{position:relative;-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;width:1%;margin-bottom:0}.input-group>.custom-file:focus,.input-group>.custom-select:focus,.input-group>.form-control:focus{z-index:3}.input-group>.custom-file+.custom-file,.input-group>.custom-file+.custom-select,.input-group>.custom-file+.form-control,.input-group>.custom-select+.custom-file,.input-group>.custom-select+.custom-select,.input-group>.custom-select+.form-control,.input-group>.form-control+.custom-file,.input-group>.form-control+.custom-select,.input-group>.form-control+.form-control{margin-left:-1px}.input-group>.custom-select:not(:last-child),.input-group>.form-control:not(:last-child){border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-select:not(:first-child),.input-group>.form-control:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.input-group>.custom-file{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.input-group>.custom-file:not(:last-child) .custom-file-label,.input-group>.custom-file:not(:last-child) .custom-file-label::before{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-file:not(:first-child) .custom-file-label,.input-group>.custom-file:not(:first-child) .custom-file-label::before{border-top-left-radius:0;border-bottom-left-radius:0}.input-group-append,.input-group-prepend{display:-webkit-box;display:-ms-flexbox;display:flex}.input-group-append .btn,.input-group-prepend .btn{position:relative;z-index:2}.input-group-append .btn+.btn,.input-group-append .btn+.input-group-text,.input-group-append .input-group-text+.btn,.input-group-append .input-group-text+.input-group-text,.input-group-prepend .btn+.btn,.input-group-prepend .btn+.input-group-text,.input-group-prepend .input-group-text+.btn,.input-group-prepend .input-group-text+.input-group-text{margin-left:-1px}.input-group-prepend{margin-right:-1px}.input-group-append{margin-left:-1px}.input-group-text{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:.375rem .75rem;margin-bottom:0;font-size:1rem;font-weight:400;line-height:1.5;color:#495057;text-align:center;white-space:nowrap;background-color:#e9ecef;border:1px solid #ced4da;border-radius:.25rem}.input-group-text input[type=checkbox],.input-group-text input[type=radio]{margin-top:0}.input-group>.input-group-append:last-child>.btn:not(:last-child):not(.dropdown-toggle),.input-group>.input-group-append:last-child>.input-group-text:not(:last-child),.input-group>.input-group-append:not(:last-child)>.btn,.input-group>.input-group-append:not(:last-child)>.input-group-text,.input-group>.input-group-prepend>.btn,.input-group>.input-group-prepend>.input-group-text{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.input-group-append>.btn,.input-group>.input-group-append>.input-group-text,.input-group>.input-group-prepend:first-child>.btn:not(:first-child),.input-group>.input-group-prepend:first-child>.input-group-text:not(:first-child),.input-group>.input-group-prepend:not(:first-child)>.btn,.input-group>.input-group-prepend:not(:first-child)>.input-group-text{border-top-left-radius:0;border-bottom-left-radius:0}.custom-control{position:relative;display:block;min-height:1.5rem;padding-left:1.5rem}.custom-control-inline{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;margin-right:1rem}.custom-control-input{position:absolute;z-index:-1;opacity:0}.custom-control-input:checked~.custom-control-label::before{color:#fff;background-color:#007bff}.custom-control-input:focus~.custom-control-label::before{box-shadow:0 0 0 1px #fff,0 0 0 .2rem rgba(0,123,255,.25)}.custom-control-input:active~.custom-control-label::before{color:#fff;background-color:#b3d7ff}.custom-control-input:disabled~.custom-control-label{color:#6c757d}.custom-control-input:disabled~.custom-control-label::before{background-color:#e9ecef}.custom-control-label{margin-bottom:0}.custom-control-label::before{position:absolute;top:.25rem;left:0;display:block;width:1rem;height:1rem;pointer-events:none;content:"";-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:#dee2e6}.custom-control-label::after{position:absolute;top:.25rem;left:0;display:block;width:1rem;height:1rem;content:"";background-repeat:no-repeat;background-position:center center;background-size:50% 50%}.custom-checkbox .custom-control-label::before{border-radius:.25rem}.custom-checkbox .custom-control-input:checked~.custom-control-label::before{background-color:#007bff}.custom-checkbox .custom-control-input:checked~.custom-control-label::after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E%3Cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::before{background-color:#007bff}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3E%3Cpath stroke='%23fff' d='M0 2h4'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:disabled:checked~.custom-control-label::before{background-color:rgba(0,123,255,.5)}.custom-checkbox .custom-control-input:disabled:indeterminate~.custom-control-label::before{background-color:rgba(0,123,255,.5)}.custom-radio .custom-control-label::before{border-radius:50%}.custom-radio .custom-control-input:checked~.custom-control-label::before{background-color:#007bff}.custom-radio .custom-control-input:checked~.custom-control-label::after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3E%3Ccircle r='3' fill='%23fff'/%3E%3C/svg%3E")}.custom-radio .custom-control-input:disabled:checked~.custom-control-label::before{background-color:rgba(0,123,255,.5)}.custom-select{display:inline-block;width:100%;height:calc(2.25rem + 2px);padding:.375rem 1.75rem .375rem .75rem;line-height:1.5;color:#495057;vertical-align:middle;background:#fff url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") no-repeat right .75rem center;background-size:8px 10px;border:1px solid #ced4da;border-radius:.25rem;-webkit-appearance:none;-moz-appearance:none;appearance:none}.custom-select:focus{border-color:#80bdff;outline:0;box-shadow:inset 0 1px 2px rgba(0,0,0,.075),0 0 5px rgba(128,189,255,.5)}.custom-select:focus::-ms-value{color:#495057;background-color:#fff}.custom-select[multiple],.custom-select[size]:not([size="1"]){height:auto;padding-right:.75rem;background-image:none}.custom-select:disabled{color:#6c757d;background-color: #3e556d}  .custom-select::-ms-expand{opacity:0}  .custom-select-sm{height:calc(1.8125rem + 2px);padding-top:.375rem;padding-bottom:.375rem;font-size:75%}  .custom-select-lg{height:calc(2.875rem + 2px);padding-top:.375rem;padding-bottom:.375rem;font-size:125%}  .custom-file{position:relative;display:inline-block;width:100%;height:calc(2.25rem + 2px);margin-bottom:0}  .custom-file-input{position:relative;z-index:2;width:100%;height:calc(2.25rem + 2px);margin:0;opacity:0}  .custom-file-input:focus~.custom-file-control{border-color:#80bdff;box-shadow:0 0 0 .2rem rgba(0,123,255,.25)}  .custom-file-input:focus~.custom-file-control::before{border-color:#80bdff}  .custom-file-input:lang(en)~.custom-file-label::after{content:"Browse"}  .custom-file-label{position:absolute;top:0;right:0;left:0;z-index:1;height:calc(2.25rem + 2px);padding:.375rem .75rem;line-height:1.5;color:#495057;background-color:#fff;border:1px solid #ced4da;border-radius:.25rem}  .custom-file-label::after{position:absolute;top:0;right:0;bottom:0;z-index:3;display:block;height:calc(calc(2.25rem + 2px) - 1px * 2);padding:.375rem .75rem;line-height:1.5;color:#495057;content:"Browse";background-color:#e9ecef;border-left:1px solid #ced4da;border-radius:0 .25rem .25rem 0}  .nav{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}  .nav-link{display:block;padding:.5rem 1rem}  .nav-link:focus,.nav-link:hover{text-decoration:none}  .nav-link.disabled{color:#6c757d}  .nav-tabs{border-bottom:1px solid #dee2e6}  .nav-tabs .nav-item{margin-bottom:-1px}  .nav-tabs .nav-link{border:1px solid transparent;border-top-left-radius:.25rem;border-top-right-radius:.25rem}  .nav-tabs .nav-link:focus,.nav-tabs .nav-link:hover{border-color:#e9ecef #e9ecef #dee2e6}  .nav-tabs .nav-link.disabled{color:#6c757d;background-color:transparent;border-color:transparent}  .nav-tabs .nav-item.show .nav-link,.nav-tabs .nav-link.active{color:#495057;background-color:#fff;border-color:#dee2e6 #dee2e6 #fff}  .nav-tabs .dropdown-menu{margin-top:-1px;border-top-left-radius:0;border-top-right-radius:0}  .nav-pills .nav-link{border-radius:.25rem}  .nav-pills .nav-link.active,.nav-pills .show>.nav-link{color:#fff;background-color:#007bff}  .nav-fill .nav-item{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;text-align:center}  .nav-justified .nav-item{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;text-align:center}  .tab-content>.tab-pane{display:none}  .tab-content>.active{display:block}  .navbar{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding:.5rem 1rem}  .navbar>.container,.navbar>.container-fluid{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}  .navbar-brand{display:inline-block;padding-top:.3125rem;padding-bottom:.3125rem;margin-right:1rem;font-size:1.25rem;line-height:inherit;white-space:nowrap}  .navbar-brand:focus,.navbar-brand:hover{text-decoration:none}  .navbar-nav{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}  .navbar-nav .nav-link{padding-right:0;padding-left:0}  .navbar-nav .dropdown-menu{position:static;float:none}  .navbar-text{display:inline-block;padding-top:.5rem;padding-bottom:.5rem}  .navbar-collapse{-ms-flex-preferred-size:100%;flex-basis:100%;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-align:center;-ms-flex-align:center;align-items:center}  .navbar-toggler{padding:.25rem .75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:.25rem}  .navbar-toggler:focus,.navbar-toggler:hover{text-decoration:none}  .navbar-toggler:not(:disabled):not(.disabled){cursor:pointer}  .navbar-toggler-icon{display:inline-block;width:1.5em;height:1.5em;vertical-align:middle;content:"";background:no-repeat center center;background-size:100% 100%}@media (max-width:575.98px){.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:576px){.navbar-expand-sm{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}  .navbar-expand-sm .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}  .navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}  .navbar-expand-sm .navbar-nav .dropdown-menu-right{right:0;left:auto}  .navbar-expand-sm .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}  .navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}  .navbar-expand-sm .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}  .navbar-expand-sm .navbar-toggler{display:none}  .navbar-expand-sm .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:767.98px){.navbar-expand-md>.container,.navbar-expand-md>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:768px){.navbar-expand-md{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}  .navbar-expand-md .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}  .navbar-expand-md .navbar-nav .dropdown-menu{position:absolute}  .navbar-expand-md .navbar-nav .dropdown-menu-right{right:0;left:auto}  .navbar-expand-md .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}  .navbar-expand-md>.container,.navbar-expand-md>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}  .navbar-expand-md .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}  .navbar-expand-md .navbar-toggler{display:none}  .navbar-expand-md .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:991.98px){.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:992px){.navbar-expand-lg{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}  .navbar-expand-lg .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}  .navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}  .navbar-expand-lg .navbar-nav .dropdown-menu-right{right:0;left:auto}  .navbar-expand-lg .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}  .navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}  .navbar-expand-lg .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}  .navbar-expand-lg .navbar-toggler{display:none}  .navbar-expand-lg .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:1199.98px){.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:1200px){.navbar-expand-xl{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}  .navbar-expand-xl .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}  .navbar-expand-xl .navbar-nav .dropdown-menu{position:absolute}  .navbar-expand-xl .navbar-nav .dropdown-menu-right{right:0;left:auto}  .navbar-expand-xl .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}  .navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}  .navbar-expand-xl .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}  .navbar-expand-xl .navbar-toggler{display:none}  .navbar-expand-xl .dropup .dropdown-menu{top:auto;bottom:100%}}  .navbar-expand{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}  .navbar-expand>.container,.navbar-expand>.container-fluid{padding-right:0;padding-left:0}  .navbar-expand .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}  .navbar-expand .navbar-nav .dropdown-menu{position:absolute}  .navbar-expand .navbar-nav .dropdown-menu-right{right:0;left:auto}  .navbar-expand .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}  .navbar-expand>.container,.navbar-expand>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}  .navbar-expand .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}  .navbar-expand .navbar-toggler{display:none}  .navbar-expand .dropup .dropdown-menu{top:auto;bottom:100%}  .navbar-light .navbar-brand{color:rgba(0,0,0,.9)}  .navbar-light .navbar-brand:focus,.navbar-light .navbar-brand:hover{color:rgba(0,0,0,.9)}  .navbar-light .navbar-nav .nav-link{color:rgba(0,0,0,.5)}  .navbar-light .navbar-nav .nav-link:focus,.navbar-light .navbar-nav .nav-link:hover{color:rgba(0,0,0,.7)}  .navbar-light .navbar-nav .nav-link.disabled{color:rgba(0,0,0,.3)}  .navbar-light .navbar-nav .active>.nav-link,.navbar-light .navbar-nav .nav-link.active,.navbar-light .navbar-nav .nav-link.show,.navbar-light .navbar-nav .show>.nav-link{color:rgba(0,0,0,.9)}  .navbar-light .navbar-toggler{color:rgba(0,0,0,.5);border-color:rgba(0,0,0,.1)}  .navbar-light .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}  .navbar-light .navbar-text{color:rgba(0,0,0,.5)}  .navbar-light .navbar-text a{color:rgba(0,0,0,.9)}  .navbar-light .navbar-text a:focus,.navbar-light .navbar-text a:hover{color:rgba(0,0,0,.9)}  .navbar-dark .navbar-brand{color:#fff}  .navbar-dark .navbar-brand:focus,.navbar-dark .navbar-brand:hover{color:#fff}  .navbar-dark .navbar-nav .nav-link{color:rgba(255,255,255,.5)}  .navbar-dark .navbar-nav .nav-link:focus,.navbar-dark .navbar-nav .nav-link:hover{color:rgba(255,255,255,.75)}  .navbar-dark .navbar-nav .nav-link.disabled{color:rgba(255,255,255,.25)}  .navbar-dark .navbar-nav .active>.nav-link,.navbar-dark .navbar-nav .nav-link.active,.navbar-dark .navbar-nav .nav-link.show,.navbar-dark .navbar-nav .show>.nav-link{color:#fff}  .navbar-dark .navbar-toggler{color:rgba(255,255,255,.5);border-color:rgba(255,255,255,.1)}  .navbar-dark .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}  .navbar-dark .navbar-text{color:rgba(255,255,255,.5)}  .navbar-dark .navbar-text a{color:#fff}  .navbar-dark .navbar-text a:focus,.navbar-dark .navbar-text a:hover{color:#fff}  .card{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;min-width:0;word-wrap:break-word;background-color:#fff;background-clip:border-box;border:1px solid rgba(0,0,0,.125);border-radius:.25rem}  .card>hr{margin-right:0;margin-left:0}  .card>.list-group:first-child .list-group-item:first-child{border-top-left-radius:.25rem;border-top-right-radius:.25rem}  .card>.list-group:last-child .list-group-item:last-child{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}  .card-body{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;padding:1.25rem}  .card-title{margin-bottom:.75rem}  .card-subtitle{margin-top:-.375rem;margin-bottom:0}  .card-text:last-child{margin-bottom:0}  .card-link:hover{text-decoration:none}  .card-link+.card-link{margin-left:1.25rem}  .card-header{padding:.75rem 1.25rem;margin-bottom:0;background-color:rgba(0,0,0,.03);border-bottom:1px solid rgba(0,0,0,.125)}  .card-header:first-child{border-radius:calc(.25rem - 1px) calc(.25rem - 1px) 0 0}  .card-header+.list-group .list-group-item:first-child{border-top:0}  .card-footer{padding:.75rem 1.25rem;background-color:rgba(0,0,0,.03);border-top:1px solid rgba(0,0,0,.125)}  .card-footer:last-child{border-radius:0 0 calc(.25rem - 1px) calc(.25rem - 1px)}  .card-header-tabs{margin-right:-.625rem;margin-bottom:-.75rem;margin-left:-.625rem;border-bottom:0}  .card-header-pills{margin-right:-.625rem;margin-left:-.625rem}  .card-img-overlay{position:absolute;top:0;right:0;bottom:0;left:0;padding:1.25rem}  .card-img{width:100%;border-radius:calc(.25rem - 1px)}  .card-img-top{width:100%;border-top-left-radius:calc(.25rem - 1px);border-top-right-radius:calc(.25rem - 1px)}  .card-img-bottom{width:100%;border-bottom-right-radius:calc(.25rem - 1px);border-bottom-left-radius:calc(.25rem - 1px)}  .card-deck{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}  .card-deck .card{margin-bottom:15px}@media (min-width:576px){.card-deck{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap;margin-right:-15px;margin-left:-15px}  .card-deck .card{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-flex:1;-ms-flex:1 0 0%;flex:1 0 0%;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;margin-right:15px;margin-bottom:0;margin-left:15px}}  .card-group{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}  .card-group>.card{margin-bottom:15px}@media (min-width:576px){.card-group{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap}  .card-group>.card{-webkit-box-flex:1;-ms-flex:1 0 0%;flex:1 0 0%;margin-bottom:0}  .card-group>.card+.card{margin-left:0;border-left:0}  .card-group>.card:first-child{border-top-right-radius:0;border-bottom-right-radius:0}  .card-group>.card:first-child .card-header,.card-group>.card:first-child .card-img-top{border-top-right-radius:0}  .card-group>.card:first-child .card-footer,.card-group>.card:first-child .card-img-bottom{border-bottom-right-radius:0}  .card-group>.card:last-child{border-top-left-radius:0;border-bottom-left-radius:0}  .card-group>.card:last-child .card-header,.card-group>.card:last-child .card-img-top{border-top-left-radius:0}  .card-group>.card:last-child .card-footer,.card-group>.card:last-child .card-img-bottom{border-bottom-left-radius:0}  .card-group>.card:only-child{border-radius:.25rem}  .card-group>.card:only-child .card-header,.card-group>.card:only-child .card-img-top{border-top-left-radius:.25rem;border-top-right-radius:.25rem}  .card-group>.card:only-child .card-footer,.card-group>.card:only-child .card-img-bottom{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}  .card-group>.card:not(:first-child):not(:last-child):not(:only-child){border-radius:0}  .card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-footer,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-header,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-top{border-radius:0}}  .card-columns .card{margin-bottom:.75rem}@media (min-width:576px){.card-columns{-webkit-column-count:3;-moz-column-count:3;column-count:3;-webkit-column-gap:1.25rem;-moz-column-gap:1.25rem;column-gap:1.25rem}  .card-columns .card{display:inline-block;width:100%}}  .breadcrumb{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;padding:.75rem 1rem;margin-bottom:1rem;list-style:none;background-color:#e9ecef;border-radius:.25rem}  .breadcrumb-item+.breadcrumb-item::before{display:inline-block;padding-right:.5rem;padding-left:.5rem;color:#6c757d;content:"/"}  .breadcrumb-item+.breadcrumb-item:hover::before{text-decoration:underline}  .breadcrumb-item+.breadcrumb-item:hover::before{text-decoration:none}  .breadcrumb-item.active{color:#6c757d}  .pagination{display:-webkit-box;display:-ms-flexbox;display:flex;padding-left:0;list-style:none;border-radius:.25rem}  .page-link{position:relative;display:block;padding:.5rem .75rem;margin-left:-1px;line-height:1.25;color:#007bff;background-color:#fff;border:1px solid #dee2e6}  .page-link:hover{color:#0056b3;text-decoration:none;background-color:#e9ecef;border-color:#dee2e6}  .page-link:focus{z-index:2;outline:0;box-shadow:0 0 0 .2rem rgba(0,123,255,.25)}  .page-link:not(:disabled):not(.disabled){cursor:pointer}  .page-item:first-child .page-link{margin-left:0;border-top-left-radius:.25rem;border-bottom-left-radius:.25rem}  .page-item:last-child .page-link{border-top-right-radius:.25rem;border-bottom-right-radius:.25rem}  .page-item.active .page-link{z-index:1;color:#fff;background-color:#007bff;border-color:#007bff}  .page-item.disabled .page-link{color:#6c757d;pointer-events:none;cursor:auto;background-color:#fff;border-color:#dee2e6}  .pagination-lg .page-link{padding:.75rem 1.5rem;font-size:1.25rem;line-height:1.5}  .pagination-lg .page-item:first-child .page-link{border-top-left-radius:.3rem;border-bottom-left-radius:.3rem}  .pagination-lg .page-item:last-child .page-link{border-top-right-radius:.3rem;border-bottom-right-radius:.3rem}  .pagination-sm .page-link{padding:.25rem .5rem;font-size:.875rem;line-height:1.5}  .pagination-sm .page-item:first-child .page-link{border-top-left-radius:.2rem;border-bottom-left-radius:.2rem}  .pagination-sm .page-item:last-child .page-link{border-top-right-radius:.2rem;border-bottom-right-radius:.2rem}  .badge{display:inline-block;padding:.25em .4em;font-size:75%;font-weight:700;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25rem}  .badge:empty{display:none}  .btn .badge{position:relative;top:-1px}  .badge-pill{padding-right:.6em;padding-left:.6em;border-radius:10rem}  .badge-primary{color:#fff;background-color:#007bff}  .badge-primary[href]:focus,.badge-primary[href]:hover{color:#fff;text-decoration:none;background-color:#0062cc}  .badge-secondary{color:#fff;background-color:#6c757d}  .badge-secondary[href]:focus,.badge-secondary[href]:hover{color:#fff;text-decoration:none;background-color:#545b62}  .badge-success{color:#fff;background-color:#28a745}  .badge-success[href]:focus,.badge-success[href]:hover{color:#fff;text-decoration:none;background-color:#1e7e34}  .badge-info{color:#fff;background-color:#17a2b8}  .badge-info[href]:focus,.badge-info[href]:hover{color:#fff;text-decoration:none;background-color:#117a8b}  .badge-warning{color:#212529;background-color:#ffc107}  .badge-warning[href]:focus,.badge-warning[href]:hover{color:#212529;text-decoration:none;background-color:#d39e00}  .badge-danger{color:#fff;background-color:#dc3545}  .badge-danger[href]:focus,.badge-danger[href]:hover{color:#fff;text-decoration:none;background-color:#bd2130}  .badge-light{color:#212529;background-color:#f8f9fa}  .badge-light[href]:focus,.badge-light[href]:hover{color:#212529;text-decoration:none;background-color:#dae0e5}  .badge-dark{color:#fff;background-color:#343a40}  .badge-dark[href]:focus,.badge-dark[href]:hover{color:#fff;text-decoration:none;background-color:#1d2124}  .jumbotron{padding:2rem 1rem;margin-bottom:2rem;background-color:#e9ecef;border-radius:.3rem}@media (min-width:576px){.jumbotron{padding:4rem 2rem}}  .jumbotron-fluid{padding-right:0;padding-left:0;border-radius:0}  .alert{position:relative;padding:.75rem 1.25rem;margin-bottom:1rem;border:1px solid transparent;border-radius:.25rem}  .alert-heading{color:inherit}  .alert-link{font-weight:700}  .alert-dismissible{padding-right:4rem}  .alert-dismissible .close{position:absolute;top:0;right:0;padding:.75rem 1.25rem;color:inherit}  .alert-primary{color:#004085;background-color:#cce5ff;border-color:#b8daff}  .alert-primary hr{border-top-color:#9fcdff}  .alert-primary .alert-link{color:#002752}  .alert-secondary{color:#383d41;background-color:#e2e3e5;border-color:#d6d8db}  .alert-secondary hr{border-top-color:#c8cbcf}  .alert-secondary .alert-link{color:#202326}  .alert-success{color:#155724;background-color:#d4edda;border-color:#c3e6cb}  .alert-success hr{border-top-color:#b1dfbb}  .alert-success .alert-link{color:#0b2e13}  .alert-info{color:#0c5460;background-color:#d1ecf1;border-color:#bee5eb}  .alert-info hr{border-top-color:#abdde5}  .alert-info .alert-link{color:#062c33}  .alert-warning{color:#856404;background-color:#fff3cd;border-color:#ffeeba}  .alert-warning hr{border-top-color:#ffe8a1}  .alert-warning .alert-link{color:#533f03}  .alert-danger{color:#721c24;background-color:#f8d7da;border-color:#f5c6cb}  .alert-danger hr{border-top-color:#f1b0b7}  .alert-danger .alert-link{color:#491217}  .alert-light{color:#818182;background-color:#fefefe;border-color:#fdfdfe}  .alert-light hr{border-top-color:#ececf6}  .alert-light .alert-link{color:#686868}  .alert-dark{color:#1b1e21;background-color:#d6d8d9;border-color:#c6c8ca}  .alert-dark hr{border-top-color:#b9bbbe}  .alert-dark .alert-link{color:#040505}  @-webkit-keyframes progress-bar-stripes{from{background-position:1rem 0} to{background-position:0 0}}  @keyframes progress-bar-stripes{from{background-position:1rem 0} to{background-position:0 0}}  .progress{display:-webkit-box;display:-ms-flexbox;display:flex;height:1rem;overflow:hidden;font-size:.75rem;background-color:#e9ecef;border-radius:.25rem}  .progress-bar{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;color:#fff;text-align:center;background-color:#007bff;transition:width .6s ease}  .progress-bar-striped{background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-size:1rem 1rem}  .progress-bar-animated{-webkit-animation:progress-bar-stripes 1s linear infinite;animation:progress-bar-stripes 1s linear infinite}  .media{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start}  .media-body{-webkit-box-flex:1;-ms-flex:1;flex:1}  .list-group{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-left:0;margin-bottom:0}  .list-group-item-action{width:100%;color:#495057;text-align:inherit}  .list-group-item-action:focus,.list-group-item-action:hover{color:#495057;text-decoration:none;background-color:#f8f9fa}  .list-group-item-action:active{color:#212529;background-color:#e9ecef}  .list-group-item{position:relative;display:block;padding:.75rem 1.25rem;margin-bottom:-1px;background-color:#fff;border:1px solid rgba(0,0,0,.125)}  .list-group-item:first-child{border-top-left-radius:.25rem;border-top-right-radius:.25rem}  .list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}  .list-group-item:focus,.list-group-item:hover{z-index:1;text-decoration:none}  .list-group-item.disabled,.list-group-item:disabled{color:#6c757d;background-color:#fff}  .list-group-item.active{z-index:2;color:#fff;background-color:#007bff;border-color:#007bff}  .list-group-flush .list-group-item{border-right:0;border-left:0;border-radius:0}  .list-group-flush:first-child .list-group-item:first-child{border-top:0}  .list-group-flush:last-child .list-group-item:last-child{border-bottom:0}  .list-group-item-primary{color:#004085;background-color:#b8daff}  .list-group-item-primary.list-group-item-action:focus,.list-group-item-primary.list-group-item-action:hover{color:#004085;background-color:#9fcdff}  .list-group-item-primary.list-group-item-action.active{color:#fff;background-color:#004085;border-color:#004085}  .list-group-item-secondary{color:#383d41;background-color:#d6d8db}  .list-group-item-secondary.list-group-item-action:focus,.list-group-item-secondary.list-group-item-action:hover{color:#383d41;background-color:#c8cbcf}  .list-group-item-secondary.list-group-item-action.active{color:#fff;background-color:#383d41;border-color:#383d41}  .list-group-item-success{color:#155724;background-color:#c3e6cb}  .list-group-item-success.list-group-item-action:focus,.list-group-item-success.list-group-item-action:hover{color:#155724;background-color:#b1dfbb}  .list-group-item-success.list-group-item-action.active{color:#fff;background-color:#155724;border-color:#155724}  .list-group-item-info{color:#0c5460;background-color:#bee5eb}  .list-group-item-info.list-group-item-action:focus,.list-group-item-info.list-group-item-action:hover{color:#0c5460;background-color:#abdde5}  .list-group-item-info.list-group-item-action.active{color:#fff;background-color:#0c5460;border-color:#0c5460}  .list-group-item-warning{color:#856404;background-color:#ffeeba}  .list-group-item-warning.list-group-item-action:focus,.list-group-item-warning.list-group-item-action:hover{color:#856404;background-color:#ffe8a1}  .list-group-item-warning.list-group-item-action.active{color:#fff;background-color:#856404;border-color:#856404}  .list-group-item-danger{color:#721c24;background-color:#f5c6cb}  .list-group-item-danger.list-group-item-action:focus,.list-group-item-danger.list-group-item-action:hover{color:#721c24;background-color:#f1b0b7}  .list-group-item-danger.list-group-item-action.active{color:#fff;background-color:#721c24;border-color:#721c24}  .list-group-item-light{color:#818182;background-color:#fdfdfe}  .list-group-item-light.list-group-item-action:focus,.list-group-item-light.list-group-item-action:hover{color:#818182;background-color:#ececf6}  .list-group-item-light.list-group-item-action.active{color:#fff;background-color:#818182;border-color:#818182}  .list-group-item-dark{color:#1b1e21;background-color:#c6c8ca}  .list-group-item-dark.list-group-item-action:focus,.list-group-item-dark.list-group-item-action:hover{color:#1b1e21;background-color:#b9bbbe}  .list-group-item-dark.list-group-item-action.active{color:#fff;background-color:#1b1e21;border-color:#1b1e21}  .close{float:right;font-size:1.5rem;font-weight:700;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.5}  .close:focus,.close:hover{color:#000;text-decoration:none;opacity:.75}  .close:not(:disabled):not(.disabled){cursor:pointer}  button.close{padding:0;background-color:transparent;border:0;-webkit-appearance:none}  .modal-open{overflow:hidden}  .modal{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;display:none;overflow:hidden;outline:0}  .modal-open .modal{overflow-x:hidden;overflow-y:auto}  .modal-dialog{position:relative;width:auto;margin:.5rem;pointer-events:none}  .modal.fade .modal-dialog{transition:-webkit-transform .3s ease-out;transition:transform .3s ease-out;transition:transform .3s ease-out,-webkit-transform .3s ease-out;-webkit-transform:translate(0,-25%);transform:translate(0,-25%)}  .modal.show .modal-dialog{-webkit-transform:translate(0,0);transform:translate(0,0)}  .modal-dialog-centered{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;min-height:calc(100% - (.5rem * 2))}  .modal-content{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;width:100%;pointer-events:auto;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem;outline:0}  .modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}  .modal-backdrop.fade{opacity:0}  .modal-backdrop.show{opacity:.5}  .modal-header{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding:1rem;border-bottom:1px solid #e9ecef;border-top-left-radius:.3rem;border-top-right-radius:.3rem}  .modal-header .close{padding:1rem;margin:-1rem -1rem -1rem auto}  .modal-title{margin-bottom:0;line-height:1.5}  .modal-body{position:relative;-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;padding:1rem}  .modal-footer{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end;padding:1rem;border-top:1px solid #e9ecef}  .modal-footer>:not(:first-child){margin-left:.25rem}  .modal-footer>:not(:last-child){margin-right:.25rem}  .modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:576px){.modal-dialog{max-width:500px;margin:1.75rem auto}  .modal-dialog-centered{min-height:calc(100% - (1.75rem * 2))}  .modal-sm{max-width:300px}}@media (min-width:992px){.modal-lg{max-width:800px}}  .tooltip{position:absolute;z-index:1070;display:block;margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;font-size:.875rem;word-wrap:break-word;opacity:0}  .tooltip.show{opacity:.9}  .tooltip .arrow{position:absolute;display:block;width:.8rem;height:.4rem}  .tooltip .arrow::before{position:absolute;content:"";border-color:transparent;border-style:solid}  .bs-tooltip-auto[x-placement^=top],.bs-tooltip-top{padding:.4rem 0}  .bs-tooltip-auto[x-placement^=top] .arrow,.bs-tooltip-top .arrow{bottom:0}  .bs-tooltip-auto[x-placement^=top] .arrow::before,.bs-tooltip-top .arrow::before{top:0;border-width:.4rem .4rem 0;border-top-color:#000}  .bs-tooltip-auto[x-placement^=right],.bs-tooltip-right{padding:0 .4rem}  .bs-tooltip-auto[x-placement^=right] .arrow,.bs-tooltip-right .arrow{left:0;width:.4rem;height:.8rem}  .bs-tooltip-auto[x-placement^=right] .arrow::before,.bs-tooltip-right .arrow::before{right:0;border-width:.4rem .4rem .4rem 0;border-right-color:#000}  .bs-tooltip-auto[x-placement^=bottom],.bs-tooltip-bottom{padding:.4rem 0}  .bs-tooltip-auto[x-placement^=bottom] .arrow,.bs-tooltip-bottom .arrow{top:0}  .bs-tooltip-auto[x-placement^=bottom] .arrow::before,.bs-tooltip-bottom .arrow::before{bottom:0;border-width:0 .4rem .4rem;border-bottom-color:#000}  .bs-tooltip-auto[x-placement^=left],.bs-tooltip-left{padding:0 .4rem}  .bs-tooltip-auto[x-placement^=left] .arrow,.bs-tooltip-left .arrow{right:0;width:.4rem;height:.8rem}  .bs-tooltip-auto[x-placement^=left] .arrow::before,.bs-tooltip-left .arrow::before{left:0;border-width:.4rem 0 .4rem .4rem;border-left-color:#000}  .tooltip-inner{max-width:200px;padding:.25rem .5rem;color:#fff;text-align:center;background-color:#000;border-radius:.25rem}  .popover{position:absolute;top:0;left:0;z-index:1060;display:block;max-width:276px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;font-size:.875rem;word-wrap:break-word;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem}  .popover .arrow{position:absolute;display:block;width:1rem;height:.5rem;margin:0 .3rem}  .popover .arrow::after,.popover .arrow::before{position:absolute;display:block;content:"";border-color:transparent;border-style:solid}  .bs-popover-auto[x-placement^=top],.bs-popover-top{margin-bottom:.5rem}  .bs-popover-auto[x-placement^=top] .arrow,.bs-popover-top .arrow{bottom:calc((.5rem + 1px) * -1)}  .bs-popover-auto[x-placement^=top] .arrow::after,.bs-popover-auto[x-placement^=top] .arrow::before,.bs-popover-top .arrow::after,.bs-popover-top .arrow::before{border-width:.5rem .5rem 0}  .bs-popover-auto[x-placement^=top] .arrow::before,.bs-popover-top .arrow::before{bottom:0;border-top-color:rgba(0,0,0,.25)}  .bs-popover-auto[x-placement^=top] .arrow::after,.bs-popover-top .arrow::after{bottom:1px;border-top-color:#fff}  .bs-popover-auto[x-placement^=right],.bs-popover-right{margin-left:.5rem}  .bs-popover-auto[x-placement^=right] .arrow,.bs-popover-right .arrow{left:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}  .bs-popover-auto[x-placement^=right] .arrow::after,.bs-popover-auto[x-placement^=right] .arrow::before,.bs-popover-right .arrow::after,.bs-popover-right .arrow::before{border-width:.5rem .5rem .5rem 0}  .bs-popover-auto[x-placement^=right] .arrow::before,.bs-popover-right .arrow::before{left:0;border-right-color:rgba(0,0,0,.25)}  .bs-popover-auto[x-placement^=right] .arrow::after,.bs-popover-right .arrow::after{left:1px;border-right-color:#fff}  .bs-popover-auto[x-placement^=bottom],.bs-popover-bottom{margin-top:.5rem}  .bs-popover-auto[x-placement^=bottom] .arrow,.bs-popover-bottom .arrow{top:calc((.5rem + 1px) * -1)}  .bs-popover-auto[x-placement^=bottom] .arrow::after,.bs-popover-auto[x-placement^=bottom] .arrow::before,.bs-popover-bottom .arrow::after,.bs-popover-bottom .arrow::before{border-width:0 .5rem .5rem .5rem}  .bs-popover-auto[x-placement^=bottom] .arrow::before,.bs-popover-bottom .arrow::before{top:0;border-bottom-color:rgba(0,0,0,.25)}  .bs-popover-auto[x-placement^=bottom] .arrow::after,.bs-popover-bottom .arrow::after{top:1px;border-bottom-color:#fff}  .bs-popover-auto[x-placement^=bottom] .popover-header::before,.bs-popover-bottom .popover-header::before{position:absolute;top:0;left:50%;display:block;width:1rem;margin-left:-.5rem;content:"";border-bottom:1px solid #f7f7f7}  .bs-popover-auto[x-placement^=left],.bs-popover-left{margin-right:.5rem}  .bs-popover-auto[x-placement^=left] .arrow,.bs-popover-left .arrow{right:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}  .bs-popover-auto[x-placement^=left] .arrow::after,.bs-popover-auto[x-placement^=left] .arrow::before,.bs-popover-left .arrow::after,.bs-popover-left .arrow::before{border-width:.5rem 0 .5rem .5rem}  .bs-popover-auto[x-placement^=left] .arrow::before,.bs-popover-left .arrow::before{right:0;border-left-color:rgba(0,0,0,.25)}  .bs-popover-auto[x-placement^=left] .arrow::after,.bs-popover-left .arrow::after{right:1px;border-left-color:#fff}  .popover-header{padding:.5rem .75rem;margin-bottom:0;font-size:1rem;color:inherit;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-top-left-radius:calc(.3rem - 1px);border-top-right-radius:calc(.3rem - 1px)}  .popover-header:empty{display:none}  .popover-body{padding:.5rem .75rem;color:#212529}  .carousel{position:relative}  .carousel-inner{position:relative;width:100%;overflow:hidden}  .carousel-item{position:relative;display:none;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:100%;transition:-webkit-transform .6s ease;transition:transform .6s ease;transition:transform .6s ease,-webkit-transform .6s ease;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-perspective:1000px;perspective:1000px}  .carousel-item-next,.carousel-item-prev,.carousel-item.active{display:block}  .carousel-item-next,.carousel-item-prev{position:absolute;top:0}  .carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{-webkit-transform:translateX(0);transform:translateX(0)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)}}  .active.carousel-item-right,.carousel-item-next{-webkit-transform:translateX(100%);transform:translateX(100%)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.active.carousel-item-right,.carousel-item-next{-webkit-transform:translate3d(100%,0,0);transform:translate3d(100%,0,0)}}  .active.carousel-item-left,.carousel-item-prev{-webkit-transform:translateX(-100%);transform:translateX(-100%)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.active.carousel-item-left,.carousel-item-prev{-webkit-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0)}}  .carousel-control-next,.carousel-control-prev{position:absolute;top:0;bottom:0;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:15%;color:#fff;text-align:center;opacity:.5}  .carousel-control-next:focus,.carousel-control-next:hover,.carousel-control-prev:focus,.carousel-control-prev:hover{color:#fff;text-decoration:none;outline:0;opacity:.9}  .carousel-control-prev{left:0}  .carousel-control-next{right:0}  .carousel-control-next-icon,.carousel-control-prev-icon{display:inline-block;width:20px;height:20px;background:transparent no-repeat center center;background-size:100% 100%}  .carousel-control-prev-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E")}  .carousel-control-next-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E")}  .carousel-indicators{position:absolute;right:0;bottom:10px;left:0;z-index:15;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;padding-left:0;margin-right:15%;margin-left:15%;list-style:none}  .carousel-indicators li{position:relative;-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto;width:30px;height:3px;margin-right:3px;margin-left:3px;text-indent:-999px;background-color:rgba(255,255,255,.5)}  .carousel-indicators li::before{position:absolute;top:-10px;left:0;display:inline-block;width:100%;height:10px;content:""}  .carousel-indicators li::after{position:absolute;bottom:-10px;left:0;display:inline-block;width:100%;height:10px;content:""}  .carousel-indicators .active{background-color:#fff}  .carousel-caption{position:absolute;right:15%;bottom:20px;left:15%;z-index:10;padding-top:20px;padding-bottom:20px;color:#fff;text-align:center}  .align-baseline{vertical-align:baseline!important}  .align-top{vertical-align:top!important}  .align-middle{vertical-align:middle!important}  .align-bottom{vertical-align:bottom!important}  .align-text-bottom{vertical-align:text-bottom!important}  .align-text-top{vertical-align:text-top!important}  .bg-primary{background-color:#007bff!important}  a.bg-primary:focus,a.bg-primary:hover,button.bg-primary:focus,button.bg-primary:hover{background-color:#0062cc!important}  .bg-secondary{background-color:#6c757d!important}  a.bg-secondary:focus,a.bg-secondary:hover,button.bg-secondary:focus,button.bg-secondary:hover{background-color:#545b62!important}  .bg-success{background-color:#28a745!important}  a.bg-success:focus,a.bg-success:hover,button.bg-success:focus,button.bg-success:hover{background-color:#1e7e34!important}  .bg-info{background-color:#17a2b8!important}  a.bg-info:focus,a.bg-info:hover,button.bg-info:focus,button.bg-info:hover{background-color:#117a8b!important}  .bg-warning{background-color:#ffc107!important}  a.bg-warning:focus,a.bg-warning:hover,button.bg-warning:focus,button.bg-warning:hover{background-color:#d39e00!important}  .bg-danger{background-color:#dc3545!important}  a.bg-danger:focus,a.bg-danger:hover,button.bg-danger:focus,button.bg-danger:hover{background-color:#bd2130!important}  .bg-light{background-color:#f8f9fa!important}  a.bg-light:focus,a.bg-light:hover,button.bg-light:focus,button.bg-light:hover{background-color:#dae0e5!important}  .bg-dark{background-color:#343a40!important}  a.bg-dark:focus,a.bg-dark:hover,button.bg-dark:focus,button.bg-dark:hover{background-color:#1d2124!important}  .bg-white{background-color:#fff!important}  .bg-transparent{background-color:transparent!important}  .border{border:1px solid #dee2e6!important}  .border-top{border-top:1px solid #dee2e6!important}  .border-right{border-right:1px solid #dee2e6!important}  .border-bottom{border-bottom:1px solid #dee2e6!important}  .border-left{border-left:1px solid #dee2e6!important}  .border-0{border:0!important}  .border-top-0{border-top:0!important}  .border-right-0{border-right:0!important}  .border-bottom-0{border-bottom:0!important}  .border-left-0{border-left:0!important}  .border-primary{border-color:#007bff!important}  .border-secondary{border-color:#6c757d!important}  .border-success{border-color:#28a745!important}  .border-info{border-color:#17a2b8!important}  .border-warning{border-color:#ffc107!important}  .border-danger{border-color:#dc3545!important}  .border-light{border-color:#f8f9fa!important}  .border-dark{border-color:#343a40!important}  .border-white{border-color:#fff!important}  .rounded{border-radius:.25rem!important}  .rounded-top{border-top-left-radius:.25rem!important;border-top-right-radius:.25rem!important}  .rounded-right{border-top-right-radius:.25rem!important;border-bottom-right-radius:.25rem!important}  .rounded-bottom{border-bottom-right-radius:.25rem!important;border-bottom-left-radius:.25rem!important}  .rounded-left{border-top-left-radius:.25rem!important;border-bottom-left-radius:.25rem!important}  .rounded-circle{border-radius:50%!important}  .rounded-0{border-radius:0!important}  .clearfix::after{display:block;clear:both;content:""}  .d-none{display:none!important}  .d-inline{display:inline!important}  .d-inline-block{display:inline-block!important}  .d-block{display:block!important}  .d-table{display:table!important}  .d-table-row{display:table-row!important}  .d-table-cell{display:table-cell!important}  .d-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}@media (min-width:576px){.d-sm-none{display:none!important}  .d-sm-inline{display:inline!important}  .d-sm-inline-block{display:inline-block!important}  .d-sm-block{display:block!important}  .d-sm-table{display:table!important}  .d-sm-table-row{display:table-row!important}  .d-sm-table-cell{display:table-cell!important}  .d-sm-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-sm-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:768px){.d-md-none{display:none!important}  .d-md-inline{display:inline!important}  .d-md-inline-block{display:inline-block!important}  .d-md-block{display:block!important}  .d-md-table{display:table!important}  .d-md-table-row{display:table-row!important}  .d-md-table-cell{display:table-cell!important}  .d-md-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-md-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:992px){.d-lg-none{display:none!important}  .d-lg-inline{display:inline!important}  .d-lg-inline-block{display:inline-block!important}  .d-lg-block{display:block!important}  .d-lg-table{display:table!important}  .d-lg-table-row{display:table-row!important}  .d-lg-table-cell{display:table-cell!important}  .d-lg-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-lg-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:1200px){.d-xl-none{display:none!important}  .d-xl-inline{display:inline!important}  .d-xl-inline-block{display:inline-block!important}  .d-xl-block{display:block!important}  .d-xl-table{display:table!important}  .d-xl-table-row{display:table-row!important}  .d-xl-table-cell{display:table-cell!important}  .d-xl-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-xl-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media print{.d-print-none{display:none!important}  .d-print-inline{display:inline!important}  .d-print-inline-block{display:inline-block!important}  .d-print-block{display:block!important}  .d-print-table{display:table!important}  .d-print-table-row{display:table-row!important}  .d-print-table-cell{display:table-cell!important}  .d-print-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}  .d-print-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}  .embed-responsive{position:relative;display:block;width:100%;padding:0;overflow:hidden}  .embed-responsive::before{display:block;content:""}  .embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;bottom:0;left:0;width:100%;height:100%;border:0}  .embed-responsive-21by9::before{padding-top:42.857143%}  .embed-responsive-16by9::before{padding-top:56.25%}  .embed-responsive-4by3::before{padding-top:75%}  .embed-responsive-1by1::before{padding-top:100%}  .flex-row{-webkit-box-orient:horizontal!important;-webkit-box-direction:normal!important;-ms-flex-direction:row!important;flex-direction:row!important}  .flex-column{-webkit-box-orient:vertical!important;-webkit-box-direction:normal!important;-ms-flex-direction:column!important;flex-direction:column!important}  .flex-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}  .flex-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}  .flex-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}  .flex-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}  .flex-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}  .justify-content-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}  .justify-content-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}  .justify-content-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}  .justify-content-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}  .justify-content-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}  .align-items-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}  .align-items-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}  .align-items-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}  .align-items-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}  .align-items-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}  .align-content-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}  .align-content-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}  .align-content-center{-ms-flex-line-pack:center!important;align-content:center!important}  .align-content-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}  .align-content-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}  .align-content-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}  .align-self-auto{-ms-flex-item-align:auto!important;align-self:auto!important}  .align-self-start{-ms-flex-item-align:start!important;align-self:flex-start!important}  .align-self-end{-ms-flex-item-align:end!important;align-self:flex-end!important}  .align-self-center{-ms-flex-item-align:center!important;align-self:center!important}  .align-self-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}  .align-self-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}@media (min-width:576px){.flex-sm-row{-webkit-box-orient:horizontal!important;-webkit-box-direction:normal!important;-ms-flex-direction:row!important;flex-direction:row!important}  .flex-sm-column{-webkit-box-orient:vertical!important;-webkit-box-direction:normal!important;-ms-flex-direction:column!important;flex-direction:column!important}  .flex-sm-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}  .flex-sm-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}  .flex-sm-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}  .flex-sm-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}  .flex-sm-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}  .justify-content-sm-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}  .justify-content-sm-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}  .justify-content-sm-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}  .justify-content-sm-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}  .justify-content-sm-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}  .align-items-sm-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}  .align-items-sm-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}  .align-items-sm-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}  .align-items-sm-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}  .align-items-sm-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}  .align-content-sm-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}  .align-content-sm-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}  .align-content-sm-center{-ms-flex-line-pack:center!important;align-content:center!important}  .align-content-sm-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}  .align-content-sm-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}  .align-content-sm-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}  .align-self-sm-auto{-ms-flex-item-align:auto!important;align-self:auto!important}  .align-self-sm-start{-ms-flex-item-align:start!important;align-self:flex-start!important}  .align-self-sm-end{-ms-flex-item-align:end!important;align-self:flex-end!important}  .align-self-sm-center{-ms-flex-item-align:center!important;align-self:center!important}  .align-self-sm-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}  .align-self-sm-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:768px){.flex-md-row{-webkit-box-orient:horizontal!important;-webkit-box-direction:normal!important;-ms-flex-direction:row!important;flex-direction:row!important}  .flex-md-column{-webkit-box-orient:vertical!important;-webkit-box-direction:normal!important;-ms-flex-direction:column!important;flex-direction:column!important}  .flex-md-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}  .flex-md-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}  .flex-md-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}  .flex-md-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}  .flex-md-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}  .justify-content-md-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}  .justify-content-md-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}  .justify-content-md-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}  .justify-content-md-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}  .justify-content-md-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}  .align-items-md-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}  .align-items-md-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}  .align-items-md-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}  .align-items-md-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}  .align-items-md-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}  .align-content-md-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}  .align-content-md-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}  .align-content-md-center{-ms-flex-line-pack:center!important;align-content:center!important}  .align-content-md-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}  .align-content-md-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}  .align-content-md-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}  .align-self-md-auto{-ms-flex-item-align:auto!important;align-self:auto!important}  .align-self-md-start{-ms-flex-item-align:start!important;align-self:flex-start!important}  .align-self-md-end{-ms-flex-item-align:end!important;align-self:flex-end!important}  .align-self-md-center{-ms-flex-item-align:center!important;align-self:center!important}  .align-self-md-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}  .align-self-md-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:992px){.flex-lg-row{-webkit-box-orient:horizontal!important;-webkit-box-direction:normal!important;-ms-flex-direction:row!important;flex-direction:row!important}  .flex-lg-column{-webkit-box-orient:vertical!important;-webkit-box-direction:normal!important;-ms-flex-direction:column!important;flex-direction:column!important}  .flex-lg-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}  .flex-lg-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}  .flex-lg-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}  .flex-lg-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}  .flex-lg-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}  .justify-content-lg-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}  .justify-content-lg-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}  .justify-content-lg-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}  .justify-content-lg-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}  .justify-content-lg-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}  .align-items-lg-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}  .align-items-lg-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}  .align-items-lg-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}  .align-items-lg-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}  .align-items-lg-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}  .align-content-lg-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}  .align-content-lg-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}  .align-content-lg-center{-ms-flex-line-pack:center!important;align-content:center!important}  .align-content-lg-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}  .align-content-lg-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}  .align-content-lg-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}  .align-self-lg-auto{-ms-flex-item-align:auto!important;align-self:auto!important}  .align-self-lg-start{-ms-flex-item-align:start!important;align-self:flex-start!important}  .align-self-lg-end{-ms-flex-item-align:end!important;align-self:flex-end!important}  .align-self-lg-center{-ms-flex-item-align:center!important;align-self:center!important}  .align-self-lg-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}  .align-self-lg-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:1200px){.flex-xl-row{-webkit-box-orient:horizontal!important;-webkit-box-direction:normal!important;-ms-flex-direction:row!important;flex-direction:row!important}  .flex-xl-column{-webkit-box-orient:vertical!important;-webkit-box-direction:normal!important;-ms-flex-direction:column!important;flex-direction:column!important}  .flex-xl-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}  .flex-xl-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}  .flex-xl-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}  .flex-xl-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}  .flex-xl-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}  .justify-content-xl-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}  .justify-content-xl-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}  .justify-content-xl-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}  .justify-content-xl-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}  .justify-content-xl-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}  .align-items-xl-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}  .align-items-xl-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}  .align-items-xl-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}  .align-items-xl-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}  .align-items-xl-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}  .align-content-xl-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}  .align-content-xl-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}  .align-content-xl-center{-ms-flex-line-pack:center!important;align-content:center!important}  .align-content-xl-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}  .align-content-xl-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}  .align-content-xl-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}  .align-self-xl-auto{-ms-flex-item-align:auto!important;align-self:auto!important}  .align-self-xl-start{-ms-flex-item-align:start!important;align-self:flex-start!important}  .align-self-xl-end{-ms-flex-item-align:end!important;align-self:flex-end!important}  .align-self-xl-center{-ms-flex-item-align:center!important;align-self:center!important}  .align-self-xl-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}  .align-self-xl-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}  .float-left{float:left!important}  .float-right{float:right!important}  .float-none{float:none!important}@media (min-width:576px){.float-sm-left{float:left!important}  .float-sm-right{float:right!important}  .float-sm-none{float:none!important}}@media (min-width:768px){.float-md-left{float:left!important}  .float-md-right{float:right!important}  .float-md-none{float:none!important}}@media (min-width:992px){.float-lg-left{float:left!important}  .float-lg-right{float:right!important}  .float-lg-none{float:none!important}}@media (min-width:1200px){.float-xl-left{float:left!important}  .float-xl-right{float:right!important}  .float-xl-none{float:none!important}}  .position-static{position:static!important}  .position-relative{position:relative!important}  .position-absolute{position:absolute!important}  .position-fixed{position:fixed!important}  .position-sticky{position:-webkit-sticky!important;position:sticky!important}  .fixed-top{position:fixed;top:0;right:0;left:0;z-index:1030}  .fixed-bottom{position:fixed;right:0;bottom:0;left:0;z-index:1030}@supports ((position:-webkit-sticky) or (position:sticky)){.sticky-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}}  .sr-only{position:absolute;width:1px;height:1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;-webkit-clip-path:inset(50%);clip-path:inset(50%);border:0}  .sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;overflow:visible;clip:auto;white-space:normal;-webkit-clip-path:none;clip-path:none}  .w-25{width:25%!important}  .w-50{width:50%!important}  .w-75{width:75%!important}  .w-100{width:100%!important}  .h-25{height:25%!important}  .h-50{height:50%!important}  .h-75{height:75%!important}  .h-100{height:100%!important}  .mw-100{max-width:100%!important}  .mh-100{max-height:100%!important}  .m-0{margin:0!important}  .mt-0,.my-0{margin-top:0!important}  .mr-0,.mx-0{margin-right:0!important}  .mb-0,.my-0{margin-bottom:0!important}  .ml-0,.mx-0{margin-left:0!important}  .m-1{margin:.25rem!important}  .mt-1,.my-1{margin-top:.25rem!important}  .mr-1,.mx-1{margin-right:.25rem!important}  .mb-1,.my-1{margin-bottom:.25rem!important}  .ml-1,.mx-1{margin-left:.25rem!important}  .m-2{margin:.5rem!important}  .mt-2,.my-2{margin-top:.5rem!important}  .mr-2,.mx-2{margin-right:.5rem!important}  .mb-2,.my-2{margin-bottom:.5rem!important}  .ml-2,.mx-2{margin-left:.5rem!important}  .m-3{margin:1rem!important}  .mt-3,.my-3{margin-top:1rem!important}  .mr-3,.mx-3{margin-right:1rem!important}  .mb-3,.my-3{margin-bottom:1rem!important}  .ml-3,.mx-3{margin-left:1rem!important}  .m-4{margin:1.5rem!important}  .mt-4,.my-4{margin-top:1.5rem!important}  .mr-4,.mx-4{margin-right:1.5rem!important}  .mb-4,.my-4{margin-bottom:1.5rem!important}  .ml-4,.mx-4{margin-left:1.5rem!important}  .m-5{margin:3rem!important}  .mt-5,.my-5{margin-top:3rem!important}  .mr-5,.mx-5{margin-right:3rem!important}  .mb-5,.my-5{margin-bottom:3rem!important}  .ml-5,.mx-5{margin-left:3rem!important}  .p-0{padding:0!important}  .pt-0,.py-0{padding-top:0!important}  .pr-0,.px-0{padding-right:0!important}  .pb-0,.py-0{padding-bottom:0!important}  .pl-0,.px-0{padding-left:0!important}  .p-1{padding:.25rem!important}  .pt-1,.py-1{padding-top:.25rem!important}  .pr-1,.px-1{padding-right:.25rem!important}  .pb-1,.py-1{padding-bottom:.25rem!important}  .pl-1,.px-1{padding-left:.25rem!important}  .p-2{padding:.5rem!important}  .pt-2,.py-2{padding-top:.5rem!important}  .pr-2,.px-2{padding-right:.5rem!important}  .pb-2,.py-2{padding-bottom:.5rem!important}  .pl-2,.px-2{padding-left:.5rem!important}  .p-3{padding:1rem!important}  .pt-3,.py-3{padding-top:1rem!important}  .pr-3,.px-3{padding-right:1rem!important}  .pb-3,.py-3{padding-bottom:1rem!important}  .pl-3,.px-3{padding-left:1rem!important}  .p-4{padding:1.5rem!important}  .pt-4,.py-4{padding-top:1.5rem!important}  .pr-4,.px-4{padding-right:1.5rem!important}  .pb-4,.py-4{padding-bottom:1.5rem!important}  .pl-4,.px-4{padding-left:1.5rem!important}  .p-5{padding:3rem!important}  .pt-5,.py-5{padding-top:3rem!important}  .pr-5,.px-5{padding-right:3rem!important}  .pb-5,.py-5{padding-bottom:3rem!important}  .pl-5,.px-5{padding-left:3rem!important}  .m-auto{margin:auto!important}  .mt-auto,.my-auto{margin-top:auto!important}  .mr-auto,.mx-auto{margin-right:auto!important}  .mb-auto,.my-auto{margin-bottom:auto!important}  .ml-auto,.mx-auto{margin-left:auto!important}@media (min-width:576px){.m-sm-0{margin:0!important}  .mt-sm-0,.my-sm-0{margin-top:0!important}  .mr-sm-0,.mx-sm-0{margin-right:0!important}  .mb-sm-0,.my-sm-0{margin-bottom:0!important}  .ml-sm-0,.mx-sm-0{margin-left:0!important}  .m-sm-1{margin:.25rem!important}  .mt-sm-1,.my-sm-1{margin-top:.25rem!important}  .mr-sm-1,.mx-sm-1{margin-right:.25rem!important}  .mb-sm-1,.my-sm-1{margin-bottom:.25rem!important}  .ml-sm-1,.mx-sm-1{margin-left:.25rem!important}  .m-sm-2{margin:.5rem!important}  .mt-sm-2,.my-sm-2{margin-top:.5rem!important}  .mr-sm-2,.mx-sm-2{margin-right:.5rem!important}  .mb-sm-2,.my-sm-2{margin-bottom:.5rem!important}  .ml-sm-2,.mx-sm-2{margin-left:.5rem!important}  .m-sm-3{margin:1rem!important}  .mt-sm-3,.my-sm-3{margin-top:1rem!important}  .mr-sm-3,.mx-sm-3{margin-right:1rem!important}  .mb-sm-3,.my-sm-3{margin-bottom:1rem!important}  .ml-sm-3,.mx-sm-3{margin-left:1rem!important}  .m-sm-4{margin:1.5rem!important}  .mt-sm-4,.my-sm-4{margin-top:1.5rem!important}  .mr-sm-4,.mx-sm-4{margin-right:1.5rem!important}  .mb-sm-4,.my-sm-4{margin-bottom:1.5rem!important}  .ml-sm-4,.mx-sm-4{margin-left:1.5rem!important}  .m-sm-5{margin:3rem!important}  .mt-sm-5,.my-sm-5{margin-top:3rem!important}  .mr-sm-5,.mx-sm-5{margin-right:3rem!important}  .mb-sm-5,.my-sm-5{margin-bottom:3rem!important}  .ml-sm-5,.mx-sm-5{margin-left:3rem!important}  .p-sm-0{padding:0!important}  .pt-sm-0,.py-sm-0{padding-top:0!important}  .pr-sm-0,.px-sm-0{padding-right:0!important}  .pb-sm-0,.py-sm-0{padding-bottom:0!important}  .pl-sm-0,.px-sm-0{padding-left:0!important}  .p-sm-1{padding:.25rem!important}  .pt-sm-1,.py-sm-1{padding-top:.25rem!important}  .pr-sm-1,.px-sm-1{padding-right:.25rem!important}  .pb-sm-1,.py-sm-1{padding-bottom:.25rem!important}  .pl-sm-1,.px-sm-1{padding-left:.25rem!important}  .p-sm-2{padding:.5rem!important}  .pt-sm-2,.py-sm-2{padding-top:.5rem!important}  .pr-sm-2,.px-sm-2{padding-right:.5rem!important}  .pb-sm-2,.py-sm-2{padding-bottom:.5rem!important}  .pl-sm-2,.px-sm-2{padding-left:.5rem!important}  .p-sm-3{padding:1rem!important}  .pt-sm-3,.py-sm-3{padding-top:1rem!important}  .pr-sm-3,.px-sm-3{padding-right:1rem!important}  .pb-sm-3,.py-sm-3{padding-bottom:1rem!important}  .pl-sm-3,.px-sm-3{padding-left:1rem!important}  .p-sm-4{padding:1.5rem!important}  .pt-sm-4,.py-sm-4{padding-top:1.5rem!important}  .pr-sm-4,.px-sm-4{padding-right:1.5rem!important}  .pb-sm-4,.py-sm-4{padding-bottom:1.5rem!important}  .pl-sm-4,.px-sm-4{padding-left:1.5rem!important}  .p-sm-5{padding:3rem!important}  .pt-sm-5,.py-sm-5{padding-top:3rem!important}  .pr-sm-5,.px-sm-5{padding-right:3rem!important}  .pb-sm-5,.py-sm-5{padding-bottom:3rem!important}  .pl-sm-5,.px-sm-5{padding-left:3rem!important}  .m-sm-auto{margin:auto!important}  .mt-sm-auto,.my-sm-auto{margin-top:auto!important}  .mr-sm-auto,.mx-sm-auto{margin-right:auto!important}  .mb-sm-auto,.my-sm-auto{margin-bottom:auto!important}  .ml-sm-auto,.mx-sm-auto{margin-left:auto!important}}@media (min-width:768px){.m-md-0{margin:0!important}  .mt-md-0,.my-md-0{margin-top:0!important}  .mr-md-0,.mx-md-0{margin-right:0!important}  .mb-md-0,.my-md-0{margin-bottom:0!important}  .ml-md-0,.mx-md-0{margin-left:0!important}  .m-md-1{margin:.25rem!important}  .mt-md-1,.my-md-1{margin-top:.25rem!important}  .mr-md-1,.mx-md-1{margin-right:.25rem!important}  .mb-md-1,.my-md-1{margin-bottom:.25rem!important}  .ml-md-1,.mx-md-1{margin-left:.25rem!important}  .m-md-2{margin:.5rem!important}  .mt-md-2,.my-md-2{margin-top:.5rem!important}  .mr-md-2,.mx-md-2{margin-right:.5rem!important}  .mb-md-2,.my-md-2{margin-bottom:.5rem!important}  .ml-md-2,.mx-md-2{margin-left:.5rem!important}  .m-md-3{margin:1rem!important}  .mt-md-3,.my-md-3{margin-top:1rem!important}  .mr-md-3,.mx-md-3{margin-right:1rem!important}  .mb-md-3,.my-md-3{margin-bottom:1rem!important}  .ml-md-3,.mx-md-3{margin-left:1rem!important}  .m-md-4{margin:1.5rem!important}  .mt-md-4,.my-md-4{margin-top:1.5rem!important}  .mr-md-4,.mx-md-4{margin-right:1.5rem!important}  .mb-md-4,.my-md-4{margin-bottom:1.5rem!important}  .ml-md-4,.mx-md-4{margin-left:1.5rem!important}  .m-md-5{margin:3rem!important}  .mt-md-5,.my-md-5{margin-top:3rem!important}  .mr-md-5,.mx-md-5{margin-right:3rem!important}  .mb-md-5,.my-md-5{margin-bottom:3rem!important}  .ml-md-5,.mx-md-5{margin-left:3rem!important}  .p-md-0{padding:0!important}  .pt-md-0,.py-md-0{padding-top:0!important}  .pr-md-0,.px-md-0{padding-right:0!important}  .pb-md-0,.py-md-0{padding-bottom:0!important}  .pl-md-0,.px-md-0{padding-left:0!important}  .p-md-1{padding:.25rem!important}  .pt-md-1,.py-md-1{padding-top:.25rem!important}  .pr-md-1,.px-md-1{padding-right:.25rem!important}  .pb-md-1,.py-md-1{padding-bottom:.25rem!important}  .pl-md-1,.px-md-1{padding-left:.25rem!important}  .p-md-2{padding:.5rem!important}  .pt-md-2,.py-md-2{padding-top:.5rem!important}  .pr-md-2,.px-md-2{padding-right:.5rem!important}  .pb-md-2,.py-md-2{padding-bottom:.5rem!important}  .pl-md-2,.px-md-2{padding-left:.5rem!important}  .p-md-3{padding:1rem!important}  .pt-md-3,.py-md-3{padding-top:1rem!important}  .pr-md-3,.px-md-3{padding-right:1rem!important}  .pb-md-3,.py-md-3{padding-bottom:1rem!important}  .pl-md-3,.px-md-3{padding-left:1rem!important}  .p-md-4{padding:1.5rem!important}  .pt-md-4,.py-md-4{padding-top:1.5rem!important}  .pr-md-4,.px-md-4{padding-right:1.5rem!important}  .pb-md-4,.py-md-4{padding-bottom:1.5rem!important}  .pl-md-4,.px-md-4{padding-left:1.5rem!important}  .p-md-5{padding:3rem!important}  .pt-md-5,.py-md-5{padding-top:3rem!important}  .pr-md-5,.px-md-5{padding-right:3rem!important}  .pb-md-5,.py-md-5{padding-bottom:3rem!important}  .pl-md-5,.px-md-5{padding-left:3rem!important}  .m-md-auto{margin:auto!important}  .mt-md-auto,.my-md-auto{margin-top:auto!important}  .mr-md-auto,.mx-md-auto{margin-right:auto!important}  .mb-md-auto,.my-md-auto{margin-bottom:auto!important}  .ml-md-auto,.mx-md-auto{margin-left:auto!important}}@media (min-width:992px){.m-lg-0{margin:0!important}  .mt-lg-0,.my-lg-0{margin-top:0!important}  .mr-lg-0,.mx-lg-0{margin-right:0!important}  .mb-lg-0,.my-lg-0{margin-bottom:0!important}  .ml-lg-0,.mx-lg-0{margin-left:0!important}  .m-lg-1{margin:.25rem!important}  .mt-lg-1,.my-lg-1{margin-top:.25rem!important}  .mr-lg-1,.mx-lg-1{margin-right:.25rem!important}  .mb-lg-1,.my-lg-1{margin-bottom:.25rem!important}  .ml-lg-1,.mx-lg-1{margin-left:.25rem!important}  .m-lg-2{margin:.5rem!important}  .mt-lg-2,.my-lg-2{margin-top:.5rem!important}  .mr-lg-2,.mx-lg-2{margin-right:.5rem!important}  .mb-lg-2,.my-lg-2{margin-bottom:.5rem!important}  .ml-lg-2,.mx-lg-2{margin-left:.5rem!important}  .m-lg-3{margin:1rem!important}  .mt-lg-3,.my-lg-3{margin-top:1rem!important}  .mr-lg-3,.mx-lg-3{margin-right:1rem!important}  .mb-lg-3,.my-lg-3{margin-bottom:1rem!important}  .ml-lg-3,.mx-lg-3{margin-left:1rem!important}  .m-lg-4{margin:1.5rem!important}  .mt-lg-4,.my-lg-4{margin-top:1.5rem!important}  .mr-lg-4,.mx-lg-4{margin-right:1.5rem!important}  .mb-lg-4,.my-lg-4{margin-bottom:1.5rem!important}  .ml-lg-4,.mx-lg-4{margin-left:1.5rem!important}  .m-lg-5{margin:3rem!important}  .mt-lg-5,.my-lg-5{margin-top:3rem!important}  .mr-lg-5,.mx-lg-5{margin-right:3rem!important}  .mb-lg-5,.my-lg-5{margin-bottom:3rem!important}  .ml-lg-5,.mx-lg-5{margin-left:3rem!important}  .p-lg-0{padding:0!important}  .pt-lg-0,.py-lg-0{padding-top:0!important}  .pr-lg-0,.px-lg-0{padding-right:0!important}  .pb-lg-0,.py-lg-0{padding-bottom:0!important}  .pl-lg-0,.px-lg-0{padding-left:0!important}  .p-lg-1{padding:.25rem!important}  .pt-lg-1,.py-lg-1{padding-top:.25rem!important}  .pr-lg-1,.px-lg-1{padding-right:.25rem!important}  .pb-lg-1,.py-lg-1{padding-bottom:.25rem!important}  .pl-lg-1,.px-lg-1{padding-left:.25rem!important}  .p-lg-2{padding:.5rem!important}  .pt-lg-2,.py-lg-2{padding-top:.5rem!important}  .pr-lg-2,.px-lg-2{padding-right:.5rem!important}  .pb-lg-2,.py-lg-2{padding-bottom:.5rem!important}  .pl-lg-2,.px-lg-2{padding-left:.5rem!important}  .p-lg-3{padding:1rem!important}  .pt-lg-3,.py-lg-3{padding-top:1rem!important}  .pr-lg-3,.px-lg-3{padding-right:1rem!important}  .pb-lg-3,.py-lg-3{padding-bottom:1rem!important}  .pl-lg-3,.px-lg-3{padding-left:1rem!important}  .p-lg-4{padding:1.5rem!important}  .pt-lg-4,.py-lg-4{padding-top:1.5rem!important}  .pr-lg-4,.px-lg-4{padding-right:1.5rem!important}  .pb-lg-4,.py-lg-4{padding-bottom:1.5rem!important}  .pl-lg-4,.px-lg-4{padding-left:1.5rem!important}  .p-lg-5{padding:3rem!important}  .pt-lg-5,.py-lg-5{padding-top:3rem!important}  .pr-lg-5,.px-lg-5{padding-right:3rem!important}  .pb-lg-5,.py-lg-5{padding-bottom:3rem!important}  .pl-lg-5,.px-lg-5{padding-left:3rem!important}  .m-lg-auto{margin:auto!important}  .mt-lg-auto,.my-lg-auto{margin-top:auto!important}  .mr-lg-auto,.mx-lg-auto{margin-right:auto!important}  .mb-lg-auto,.my-lg-auto{margin-bottom:auto!important}  .ml-lg-auto,.mx-lg-auto{margin-left:auto!important}}@media (min-width:1200px){.m-xl-0{margin:0!important}  .mt-xl-0,.my-xl-0{margin-top:0!important}  .mr-xl-0,.mx-xl-0{margin-right:0!important}  .mb-xl-0,.my-xl-0{margin-bottom:0!important}  .ml-xl-0,.mx-xl-0{margin-left:0!important}  .m-xl-1{margin:.25rem!important}  .mt-xl-1,.my-xl-1{margin-top:.25rem!important}  .mr-xl-1,.mx-xl-1{margin-right:.25rem!important}  .mb-xl-1,.my-xl-1{margin-bottom:.25rem!important}  .ml-xl-1,.mx-xl-1{margin-left:.25rem!important}  .m-xl-2{margin:.5rem!important}  .mt-xl-2,.my-xl-2{margin-top:.5rem!important}  .mr-xl-2,.mx-xl-2{margin-right:.5rem!important}  .mb-xl-2,.my-xl-2{margin-bottom:.5rem!important}  .ml-xl-2,.mx-xl-2{margin-left:.5rem!important}  .m-xl-3{margin:1rem!important}  .mt-xl-3,.my-xl-3{margin-top:1rem!important}  .mr-xl-3,.mx-xl-3{margin-right:1rem!important}  .mb-xl-3,.my-xl-3{margin-bottom:1rem!important}  .ml-xl-3,.mx-xl-3{margin-left:1rem!important}  .m-xl-4{margin:1.5rem!important}  .mt-xl-4,.my-xl-4{margin-top:1.5rem!important}  .mr-xl-4,.mx-xl-4{margin-right:1.5rem!important}  .mb-xl-4,.my-xl-4{margin-bottom:1.5rem!important}  .ml-xl-4,.mx-xl-4{margin-left:1.5rem!important}  .m-xl-5{margin:3rem!important}  .mt-xl-5,.my-xl-5{margin-top:3rem!important}  .mr-xl-5,.mx-xl-5{margin-right:3rem!important}  .mb-xl-5,.my-xl-5{margin-bottom:3rem!important}  .ml-xl-5,.mx-xl-5{margin-left:3rem!important}  .p-xl-0{padding:0!important}  .pt-xl-0,.py-xl-0{padding-top:0!important}  .pr-xl-0,.px-xl-0{padding-right:0!important}  .pb-xl-0,.py-xl-0{padding-bottom:0!important}  .pl-xl-0,.px-xl-0{padding-left:0!important}  .p-xl-1{padding:.25rem!important}  .pt-xl-1,.py-xl-1{padding-top:.25rem!important}  .pr-xl-1,.px-xl-1{padding-right:.25rem!important}  .pb-xl-1,.py-xl-1{padding-bottom:.25rem!important}  .pl-xl-1,.px-xl-1{padding-left:.25rem!important}  .p-xl-2{padding:.5rem!important}  .pt-xl-2,.py-xl-2{padding-top:.5rem!important}  .pr-xl-2,.px-xl-2{padding-right:.5rem!important}  .pb-xl-2,.py-xl-2{padding-bottom:.5rem!important}  .pl-xl-2,.px-xl-2{padding-left:.5rem!important}  .p-xl-3{padding:1rem!important}  .pt-xl-3,.py-xl-3{padding-top:1rem!important}  .pr-xl-3,.px-xl-3{padding-right:1rem!important}  .pb-xl-3,.py-xl-3{padding-bottom:1rem!important}  .pl-xl-3,.px-xl-3{padding-left:1rem!important}  .p-xl-4{padding:1.5rem!important}  .pt-xl-4,.py-xl-4{padding-top:1.5rem!important}  .pr-xl-4,.px-xl-4{padding-right:1.5rem!important}  .pb-xl-4,.py-xl-4{padding-bottom:1.5rem!important}  .pl-xl-4,.px-xl-4{padding-left:1.5rem!important}  .p-xl-5{padding:3rem!important}  .pt-xl-5,.py-xl-5{padding-top:3rem!important}  .pr-xl-5,.px-xl-5{padding-right:3rem!important}  .pb-xl-5,.py-xl-5{padding-bottom:3rem!important}  .pl-xl-5,.px-xl-5{padding-left:3rem!important}  .m-xl-auto{margin:auto!important}  .mt-xl-auto,.my-xl-auto{margin-top:auto!important}  .mr-xl-auto,.mx-xl-auto{margin-right:auto!important}  .mb-xl-auto,.my-xl-auto{margin-bottom:auto!important}  .ml-xl-auto,.mx-xl-auto{margin-left:auto!important}}  .text-justify{text-align:justify!important}  .text-nowrap{white-space:nowrap!important}  .text-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}  .text-left{text-align:left!important}  .text-right{text-align:right!important}  .text-center{text-align:center!important}@media (min-width:576px){.text-sm-left{text-align:left!important}  .text-sm-right{text-align:right!important}  .text-sm-center{text-align:center!important}}@media (min-width:768px){.text-md-left{text-align:left!important}  .text-md-right{text-align:right!important}  .text-md-center{text-align:center!important}}@media (min-width:992px){.text-lg-left{text-align:left!important}  .text-lg-right{text-align:right!important}  .text-lg-center{text-align:center!important}}@media (min-width:1200px){.text-xl-left{text-align:left!important}  .text-xl-right{text-align:right!important}  .text-xl-center{text-align:center!important}}  .text-lowercase{text-transform:lowercase!important}  .text-uppercase{text-transform:uppercase!important}  .text-capitalize{text-transform:capitalize!important}  .font-weight-light{font-weight:300!important}  .font-weight-normal{font-weight:400!important}  .font-weight-bold{font-weight:700!important}  .font-italic{font-style:italic!important}  .text-white{color:#fff!important}  .text-primary{color:#007bff!important}  a.text-primary:focus,a.text-primary:hover{color:#0062cc!important}  .text-secondary{color:#6c757d!important}  a.text-secondary:focus,a.text-secondary:hover{color:#545b62!important}  .text-success{color:#28a745!important}  a.text-success:focus,a.text-success:hover{color:#1e7e34!important}  .text-info{color:#17a2b8!important}  a.text-info:focus,a.text-info:hover{color:#117a8b!important}  .text-warning{color:#ffc107!important}  a.text-warning:focus,a.text-warning:hover{color:#d39e00!important}  .text-danger{color:#dc3545!important}  a.text-danger:focus,a.text-danger:hover{color:#bd2130!important}  .text-light{color:#f8f9fa!important}  a.text-light:focus,a.text-light:hover{color:#dae0e5!important}  .text-dark{color:#343a40!important}  a.text-dark:focus,a.text-dark:hover{color:#1d2124!important}  .text-muted{color:#6c757d!important}  .text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}  .visible{visibility:visible!important}  .invisible{visibility:hidden!important}@media print{*,::after,::before{text-shadow:none!important;box-shadow:none!important}  a:not(.btn){text-decoration:underline}  abbr[title]::after{content:" (" attr(title) ")"}  pre{white-space:pre-wrap!important}  blockquote,pre{border:1px solid #999;page-break-inside:avoid}  thead{display:table-header-group}  img,tr{page-break-inside:avoid}  h2,h3,p{orphans:3;widows:3}  h2,h3{page-break-after:avoid}@page{size:a3}  body{min-width:992px!important}  .container{min-width:992px!important}  .navbar{display:none}  .badge{border:1px solid #000}  .table{border-collapse:collapse!important}  .table td,.table th{background-color:#fff!important}  .table-bordered td,.table-bordered th{border:1px solid #ddd!important}}


		@font-face {
			font-family: 'Futura';
		/*	src: url("../fonts/Futura.woff"); */
		}

		html,
		body {
			height: 100%;
			font-family: "Lato", sans-serif;
			-webkit-font-smoothing: antialiased;
			font-smoothing: antialiased;
		}

		h1,
		h2,
		h3,
		h4,
		h5,
		h6 {
			color: #20509e;
			margin: 0;
			font-weight: 500;
			font-family: "Futura", sans-serif;
		}

		h1 {
			font-size: 3px;
		}

		h2 {
			font-size: 28px;
		}

		h3 {
			font-size: 30px;
		}

		h4 {
			font-size: 24px;
		}

		h5 {
			font-size: 20px;
		}

		h6 {
			font-size: 14px;
		}

		p {
			font-size: 15.7px;
			color: #75849a;
			line-height: 1.6;
		}

		img {
			max-width: 100%;
		}

		input:focus,
		select:focus,
		button:focus,
		textarea:focus {
			outline: none;
		}

		a:hover,
		a:focus {
			text-decoration: none;
			outline: none;
		}

		ul,
		ol {
			padding: 0;
			margin: 0;
		}

		/*---------------------
            Helper CSS
        -----------------------*/

		.spad {
			padding-top: 100px;
			padding-bottom: 90px;
		}

		.section-title {
			margin-bottom: 60px;
		}

		.section-title h2 {
			margin-bottom: 20px;
		}

		.section-title p {
			margin-bottom: 0;
		}

		.set-bg {
			background-repeat: no-repeat;
			background-size: cover;
			background-position: center 0;
		}

		.text-white h1,
		.text-white h2,
		.text-white h3,
		.text-white h4,
		.text-white h5,
		.text-white p,
		.text-white span,
		.text-white li,
		.text-white a {
			color: #fff;
		}

		/*---------------------
            Commom elements
        -----------------------*/

		/* Buttons */

		.site-btn {
			position: relative;
			display: inline-block;
			padding: 15px 30px;
			font-size: 16px;
			font-weight: 500;
			line-height: 16px;
			border-radius: 50px;
			font-family: "Futura", sans-serif;
			min-width: 170px;
			text-align: center;
			border: 2px solid #7ad4cc;
			cursor: pointer;
			color: #16d0c5;
		}

		.site-btn:hover {
			color: #fff;
		}

		.site-btn.no-radius {
			border-radius: 2px;
		}

		.site-btn.sb-full-- {
			display: block;
			width: 100%;
			border-radius: 0;
		}

		.site-btn.sb-gradients {
			padding: 17px 32px;
			border: none;
			color: #fff;
		}

		.site-btn.sb-gradients.sbg-line {
			color: #20509e;
			z-index: 1;
		}

		.site-btn.sb-gradients.sbg-line:after {
			position: absolute;
			content: '';
			width: calc(100% - 4px);
			height: calc(100% - 4px);
			background: #fff;
			top: 2px;
			left: 2px;
			z-index: -1;
			border-radius: 50px;
		}

		.site-btn.sb-gradients.sbg-line:hover {
			color: #20509e;
		}

		.gradient-bg,
		.site-btn.sb-gradients,
		.member-social a:hover,
		.single-blog-page .social-share a:hover,
		.comment .comment-content .c-btn:hover,
		.comment-form label {
			/* FF3.6-15 */
			/* Chrome10-25,Safari5.1-6 */
			background: -webkit-gradient(linear, left top, right top, from(#3e2bce), color-stop(100%, #2dd3aa), color-stop(100%, #2dd3aa), to(#2dd3aa));
			background: -o-linear-gradient(left, #3e2bce 0%, #2dd3aa 100%, #2dd3aa 100%, #2dd3aa 100%);
			background: linear-gradient(to right, #3e2bce 0%, #2dd3aa 100%, #2dd3aa 100%, #2dd3aa 100%);
			/* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
			filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#3e2bce', endColorstr='#2dd3aa', GradientType=1);
			/* IE6-9 */
		}

		/* Image Popup */

		.img-popup-warp .mfp-content,
		.img-popup-warp.mfp-ready.mfp-removing .mfp-content {
			opacity: 0;
			-webkit-transform: scale(0.8);
			-ms-transform: scale(0.8);
			transform: scale(0.8);
			-webkit-transition: all 0.4s;
			-o-transition: all 0.4s;
			transition: all 0.4s;
		}

		.img-popup-warp.mfp-ready .mfp-content {
			opacity: 1;
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}

		/* Preloder */

		#preloder {
			position: fixed;
			width: 100%;
			height: 100%;
			top: 0;
			left: 0;
			z-index: 999999;
			background: #fff;
		}

		.loader {
			width: 40px;
			height: 40px;
			position: absolute;
			top: 50%;
			left: 50%;
			margin-top: -13px;
			margin-left: -13px;
			border-radius: 60px;
			animation: loader 0.8s linear infinite;
			-webkit-animation: loader 0.8s linear infinite;
		}

		@keyframes loader {
			0% {
				-webkit-transform: rotate(0deg);
				transform: rotate(0deg);
				border: 4px solid #f44336;
				border-left-color: transparent;
			}
			50% {
				-webkit-transform: rotate(180deg);
				transform: rotate(180deg);
				border: 4px solid #673ab7;
				border-left-color: transparent;
			}
			100% {
				-webkit-transform: rotate(360deg);
				transform: rotate(360deg);
				border: 4px solid #f44336;
				border-left-color: transparent;
			}
		}

		@-webkit-keyframes loader {
			0% {
				-webkit-transform: rotate(0deg);
				border: 4px solid #f44336;
				border-left-color: transparent;
			}
			50% {
				-webkit-transform: rotate(180deg);
				border: 4px solid #673ab7;
				border-left-color: transparent;
			}
			100% {
				-webkit-transform: rotate(360deg);
				border: 4px solid #f44336;
				border-left-color: transparent;
			}
		}

		/*---------------------
            Header section
        -----------------------*/

		.header-section {
			position: absolute;
			width: 100%;
			top: 0;
			padding: 30px 50px 0;
			z-index: 99;
		}

		.header-section .site-btn {
			float: right;
			margin-left: 6px;
		}

		.header-section .responsive-bar,
		.header-section .user {
			display: none;
		}

		.main-menu {
			float: right;
		}

		.menu-list {
			list-style: none;
		}

		.menu-list li {
			display: inline;
		}

		.menu-list li a {
			display: inline-block;
			font-family: "Futura", sans-serif;
			font-size: 16px;
			padding: 10px 5px;
			margin-right: 30px;
			color: #16d0c5;
		}

		/*---------------------
            Hero Section
        -----------------------*/

		.hero-section {
			height: 900px;
			padding-top: 260px;
			display: block;
			background-color: #f3f7f9;
			background-position: right top;
			background-repeat: no-repeat;
			position: relative;
			overflow: hidden;
		}

		.hero-section .laptop-image {
			width: 685px;
			max-width: none;
			position: relative;
			left: 80px;
		}

		.hero-text {
			padding-top: 60px;
		}

		.hero-text h2 {
			font-size: 20px;
			margin-bottom: 35px;
		}

		.hero-text h2 span {
			color: #16d0c5;
		}

		.hero-text h4 {
			color: #75849a;
			font-size: 22px;
		}

		.hero-subscribe-from {
			margin-top: 50px;
			display: block;
		}

		.hero-subscribe-from input {
			width: 315px;
			border: 1px solid #ebebeb;
			background: #fff;
			height: 48px;
			padding: 0 25px;
			border-radius: 50px;
			font-family: "Futura", sans-serif;
			font-size: 16px;
			margin-right: 8px;
			margin-bottom: 20px;
		}

		/*---------------------
          About Section
        -----------------------*/

		.about-section .container {
			position: relative;
		}

		.about-text h2 {
			font-size: 48px;
			margin-bottom: 25px;
		}

		.about-text h5 {
			font-family: "Lato", sans-serif;
			margin-bottom: 20px;
		}

		.about-text p {
			font-size: 18px;
		}

		.about-img {
			position: absolute;
			top: 0;
			left: -120px;
			width: 662px;
		}



		/*---------------------
            Fact Section
        -----------------------*/

		.fact-section {
			padding: 100px 0;
		}

		.fact {
			display: inline-block;
			position: relative;
		}

		.fact h2 {
			float: left;
			color: #16d0c5;
			font-size: 60px;
			margin-right: 20px;
		}

		.fact p {
			float: left;
			padding-top: 14px;
			line-height: 1.4;
			color: #fff;
			text-transform: uppercase;
		}

		.fact i {
			position: absolute;
			right: -20px;
			top: -10px;
			font-size: 90px;
			color: #fff;
			z-index: 0;
			opacity: 0.1;
		}

		/*---------------------
            Team Section
        -----------------------*/

		.team-section {
			background: #f3f7f9;
			overflow: hidden;
		}

		.team-members {
			margin: 0 -10px;
		}

		.member {
			background: #fff;
			width: calc(20% - 25px);
			display: inline-block;
			margin: 0 10px;
			text-align: center;
			padding: 50px 10px;
			-webkit-box-shadow: 1px 1px 1px rgba(33, 54, 61, 0.15);
			box-shadow: 1px 1px 1px rgba(33, 54, 61, 0.15);
			border-radius: 10px;
			position: relative;
		}

		.member h2 {
			font-size: 22px;
			margin-bottom: 5px;
		}

		.member span {
			font-size: 14px;
			color: #75849a;
			display: block;
		}

		.member .member-text {
			-webkit-transition: all 0.4s;
			-o-transition: all 0.4s;
			transition: all 0.4s;
			opacity: 1;
		}

		.member:hover {
			-webkit-box-shadow: 1px 14px 43px rgba(33, 54, 61, 0.15);
			box-shadow: 1px 14px 43px rgba(33, 54, 61, 0.15);
		}

		.member:hover .member-info {
			opacity: 1;
		}

		.member:hover .member-text {
			opacity: 0;
		}

		.member-img {
			width: 230px;
			height: 230px;
			display: inline-block;
			border-radius: 50%;
			margin-bottom: 25px;
		}

		.member-social {
			padding-top: 25px;
			background: #fff;
			position: relative;
			z-index: 2;
		}

		.member-social a {
			width: 50px;
			height: 50px;
			display: inline-block;
			border-radius: 50%;
			background: #cbd3df;
			color: #fff;
			padding-top: 13px;
			margin: 0 8px;
		}

		.member-meta {
			padding-left: 85px;
		}

		.member-info {
			padding: 50px 60px 10px;
			position: absolute;
			width: 100%;
			top: 0;
			left: 0;
			text-align: left;
			opacity: 0;
			-webkit-transition: all 0.4s;
			-o-transition: all 0.4s;
			transition: all 0.4s;
			height: 380px;
			overflow-y: auto;
		}

		.member-info p {
			display: block;
			padding-top: 25px;
			margin-bottom: 0;
		}

		.member-img.mf {
			width: 60px;
			height: 60px;
			opacity: 1;
			float: left;
			margin-bottom: 0;
		}

		/*---------------------
          Review Section
        -----------------------*/

		.review-meta-slider {
			position: relative;
			width: 300px;
		}

		.author-meta {
			padding: 50px 0 70px;
			position: relative;
			text-align: center;
		}

		.author-meta:last-child {
			margin-right: 0;
		}

		.author-avatar {
			width: 80px;
			height: 80px;
			border: 6px solid #fff;
			border-radius: 50%;
			-webkit-box-shadow: 0px 16px 21px rgba(33, 54, 61, 0.15);
			box-shadow: 0px 16px 21px rgba(33, 54, 61, 0.15);
			display: inline-block;
		}

		.author-avatar h4 {
			font-size: 22px;
		}

		.author-avatar p {
			font-size: 14px;
		}

		.author-name {
			position: absolute;
			width: 280px;
			left: -50%;
			bottom: -10px;
			margin-left: -50px;
			text-align: center;
			visibility: hidden;
		}

		.center .author-meta {
			top: -6px;
		}

		.center .author-name {
			visibility: visible;
		}

		.center .author-avatar {
			width: 100px;
			height: 100px;
		}

		.review-text p {
			font-size: 22px;
		}

		.review-text-slider .owl-nav {
			padding-top: 15px;
		}

		.review-text-slider .owl-prev,
		.review-text-slider .owl-next {
			width: 50px;
			height: 50px;
			display: inline-block;
			background: #cbd3df;
			color: #fff;
			font-size: 24px;
			text-align: center;
			margin-right: 10px;
			border-radius: 50%;
			padding-top: 8px;
		}

		.pull-3 {
			right: 66.666667%;
		}

		.push-8 {
			left: 33.333333%;
		}

		/*---------------------
            Newsletter Section
        -----------------------*/

		.newsletter-section {
			padding: 50px 0;
		}

		.newsletter-text h2 {
			font-size: 36px;
			margin-bottom: 10px;
		}

		.newsletter-text p {
			margin-bottom: 0;
		}

		.newsletter-form {
			position: relative;
			margin-top: 20px;
			padding-left: 40px;
		}

		.newsletter-form input {
			width: 100%;
			font-size: 16px;
			padding: 12px 30px;
			border: none;
			border-radius: 50px;
			padding-right: 160px;
			background: rgba(255, 255, 255, 0.2);
			color: #fff;
		}

		.newsletter-form button {
			position: absolute;
			right: 0;
			top: 0;
			height: 100%;
			border: none;
			border-radius: 0px 50px 50px 0px;
			min-width: 140px;
			background: #fff;
			color: #20509e;
			font-size: 14px;
			font-weight: 600;
			cursor: pointer;
		}

		.newsletter-form ::-webkit-input-placeholder {
			color: #fff;
		}

		.newsletter-form :-ms-input-placeholder {
			color: #fff;
		}

		.newsletter-form ::-ms-input-placeholder {
			color: #fff;
		}

		.newsletter-form ::placeholder {
			color: #fff;
		}

		/*---------------------
          Blog Section
        -----------------------*/

		.blog-section {
			background: #f3f7f9;
		}

		.blog-thumb {
			margin-bottom: 0;
		}

		.blog-text {
			background: #fff;
			padding: 30px;
			-webkit-box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.1);
			box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.1);
		}

		.blog-text .post-date {
			font-size: 14px;
			font-family: "Futura", sans-serif;
			color: #16d0c5;
			text-transform: uppercase;
			margin-bottom: 15px;
			display: block;
			letter-spacing: 2px;
		}
                        
           .scrollable-boxneriman {
    width: 600px;
    height: 555px;
    overflow: overlay;
    background-color: #16d0c5;
    color: #fff;
    padding: 10px;
    border-radius: 15px;
  }
  code{
    color: black;
  }

  nerimanbaslik2{
    color:black;

  }             
.nerimanbaslik1 

		.blog-text .blog-title {
			font-size: 22px;
			margin-bottom: 20px;
		}

		.blog-text .blog-title a {
			color: #20509e;
		}

		.blog-text .post-meta a {
			font-size: 13px;
			color: #75849a;
			margin-right: 25px;
		}

		.blog-text .post-meta a:last-child {
			margin-right: 0;
		}

		.blog-text .post-meta a span {
			color: #cbd3df;
		}

		.blog-text .post-meta a i {
			color: #16d0c5;
		}

		.post-loadmore {
			width: 100%;
			border-radius: 0px;
		}

		.post-loadmore.site-btn.sb-gradients.sbg-line:after {
			border-radius: 0px;
		}

		/*---------------------
            Footer Section
        -----------------------*/

		.footer-widget span {
			color: #acb9cc;
		}

		.footer-widget p {
			margin-bottom: 20px;
		}

		.footer-widget .widget-title {
			margin-bottom: 30px;
			font-size: 20px;
		}

		.footer-widget ul {
			list-style: none;
		}

		.footer-widget ul a {
			font-size: 16px;
			color: #75849a;
			display: block;
			margin-bottom: 12px;
		}

		.footer-widget ul li:last-child a {
			margin-bottom: 0;
		}

		.social a {
			width: 40px;
			height: 40px;
			border-radius: 50%;
			color: #fff;
			display: inline-block;
			margin-right: 10px;
			text-align: center;
			padding-top: 7px;
			font-size: 18px;
		}

		.social a:last-child {
			margin-right: 0;
		}

		.social .facebook {
			background: #4b6cd0;
		}

		.social .google {
			background: #f03b3b;
		}

		.social .instagram {
			background: #bb8950;
		}

		.social .twitter {
			background: #49a7f3;
		}

		.footer-bottom {
			border-top: 1px solid #ebebeb;
			padding: 30px 0;
		}

		.footer-nav {
			list-style: none;
		}

		.footer-nav li {
			display: inline-block;
		}

		.footer-nav li a {
			color: #75849a;
			font-size: 14px;
			margin-left: 20px;
		}

		/*---------------------
            Other Pages
        ----------------------
        ======================*/

		.page-info-section {
			height: 300px;
			background-image: url("https://cdn.discordapp.com/attachments/1099776572988334160/1172918183540314152/page-info-bg.png?ex=6562102e&is=654f9b2e&hm=cf1078171f7ed417a3a464deffa3943c5cb061cf02d0c07a1c4f171db089ef37&");
			background-size: cover;
			background-color: #f3f7f9;
			background-position: right top;
			background-repeat: no-repeat;
			position: relative;
			overflow: hidden;
			display: block;
			padding-top: 100px;
		}

		.page-info-section h2 {
			font-size: 48px;
		}

		.site-beradcamb {
			padding-top: 10px;
		}

		.site-beradcamb a {
			color: #20509e;
			font-size: 16px;
		}

		.site-beradcamb span {
			color: #acb9cc;
			font-size: 16px;
		}

		.site-beradcamb i {
			margin: 0 3px;
		}

		/*---------------------
          Blog page
        -----------------------*/

		.blog-page .blog-item {
			margin-bottom: 30px;
		}

		.blog-page .readmore {
			color: #20509e;
		}

		.blog-page .readmore i {
			color: #16d0c5;
		}

		.bi-feature .post-meta {
			margin-bottom: 30px;
		}

		.bi-feature .blog-text .blog-title {
			font-size: 36px;
		}

		.widget-area {
			padding: 30px;
			-webkit-box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.15);
			box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.15);
			margin-bottom: 32px;
		}

		.widget-area .widget-title {
			margin-bottom: 25px;
		}

		.widget-area .widget {
			margin-bottom: 20px;
		}

		.widget-area .widget .widget-title {
			padding-bottom: 30px;
			margin-bottom: 30px;
			border-bottom: 1px solid #ebebeb;
			line-height: 24px;
		}

		.widget-area .widget ul {
			list-style: none;
		}

		.widget-area .widget ul a {
			display: inline-block;
			font-size: 16px;
			color: #20509e;
			margin-bottom: 20px;
		}

		.widget-area .widget ul a:hover {
			color: #16d0c5;
		}

		.widget-area .widget .popular-posts span {
			color: #16d0c5;
			font-size: 12px;
			display: block;
			margin-bottom: 7px;
			text-transform: uppercase;
		}

		.widget-area .widget .popular-posts h5 a {
			font-size: 18px;
			color: #20509e;
		}

		.widget-area .widget .popular-posts h5 a:hover {
			color: #20509e;
		}

		.widget-area .widget .twitter-widget li {
			margin-bottom: 20px;
		}

		.widget-area .widget .twitter-widget span {
			color: #16d0c5;
			font-size: 12px;
			display: block;
			text-transform: uppercase;
		}

		.widget-area .widget .twitter-widget h5 {
			font-size: 18px;
			color: #20509e;
			margin-bottom: 5px;
		}

		.widget-area .widget .twitter-widget a {
			font-size: 18px;
			color: #1f6ae5;
			display: block;
			margin-bottom: 5px;
		}

		.widget-area .widget .twitter-widget a:hover {
			color: #1f6ae5;
		}

		.widget-area .widget-subscribe-from {
			padding-top: 10px;
			display: block;
		}

		.widget-area .widget-subscribe-from input {
			margin-right: 0;
			margin-bottom: 20px;
			width: 100%;
			background: #f3f7f9;
			border: 1px solid #ebebeb;
			padding: 15px 20px;
			font-size: 14px;
		}

		.single-blog-page blockquote {
			font-size: 24px;
			color: #20509e;
			padding-left: 25px;
			border-left: 2px solid #16d0c5;
			line-height: normal;
			margin: 40px 0;
			display: block;
		}

		.single-blog-page blockquote span {
			display: block;
			font-size: 16px;
			color: #16d0c5;
			padding-top: 10px;
		}

		.single-blog-page .post-tags a {
			display: inline-block;
			font-size: 11px;
			text-transform: uppercase;
			padding: 6px 15px;
			margin-right: 2px;
			margin-top: 5px;
			color: #75849a;
			background: #f3f7f9;
			border: 1px solid #ebebeb;
			margin-right: 5px;
		}

		.single-blog-page .social-share {
			display: block;
			text-align: right;
		}

		.single-blog-page .social-share p {
			display: inline-block;
			font-size: 14px;
			margin-right: 10px;
			color: #595959;
		}

		.single-blog-page .social-share a {
			display: inline-block;
			width: 40px;
			height: 40px;
			margin-left: 8px;
			text-align: center;
			border-radius: 40px;
			background: #f3f7f9;
			color: #75849a;
			padding-top: 9px;
			font-size: 14px;
			-webkit-box-shadow: 0 0 0 1px #ebebeb;
			box-shadow: 0 0 0 1px #ebebeb;
			-webkit-transition: all 0.4s;
			-o-transition: all 0.4s;
			transition: all 0.4s;
		}

		.single-blog-page .social-share a:hover {
			color: #fff;
		}

		.releted-posts {
			padding-top: 50px;
			margin-top: 25px;
			border-top: 1px solid #ebebeb;
		}

		.releted-posts .blog-item {
			padding-top: 25px;
		}

		.releted-posts .blog-text {
			-webkit-box-shadow: 0 0 0 1px #ebebeb;
			box-shadow: 0 0 0 1px #ebebeb;
			padding: 28px 28px 20px;
		}

		.releted-posts .blog-text .blog-title {
			font-size: 22px;
		}

		.releted-posts .post-meta {
			margin-bottom: 0;
		}

		.comment-area {
			padding-top: 50px;
		}

		.comment-list {
			padding-top: 40px;
			margin-top: 25px;
			border-top: 1px solid #ebebeb;
			list-style: none;
		}

		.comment-list .replay-comment-list {
			list-style: none;
			margin-left: 14%;
		}

		.comment {
			margin-bottom: 40px;
		}

		.comment .comment-avator {
			float: left;
			width: 70px;
			height: 70px;
			border-radius: 50%;
		}

		.comment .comment-content {
			padding-left: 100px;
		}

		.comment .comment-content h5 {
			font-size: 18px;
			margin-bottom: 10px;
		}

		.comment .comment-content h5 span {
			font-size: 12px;
			color: #acb9cc;
			font-family: "Lato", sans-serif;
		}

		.comment .comment-content p {
			margin-bottom: 0;
		}


		.comment .comment-content .c-btn:hover {
			color: #fff;
		}

		.comment-form .form-group {
			position: relative;
			padding: 1px;
			margin-bottom: 20px;
		}

		.comment-form input,
		.comment-form textarea {
			width: 100%;
			padding: 11px 20px;
			border: none;
			border: 1px solid #e5e5e5;
			position: relative;
			z-index: 1;
			-webkit-transition: all 0.3s ease;
			-o-transition: all 0.3s ease;
			transition: all 0.3s ease;
		}

		.comment-form input:focus,
		.comment-form textarea:focus {
			border-color: transparent;
		}

		.comment-form input:focus+label,
		.comment-form textarea:focus+label {
			opacity: 1;
		}

		.comment-form label {
			position: absolute;
			width: 100%;
			height: 100%;
			left: 0;
			top: 0;
			display: block;
			opacity: 0;
			-webkit-transition: all 0.3s ease;
			-o-transition: all 0.3s ease;
			transition: all 0.3s ease;
		}

		.comment-form textarea {
			height: 115px;
			display: -ms-grid;
			display: grid;
		}

		/*---------------------
            Contact page
        -----------------------*/

		.contact-form {
			padding-right: 35px;
		}

		.contact-form h5 {
			font-size: 16px;
			font-family: "Lato", sans-serif;
		}

		.contact-form h5 span {
			color: #16d0c5;
		}

		.contact-form .form-group {
			position: relative;
			margin-bottom: 20px;
		}

		.contact-form .form-group span {
			position: absolute;
			right: 0;
			top: 10px;
			font-size: 16px;
			color: #7bc063;
			opacity: 0;
			-webkit-transition: all 0.3s;
			-o-transition: all 0.3s;
			transition: all 0.3s;
		}

		.contact-form .form-group span.active {
			opacity: 1;
		}

		.contact-form .check-form {
			padding-right: 20px;
		}

		.contact-form input,
		.contact-form textarea {
			width: 100%;
			height: 50px;
			border: none;
			border-bottom: 1px solid #ebebeb;
			font-size: 16px;
			padding-bottom: 10px;
			color: #20509e;
		}

		.contact-form input:focus,
		.contact-form textarea:focus {
			border-color: #20509e;
		}

		.contact-form textarea {
			padding-bottom: 10px;
			padding-top: 10px;
			height: 115px;
		}

		.contact-form .contact-type .ct-label {
			display: inline-block;
			position: relative;
			padding-left: 20px;
			margin-bottom: 12px;
			margin-right: 40px;
			cursor: pointer;
			font-size: 16px;
			color: #acb9cc;
			-webkit-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;
		}

		.contact-form .contact-type .ct-label input {
			position: absolute;
			opacity: 0;
			cursor: pointer;
		}

		.contact-form .contact-type .ct-label input:checked~.checkmark:after {
			content: '\f111';
			color: #16d0c5;
		}

		.contact-form .contact-type .ct-label .checkmark {
			position: absolute;
			top: 3px;
			left: 0;
			height: 25px;
			width: 25px;
		}

		.contact-form .contact-type .ct-label .checkmark:after {
			position: absolute;
			content: "\f10c";
			font-family: 'FontAwesome';
			font-size: 14px;
		}

		.contact-form .contact-type .ct-label:last-child {
			margin-right: 0;
		}

		.contact-form ::-webkit-input-placeholder {
			color: #acb9cc;
		}

		.contact-form :-ms-input-placeholder {
			color: #acb9cc;
		}

		.contact-form ::-ms-input-placeholder {
			color: #acb9cc;
		}

		.contact-form ::placeholder {
			color: #acb9cc;
		}

		.map {
			height: 390px;
			-webkit-box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.15);
			box-shadow: 0px 23px 49px rgba(33, 54, 61, 0.15);
		}

		/*------------------
            Responsive
        ---------------------*/

		@media (min-width: 1200px) {
			.container {
				max-width: 1170px;
			}
		}

		@media (max-width: 1585px) {
			.hero-section .laptop-image {
				left: 0;
			}
		}

		@media (max-width: 1425px) {
			.header-section .site-btn {
				margin-left: 0;
			}
			.hero-section,
			.page-info-section {
				background-position: right 30% top;
			}
			.hero-section .laptop-image {
				width: auto;
				max-width: 100%;
				top: 70px;
			}
			.about-img {
				left: -50px;
				width: 600px;
			}
		}

		@media (min-width: 1199px) and (max-width: 1390px) {
			.member {
				padding: 35px 10px;
			}
			.member-img {
				width: 160px;
				height: 160px;
			}
			.member-info {
				padding: 50px 27px 10px;
				height: 275px;
			}
			.member-social a {
				margin: 0 5px;
			}
		}

		/* Medium screen : 992px. */

		@media only screen and (min-width: 992px) and (max-width: 1199px) {
			.menu-list li a {
				margin-right: 15px;
			}
			.hero-section,
			.page-info-section {
				background-position: right 23% top;
			}
			.about-img {
				left: 0px;
				width: 480px;
			}
			.member {
				width: calc(33.333333% - 25px);
				margin-bottom: 30px;
			}
			.team-members {
				text-align: center;
			}
			.fact h2 {
				font-size: 45px;
				margin-right: 10px;
			}
			.fact p {
				padding-top: 7px;
			}
			.fact i {
				font-size: 67px;
			}
		}

		/* Tablet :768px. */

		@media only screen and (min-width: 768px) and (max-width: 991px) {
			.header-section {
				padding: 30px 15px 0;
			}
			.menu-list li a {
				margin-right: 6px;
			}
			.header-section .site-btn {
				margin-left: 10px;
			}
			.hero-section {
				background-position: right 25% top;
				height: 730px;
				padding-top: 160px;
			}
			.page-info-section {
				background-position: right 33% top;
			}
			.page-info-section h2 {
				font-size: 40px;
			}
			.hero-text h2 {
				font-size: 45px;
			}
			.process-step:after {
				width: 154px;
				height: 35px;
				top: -10px;
				right: -44%;
				background-size: contain;
			}
			.about-img {
				position: relative;
				display: block;
				left: 0;
				width: auto;
				margin-top: 50px;
			}
			.member {
				width: calc(33.333333% - 25px);
				margin-bottom: 30px;
				padding: 35px 10px;
			}
			.member-img {
				width: 160px;
				height: 160px;
			}
			.member-info {
				padding: 50px 27px 10px;
				height: 275px;
			}
			.member-social a {
				margin: 0 5px;
			}
			.team-members {
				text-align: center;
			}
			.fact {
				margin-bottom: 30px;
			}
			.pull-3 {
				right: 0;
			}
			.push-8 {
				left: 0;
			}
			.review-section {
				text-align: center;
			}
			.review-text {
				padding: 0 60px;
			}
			.review-text-slider .owl-nav {
				padding-top: 0;
				position: absolute;
				top: 50%;
				margin-top: -45px;
				left: 0;
				width: 100%;
			}
			.review-text-slider .owl-prev {
				float: left;
			}
			.review-text-slider .owl-next {
				float: right;
			}
			.review-meta-slider {
				margin: auto;
			}
			.author-meta {
				padding-top: 0;
			}
			.newsletter-form {
				padding-left: 0;
			}
			.footer-widget {
				margin-bottom: 30px;
			}
			.newsletter-section {
				text-align: center;
			}
		}

		/* Large Mobile :480px. */

		@media only screen and (max-width: 767px) {
			.header-section {
				padding: 30px 0;
				background: #fff;
			}
			.header-section .responsive-bar {
				float: right;
				font-size: 25px;
				display: block;
				cursor: pointer;
			}
			.header-section .user {
				float: right;
				font-size: 25px;
				color: #333;
				margin-right: 20px;
				display: block;
			}
			.main-menu {
				float: none;
				position: absolute;
				width: 100%;
				left: 0;
				top: 100%;
				background: #fff;
				padding: 0 15px;
				display: none;
				-webkit-box-shadow: 0 14px 43px rgba(33, 54, 61, 0.15);
				box-shadow: 0 14px 43px rgba(33, 54, 61, 0.15);
			}
			.menu-list {
				list-style: none;
			}
			.menu-list li {
				display: block;
				border-top: 1px solid #e1e1e1;
			}
			.menu-list li a {
				display: block;
				padding: 10px 5px;
				margin-right: 0;
				color: #16d0c5;
			}
			.hero-text h2 {
				font-size: 40px;
			}
			.hero-section {
				height: auto;
				padding-bottom: 100px;
				padding-top: 160px;
				background-position: right 50% top;
			}
			.page-info-section {
				background-position: right 56% top;
				margin-top: 97px;
			}
			.page-info-section h2 {
				font-size: 40px;
			}
			.about-img {
				position: relative;
				display: block;
				left: 0;
				width: auto;
				margin-top: 50px;
			}
			.team-members {
				margin: 0;
				padding: 0 15px;
			}
			.member {
				width: 100%;
				margin-bottom: 30px;
				margin-left: 0;
			}
			.fact {
				margin-bottom: 30px;
			}
			.process-step:after {
				display: none;
			}
			.pull-3 {
				right: 0;
			}
			.push-8 {
				left: 0;
			}
			.review-section {
				text-align: center;
			}
			.review-text {
				padding: 0 60px;
			}
			.review-text-slider .owl-nav {
				padding-top: 0;
				position: absolute;
				top: 50%;
				margin-top: -45px;
				left: 0;
				width: 100%;
			}
			.review-text-slider .owl-prev {
				float: left;
			}
			.review-text-slider .owl-next {
				float: right;
			}
			.review-meta-slider {
				margin: auto;
			}
			.author-meta {
				padding-top: 0;
			}
			.header-section .site-btn {
				display: none;
			}
			.newsletter-form {
				padding-left: 0;
			}
			.newsletter-section {
				text-align: center;
			}
			.review-text p {
				font-size: 20px;
			}
			.blog-item {
				margin-bottom: 30px;
			}
			.footer-widget {
				margin-bottom: 30px;
			}
			.single-blog-page .social-share {
				text-align: left;
				margin-top: 20px;
			}
		}

		/* small Mobile :320px. */

		@media only screen and (max-width: 479px) {
			.review-text {
				padding: 0 45px;
			}
			.review-text p {
				font-size: 18px;
			}
			.newsletter-form input {
				padding-right: 30px;
			}
			.newsletter-form button {
				position: relative;
				padding: 14px;
				border-radius: 50px;
				margin-top: 23px;
			}
			.review-text-slider .owl-prev,
			.review-text-slider .owl-next {
				width: 40px;
				height: 40px;
				font-size: 18px;
			}
			.review-meta-slider {
				width: auto;
			}
			.comment .comment-avator {
				float: none;
				margin-bottom: 20px;
			}
			.comment .comment-content {
				padding-left: 0;
			}
		}
	#active {
                        text-decoration:underline
                        }
	</style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/js/bootstrap.min.js" integrity="sha512-WW8/jxkELe2CAiE4LvQfwm1rajOS8PHasCCx+knHG0gBHt8EXxS6T6tJRTGuDQVnluuAvMxWF4j8SNFDKceLFg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

	<meta charset="UTF-8">
	<meta name="description" content="Cryptocurrency Landing Page Template">
	<meta name="keywords" content="cryptocurrency, unica, creative, html">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Favicon -->
	<link href="https://cdn.discordapp.com/attachments/1099776572988334160/1173011092331561030/logo.png?ex=656266b5&is=654ff1b5&hm=4552100c1d8a001801e9f5ca8b23621e129b121832abdec4c62f907f94a55c19&" rel="shortcut icon"/>

	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

	<!-- Stylesheets -->
	<!--[if lt IE 9]>
	  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	  <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
	<![endif]-->

</head>
<body>

	<!-- Page Preloder -->
	<div id="preloder">
		<div class="loader"></div>
	</div>

	<!-- Header section -->
	<header class="header-section clearfix">
		<div class="container-fluid">
			<a href="/ " class="site-logo">
				<img src="https://cdn.discordapp.com/attachments/1099776572988334160/1173011092331561030/logo.png?ex=656266b5&is=654ff1b5&hm=4552100c1d8a001801e9f5ca8b23621e129b121832abdec4c62f907f94a55c19&" alt="">
			</a>
			<div class="responsive-bar"><i class="fa fa-bars"></i></div>
			<a href="" class="user"><i class="fa fa-user"></i></a>
			<a href="/kayitol" class="site-btn"   >Giriş Yap</a>
			<nav class="main-menu">
				<ul class="menu-list">
                        <li><a href="/anket"id="active" >Eğitimlerimiz</a></li>
					<li><a href="/piyasalar" >Piyasalar</a></li>
					<li><a href="/hakkimizda"   >Hakkımızda</a></li>
					<li><a href="/sss"  >SSS</a></li>
					<li><a href="https://view.forms.app/nerimantopcu/iletisim"target="_blank" >İletişim</a></li>
				</ul>
			</nav>
		</div>
	</header>

	<section class="hero-section">
	  <div class="scrollable-boxneriman">

    <h1>Kod Blokları</h1>
                        
                        
                        
                        
                        
    
    <h2>#remove listede eleman siler</h2>
    <pre>
    <code>
    liste = [1,2,3,4,5,6,7]
    liste.append(34)
    liste
    liste.append("python")
    liste
    liste.extend([10,11,12]) #listeyi genişletmek.  
    </code>
    </pre>
    
    <h2>#insert 2. indexe "python" değerini atamak</h2>
    <pre>
    <code>
    liste1= [1,2,3,4,5,6,7,8,9]
    liste1.insert(3, "python")
    liste1
    </code>
    </pre>
    
    <h2>#pop ile son elemanı ve belirli bir index'i silme</h2>
    <pre>
    <code>
    liste2= [1,2,3,4,5,6,7]
    liste2.pop() #son eleman silinir
    liste2
    liste2.pop(2) #2. indexi siler
    liste2
    </code>
    </pre>
    
    <h2>#remove ile belirli bir elemanı silme</h2>
    <pre>
    <code>
    liste3=["python", "neriman", "sena"]
    liste3.remove("python")
    liste3
    </code>
    </pre>
    
    <h2>#count ile eleman sayısını bulma</h2>
    <pre>
    <code>
    liste4=[1,2,3,4,5,5,5,5,5,6,7,8,8,8,8]
    liste4.count(5)
    liste4.count(8)
    </code>
    </pre>
    
    <h2>#sort ile sıralama</h2>
    <pre>
    <code>
    liste6= [4,2,423,2,1,222,234]
    liste6.sort() #küçükten başlayarak sıralar
    liste6 
    liste6.sort(reverse=True) #tersten başlayarak sıralar
    liste6
    </code>
    </pre>
    
    <h2>#demet (tuple) örnekleri</h2>
    <pre>
    <code>
    t= ('p','y','t')
    p= (1,2,3,4)
    T= (1,2,3,4,5,6,7) #TAM SAYI 
    </code>
    </pre>
    <h2>#remove listede eleman siler</h2>
<pre>
<code>
liste = [1,2,3,4,5,6,7]
liste.append(34)
liste
liste.append("python")
liste
liste.extend([10,11,12]) #listeyi genişletmek.  
</code>
</pre>

<h2>#insert 2. indexe "python" değerini atamak</h2>
<pre>
<code>
liste1= [1,2,3,4,5,6,7,8,9]
liste1.insert(3, "python")
liste1
</code>
</pre>

<h2>#pop ile son elemanı ve belirli bir index'i silme</h2>
<pre>
<code>
liste2= [1,2,3,4,5,6,7]
liste2.pop() #son eleman silinir
liste2
liste2.pop(2) #2. indexi siler
liste2
</code>
</pre>

<h2>#remove ile belirli bir elemanı silme</h2>
<pre>
<code>
liste3=["python", "neriman", "sena"]
liste3.remove("python")
liste3
</code>
</pre>

<h2>#count ile eleman sayısını bulma</h2>
<pre>
<code>
liste4=[1,2,3,4,5,5,5,5,5,6,7,8,8,8,8]
liste4.count(5)
liste4.count(8)
</code>
</pre>

<h2>#sort ile sıralama</h2>
<pre>
<code>
liste6= [4,2,423,2,1,222,234]
liste6.sort() #küçükten başlayarak sıralar
liste6 
liste6.sort(reverse=True) #tersten başlayarak sıralar
liste6
</code>
</pre>

<h2>#demet (tuple) örnekleri</h2>
<pre>
<code>
t= ('p','y','t')
p= (1,2,3,4)
T= (1,2,3,4,5,6,7) #TAM SAYI 
</code>
</pre>

<h2>#dilimleme yöntemi</h2>
<pre>
<code>
dil= ("kotlin", "C++","JAVA","PYTHON","ObjectC")
yenidil=[dil[:4],'SWİFT']
print(yenidil) #2 elemanlı tuple çıkacak
dil= ("kotlin", "C++","JAVA","PYTHON","ObjectC")
dil=list(dil )#listeye dönüştü
dil.remove("ObjectC")
dil.append("SWİFT")
print(tuple(dil))
</code>
</pre>

<h2>#tuple yapılarında arama</h2>
<pre>
<code>
A=(2,3,5,8,9,12,34,6,77)
ara=int(input("Aranan sayı: "))
if ara in A:
   i=A.index(ara)
   print("Aranan sayı",i+1,". sırada bulundu.")
else: 
   print("aranan sayı bulunamadı.")
</code>
</pre>
<h2>#remove listede eleman siler</h2>
<pre>
<code>
liste = [1,2,3,4,5,6,7]
liste.append(34)
liste
liste.append("python")
liste
liste.extend([10,11,12]) #listeyi genişletmek.  
</code>
</pre>

<h2>#insert 2. indexe "python" değerini atamak</h2>
<pre>
<code>
liste1= [1,2,3,4,5,6,7,8,9]
liste1.insert(3, "python")
liste1
</code>
</pre>

<h2>#pop ile son elemanı ve belirli bir index'i silme</h2>
<pre>
<code>
liste2= [1,2,3,4,5,6,7]
liste2.pop() #son eleman silinir
liste2
liste2.pop(2) #2. indexi siler
liste2
</code>
</pre>

<h2>#remove ile belirli bir elemanı silme</h2>
<pre>
<code>
liste3=["python", "neriman", "sena"]
liste3.remove("python")
liste3
</code>
</pre>

<h2>#count ile eleman sayısını bulma</h2>
<pre>
<code>
liste4=[1,2,3,4,5,5,5,5,5,6,7,8,8,8,8]
liste4.count(5)
liste4.count(8)
</code>
</pre>

<h2>#sort ile sıralama</h2>
<pre>
<code>
liste6= [4,2,423,2,1,222,234]
liste6.sort() #küçükten başlayarak sıralar
liste6 
liste6.sort(reverse=True) #tersten başlayarak sıralar
liste6
</code>
</pre>

<h2>#demet (tuple) örnekleri</h2>
<pre>
<code>
t= ('p','y','t')
p= (1,2,3,4)
T= (1,2,3,4,5,6,7) #TAM SAYI 
</code>
</pre>

<h2>#dilimleme yöntemi</h2>
<pre>
<code>
dil= ("kotlin", "C++","JAVA","PYTHON","ObjectC")
yenidil=[dil[:4],'SWİFT']
print(yenidil) #2 elemanlı tuple çıkacak
dil= ("kotlin", "C++","JAVA","PYTHON","ObjectC")
dil=list(dil )#listeye dönüştü
dil.remove("ObjectC")
dil.append("SWİFT")
print(tuple(dil))
</code>
</pre>

<h2>#tuple yapılarında arama</h2>
<pre>
<code>
A=(2,3,5,8,9,12,34,6,77)
ara=int(input("Aranan sayı: "))
if ara in A:
   i=A.index(ara)
   print("Aranan sayı",i+1,". sırada bulundu.")
else: 
   print("aranan sayı bulunamadı.")
</code>
</pre>

<h2>#set tanımlama şekilleri</h2>
<pre>
<code>
#kümede indx yoktur
k={1,2,4,5} #tek sayılar kümesi
k1={"abracadabra"}
b=set("alacazam") #b={alczm} kümesi
j=set() #küme ise set konulmalı. Yoksa sözlük olur. 
</code>
</pre>

<h2>#Set İşlemleri</h2>
<pre>
<code>
#A-B ---> A.difference(B)
#A simetrik fark B ----> A^B ----> A.symmetric_difference(B)
#A kesişim B ----> A&B ------> A.intersection(B)
#A birleşim B ----> A | B -----> A.union(B)
#A alt küme B ---> A<=B ----> A.issubset(B)
#A B'yi kapsar ---> A>=B ----> A.issuperset(B) A'nın B'yi kapsaması sonucu True False'u dönecektir.

#K.add(x) kümeye x elemanını ekler
#K.copy() küme kopyalanır
#K.remove(x) içerisine yazılan veriyi siler. O veri yoksa hata verir.
#K.discard() görmezden gelir. 
#K.pop() kümenin İLK elemanını siler. Listede son elemanı siliyordu
#K.isdisjoint() iki kümenin kesişim kümesinin boş olup olmadığını sorgular. Boş ise True, değil ise False döner.
#K.update(B) -----> K.intersection_update --> A kesişim B gerçekleşir ve A küme elemanları buna göre güncellenir.
#K.difference_update(B) K fark B işlemi yapılır. 
</code>
</pre>

<h2>#frozenset</h2>
<pre>
<code>
#0'dan 24'e kadar olan çift sayıların karesini veren uygulama
A= (2,3,4,5,6,7,8,9,12,43,6,77)
A=frozenset(A)
A.add(90) #Hata verecek çünkü frozenset üzerinde değişiklik yapamayız.
</code>
</pre>

<h2>#Sözlükler (Dict)</h2>
<pre>
<code>
derece= dict(ankara=30, istanbul=14.5, yozgat=10, eskişehir=26)
print(list(sorted(derece)))
for il in derece:
    print(il,"sıcaklık...",derece[il])
</code>
</pre>

<h2>#Hata Fırlatmak</h2>
<pre>
<code>
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen bir sayı giriniz")
terscevir()
</code>
</pre>

<h2>#Hata Ayıklama (try, except, finally)</h2>
<pre>
<code>
try:
    a= int("sdkljflksj35435") #ValueError
    print("program burada")
except ValueError:
    print("hatalı")
    
try:
    a=int(input("sayı1: "))
    b=int(input("sayı2: ")) #ZeroDivisionError
    print(a/b)
except ValueError:
    print("Lütfen sayıları doğru girin")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
    
finally:
    print("her halükarda çalışıyorum")
</code>
</pre>


  
  </div>
		   <h1> 1st=[2,-3,0,4,-1]
        A=[] 
    </h1> 
    <p>1st=[2,-3,0,4,-1]: Bu satır, "1st" adlı bir liste oluşturur ve bu listeye [2, -3, 0, 4, -1] elemanlarını atar. Bu listenin elemanları tam sayı değerleridir.
 A=[]: Bu satır, "A" adlı boş bir liste oluşturur. Yani, başlangıçta bu liste içinde hiç eleman yoktur.</p>
    <h1>lst=[2,-3,0,4,-1]
        lst[0]=5
        print(lst[1])
        lst[4]=12
        print(lst)
        print([10,20,30][1])</h1> 
    <p>lst=[2,-3,0,4,-1]: "lst" adında bir liste oluşturulur ve içine [2, -3, 0, 4, -1] elemanları eklenir.
        lst[0]=5: Listenin ilk elemanı (0. index), 5 ile değiştirilir. Yani, liste şu hale gelir: [5, -3, 0, 4, -1].
        print(lst[1]): Listenin ikinci elemanı (1. index), yani -3 ekrana yazdırılır.
        lst[4]=12: Listenin beşinci elemanı (4. index), 12 ile değiştirilir. Şimdi liste şu şekildedir: [5, -3, 0, 4, 12].
        print(lst): Liste, en son haliyle yani [5, -3, 0, 4, 12] ekrana yazdırılır.
        print([10,20,30][1]): [10, 20, 30] listesinin ikinci elemanı (1. index), yani 20 ekrana yazdırılır. ...</p>
    <h1>def main():
        data=[10,20,30,40]
        print(data[-1])
        print(data[-3])</h1> 
    <p>Bu kod, negatif indeks kullanarak bir listenin sondan başlayarak elemanlarına erişim gösterir.
       -1 indeksi son elemanı, -2 indeksi sondan bir önceki elemanı, ve böyle devam eder. Bu, listedeki elemanlara ters yönde indeksleme yapmak için kullanışlı bir yöntemdir.</p>
    <h1>a= [2,4,6,8]
        a+[1,3,5]
        a=a+[1,3,5]
        a+= [10]  
        print(a)</h1> 
    <p>La = [2, 4, 6, 8]: İlk olarak, "a" adında bir liste oluşturulur ve içine [2, 4, 6, 8] elemanları eklenir.
        a + [1, 3, 5]: Bu ifade, "a" listesini [1, 3, 5] listesi ile birleştirir, ancak bu işlem "a" listesini değiştirmez. Yani, bu ifadeyi kullanarak "a" listesinin kendisi değişmez.
        a = a + [1, 3, 5]: Bu ifade, "a" listesini [1, 3, 5] listesi ile birleştirir ve bu birleşmiş listeyi "a" değişkenine atar. Yani, "a" listesi bu ifade sonrasında [2, 4, 6, 8, 1, 3, 5] olur.
        a += [10]: Bu ifade, "a" listesine [10] elemanını ekler. Bu ifade, "a" listesini değiştirir ve "a" listesi şu şekilde olur: [2, 4, 6, 8, 1, 3, 5, 10].
        print(a): Son olarak, "a" listesi ekrana yazdırılır. Bu durumda, "a" listesi [2, 4, 6, 8, 1, 3, 5, 10] olarak ekrana yazdırılır.</p>
    <h1>x=2
        a=[0,1]
        a+= [x]
        print(a)</h1> 
    <p>Lx = 2: Bu satırda, x adında bir değişken oluşturulur ve değeri 2 olarak atanır.
        a = [0, 1]: Bu satırda, a adında bir liste oluşturulur ve içine [0, 1] elemanları eklenir.
        a += [x]: Bu ifade, a listesine x değişkeninin değerini ekler. Yani, a listesi [0, 1, 2] olur. Burada += operatörü, bir listeyi başka bir listeyle genişletmek için kullanılır.
        print(a): Son olarak, "a" listesi ekrana yazdırılır. Bu durumda, "a" listesi [0, 1, 2] olarak ekrana yazdırılır.</p>
    <h1>def listeOluştur():
        sonuc=[]
        girilen_Sayi=0
        while girilen_Sayi>=0:
            girilen_Sayi = int(input("Sayı Giriniz:  (Çıkış için -1)"))
            if(girilen_Sayi>=0):
                sonuc+=[girilen_Sayi]
        return sonuc
    def main():
        liste=listeOluştur()
        print(liste)
        
    main()</h1> 
    <p>def listeOluştur()::
        Bu fonksiyon, boş bir liste olan sonuc adında bir liste oluşturur.
        girilen_Sayi değişkenini sıfıra eşitler.
        Bir döngü başlatır ve kullanıcıdan sayı girişi ister.
        Kullanıcıdan alınan sayı, 0 veya daha büyükse, bu sayıyı sonuc listesine ekler.
        Eğer kullanıcı -1 girerse veya daha küçük bir sayı girerse, döngüyü sonlandırır.
        Son olarak, oluşturulan sonuc listesini döndürür.
        def main()::
        Bu fonksiyon listeOluştur fonksiyonunu çağırarak bir liste alır.
        Ardından, alınan listeyi ekrana yazdırır.
        main(): Bu satır, main fonksiyonunu çağırarak programın çalışmasını sağlar.</p>
    <h1>def main():
        a = list(range(0,10))
        print(a)
        a = list(range(10,-1,-1))
        print(a)
    main()     ...</h1> 
    <p>Bu Python programı iki adet liste oluşturur ve bu listeleri ekrana yazdırır. İlk liste, 0'dan 9'a kadar olan sayıları içerir, ikinci liste ise 10'dan 0'a kadar olan sayıları tersten içerir. Bu işlemleri gerçekleştiren bir main fonksiyonu tanımlanmıştır. Program çalıştırıldığında, bu iki liste ekrana yazdırılır.</p>
    <h1>def main():
        a= [0]*10
        print(a)
        a= [3.4] *5
        print(a)
        n=3
        a=n*["abc", 22,8.8]
        print(a)
    main()</h1> 
    <p>a adında bir liste oluşturulur ve tüm elemanları sıfır olan 10 elemanlı bir liste oluşturulur. a liste olarak adlandırılmış ve ekrana yazdırılır.
        a adında bir başka liste oluşturulur ve tüm elemanları 3.4 olan 5 elemanlı bir liste oluşturulur. Bu liste de a adıyla adlandırılır ve ekrana yazdırılır.
        n adında bir değişken tanımlanır ve a listesini bu değişkenin değeri kadar tekrar eden bir liste oluşturulur. Bu durumda, 3 kez ["abc", 22, 8.8] içeren bir liste elde edilir ve ekrana yazdırılır.</p>

    <h1>def main():
        toplam=0.0
        girilecek_sayi_adeti=5
        sayilar=[]
        print("Lütfen ", girilecek_sayi_adeti, "adet sayı giriniz: ")
        for sayi in range(0,girilecek_sayi_adeti):
            sayi1=float(input(str(sayi+1)+" .sayıyı giriniz: "))
            sayilar+=[sayi1]
            toplam+=sayi1
        for i in sayilar:
            print(end="Girilen sayılar: ")
            print(i, end="")
            print() #alt satıra geç
            print("Ortalama: ", toplam/girilecek_sayi_adeti)
    main()</h1> 
    <p>Bu Python programı, kullanıcıdan belirli bir sayıda sayı girişi alarak bu sayıların toplamını ve ortalamasını hesaplar. İlgili main fonksiyonu şu işlemleri gerçekleştirir:

toplam adında bir değişken oluşturulur ve başlangıçta 0.0 olarak ayarlanır.
girilecek_sayi_adeti adında bir değişken tanımlanır ve başlangıçta 5 olarak ayarlanır.
Boş bir liste olan sayilar oluşturulur.
Kullanıcıya belirtilen sayıda sayı girmesi istenir ve her girilen sayı sayilar listesine eklenir ve toplam değişkenine eklenir.
Girilen sayılar ve ortalama ekrana yazdırılır.
Sonuç olarak, bu program kullanıcının belirtilen adette sayı girmesini sağlar, bu sayıları bir listeye ekler, toplamını ve ortalamasını hesaplar, ve ekrana yazdırır.</p>
    <h1>a=[10,20,30,40]
        b=[10,20,30,40]
        print("a=",a)
        print("b=",b)
        b[2]
        print("a=",a)
        print("b=",b)</h1> 
    <p>Bu Python kodu, iki adet liste (a ve b) oluşturur ve ardından bu listeleri ekrana yazdırır. Ancak, listenin elemanları üzerinde herhangi bir değişiklik yapmaz. Kodun akışını adım adım açıklamak gerekirse:

        a ve b adında iki liste oluşturulur ve her ikisi de aynı elemanları içerir: [10, 20, 30, 40].
        a ve b listeleri ekrana yazdırılır.
        b[2] ifadesi liste b'nin 2. elemanına erişir, ancak bu değer kullanılmadığı ve bir değişkene atanmadığı için bir etkisi olmaz.
        a ve b listeleri tekrar ekrana yazdırılır.
        Sonuç olarak, kodun temel amacı iki listeyi oluşturmak ve içeriklerini ekrana yazdırmaktır. Ancak, b[2] ifadesinin sonucu kullanılmadığı için herhangi bir değişiklik olmaz.</p>
    <h1>lst= [10,20,30,40,50,60,70,80,90,100,110,120]
        print(lst)
        print(lst[0:3]) #3. index dahil değil
        print(lst[4:8])
        print(lst[-5:-3])
        print(lst[2:-2:2])
        print(lst[:])
        print(lst[-100:3])</h1> 
    <p>Bu Python kodu, bir liste olan lst üzerinde farklı dilimleme (slicing) işlemlerini kullanarak belirli alt listeleri seçer ve ekrana yazdırır. İşte kodun temel amacını açıklayan adımlar:

        lst listesi oluşturulur ve ekrana yazdırılır.
        lst[0:3] ifadesi kullanılarak, lst'nin 0. (dahil) ile 3. (hariç) indexleri arasındaki elemanlar seçilir ve ekrana yazdırılır.
        lst[4:8] ifadesi kullanılarak, lst'nin 4. (dahil) ile 8. (hariç) indexleri arasındaki elemanlar seçilir ve ekrana yazdırılır.
        lst[-5:-3] ifadesi kullanılarak, lst'nin sondan 5. (dahil) ile sondan 3. (hariç) indexleri arasındaki elemanlar seçilir ve ekrana yazdırılır.
        lst[2:-2:2] ifadesi kullanılarak, lst'nin 2. (dahil) ile sondan 2. (hariç) indexleri arasındaki elemanlar seçilir ve 2'şer atlayarak ekrana yazdırılır.
        lst[:] ifadesi kullanılarak, lst'nin tamamı seçilir ve ekrana yazdırılır.
        lst[-100:3] ifadesi kullanılarak, -100 (eksi indeksler, listenin başından başlayarak) ile 3. (hariç) indexleri arasındaki elemanlar seçilir. Ancak, liste boyutu kadar eleman olmadığı için tüm liste seçilir ve ekrana yazdırılır.
        Kısacası, kod, bir listenin belirli dilimlerini seçerek ve ekrana yazdırarak dilimleme işlemlerini gösterir.</p>
    <h1>a=[1,2,3,4,5,6,7,8]
        print("listenin sondan başlanarak dilimlenmesi")
        print("Liste bir dilimle örneğidir: ",a)
        
        for i in range (0,len(a)+1):
            print("<",a[0:i],">",sep="")
        print("-------------------------------")
        for i in range (0,len(a)+1):
            print("<",a[i:len(a)+1],">",sep="")</h1> 
    <p>Bu Python kodu, bir listenin sondan başlanarak dilimlenmesini gösterir. İki for döngüsü kullanılarak, listenin farklı dilimleri (a[0:i] ve a[i:len(a)+1]) oluşturularak ekrana yazdırılır. İşte kodun temel amacını açıklayan adımlar:

        a adında bir liste oluşturulur ve ekrana yazdırılır.
        İlk for döngüsü, listenin başından itibaren (a[0:i]) giderek artan dilimleri oluşturur ve her bir dilimi <...> içinde ekrana yazdırır.
        İkinci for döngüsü, listenin sondan başlanarak (a[i:len(a)+1]) giderek azalan dilimleri oluşturur ve yine her bir dilimi <...> içinde ekrana yazdırır.</p>
    <h1>b=list(range(20))
        print(b)
        del b[2]
        print(b)</h1> 
    <p>Bu kod, bir liste oluşturur, listenin içeriğini ekrana yazdırır, ardından listenin belirli bir indeksindeki elemanı (b[2]) siler ve güncellenmiş listeyi ekrana yazdırır. Kısaca:

        list(range(20)) ifadesi ile 0'dan 19'a kadar olan sayıları içeren bir liste (b) oluşturulur.
        print(b) ile liste içeriği ekrana yazdırılır.
        del b[2] ifadesi ile listenin 2. indeksindeki eleman silinir.
        print(b) ile güncellenmiş liste içeriği ekrana yazdırılır.</p>
    <h1>import random

        def Topla(lst):
            sonuc = 0
            for eleman in lst:
                sonuc += eleman
            return sonuc
        
        def SifirAta(lst):
            for i in range(len(lst)):
                lst[i] = 0
        
        def RastgeleDegerAta(n):
            sonuc = 0
            for i in range(n):
                RastgeleDeger = random.randrange(100)
                sonuc += RastgeleDeger
            return sonuc
        
        def main():
            a = [2, 4, 6, 8]
            print(a)
            print(sum(a))
        
            SifirAta(a)
            print(a)
            print(sum(a))
        
            a = []
            print(a)
            print(sum(a))
        
            a = RastgeleDegerAta(10)
            print(a)
            print(sum(a))
        
        main()</h1> 
    <p>Topla fonksiyonu: Bir listenin elemanlarını toplar ve toplamı döndürür.
        SifirAta fonksiyonu: Bir listenin tüm elemanlarını sıfıra ayarlar.
        RastgeleDegerAta fonksiyonu: Belirli bir sayıda rastgele değer üretir (0 ile 99 arasında) ve bu değerlerin toplamını döndürür.
        main fonksiyonu: Önceden tanımlanmış bir liste üzerinde bu fonksiyonları çağırır ve sonuçları ekrana yazdırır.
        Örneğin:
        
        İlk olarak, a listesi [2, 4, 6, 8] olarak belirlenir ve bu listenin elemanları toplamı (sum(a)) ve kendisi ekrana yazdırılır.
        Ardından, SifirAta(a) fonksiyonu çağrılarak listenin tüm elemanları sıfıra ayarlanır ve bu güncellenmiş liste ve elemanları toplamı ekrana yazdırılır.
        Daha sonra, boş bir liste oluşturulur, elemanları toplamı ve liste ekrana yazdırılır.
        Son olarak, RastgeleDegerAta(10) fonksiyonu çağrılarak rastgele değerler üretilir, bu değerlerin toplamı ve liste ekrana yazdırılır.</p>
    <h1>ipsum dolor sit amet, consectetur adipiscing elit. ...</h1> 
                        
      <h1>from math import sqrt 
sayi = float(input("sayı giriniz: "))
kok= sqrt(sayi)
print(sayi, "sayısının karekökü", kok)
</h1>
<p>Kullanıcıdan sayı al, karekökünü hesapla, sonuçları yazdır.</p>
<p>fonskiyonlar: her biri kendine has. Metotların yerine geçebilir.</p> 
<p>sqrt:karekök alma </p>

<h1>
from math import sqrt 
x=16 
y = sqrt(x)
print(y)
</h1>
<p>from math import sqrt: math modülünden sqrt fonksiyonunu içe aktarır. Bu fonksiyon, bir sayının karekökünü hesaplamak için kullanılır.</p>
<p>x = 16: x adında bir değişken oluşturup değerini 16 olarak ayarlar.</p> 
<p>y = sqrt(x): sqrt fonksiyonunu kullanarak x değişkeninin karekökünü hesaplar ve sonucu y değişkenine atar.</p>
<p>y = sqrt(x): sqrt fonksiyonunu kullanarak x değişkeninin karekökünü hesaplar ve sonucu y değişkenine atar.</p>
<p>print(y): Elde edilen karekök değerini ekrana yazdırır.</p>
<p>Bu kodu çalıştırdığınızda, 16 sayısının karekökü olan 4.0 değeri ekrana yazdırılacaktır.</p>
 <p>sqrt fonksiyonu her zaman bir float (ondalık) değeri döndürdüğü için, sonuç 4.0 olarak ifade edilir.</p>    
<h1>from math import sqrt 
y= 2*sqrt(x+16)-4
print(y)
print(sqrt(int("45")))</h1>
<p>Bu Python kodu, matematiksel hesaplamalar yaparak iki farklı değeri ekrana yazdırmaktadır. İşte kodun adım adım açıklaması:</p>
<p>from math import sqrt: math modülünden sqrt fonksiyonunu içe aktarır.</p>
<p>x = 16: x adında bir değişken oluşturup değerini 16 olarak ayarlar.</p>

<p>y = 2 * sqrt(x + 16) - 4: y değişkenine, matematiksel ifade 2 * sqrt(x + 16) - 4'ü hesaplayarak değerini atar.</p>
<p>print(y): İlk hesaplanan değeri ekrana yazdırır.</p>
<p>print(sqrt(int("45"))): "45" string'ini önce integer'a (int) çevirir, sonra bu sayının karekökünü (sqrt) alarak ekrana yazdırır.</p>
<p>Kodun çıktısı, ilk olarak y değişkeninin değerini, ardından "45" sayısının karekökünü içerir.</p>
<h1>def selamla():
    print("selam arkadaşlar")
    print("nasılsınız")
type(selamla)</h1>
<p>#fonksiyoların 3 bölümü vardır: isim ,parametre kısmı,sonuç bölümü.</p>
<p>#parametre kısmı parantezin içine yazılan. </p>
<p>#def fonksiyon adı (parametre 1, 2, 3,...(opsiyonel1)):</p>
<p>#fonksiyon blogu</p>
<h1>selamla()</h1>
<p>selam arkadaşlar
 nasılsınız</p>
 <h1>def selamla(isim): #isim parametresi
    print("merhaba",isim)</h1>
  <h1>selamla("kemal") #merhaba isim</h1>
  <p>#argüman: gerçek değerler, parametre:argümanların değerlerle eşleşmesi</p>
  <h1>selamla("ayşe")</h1>
  <h1>def toplama(a,b,c):
    print("toplamları:", a+b+c)</h1>
    <h1>toplama(3,4,5):12</h1>
    <h1>toplama(111,112,122):345</h1>

    <h1>def faktoriyel(number):
    factorial = 1
    if number >= 0:
        for i in range(1, number + 1):
            factorial *= i
        return factorial
    else:
        return None
 
number = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
factorial = faktoriyel(number)
 
if factorial:
    print(f"Girdiğiniz sayının faktöriyeli: {number}! = {factorial}")
else:
    print("Negatif sayıların faktöriyeli olmaz!")</h1>
    <p>Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...</p>
 <p>4</p>
<p>Girdiğiniz sayının faktöriyeli: 4! = 24</p>
<h1>def faktoriyel(sayı):
    faktoriyel=1
    if (sayı ==0 or sayı == 1):
        print("faktoriyel,", faktoriyel)
    else: 
        while (sayı>=1):
            faktoriyel *= sayı
            sayı -=1
        print("faktöriyel",faktoriyel)</h1>
        <h1>faktoriyel(5)=faktöriyel 120</h1>
        <h1>from random import random
random()=0.5723086058492693</h1>
<h1>print(print(4))=4
None</h1>
<h1>type(int())=int</h1>
<p>def bilgilerinigöster(ad="bilgi yok", soyad="bilgi yok", numara="bilgi yok"):: Bu satır, bilgilerinigöster adında bir fonksiyon tanımlar.</p>
 <p>Bu fonksiyon üç adet parametre alabilir: ad, soyad, ve numara. Her bir parametrenin varsayılan değeri "bilgi yok" olarak belirlenmiştir.</p>
 <h1>def bilgilerinigöster(ad= "bilgi yok", soyad= "bilgi yok", numara="bilgi yok "):
    print("ad: ", ad, "soyad: ", soyad, "numara: ", numara) </h1>
    <h1>bilgilerinigöster()</h1>
    <p>ad:  bilgi yok soyad:  bilgi yok numara:  bilgi yok </p>
    <h1>bilgilerinigöster(ad="efe", numara= "12121")</h1>
    <p>ad:  efe soyad:  bilgi yok numara:  12121</p>

    <h1>from math import sqrt 

  def kökalmak(sayı):
    kök=sqrt(sayı)
    print(kök)
  </h1>
  <p>from math import sqrt: math modülünden sqrt fonksiyonunu içe aktarır.</p> 
  <p>Bu fonksiyon, bir sayının karekökünü hesaplamak için kullanılır.</p>
   <p>kök = sqrt(sayı): Fonksiyon içinde, sqrt fonksiyonunu kullanarak sayı parametresinin karekökünü hesaplar ve bu değeri kök değişkenine atar.</p>
   <p>print(kök): Hesaplanan karekök değerini ekrana yazdırmak için print fonksiyonunu kullanır.</p>
   <h1>kökalmak(4)</h1>
   <p>2.0</p>
   <h1>from math import exp 
def eulersabiti(sayı):
    sabit=exp(sayı)
    print(sabit)</h1>
    <h1>eulersabiti(2)</h1>
    <p>7.38905609893065</p>       



    <h1> YAŞ SORGULAMA KODLARI...</h1>
    <p>yaş = int(input("yaşınızı giriniz:"))

        if (yaş <18):
            print("bu mekana giremezsiniz")
        else:
            print("mekana hoşgeldiniz")</p>
    <h1>DERSTEN GEÇTİ KALDI KODLARI ...</h1>
    <p>note = float ( input ( "notunuzu giriniz:" )) 
        if  note >= 90 : 
            print ( "AA" ) 
        elif  note >= 85 : 
            print ( "BA" ) 
        elif  note >= 80 : 
            print ( "BB" ) 
        elif  not >= 75 : 
            print ( "CB" ) 
        elif  notu >= 70 : 
            print ( "CC" ) 
        elif  notu >= 65 : 
            print ( "DC" ) 
        elif  notu >= 60 : 
            print ( "DD" ) 
        else : 
            print ( "DERSTEN KALDINIZ....:" )</p>
    <h1>SESLİ VE SESSİZ HARF ÖĞRENME KODLARI</h1>
    <p> harf =  input  ( "bir harf giriniz:" ) 
        if  harf .  isalpha (): 
            if  harf  in  "aeiouAEIOU" : 
                print ( "sesli harf" ) 
            else : 
                print ( "sessiz harf" ) 
        else : 
            print ( "geçersiz karakter..." )</p>
    <h1>POZİTİF NEGATİF SAYI ÖĞRENME KODLARI</h1>
    <p>sayi = int ( input ( "1.sayıyı giriniz:" )) 
        sayi = int ( input ( "2.sayıyı giriniz:" )) 
        sayi = int ( input ( "3.sayıyı giriniz:" )) 
        if  ( sayi < 0 ): 
            print ( "s" ) 
        elif ( sayi > 0 ): 
            print ( "sayı pozitiftir" ) 
        else : 
            print ( "0 sayınız girdiniz" )</p>
    <h1>LOGIN SAYFASI HAZIRLAMA KODLARI</h1>
    <p>dogru_kullanıcı_Adi = "yönetici" 
        dogru_sifre = "şifre123"
        
        girilen_kullanıcı_Adi = input ( "kullanıcı adı:" ) 
        girilen_şifre = input ( "şifre:" )
        
        if ( girilen_kullanıcı_Adi != dogru_kullanıcı_Adi  ve  girilen_şifre ==  doğru_şifre ): 
            print ( "kullanıcı adı hatalıdır...." ) 
        elif ( girilen_kullanıcı_Adi == dogru_kullanıcı_Adi   ve  girilen_şifre !=  doğru_şifre ): 
            print ( "parola hatalıdır.." ) 
        elif ( girilen_kullanıcı_Adi != dogru_kullanıcı_Adi  ve  girilen_şifre  !=  dogru_şifre ): 
            print ( "kullanıcı adı ve paroladır..." ) 
        else : 
            print ( "başarıyla giriş yapıldı...." )</p>
    <h1>BOY KİLO ENDEKSİ HESAPLAMA KODLARI</h1>
    <p>adınız = input ( "adınızı giriniz:" ) 
        kilo = int ( input ( "kilonuzu giriniz:" )) 
        boy = float ( input ( "boyunuzu giriniz:" )) 
        formül = kilo / ( boy * boy ) 
        print ( adınız , " ,boy kilo dijital değerin:" , formülü ) 
        if  0 <= formülü <= 18  : 
            print ( "zayıf çıktın." ) 
        elif  18 < formülü <= 24 : 
            print ( "normal çıktın." ) 
        elif  24 < formülü <= 29 : 
           print ( "fazla kilolu çıktın." ) 
        else : 
            print ( "obez çıktın..." )</p>
    <h1>EN BÜYÜK OLAN SAYIYI BULMA KODLARI</h1>
    <p>sayi1  =  int ( input ( "1. Sayı: " )) 
        sayi2  =  int ( input ( "2. Sayı: " )) 
        sayi3  =  int ( input ( "3. Sayı: " ))
         
        if  ( sayi1  >=  sayi2 )  ve  ( sayi1  >=  sayi3 ): 
           buyuk  =  sayi1 
        elif  ( sayi2  >=  sayi1 )  ve  ( sayi2  >=  sayi3 ): 
           buyuk  =  sayi2 
        else : 
           buyuk  =  sayi3
         
        print ( sayi1 , "," , sayi2 , "ve" , sayi3 , "içinde büyük olan sayı" , buyuk )
         </p>
    <h1>SORU CEVAP İLE SORUN ÇÖZME KODLARI</h1>    
    <p>print("bilgisayarım çalışmıyor")
        çözüm=False
        while not çözüm:
            print("elektrik var mı")
            secim=input("y or n:  ")
            if secim=="n":
                print("fişe takılımı")
                secim=input("y or n:  ")
                if secim=="n":
                    print("fişe takın")
                elif secim=="y":
                    print("açma düğmesine bastınızmı")
                    secim=input("y or n:  ")
                    if secim=="n":
                        print("düğmeye basın")
                    elif secim=="y":
                        print("sigorta atmış mı")
                        secim=input("y or n:  ")
                        if secim=="n":
                            print("şalteri kontrol edin")
                        else:
                            print("teknik servise başvurun")
                    else:
                        print("teknik servise başvurun")
        </p>
    <h1>GİRİLEN SAYILARIN ORTALAMASINI BULMA KODLARI</h1>
    <p>def main():
        toplam=0.0
        girilecek_sayi_adeti=5
        sayilar=[]
        print("lütfen",girilecek_sayi_adeti,"adet sayı giriniz:")
        for sayı in range(0,girilecek_sayi_adeti):
            sayi1=float(input(str(sayi1+1)+". sayıyı giriniz:"))
            sayilar+=[sayi1]
            toplam+=sayi1
        for i in sayilar:
            print(end="girilen sayılar:")
            print(i, end="")
            print()#alt satıra geçiş
            print("ortalama:",toplam/girilecek_sayi_adeti)
            
    main()     </p>
    <h1>LİSTEYE ELEMAN EKLEME KODLARI</h1>
    <p>liste = [1,2,3,4,5,6,7]
        liste.insert(2,"pyhton")
        liste</p>
    <h1>LİSTEDEN ELEMAN KALDIRMA KODLARI</h1>
    <p>liste = [1,2,3,4,5,6,7]
        liste.remove(1)
        liste</p>
    <h1>ÜÇGEN VE KARE İÇİN KENAR HESAPLAMA KODLARI</h1>    
    <p>n= int(input("Üçgen için 3, dörtgen için 4 yaz: "))
        if(n!=4 and n!=3):
            print(" geçerli kenar sayısı için 3 veya 4 yaz.")
            n= int(input("Üçgen için 3, dörtgen için 4 yaz: "))
        if(n==3):
            b= float(input("1.kenarı gir: "))
            c= float(input("2.kenarı gir: "))
            d= float(input("3.kenarı gir: "))
            if (b==c or b==d or d==c):
                print("Eşkenar üçgen!")
            elif (b==c==d):
                print("İkizkenar üçgen!")
            elif (b!=c and b!=d and c!=d):
                print("Sıradan bir üçgen!") 
            elif (b+c<d or b+d<c or d+c<b):
                print(" üçgen belirtmiyor.")
                print("Bir üçgenin iki kenarının uzunlukları toplamı üçüncü kenarın uzunluğundan büyük olmalıdır!")
        elif(n==4):
            e= float(input("1.kenarı gir: "))
            f= float(input("1.kenara dik olan kenarı gir: "))
            g= float(input("2.kenarı gir: "))
            h= float(input("2.kenara dik olan kenarı gir: "))
            if (e==f==g==h):
                print(" kare!")
            elif (e==g and f==h):
                print(" dikdörtgen!")
            elif (e!=f and f!=g and g!=h):
                print("dörtgen")
        </p>
    <h1>İL PLAKA SORGULAMA KODLARI/h1>
    <p>il={}
        il["ankara"]="06"
        il["istanbul"]="34"
        il["giresun"]="28"
        il["bursa"]="16"
        il["rize"]="53"
        il["eskişehir"]="26"
        plaka={}
        plaka["01"]="Adana"
        plaka["08"]="Artvin"
        plaka["76"]="ığdır"
        plaka["37"]="kastamonu"
        plaka["61,5"]="of"
        plaka["21"]="diyarbakır"
        print("-"*10)
        print("21 plakalı il: ",plaka.get("21"))
        print("-"*10)
        print("Eskişehir in il plakası:",il.get("eskişehir")+"dir.")
        
        </p>           
                        
	</section>


	
	<!-- Newsletter section end -->
	<!-- Footer section -->
	<footer class="footer-section">
		<div class="container">
			<div class="row spad">
				<div class="col-md-6 col-lg-3 footer-widget">
					<img src="https://cdn.discordapp.com/attachments/1099776572988334160/1173011092331561030/logo.png?ex=656266b5&is=654ff1b5&hm=4552100c1d8a001801e9f5ca8b23621e129b121832abdec4c62f907f94a55c19&" class="mb-4" alt="">
				</div>
				<div class="col-md-6 col-lg-2 offset-lg-1 footer-widget">
					<h5 class="widget-title">Kaynaklar</h5>
					<ul>
						<li><a href="https://www.coinbase.com/tr/how-to-buy/midas#:~:text=Varl%C4%B1klar%20sekmesinde%20%E2%80%9CTakas%E2%80%9D%20simgesine%20dokunun,sonland%C4%B1rmak%20i%C3%A7in%20ekrandaki%20talimatlar%C4%B1%20izleyin."  target="_blank">Coin Nasıl Alınır?</a></li>
						<li><a href="https://www.spl.com.tr/icerik/kripto-paralara-genel-bakis-ve-kripto-para-arzinin-ico-hukuki-niteligi"target="_blank">Paraya Genel Bakış</a></li>
						<li><a href="https://www.getmidas.com/midas-kulaklari/haberleri/"target="_blank">Blog Haberleri</a></li>
						<li><a href="https://www.getmidas.com/destek/midas-ile-yatirima-baslarken/midas-ile-neler-yapabilirim/nasil-satis-islemi-gerceklestirebilirsin/#:~:text=Midas%20hesab%C4%B1ndaki%20bir%20hisseyi%20satmak,%C4%B0stedi%C4%9Fin%20tutar%C4%B1%20veya%20adeti%20girebilirsin."target="_blank">Coin Nasıl Satılır?</a></li>
					</ul>
				</div>
				<div class="col-md-6 col-lg-2 offset-lg-1 footer-widget">
					<h5 class="widget-title">Hızlı Linkler</h5>
					<ul>
						<li><a href="#">Piyasalar</a></li>
						<li><a href="#">Hakkımızda</a></li>
						<li><a href="#">SSS</a></li>
						<li><a href="#">Kayıt Ol</a></li>
						<li><a href="#">Giriş Yap</a></li>
						<li><a href="https://view.forms.app/nerimantopcu/iletisim"target="_blank">İletişim</a></li>
						<li><a href="#neriman">Abone Ol</a></li>
					</ul>
				</div>
				<div class="col-md-6 col-lg-3 footer-widget pl-lg-5 pl-3">
					<p>Copyright © 2023 Tüm hakları saklıdır. | <b>İGÜ Bilişim Güvenliği Teknolojisi </b></p>

				</div>
			</div>
			<div class="footer-bottom">
				<div class="row">
					<div class="col-lg-4 store-links text-center text-lg-left pb-3 pb-lg-0">
						<a href=""><img src="https://cdn.discordapp.com/attachments/1099776572988334160/1173047385568596038/aaaa.png?ex=65628882&is=65501382&hm=9d96bcf160b4529d939911b0169180857764fd6c4905279a2df65dc784ff0506&" alt="" class="mr-2"></a>
					</div>
					<div class="col-lg-8 text-center text-lg-right">
						<ul class="footer-nav">
							<li><a href="https://www.detayyayin.com.tr/sayfa/site-kullanim-sartlari " target="_blank">Kullanım Koşulları</a></li>
							<li><a href="https://www.getmidas.com/gizlilik-politikasi/" target="_blank">Gizlilik Politikası</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</footer>


	<script src="https://forms.app/static/embed.js" type="text/javascript" async defer onload="new formsapp('5e5b913c0a3f334aaf069b50', 'sidetab', {'button':{'text':'Bizimle İletişime Geç','color':'red'},'align':{'horizontal':'right','vertical':'middle'},'width':'400px','height':'500px'});"></script>

	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

	<script>


		'use strict';


		$(window).on('load', function() {
			/*------------------
                Preloder
            --------------------*/
			$(".loader").fadeOut();
			$("#preloder").delay(400).fadeOut("slow");

		});

		(function($) {

			$('.responsive-bar').on('click', function(event) {
				$('.main-menu').slideToggle(400);
				event.preventDefault();
			});


			/*------------------
                Background set
            --------------------*/
			$('.set-bg').each(function() {
				var bg = $(this).data('setbg');
				$(this).css('background-image', 'url(' + bg + ')');
			});


			/*------------------
                Review
            --------------------*/
			var review_meta = $(".review-meta-slider");
			var review_text = $(".review-text-slider");


			review_meta.owlCarousel({
				loop: true,
				nav: false,
				dots: true,
				items: 3,
				center: true,
				margin: 20,
				autoplay: true,
				mouseDrag: false,
			});


			review_text.owlCarousel({
				loop: true,
				nav: true,
				dots: false,
				items: 1,
				margin: 20,
				autoplay: true,
				navText: ['<i class="ti-angle-left"><i>', '<i class="ti-angle-right"><i>'],
				animateOut: 'fadeOutDown',
				animateIn: 'fadeInDown',
			});



			/*------------------
               Contact Form
           --------------------*/
			$(".check-form").focus(function () {
				$(this).next("span").addClass("active");
			});
			$(".check-form").blur(function () {
				if ($(this).val() === "") {
					$(this).next("span").removeClass("active");
				}
			});


		})(jQuery);

		function initialize() {
			var myOptions = {
				zoom: 16,
				center: new google.maps.LatLng(51.489500, -0.096777), //change the coordinates
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				scrollwheel: false,
				mapTypeControl: false,
				zoomControl: false,
				streetViewControl: false,
				styles: [{"elementType":"geometry","stylers":[{"color":"#f5f5f5"}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#616161"}]},{"elementType":"labels.text.stroke","stylers":[{"color":"#f5f5f5"}]},{"featureType":"administrative.land_parcel","elementType":"labels.text.fill","stylers":[{"color":"#bdbdbd"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#eeeeee"}]},{"featureType":"poi","elementType":"labels.text.fill","stylers":[{"color":"#757575"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#e5e5e5"}]},{"featureType":"poi.park","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#ffffff"}]},{"featureType":"road.arterial","elementType":"labels.text.fill","stylers":[{"color":"#757575"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#dadada"}]},{"featureType":"road.highway","elementType":"labels.text.fill","stylers":[{"color":"#616161"}]},{"featureType":"road.local","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]},{"featureType":"transit.line","elementType":"geometry","stylers":[{"color":"#e5e5e5"}]},{"featureType":"transit.station","elementType":"geometry","stylers":[{"color":"#eeeeee"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#c9c9c9"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]}]
			}
			var img_icon = 'img/map-marker.png'
			var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
			var marker = new google.maps.Marker({
				map: map,
				icon: img_icon,
				position: new google.maps.LatLng(51.488966, -0.096777) //change the coordinates
			});
			google.maps.event.addListener(marker, "click", function() {
				infowindow.open(map, marker);
			});
		}
		google.maps.event.addDomListener(window, 'load', initialize);
	</script>

</body>
</html>
    """)
